class NitrateNitrogen:
    def __init__(self, initial_concentration):
        self.ycon_alg = 0.214
        self.ygen_nit = 0.355
        self.initial_concentration = initial_concentration

    def nitrate_nitrogen_concentration(self, algae_concentration, mi_alg, nit_bac_concentration, mi_nit):
        Cx = algae_concentration
        Cnit = nit_bac_concentration
        return Cnit * mi_nit * self.ygen_nit - Cx * mi_alg * self.ycon_alg  # checar se realmetne é Cnit ou outra coisa no bioalgae