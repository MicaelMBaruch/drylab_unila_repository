import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode

from ode_system import ODESystem


###Defining a scenario
#Duration
hidraulic_retention_period_days = 4.2
time = np.arange(0, hidraulic_retention_period_days, 0.01 )
#algae
algae_initial_concentration = float
#substrate
pet_initial_concentration = float
mhet_initial_concentration = float
#nutrients
amonium_concentration = 30.9 #+-1.5
nitrate_concentration = 0.4 #+-0.7
phospurum_phosphate_concentration = 119.2 #+-5.1
#enviroment
surface_irradiance = 0 #Ainda precisa ser definido, em miE/m2
#putting it all togheter
scenario = [algae_initial_concentration, 0, 0, pet_initial_concentration, mhet_initial_concentration]

###Results
algae_concentration, petase_concentration, mhetase_concentration, pet_concentration, mhet_concentration = ode(ODESystem, scenario)

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