import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from ode_system import ODESystem


###Defining a scenario
#Duration
hidraulic_retention_period_days = 4.2
time = np.arange(0, hidraulic_retention_period_days, 0.6)
#algae
algae_initial_concentration = 10
#substrate
pet_initial_concentration = 10
mhet_initial_concentration = 0
#nutrients
amonium_concentration = 30.9  # +-1.5
nitrate_concentration = 0.4  # +-0.7
phosphate_phosphorum_concentration = 119.2  # +-5.1
#enviroment
irradiance_superfitial = 0  # Ainda precisa ser definido, em miE/m2
temperature = 30  # graus celsius
medium_ph = 7  # pH
dissolved_o2 = 0
bicarbonate_concentration = 288
co2_concentration = 3000000  # falta, inventei valor super alto para que seja irrelevante

#putting it all togheter
petase_concentration, mhetase_concentration = [0,0]
scenario = [algae_initial_concentration,
            petase_concentration,
            mhetase_concentration,
            pet_initial_concentration,
            mhet_initial_concentration,
            irradiance_superfitial,
            temperature,
            medium_ph,
            dissolved_o2,
            co2_concentration,
            bicarbonate_concentration,
            nitrate_concentration,
            amonium_concentration,
            phosphate_phosphorum_concentration]

###Results
ode_system = ODESystem()
results = solve_ivp(ode_system.ode_system, (4.2, 0), scenario)
algae_concentration, petase_concentration, mhetase_concentration, pet_concentration, mhet_concentration, irradiance_superfitial, temperature, medium_ph, dissolved_o2, co2_concentration, bicarbonate_concentration, nitrogen_concentration, amonium_concentration, phosphate_phosphorum_concentration = results.y
print(f'algae concentration: {algae_concentration}\n -----------\n petase concentration: {petase_concentration}\n ---------\npet concentration: {pet_concentration}\n ---------')
###ploting the results
plt.figure(figsize=(10, 6))
plt.plot(time, algae_concentration, label='Algae Concentration')
plt.plot(time, pet_concentration, label='PET Concentration')
plt.plot(time, mhet_concentration, label='MHET Concentration')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.title('Microalgae and PET/MHET Concentrations Over Time')
plt.show()