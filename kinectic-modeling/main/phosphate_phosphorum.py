class PhosphatePhosphorous:
    def __init__(self, initial_concentration):
        self.ycon_alg = 0.008
        self.ycon_nit = 0.182
        self.ycon_het = 0.017
        self.initial_concentration = initial_concentration

    def concentration(self, algae_concentration, mi_alg, het_bac_concentration, mi_het, nit_bac_concentration, mi_nit):
        Cx = algae_concentration
        Chet = het_bac_concentration
        Cnit = nit_bac_concentration
        return - Cnit * mi_nit * self.ycon_nit + Cx * mi_alg * self.ycon_alg + Chet * mi_het * self.ycon_het  # checar se realmetne é Cnit ou outra coisa no bioalgae