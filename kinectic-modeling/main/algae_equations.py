import numpy as np


class AlgaeEquations():                       

    def irradiance_average(
            self,
            microalgae_concentration: float,
            irradiance_superfitial: float,
            depth: float=1.8,  # m
            biomass_extintion_coefficient: float=1  # falta criei
            ) -> float:
        return ((irradiance_superfitial / (biomass_extintion_coefficient * microalgae_concentration * depth)) * (1 - np.exp( - biomass_extintion_coefficient * microalgae_concentration * depth)) )

    def algae_mi_irradiance(
            self,
            irradiance_average: float,
            mi_max: float=38.184,
            irradiance_constant: float=168,
            form_parameter: float=1.7
            ) -> float:
        return mi_max * irradiance_average ** form_parameter/(irradiance_constant**form_parameter + irradiance_average**form_parameter)

    def algae_mi_temperature(
            self,
            temperature: float,
            algae_temperature_max: float=12.9,  
            algae_temperature_min: float =3.4,  
            algae_temperature_optimal: float=30
            ) -> float:  
        return ((temperature - algae_temperature_max)*(temperature - algae_temperature_min)**2)/((algae_temperature_optimal - algae_temperature_min) * (((algae_temperature_optimal - algae_temperature_min)* temperature - algae_temperature_optimal) - ((algae_temperature_optimal-algae_temperature_max)* (algae_temperature_optimal + algae_temperature_min -2*temperature))))

    def algae_mi_ph(
            self,
            medium_ph: float,
            algae_ph_max: float=12.9,
            algae_ph_min: float=1.8,
            algae_ph_optimal: float=8.5
            ) -> float:
        return ((medium_ph - algae_ph_max)*(medium_ph- algae_ph_min)**2)/((algae_ph_optimal - algae_ph_min) * (((algae_ph_optimal - algae_ph_min)* (medium_ph- algae_ph_optimal) - ((algae_ph_optimal-algae_ph_max) * (algae_ph_optimal + algae_ph_min -2*medium_ph)))))

    def algae_mi_dissolvedO2(
            self,
            dissolved_o2: float,
            algae_o2_max: float= 32,
            form_parameter: float= 4.150
            ) -> float:
        if dissolved_o2 != 0:
            return 1-(dissolved_o2/(dissolved_o2*algae_o2_max))**form_parameter
        else: 
            return 1

    def algae_mi_dissolvedCO2(
            self,
            co2_concentration: float,
            bicarbonate_concentration: float,
            half_saturation_constant: float= 4,
            inhibition_constant: float= 120000,
            form_parameter: float=1  # falta criei o valor
            ) -> float:
        return (co2_concentration + bicarbonate_concentration)/(half_saturation_constant + co2_concentration + bicarbonate_concentration + (co2_concentration**form_parameter)/inhibition_constant)

    def algae_mi_nitrate(
            self,
            nitrogen_concentration: float,
            form_parameter: float=1,  # falta criei o valor
            half_saturation_constant: float=2770,
            inhibition_constant: float=386600 
            ) -> float:
        return nitrogen_concentration/(half_saturation_constant + nitrogen_concentration + (nitrogen_concentration**form_parameter)/inhibition_constant)

    def algae_mi_amonium(
            self,
            nitrogen_concentration: float,
            half_saturation_constant: float=1540,
            inhibition_constant: float=571000,
            form_parameter: float=1  # falta criei
            ) -> float:
        return nitrogen_concentration/(half_saturation_constant +  nitrogen_concentration + (nitrogen_concentration ** form_parameter) / inhibition_constant)

    def algae_mi_p(
            self,
            phosphate_phosphorum_concentration: float,
            half_saturation_constant: float=430
            ) -> float:
        return phosphate_phosphorum_concentration / (phosphate_phosphorum_concentration + half_saturation_constant)

    def algae_manutention(
            self,
            irradiance_average: float,
            algae_respiration_min: float=0.01,
            algae_respiration_max: float=0.267,
            irradiance_required: float=134,
            form_parameter_resp: float=1.4
            ) -> float:
        return algae_respiration_min + (algae_respiration_max * irradiance_average ** form_parameter_resp/(irradiance_required ** form_parameter_resp + irradiance_average ** form_parameter_resp))

    def algae_mi(
            self,
            algae_mi_irradiance: float,
            algae_mi_temperature: float,  
            algae_mi_ph: float,  
            algae_mi_dissolvedO2: float,  
            algae_mi_dissolvedCO2: float, 
            algae_mi_nitrogen: float,  
            algae_mi_p: float,  
            algae_manutention: float
            ):
        return (algae_mi_irradiance * algae_mi_temperature * algae_mi_ph * algae_mi_dissolvedO2 * algae_mi_dissolvedCO2 * algae_mi_nitrogen * algae_mi_p)
    def calculate_mi(
            self,
            algae_concentration,
            irradiance_superfitial: float,
            temperature: float,
            medium_ph: float,
            dissolved_o2: float,
            co2_concentration: float,
            bicarbonate_concentration: float,
            nitrogen_concentration: float,
            amonium_concentration: float,
            phosphate_phosphorum_concentration: float
            ) -> float:
        irradiance_average = self.irradiance_average(algae_concentration, irradiance_superfitial)
        mi_irradiance = self.algae_mi_irradiance(irradiance_average)
        mi_temperature = self.algae_mi_temperature(temperature)
        mi_ph = self.algae_mi_ph(medium_ph)
        mi_dissolved_o2 = self.algae_mi_dissolvedO2(dissolved_o2)
        mi_dissolved_co2 = self.algae_mi_dissolvedCO2(co2_concentration, bicarbonate_concentration)
        if nitrogen_concentration > 0: mi_nitrogen =  self.algae_mi_nitrate(nitrogen_concentration) 
        else: mi_nitrogen = self.algae_mi_amonium(amonium_concentration)
        mi_phosphate = self.algae_mi_p(phosphate_phosphorum_concentration)
        manutention_expense = self.algae_manutention(irradiance_average)

        return self.algae_mi(
            mi_irradiance,
            mi_temperature,
            mi_ph,
            mi_dissolved_o2,
            mi_dissolved_co2,
            mi_nitrogen,
            mi_phosphate,
            manutention_expense
            ) 
