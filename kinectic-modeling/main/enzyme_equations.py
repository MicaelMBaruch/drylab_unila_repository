
class EnzymeEquations():
    def degradation_rate(self,
                         enzyme_concentration,
                         substrate_concentration,
                         substrate_degradation_rate,
                         enzyme_substrate_affinity_constant): 
        return substrate_degradation_rate * enzyme_concentration * substrate_concentration/(enzyme_substrate_affinity_constant + substrate_concentration) 

    def enzyme_concentration(self,
                             algae_concentration,
                             expression_rate,
                             secretion_rate):  # define a concentração enzimática e conecta o modelo de degradação com o modelo de crescimento 
        pass  # falta

