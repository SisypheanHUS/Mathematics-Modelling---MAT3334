# Seasonal Epidemic Simulation using the SIER Model

## Overview
This project models and simulates the spread of infectious diseases using the **SIER model** (Susceptible–Infected–Exposed–Recovered) with **seasonal transmission dynamics**.  
By introducing a periodic infection rate that varies over time, the simulation captures real-world effects such as seasonal outbreaks or periodic waves of infection.

---

## Model Description
The classical SIER model divides the population into four compartments:

- **S (Susceptible)**: individuals who can be infected  
- **E (Exposed)**: infected but not yet infectious  
- **I (Infected)**: actively infectious individuals  
- **R (Recovered)**: recovered and immune individuals  

The model is governed by the following differential equations:

\[
\begin{aligned}
\frac{dS}{dt} &= -\beta(t) \frac{S I}{N} \\
\frac{dE}{dt} &= \beta(t) \frac{S I}{N} - \sigma E \\
\frac{dI}{dt} &= \sigma E - \gamma I \\
\frac{dR}{dt} &= \gamma I
\end{aligned}
\]

where:
- \( \beta(t) = \beta_0 \times (1 + \alpha \sin(2\pi t / T)) \) introduces **seasonal variation** in transmission rate  
- \( \sigma \): rate of exposed individuals becoming infectious  
- \( \gamma \): recovery rate  
- \( N \): total population  

---

## Implementation
The simulation is implemented in **Python** using:
- `numpy` for numerical operations  
- `scipy.integrate.odeint` for solving ODEs  
- `matplotlib` for visualization  

