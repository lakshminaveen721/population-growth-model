## population-growth-model
This project simulates population growth using the logistic growth model, with additional features like seasonal variations, immigration, and stochastic noise. The simulation is implemented using numerical methods such as SciPy's odeint and Euler's method, and provides an interactive graphical user interface (GUI) for easy parameter manipulation. Users can save their settings, export the simulation results to CSV, and save the plot and model description as a PDF.

#Technologies Used:

Python: The main programming language used for the simulation and GUI.
Tkinter: Used for creating the graphical user interface.
Matplotlib: For plotting the simulation results.
SciPy: For solving differential equations (odeint method).
FPDF: To export the plot and description to PDF.
CSV Module: To save the simulation data to a CSV file.

## How It Works:
The project simulates population growth using the following logistic growth equation:

\[
\frac{dP}{dt} = rP \left(1 - \frac{P}{K}\right) + \text{immigration\_rate}
\]

Where:
- \(P\) is the population size.
- \(r\) is the growth rate.
- \(K\) is the carrying capacity (can vary seasonally).
- Immigration rate adds a constant number of individuals to the population.

The model can include seasonal variations where \(K_t\) changes periodically:

\[
K_t = K \left(1 + \text{seasonal\_factor} \cdot \sin\left(\frac{2\pi t}{365}\right)\right)
\]

The population growth is simulated over time, and the plot shows how the population evolves based on user-defined parameters.

## Features Overview:

### 1. Interactive GUI
The Tkinter-based graphical interface allows users to input parameters for the simulation, including growth rate, carrying capacity, initial population, seasonal factor, immigration rate, and noise intensity. The model automatically updates the plot when the user clicks the "Update Plot" button.

### 2. Save/Load Parameters
Users can save their current simulation settings to a JSON file and reload them later. This makes it easy to compare different scenarios or continue simulations later.

### 3. Export to PDF
The plot and a detailed description of the simulation can be exported as a PDF file, which can be shared or printed for reports and presentations.

### 4. Save Simulation Data
Simulation results, including the time series of population values, are exportable to CSV for further analysis in tools like Excel or other data analysis platforms.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/population-growth-model.git
   cd population-growth-model
   ```

2. Install the required Python libraries:
   ```bash
   pip install numpy matplotlib scipy fpdf
   ```

3. Run the program:
   ```bash
   python advanced_population_growth.py
   ```

## How to Use:
1. Input values for the following parameters in the GUI:
   - Growth Rate (r)
   - Carrying Capacity (K)
   - Initial Population (P0)
   - Seasonal Factor
   - Immigration Rate
   - Noise Intensity
2. Click "Update Plot" to generate the population growth graph.
3. Save your parameter settings using the "Save Parameters" button and load them later with "Load Parameters."
4. Export the plot and description to PDF by clicking "Export to PDF."
5. Save the simulation data (time and population) to a CSV file by clicking "Save Data to CSV."

#Screenshots
