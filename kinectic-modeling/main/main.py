"""Here we build and test our other codes :)"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import ode

#version 20-08-2023_01
#modeling the microalgae growth 

###"Complete" equations
def irradiance_average(irradiance_superficial, biomass_extintion_coefficient, microalgae_concentration):
    return 

def algae_mi_irradiance(irradiance_average, mi_max = 38.184, irradiance_constant= 168, form_parameter=1.7):
    
    return mi_max * irradiance_average ** form_parameter/(irradiance_constant**form_parameter + irradiance_average**form_parameter)

def algae_mi_temperature(temperature, algae_temperature_max = 12.9, algae_temperature_min = 3.4, algae_temperature_optimal = 30):
    
    return ((temperature - algae_temperature_max)*(temperature - algae_temperature_min)**2)/(algae_temperature_optimal - algae_temperature_min) * (((algae_temperature_optimal - algae_temperature_min)* temperature - algae_temperature_optimal) - ((algae_temperature_optimal-algae_temperature_max)* (algae_temperature_optimal + algae_temperature_min -2*temperature)))

def algae_mi_ph(medium_ph, algae_ph_max= 12.9, algae_ph_min= 1.8, algae_ph_optimal = 8.5): #constante
    
    return ((medium_ph - algae_ph_max)*(medium_ph- algae_ph_min)**2)/(algae_ph_optimal - algae_ph_min) * (((algae_ph_optimal - algae_ph_min)* medium_ph- algae_ph_optimal) - ((algae_ph_optimal-algae_ph_max)* (algae_ph_optimal + algae_ph_min -2*medium_ph)))

def algae_mi_dissolvedO2(dissolved_o2, algae_o2_max= 32, form_parameter= 4.150): # variável dependente
    
    return 1-(dissolved_o2/dissolved_o2*algae_o2_max)**form_parameter

def algae_mi_dissolvedCO2(co2_concentration, bicarbonate_concentration, half_saturation_constant= 0.004, inhibition_constant= 120, form_parameter= float):
    
    return (co2_concentration + bicarbonate_concentration)/(half_saturation_constant + co2_concentration + bicarbonate_concentration + (co2_concentration**form_parameter)/inhibition_constant)

def algae_mi_nitrate(nitrogen_concentration, form_parameter,  half_saturation_constant= 2.77, inhibition_constant =386.6 ):
    return nitrogen_concentration/(half_saturation_constant +  nitrogen_concentration + (nitrogen_concentration**form_parameter)/inhibition_constant)

def algae_mi_amonium(nitrogen_concentration,half_saturation_constant, inhibition_constant, form_parameter ):
    
    return nitrogen_concentration/(half_saturation_constant +  nitrogen_concentration + (nitrogen_concentration**form_parameter)/inhibition_constant)

def algae_mi_p(phosphate_phosphorum_concentration, half_saturation_constant):

    return phosphate_phosphorum_concentration/(phosphate_phosphorum_concentration+half_saturation_constant)

def algae_manutention(algae_respiration_min, algae_respiration_max, irradiance_average, irradiance_required, form_parameter_resp ):

    return algae_respiration_min + (algae_respiration_max*irradiance_average ** form_parameter_resp/(irradiance_required ** form_parameter_resp + irradiance_average ** form_parameter_resp))

def algae_mi(algae_mi_irradiance, algae_mi_temperature, algae_mi_ph, algae_mi_dissolvedO2, algae_mi_dissolvedCO2, algae_mi_nitrogen, algae_mi_p, algae_manutention):

    return (algae_mi_irradiance * algae_mi_temperature * algae_mi_ph * algae_mi_dissolvedO2 * algae_mi_dissolvedCO2 * algae_mi_nitrogen * algae_mi_p) - algae_manutention

def calculate_mi(irradiance_superfitial, temperature, medium_ph, dissolved_o2, co2_concentration, bicarbonate_concentration, nitrogen_concentration, phosphate_phosphorum_concentration):

    irradiance_average = irradiance_average(irradiance_superfitial)
    mi_irradiance = algae_mi_irradiance(irradiance_average)
    mi_temperature = algae_mi_temperature(temperature)
    mi_ph = algae_mi_ph(medium_ph)
    mi_dissolved_o2 = algae_mi_dissolvedO2(dissolved_o2)
    mi_dissolved_co2 = algae_mi_dissolvedCO2(co2_concentration, bicarbonate_concentration)
    if nitrogen_concentration > 0: mi_nitrogen =  algae_mi_nitrate(nitrogen_concentration) 
    else: mi_nitrogen = algae_mi_amonium(amonium_concentration)
    mi_phosphate = algae_mi_p(phosphate_phosphorum_concentration)
    manutention_expense = algae_manutention(irradiance_average)
    
    return algae_mi(mi_irradiance, mi_temperature, mi_ph, mi_dissolved_o2, mi_dissolved_co2, mi_nitrogen, mi_phosphate, manutention_expense) 

def degradation_rate(enzyme_concentration, substrate_concentration, substrate_degradation_rate, enzyme_substrate_affinity_constant): #Serve tanto para calcular a velocidade de formação de produto da fast petase quanto da mhetase, a ideia é deixar o código mais limpo
    return substrate_degradation_rate * enzyme_concentration*substrate_concentration/(enzyme_substrate_affinity_constant + substrate_concentration) 

### Equations we lack

def enzyme_concentration(algae_concentration, expression_rate, secretion_rate): #define a concentração enzimática e conecta o modelo de degradação com o modelo de crescimento 
    pass


###Skeleton of the ODE system:

def ODE_system(algae_concentration, petase_concentration, mhetase_concentration, pet_concentration, mhet_concentration, irradiance_superfitial, temperature, medium_ph, dissolved_o2, co2_concentration, bicarbonate_concentration, nitrogen_concentration, phosphate_phosphorum_concentration):

    mi = calculate_mi(irradiance_superfitial, temperature, medium_ph, dissolved_o2, co2_concentration, bicarbonate_concentration, nitrogen_concentration, phosphate_phosphorum_concentration)
    dalgae_dt = algae_concentration * mi
    dpetase_mhetase_dt = enzyme_concentration(algae_concentration)
    dpet_dt = pet_concentration - degradation_rate(petase_concentration, pet_concentration)
    dmhet_dt = mhet_concentration - degradation_rate(mhetase_concentration, mhet_concentration)

    return [dalgae_dt, dpetase_mhetase_dt, dpet_dt, dmhet_dt]

###Defining a scenario
#Duration
hidraulic_retention_period_days = 4.2
hidraulic_retention_period_hours = hidraulic_retention_period_days * 24
time = np.arange(0, hidraulic_retention_period_hours, 0.01 )
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
algae_concentration, petase_concentration, mhetase_concentration, pet_concentration, mhet_concentration = ode(ODE_system, scenario)

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