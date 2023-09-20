class EnzymeEquations():
    def degradation_rate(self,
                         enzyme_concentration: float,
                         substrate_concentration: float,
                         substrate_degradation_rate: float,
                         enzyme_substrate_affinity_constant: float):
        return substrate_degradation_rate * enzyme_concentration * substrate_concentration/(enzyme_substrate_affinity_constant + substrate_concentration) 

    def enzyme_concentration(self,
                             algae_concentration: float,
                             enzyme_concentration: float,
                             expression_rate: float=1,  # falta (criei)
                             secretion_rate: float=1):  # falta  (criei)
        return algae_concentration*expression_rate*secretion_rate + enzyme_concentration  # falta (criei da minha cabeuça)

