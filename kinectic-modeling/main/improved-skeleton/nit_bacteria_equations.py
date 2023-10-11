class NitrifyingBac:
    def __init__(self, initial_concentration):
        self.mi_max = 0.730
        self.initial_concentration = initial_concentration
        self.current_concentration = initial_concentration

    def mi(
        self,
        mi_temperature: float,  
        mi_ph: float,  
        mi_dissolvedO2: float,  
        mi_dissolvedCO2: float, 
        mi_nitrogen: float,  
        mi_p: float,  
        manutention: float
    ):
        return self.mi_max * (mi_temperature * mi_ph * mi_dissolvedO2 * mi_dissolvedCO2 * mi_nitrogen * mi_p) - manutention


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
            half_saturation_o2: float,
            inhibition_constant_o2: float
            ) -> float:
        return (dissolved_o2/(dissolved_o2 + half_saturation_o2)) * (1 + dissolved_o2/inhibition_constant_o2)

    def mi_dissolvedCO2(
            self,
            co2_concentration: float,
            bicarbonate_concentration: float,
            half_saturation_constant: float= 4,
            inhibition_constant: float= 120000,
            form_parameter: float=1  # falta criei o valor
            ) -> float:
        return (co2_concentration + bicarbonate_concentration)/(half_saturation_constant + co2_concentration + bicarbonate_concentration + (co2_concentration**form_parameter)/inhibition_constant)

    def mi_amonium(
            self,
            nitrogen_concentration: float,
            half_saturation_constant: float=1540
            ) -> float:
        return nitrogen_concentration/(half_saturation_constant +  nitrogen_concentration)

    def mi_p(
            self,
            phosphate_phosphorum_concentration: float,
            half_saturation_constant: float
            ) -> float:
        return phosphate_phosphorum_concentration / (phosphate_phosphorum_concentration + half_saturation_constant)

