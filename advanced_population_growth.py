import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import tkinter as tk
from tkinter import messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import csv
from fpdf import FPDF

# Logistic growth model with additional factors
def logistic_growth(P, t, r, K, seasonal_factor, immigration_rate):
    K_t = K * (1 + seasonal_factor * np.sin(2 * np.pi * t / 365))
    dPdt = r * P * (1 - P / K_t) + immigration_rate
    return dPdt

# Euler's method for numerical comparison
def euler_method(f, P0, t, r, K, seasonal_factor, immigration_rate):
    P_values = [P0]
    dt = t[1] - t[0]
    P = P0
    for i in range(1, len(t)):
        dPdt = f(P, t[i-1], r, K, seasonal_factor, immigration_rate)
        P += dPdt * dt
        P_values.append(P)
    return np.array(P_values)

# Update plot based on user input
def update_plot():
    try:
        r = float(entry_r.get())
        K = float(entry_K.get())
        P0 = float(entry_P0.get())
        seasonal_factor = float(entry_seasonal.get())
        immigration_rate = float(entry_immigration.get())
        noise_intensity = float(entry_noise.get())

        if r <= 0 or K <= 0 or P0 <= 0:
            messagebox.showerror("Invalid input", "Growth rate, carrying capacity, and initial population must be positive.")
            return

        t = np.linspace(0, 1000, 1000)
        P_odeint = odeint(logistic_growth, P0, t, args=(r, K, seasonal_factor, immigration_rate))
        P_euler = euler_method(logistic_growth, P0, t, r, K, seasonal_factor, immigration_rate)
        P_stochastic = P_odeint.flatten() + np.random.normal(0, noise_intensity * P_odeint.flatten(), len(t))

        ax.clear()
        ax.plot(t, P_odeint, label='Odeint Method', color='blue')
        ax.plot(t, P_euler, label='Euler\'s Method', linestyle='--', color='green')
        ax.plot(t, P_stochastic, label='With Stochastic Noise', linestyle=':', color='red')
        ax.set_xlabel('Time (days)')
        ax.set_ylabel('Population Size')
        ax.set_title('Enhanced Population Growth Model')
        ax.legend()
        ax.grid()
        canvas.draw()

        # Update the description text
        description_text = (
            f"The plot shows the population growth dynamics using the following models:\n\n"
            f"1. **Odeint Method (Blue Line):** Solves the logistic growth equation using a highly precise numerical method.\n\n"
            f"2. **Euler's Method (Green Dashed Line):** A simpler numerical method to approximate the solution.\n\n"
            f"3. **Stochastic Noise (Red Dotted Line):** Introduces randomness into the population model.\n\n"
            f"With the current parameters:\n- Growth Rate (r): {r}\n- Carrying Capacity (K): {K}\n- Initial Population (P0): {P0}\n"
            f"- Seasonal Variation Factor: {seasonal_factor}\n- Immigration Rate: {immigration_rate}\n"
            f"The model helps visualize how population changes over time, influenced by natural growth, seasonal variations, immigration, and randomness."
        )
        description_box.delete(1.0, tk.END)
        description_box.insert(tk.END, description_text)

        # Store the current simulation results for export
        global current_simulation_data
        current_simulation_data = {
            'time': t,
            'odeint': P_odeint.flatten(),
            'euler': P_euler.flatten(),
            'stochastic': P_stochastic.flatten()
        }
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numerical values.")

# Save parameters to a JSON file
def save_parameters():
    params = {
        "r": entry_r.get(),
        "K": entry_K.get(),
        "P0": entry_P0.get(),
        "seasonal_factor": entry_seasonal.get(),
        "immigration_rate": entry_immigration.get(),
        "noise_intensity": entry_noise.get()
    }
    with open('simulation_parameters.json', 'w') as f:
        json.dump(params, f)
    messagebox.showinfo("Saved", "Parameters saved successfully.")

# Load parameters from a JSON file
def load_parameters():
    try:
        with open('simulation_parameters.json', 'r') as f:
            params = json.load(f)
            entry_r.delete(0, tk.END)
            entry_r.insert(0, params['r'])
            entry_K.delete(0, tk.END)
            entry_K.insert(0, params['K'])
            entry_P0.delete(0, tk.END)
            entry_P0.insert(0, params['P0'])
            entry_seasonal.delete(0, tk.END)
            entry_seasonal.insert(0, params['seasonal_factor'])
            entry_immigration.delete(0, tk.END)
            entry_immigration.insert(0, params['immigration_rate'])
            entry_noise.delete(0, tk.END)
            entry_noise.insert(0, params['noise_intensity'])
        update_plot()
        messagebox.showinfo("Loaded", "Parameters loaded successfully.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No saved parameters found.")

# Export the current plot and description to a PDF file
def export_to_pdf():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[('PDF Files', '*.pdf')])
        if file_path:
            # Export plot to PDF
            fig.savefig(file_path)

            # Add description to PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(200, 10, 'Population Growth Model', 0, 1, 'C')
            pdf.set_font('Arial', '', 12)
            description = description_box.get("1.0", tk.END)
            pdf.multi_cell(0, 10, description)
            pdf.output(file_path)

            messagebox.showinfo("Exported", "Plot and description exported successfully to PDF.")
    except Exception as e:
        messagebox.showerror("Export Error", f"Failed to export: {e}")

# Save simulation data to a CSV file
def save_simulation_data():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV Files', '*.csv')])
        if file_path:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Time', 'Odeint', 'Euler', 'Stochastic'])
                for i in range(len(current_simulation_data['time'])):
                    writer.writerow([current_simulation_data['time'][i], current_simulation_data['odeint'][i],
                                     current_simulation_data['euler'][i], current_simulation_data['stochastic'][i]])
            messagebox.showinfo("Saved", "Simulation data saved successfully to CSV.")
    except Exception as e:
        messagebox.showerror("Save Error", f"Failed to save simulation data: {e}")

# Create GUI
root = tk.Tk()
root.title("Population Growth Model")

frame = tk.Frame(root)
frame.pack(side=tk.TOP)

# Parameter input fields
tk.Label(frame, text="Growth Rate (r):").grid(row=0, column=0)
entry_r = tk.Entry(frame)
entry_r.grid(row=0, column=1)

tk.Label(frame, text="Carrying Capacity (K):").grid(row=1, column=0)
entry_K = tk.Entry(frame)
entry_K.grid(row=1, column=1)

tk.Label(frame, text="Initial Population (P0):").grid(row=2, column=0)
entry_P0 = tk.Entry(frame)
entry_P0.grid(row=2, column=1)

tk.Label(frame, text="Seasonal Factor:").grid(row=3, column=0)
entry_seasonal = tk.Entry(frame)
entry_seasonal.grid(row=3, column=1)

tk.Label(frame, text="Immigration Rate:").grid(row=4, column=0)
entry_immigration = tk.Entry(frame)
entry_immigration.grid(row=4, column=1)

tk.Label(frame, text="Noise Intensity:").grid(row=5, column=0)
entry_noise = tk.Entry(frame)
entry_noise.grid(row=5, column=1)

# Buttons
update_button = tk.Button(frame, text="Update Plot", command=update_plot)
update_button.grid(row=6, column=0, columnspan=2)

save_button = tk.Button(frame, text="Save Parameters", command=save_parameters)
save_button.grid(row=7, column=0)

load_button = tk.Button(frame, text="Load Parameters", command=load_parameters)
load_button.grid(row=7, column=1)

export_button = tk.Button(frame, text="Export to PDF", command=export_to_pdf)
export_button.grid(row=8, column=0)

save_data_button = tk.Button(frame, text="Save Data to CSV", command=save_simulation_data)
save_data_button.grid(row=8, column=1)

# Plotting area
fig, ax = plt.subplots(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Description box
description_box = tk.Text(root, height=12, wrap=tk.WORD)
description_box.pack(pady=10)
description_box.insert(tk.END, "The description of the plot will appear here after you update the plot.")

root.mainloop()
