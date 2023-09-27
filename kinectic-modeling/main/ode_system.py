from enzyme_equations import EnzymeEquations
from algae_equations import AlgaeEquations
import warnings

class ODESystem():
    def ode_system(self, t, y, variable_independents, fixed_independents) -> list:
        print(t)
        algae_concentration, petase_concentration, mhetase_concentration, pet_concentration, mhet_concentration = y
        irradiance_superfitial_list, temperature_list, = variable_independents
        irradiance_superfitial = irradiance_superfitial_list[int(t)]
        temperature = temperature_list[int(t)]
        medium_ph, dissolved_o2, co2_concentration, bicarbonate_concentration, nitrogen_concentration, amonium_concentration, phosphate_phosphorum_concentration, volume = fixed_independents
        print(irradiance_superfitial)
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
        if algae_concentration < 0:
            warnings.warn(f'concentração de algas inválida: {algae_concentration}', UserWarning)
        petase_concentration = enzyme_equations.enzyme_concentration(algae_concentration, petase_concentration)
        mhetase_concentration = enzyme_equations.enzyme_concentration(algae_concentration, petase_concentration)
        pet_concentration = enzyme_equations.pet_degradation_rate(pet_concentration, volume, petase_concentration)  # criei (tirei do popo pra ser mais exato)
        mhet_concentration = mhet_concentration - enzyme_equations.degradation_rate(
            mhetase_concentration,
            mhet_concentration,
            substrate_degradation_rate=21600,
            enzyme_substrate_affinity_constant=23.17
            )
        # print(pet_concentration)
        return [
            algae_concentration,
            petase_concentration,
            mhetase_concentration,
            pet_concentration,
            mhet_concentration,
    ]
