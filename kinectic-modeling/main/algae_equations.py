import numpy as np


class AlgaeEquations():                       

    def irradiance_average(
            self,
            microalgae_concentration: float,
            irradiance_superfitial: float,
            depth: float=1.8,  # m
            biomass_extintion_coefficient: float=0.000007  # m2/mg
            ) -> float:
        return ((irradiance_superfitial / (biomass_extintion_coefficient * microalgae_concentration * depth)) * (1 - np.exp( - biomass_extintion_coefficient * microalgae_concentration * depth)) )

    def mi_irradiance(
            self,
            irradiance_average: float,
            mi_max: float=38.184,
            irradiance_constant: float=168,
            form_parameter: float=1.7
            ) -> float:
        return mi_max * irradiance_average ** form_parameter/(irradiance_constant**form_parameter + irradiance_average**form_parameter)

    def mi_temperature(
            self,
            temperature: float,
            temperature_max: float=12.9,  
            temperature_min: float =3.4,  
            temperature_optimal: float=30
            ) -> float:  
        return ((temperature - temperature_max)*(temperature - temperature_min)**2)/((temperature_optimal - temperature_min) * (((temperature_optimal - temperature_min)* temperature - temperature_optimal) - ((temperature_optimal-temperature_max)* (temperature_optimal + temperature_min -2*temperature))))

    def mi_ph(
            self,
            medium_ph: float,
            ph_max: float=12.9,
            ph_min: float=1.8,
            ph_optimal: float=8.5
            ) -> float:
        return ((medium_ph - ph_max)*(medium_ph- ph_min)**2)/((ph_optimal - ph_min) * (((ph_optimal - ph_min)* (medium_ph- ph_optimal) - ((ph_optimal-ph_max) * (ph_optimal + ph_min -2*medium_ph)))))

    def mi_dissolvedO2(
            self,
            dissolved_o2: float,
            o2_max: float= 32,
            form_parameter: float= 4.150
            ) -> float:
        if dissolved_o2 != 0:
            return 1-(dissolved_o2/(dissolved_o2*o2_max))**form_parameter
        else: 
            return 1

    def mi_dissolvedCO2(
            self,
            co2_concentration: float,
            bicarbonate_concentration: float,
            half_saturation_constant: float= 4,
            inhibition_constant: float= 120000,
            form_parameter: float=1  # falta criei o valor
            ) -> float:
        return (co2_concentration + bicarbonate_concentration)/(half_saturation_constant + co2_concentration + bicarbonate_concentration + (co2_concentration**form_parameter)/inhibition_constant)

    def mi_nitrate(
            self,
            nitrogen_concentration: float,
            form_parameter: float=1,  # falta criei o valor
            half_saturation_constant: float=2770,
            inhibition_constant: float=386600 
            ) -> float:
        return nitrogen_concentration/(half_saturation_constant + nitrogen_concentration + (nitrogen_concentration**form_parameter)/inhibition_constant)

    def mi_amonium(
            self,
            nitrogen_concentration: float,
            half_saturation_constant: float=1540,
            inhibition_constant: float=571000,
            form_parameter: float=1  # falta criei
            ) -> float:
        return nitrogen_concentration/(half_saturation_constant +  nitrogen_concentration + (nitrogen_concentration ** form_parameter) / inhibition_constant)

    def mi_p(
            self,
            phosphate_phosphorum_concentration: float,
            half_saturation_constant: float=430
            ) -> float:
        return phosphate_phosphorum_concentration / (phosphate_phosphorum_concentration + half_saturation_constant)

    def manutention(
            self,
            irradiance_average: float,
            respiration_min: float=0.01,
            respiration_max: float=0.267,
            irradiance_required: float=134,
            form_parameter_resp: float=1.4
            ) -> float:
        return respiration_min + (respiration_max * irradiance_average ** form_parameter_resp/(irradiance_required ** form_parameter_resp + irradiance_average ** form_parameter_resp))

    def mi(
            self,
            mi_irradiance: float,
            mi_temperature: float,  
            mi_ph: float,  
            mi_dissolvedO2: float,  
            mi_dissolvedCO2: float, 
            mi_nitrogen: float,  
            mi_p: float,  
            manutention: float
            ):
        return (mi_irradiance * mi_temperature * mi_ph * mi_dissolvedO2 * mi_dissolvedCO2 * mi_nitrogen * mi_p) - manutention

    def calculate_mi(
            self,
            concentration,
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
        irradiance_average = self.irradiance_average(concentration, irradiance_superfitial)
        mi_irradiance = self.mi_irradiance(irradiance_average)
        mi_temperature = self.mi_temperature(temperature)
        mi_ph = self.mi_ph(medium_ph)
        mi_dissolved_o2 = self.mi_dissolvedO2(dissolved_o2)
        mi_dissolved_co2 = self.mi_dissolvedCO2(co2_concentration, bicarbonate_concentration)
        if nitrogen_concentration > 0: mi_nitrogen =  self.mi_nitrate(nitrogen_concentration) 
        else: mi_nitrogen = self.mi_amonium(amonium_concentration)
        mi_phosphate = self.mi_p(phosphate_phosphorum_concentration)
        manutention_expense = self.manutention(irradiance_average)

        return self.mi(
            mi_irradiance,
            mi_temperature,
            mi_ph,
            mi_dissolved_o2,
            mi_dissolved_co2,
            mi_nitrogen,
            mi_phosphate,
            manutention_expense
            ) 
