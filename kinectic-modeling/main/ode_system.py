from enzyme_equations import EnzymeEquations
from algae_equations import AlgaeEquations


class ODESystem():
    def __init__(
            algae_concentration,
            petase_concentration,
            mhetase_concentration,
            pet_concentration,
            mhet_concentration,
            irradiance_superfitial,
            temperature,
            medium_ph,
            dissolved_o2,
            co2_concentration,
            bicarbonate_concentration,
            nitrogen_concentration,
            amonium_concentration,
            phosphate_phosphorum_concentration) -> list:
        mi = AlgaeEquations.calculate_mi(irradiance_superfitial,
                                         temperature,
                                         medium_ph,
                                         dissolved_o2,
                                         co2_concentration,
                                         bicarbonate_concentration,
                                         nitrogen_concentration,
                                         amonium_concentration,
                                         phosphate_phosphorum_concentration)
        dalgae_dt = algae_concentration * mi
        dpetase_mhetase_dt = EnzymeEquations.enzyme_concentration(algae_concentration)
        dpet_dt = pet_concentration - EnzymeEquations.degradation_rate(petase_concentration, pet_concentration)
        dmhet_dt = mhet_concentration - EnzymeEquations.degradation_rate(mhetase_concentration, mhet_concentration)

        return [dalgae_dt, dpetase_mhetase_dt, dpet_dt, dmhet_dt]
