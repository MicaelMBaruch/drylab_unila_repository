import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

class WasteWaterSimulator():
    def __init__(self, Cx0, time_array, mi_max):
        self.Cx0 = Cx0
        self.time_array = time_array
        self.mi_max = mi_max
        self. maximum_algae_concentration = 0.003322  # uM/m^3

    def algae_concentration(self, time_array, mi_max):

        algae_concentrations_list = []
        for day in time_array:
            current_concentration = self.Cx0 * math.e ** (np.log(self.maximum_algae_concentration/self.Cx0) * (1 - math.e ** (-mi_max*day)))
            algae_concentrations_list.append(current_concentration)
        return algae_concentrations_list

    def mi_variation(self, day):
        current_mi = self.Cx0 * math.e ** (np.log(self.maximum_algae_concentration / self.Cx0) * (1 - math.e ** (-self.mi_max * day))) * np.log(self.maximum_algae_concentration / self.Cx0) * self.mi_max * math.e ** (-self.mi_max * day)
        return current_mi

    def enzyme_concentration(self):
        previous_concentration = 0
        enzyme_concentrations_list = []
        for algae_concentration in self.Cx_list:
            current_concentration = algae_concentration * 75 + previous_concentration * 0.7
            previous_concentration = current_concentration
            enzyme_concentrations_list.append(current_concentration)
        return enzyme_concentrations_list

    def pet_concentration(self, enzyme_concentrations, initial_pet_concentration):
        degradation_rate = 33.5
        previous_concentration = initial_pet_concentration
        pet_concentrations_list = []
        for day_concentration in enzyme_concentrations:
            current_pet_concentration = previous_concentration - day_concentration * degradation_rate
            if current_pet_concentration <= 0:
                current_pet_concentration = 0
            pet_concentrations_list.append(current_pet_concentration)
            previous_concentration = current_pet_concentration
        return pet_concentrations_list

    def simulate(self, initial_pet_concentration):
        self.Cx_list = self.algae_concentration(self.time_array, self.mi_max) 
        self.Cenz = self.enzyme_concentration()
        self.cpet = self.pet_concentration(self.Cenz, initial_pet_concentration)
        self.algae_concentration = pd.DataFrame([self.Cx_list, self.time_array])
        self.pet_concentration = pd.DataFrame([self.cpet, self.time_array])
        self.enzyme_concentration = pd.DataFrame([self.Cenz, self.time_array])

    def enzyme_production(self):  # doi/epdf/10.1038/msb.2013.14
        Vmaxtx = 0.2 # ng/dia https://doi.org/10.1016/j.algal.2013.09.002
        Km = self.mi_max/2  # estimated
        for day in self.time_array:
            k = (Vmaxtx * (self.mi_variation(day)/ Km) )/ ((1 + ((self.mi_variation(day)/ Km))))
        return k

    def plot_algae(self, title):
        plt.plot(self.time_array, self.Cx_list, label='C. reinhardtii Concentration', c='green', marker='o')
        plt.ylabel('C. reinhardtii [uM/m³]')
        plt.xlabel('Days')
        plt.grid('True')
        plt.gca().set_facecolor('#f2f2f2')  # Background color
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.legend()
        plt.xticks(self.time_array)
        plt.savefig(f'results/plt_Algae_concentration_{title}.png', dpi=300)  
        plt.legend()
        plt.show()

    def plot_enzyme(self, title):
        plt.plot(self.time_array, self.Cenz, label='PETase-MHETase concentration', c='red', marker='+')
        plt.ylabel('FPETase-MHETase [uM/m³]')
        plt.xlabel('Days')
        plt.grid('True')
        plt.gca().set_facecolor('#f2f2f2')  # Background color
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.legend()
        plt.xticks(self.time_array)
        plt.savefig(f'results/plt_enzyme_concentration_{title}.png', dpi=300)  
        plt.legend()
        plt.show()

    def plot_PET(self, title):
        plt.plot(self.time_array, self.cpet, label='PET concentration', c='black', marker='x')
        plt.ylabel('PET [mg/m³]')
        plt.xlabel('Days')
        plt.grid('True')
        plt.gca().set_facecolor('#f2f2f2')  # Background color
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.legend()
        plt.xticks(self.time_array)
        plt.yticks(self.cpet[::2])
        plt.savefig(f'results/plt_PET_concentration_{title}.png', dpi=300)  
        plt.show()
