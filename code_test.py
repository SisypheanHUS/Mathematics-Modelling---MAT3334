import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameters
N = 1_000_000
beta0 = 0.3       # baseline infection rate
alpha = 0.25      # seasonal amplitude
phi = 0.0         # phase shift
T = 365           # period (1 year)
sigma = 1/5.0     # incubation period = 5 days
gamma = 1/7.0     # infectious period = 7 days

def beta_t(t):
    return beta0 * (1 + alpha * np.sin(2*np.pi*t/T + phi))

def sier(y, t):
    S, E, I, R = y
    b = beta_t(t)
    dS = -b * S * I / N
    dE = b * S * I / N - sigma * E
    dI = sigma * E - gamma * I
    dR = gamma * I
    return [dS, dE, dI, dR]

# Initial conditions
E0, I0, R0 = 5, 10, 0
S0 = N - E0 - I0 - R0
y0 = [S0, E0, I0, R0]
t = np.linspace(0, 5*T, 5*T+1)  # 5 years, daily

sol = odeint(sier, y0, t)
S, E, I, R = sol.T

plt.figure(figsize=(10,5))
plt.plot(t/365, I, label='Infectious')
plt.plot(t/365, E, label='Exposed', linestyle='--')
plt.xlabel('Years')
plt.ylabel('Population')
plt.title('Seasonal SIER Model Simulation')
plt.legend()
plt.show()
