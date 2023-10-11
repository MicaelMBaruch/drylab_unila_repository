class HeteroTrophBac:
    def __intit__(self):
        self.mi_max = 1.235

    def final_mi(
            self,
            mi_temperature: float,  
            mi_ph: float,  
            mi_dissolvedO2: float,  
            mi_nitrogen: float,  
            mi_phosphorum: float,  
            manutention: float
    ):
        return self.mi_max * (mi_temperature * mi_ph * mi_dissolvedO2 * mi_nitrogen * mi_phosphorum) - manutention

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

    def mi_bsom(
                self,
                bsom_concentration,
                half_concentration_bsom
        ):
            return bsom_concentration/(bsom_concentration + half_concentration_bsom)

    def mi_O2(
            self,
            dissolved_o2: float,
            half_saturation_o2
            ) -> float:
            return dissolved_o2/(dissolved_o2 + half_saturation_o2)

    def mi_amonium(
            self,
            nitrogen_concentration: float,
            half_saturation_constant: float=1540,
            inhibition_constant: float=571000,
            form_parameter: float=1  # falta criei
            ) -> float:
        return nitrogen_concentration/(half_saturation_constant +  nitrogen_concentration + (nitrogen_concentration ** form_parameter) / inhibition_constant)

    def mi_po4(
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

