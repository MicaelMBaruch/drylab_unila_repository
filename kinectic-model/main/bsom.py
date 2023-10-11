class BSOM:  # Biodegradable Organic Soluble Matter
    def __init__(self):
        self.ygen_alg = 0.148
        self.ygen_het = 0.153
        self.ygen_nit = 0.149
        self.ycon_het = 0.478
    
    def bsom_concentration(self, algae_concentration, mi_alg, heterotrophic_bac_concentration, mi_het, nitrogen_bac_concentration, mi_nit):
        Cx = algae_concentration
        Chet = heterotrophic_bac_concentration 
        Cnit = nitrogen_bac_concentration
        return Cx * mi_alg * self.ygen_alg + Chet * mi_het * self.ygen_het + Cnit * mi_nit * self.ygen_nit - Chet * mi_het * self.ycon_het