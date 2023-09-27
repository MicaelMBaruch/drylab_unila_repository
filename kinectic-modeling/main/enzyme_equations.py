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
            algae_concentration: float,
            expression_rate: float=1,  # falta (criei)
            secretion_rate: float=1  # falta  (criei)
            ) -> float:
        return algae_concentration * expression_rate * secretion_rate * 0.006  # falta (criei da minha cabeuça)

    def pet_degradation_rate(
            self,
            petase_concentration,
            pet_concentration
            ) -> float:
        if pet_concentration <= 0:
            return 0
        else:
            return - 33.5 * petase_concentration