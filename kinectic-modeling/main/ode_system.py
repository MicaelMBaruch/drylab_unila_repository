from enzyme_equations import EnzymeEquations
from algae_equations import AlgaeEquations


class ODESystem():
    def ode_system(self, y, t, variable_independents, fixed_independents) -> list:
        algae_concentration, petase_concentration, mhetase_concentration, pet_concentration, mhet_concentration = y
        irradiance_superfitial, temperature = variable_independents
        medium_ph, dissolved_o2, co2_concentration, bicarbonate_concentration, nitrogen_concentration, amonium_concentration, phosphate_phosphorum_concentration = fixed_independents
        algae_equations = AlgaeEquations()
        mi_max = algae_equations.calculate_mi(
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
        algae_concentration_variation = algae_concentration * 0.00
        petase_concentration_variation = enzyme_equations.enzyme_concentration(algae_concentration)
        mhetase_concentration_variation = enzyme_equations.enzyme_concentration(algae_concentration)
        if int(t)%2 == 0:
            petase_concentration_variation -= petase_concentration * 0.5
            mhetase_concentration_variation -= mhetase_concentration * 0.5
        pet_concentration_variation = enzyme_equations.pet_degradation_rate(petase_concentration, pet_concentration)  # criei (tirei do popo pra ser mais exato)
        mhet_concentration_variation = - enzyme_equations.degradation_rate(
            mhetase_concentration,
            mhet_concentration,
            substrate_degradation_rate=2384640,
            enzyme_substrate_affinity_constant=23.17
            )
        return [
            algae_concentration_variation,
            petase_concentration_variation,
            mhetase_concentration_variation,
            pet_concentration_variation,
            mhet_concentration_variation,
    ]
