import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from ode_system import ODESystem
from algae_equations import AlgaeEquations
from het_bacteria_equations import HeteroTrophBac
from nit_bacteria_equations import NitrifyingBac
from dissolved_co2 import DissolvedCO2
from bsom import BSOM
from amonium_nitrogen import AmoniumNitrogen
from nitrate_nitrogen import NitrateNitrogen
from phosphate_phosphorum import PhosphatePhosphorous
from enzyme_equations import EnzymeEquations

#  Defining a scenario
# organisms
algae = AlgaeEquations(0.003322 * 10^(-4))
het_bac = HeteroTrophBac()
nit_bac = NitrifyingBac()

# nutrients
co2 = DissolvedCO2()
bsom = BSOM()
amonium_nitrogen = AmoniumNitrogen()
nitrate_nitrogen = NitrateNitrogen()
phosphate_phosphorous = PhosphatePhosphorous()

# enviromental conditions
o2 = 125
av_temperature = 32
pH = 7.8
superficial_irradiance = 934

# enzymes
pet_mhetase = EnzymeEquations()

# equation system
co2.dissolved_hco3()
co2.dissolved_co2()
bsom.bsom_concentration()
amonium_nitrogen.amonium_nitrogen_concentration()
nitrate_nitrogen.nitrate_nitrogen_concentration()
phosphate_phosphorous.concentration()

algae_mi = algae.calculate_mi()
het_mi = het_bac = het_bac.mi()
nit_mi = nit_bac = nit_bac.mi()
algae.current_concentration = algae_mi * algae.current_concentration
het_bac.current_concentration = het_mi * het_bac.current_concentration
nit_bac.current_concentration = nit_mi * nit_bac.current_concentration

# duration
time_array = np.arange(0, 21, 1)