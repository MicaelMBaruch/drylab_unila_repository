class DissolvedCO2:
    def __init__(self):
        self.k1 = 10 ^ ( -6.381)
        self.k2 = 10 ^ ( -10.377)
        self.ic = 0.1  # mg/m^3 - inorganic carbon concentration
    
    def hydrogen_ions(self, pH):
        return 10 ^ (- pH)

    def dissolved_co2(self, hco3_concentration, pH):
        return (hco3_concentration * self.hydrogen_ions(pH)) / self.k1
    
    def dissolved_hco3(self, pH):
        hydrogen_ions = self.hydrogen_ions(pH)
        return (hydrogen_ions * self.ic) / (self.k2 + hydrogen_ions + hydrogen_ions ** 2)