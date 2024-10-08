# population-growth-model
This project simulates population growth using the logistic growth model, with additional features like seasonal variations, immigration, and stochastic noise. The simulation is implemented using numerical methods such as SciPy's odeint and Euler's method, and provides an interactive graphical user interface (GUI) for easy parameter manipulation. Users can save their settings, export the simulation results to CSV, and save the plot and model description as a PDF.

Technologies Used:

Python: The main programming language used for the simulation and GUI.
Tkinter: Used for creating the graphical user interface.
Matplotlib: For plotting the simulation results.
SciPy: For solving differential equations (odeint method).
FPDF: To export the plot and description to PDF.
CSV Module: To save the simulation data to a CSV file.
How It Works:

The project simulates population growth using the following logistic growth equation:
d
P
d
t
=
r
P
(
1
−
P
K
)
+
immigration_rate
dt
dP
​	
 =rP(1− 
K
P
​	
 )+immigration_rate
Where:
P
P is the population size.
r
r is the growth rate.
K
K is the carrying capacity (can vary seasonally).
Immigration rate adds a constant number of individuals to the population.
The model can include seasonal variations where 
K
t
K 
t
​	
  changes periodically:
K
t
=
K
(
1
+
seasonal_factor
⋅
sin
⁡
(
2
π
t
365
)
)
K 
t
​	
 =K(1+seasonal_factor⋅sin( 
365
2πt
​	
 ))
The population growth is simulated over time, and the plot shows how the population evolves based on user-defined parameters.
Features Overview:

1. Interactive GUI
The Tkinter-based graphical interface allows users to input parameters for the simulation, including growth rate, carrying capacity, initial population, seasonal factor, immigration rate, and noise intensity. The model automatically updates the plot when the user clicks the "Update Plot" button.
2. Save/Load Parameters
Users can save their current simulation settings to a JSON file and reload them later. This makes it easy to compare different scenarios or continue simulations later.
3. Export to PDF
The plot and a detailed description of the simulation can be exported as a PDF file, which can be shared or printed for reports and presentations.
4. Save Simulation Data
Simulation results, including the time series of population values, are exportable to CSV for further analysis in tools like Excel or other data analysis platforms.
Installation

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/population-growth-model.git
cd population-growth-model
Install the required Python libraries:
bash
Copy code
pip install numpy matplotlib scipy fpdf
Run the program:
bash
Copy code
python advanced_population_growth.py
How to Use:

Input values for the following parameters in the GUI:
Growth Rate (r)
Carrying Capacity (K)
Initial Population (P0)
Seasonal Factor
Immigration Rate
Noise Intensity
Click "Update Plot" to generate the population growth graph.
Save your parameter settings using the "Save Parameters" button and load them later with "Load Parameters."
Export the plot and description to PDF by clicking "Export to PDF."
Save the simulation data (time and population) to a CSV file by clicking "Save Data to CSV."
