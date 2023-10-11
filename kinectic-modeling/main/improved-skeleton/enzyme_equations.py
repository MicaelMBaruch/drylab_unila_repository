class EnzymeEquations():
    def degradation_rate(
            self,
            enzyme_concentration: float,
            substrate_concentration: float,
            substrate_degradation_rate: float,
            enzyme_substrate_affinity_constant: float
            ) -> float:
        return - substrate_degradation_rate * enzyme_concentration * substrate_concentration/(enzyme_substrate_affinity_constant + substrate_concentration) 

    def enzyme_concentration(
            self,
            algae_mi
            ) -> float:
        Vmaxtx = 0.2 # ng/dia https://doi.org/10.1016/j.algal.2013.09.002
        Km = algae_mi/2  # estimated, please search for a decent value
        return (Vmaxtx * (algae_mi/ Km) )/ ((1 + ((algae_mi/ Km))))  # 10.1038/msb.2013.14


    def pet_degradation_rate(
            self,
            petase_concentration,
            pet_concentration
            ) -> float:
        if pet_concentration <= 0:
            return 0
        else:
            return - 33.5 * petase_concentration