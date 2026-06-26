**1.Project Objective:**

This project aims to simulate vertical rocket launches using numerical methods and progressively more realistic physical models.

The main objective is to study how different variables such as gravity acceleration, air density, mass and thrust not being constant affect the rocket's maximum speed, and maximum altitude by implementing and improving the simulation step by step. 

**2.Methodology:**

Instead of building a fully complex model from the beginning, the simulation starts with simpler assumptions and progressively adds new physical factors.

*Current progression:*

*Level 1:*

- Constant gravity
- Constant air density
- Constant mass

*Level 2 (current):*

- Variable gravity
- Variable mass

*Level 3:*

- Variable atmospheric density and pressure
- (affecting DRAG resistance and fuel combustion efficiency)

*Future versions:*

- Multi-stage rockets
- Escape velocity analysis

Each version is documented separately to show the evolution of the model and the impact of each physical improvement.

**3.Reference Environment:**

The simulation uses rocket and planetary parameters based on the Kerbin system from Kerbal Space Program.

Kerbal Space Program is a spaceflight simulator widely recognized for its strong physics-based mechanics, including realistic orbital dynamics, fuel consumption, thrust-to-weight ratio, drag, and staging systems.

Although Kerbin is a fictional planet, its physical parameters are internally consistent and provide a reliable environment for testing and validating launch dynamics.

*Important differences from Earth:*

- Surface gravity is approximately equal to Earth
- Radius is 10 times smaller
- Mass is 100 times smaller
- Atmospheric limit at 70 km

These differences significantly affect gravitational and atmospheric behavior throughout the flight.

**4.Validation and Comparison:**

To validate the simulation results, this project compares its outputs against data collected from Kerbal Space Program.

The comparison includes:

- Maximum velocity
- Maximum altitude
- Velocity at burnout
- Altitude at maximum velocity
- Percentage error between simulation and game data

This validation process helps measure how close the mathematical model is to the simulated environment.
