from enzyme_equations import EnzymeEquations
from algae_equations import AlgaeEquations


class ODESystem():
    def ode_system(self, t, y) -> list:
        algae_concentration, petase_concentration, mhetase_concentration, pet_concentration, mhet_concentration, irradiance_superfitial, temperature, medium_ph, dissolved_o2, co2_concentration, bicarbonate_concentration, nitrogen_concentration, amonium_concentration, phosphate_phosphorum_concentration = y
        algae_equations = AlgaeEquations()
        mi = algae_equations.calculate_mi(
            algae_concentration,
            irradiance_superfitial,
            temperature,
            medium_ph,
            dissolved_o2,
            co2_concentration,
            bicarbonate_concentration,
            nitrogen_concentration,
            amonium_concentration,
            phosphate_phosphorum_concentration
            )
        enzyme_equations = EnzymeEquations()
        algae_concentration = algae_concentration * mi
        petase_concentration = enzyme_equations.enzyme_concentration(algae_concentration, petase_concentration)
        mhetase_concentration = enzyme_equations.enzyme_concentration(algae_concentration, petase_concentration)
        pet_concentration = pet_concentration - 0.0335 * petase_concentration  # criei (tirei do popo pra ser mais exato)
        mhet_concentration = mhet_concentration - enzyme_equations.degradation_rate(
            mhetase_concentration,
            mhet_concentration,
            substrate_degradation_rate=21600,
            enzyme_substrate_affinity_constant=23.17
            )

        return [
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
            phosphate_phosphorum_concentration
            ]
