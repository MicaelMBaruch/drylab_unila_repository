import numpy as np
import matplotlib.pyplot as plt
import math

class WasteWaterSimulator():
    def __init__(self, Cx0, time_array, mi_max):
        self.Cx0 = Cx0
        self.time_array = time_array
        self.mi_max = mi_max

    def algae_concentration(self, initial_concentration, time_array, mi_max):
        maximum_algae_concentration = 0.003322
        algae_concentrations_list = []
        for day in time_array:
            current_concentration = initial_concentration * math.e ** (np.log(maximum_algae_concentration/initial_concentration) * 1 - math.e ** (-mi_max*day))
            algae_concentrations_list.append(current_concentration)
        return algae_concentrations_list


    def enzyme_concentration(self):
        previous_concentration = 0
        enzyme_concentrations_list = []
        for day_concentration in self.Cx_list:
            current_concentration = day_concentration * 75 + previous_concentration * 0.7
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
        self.Cx_list = self.algae_concentration(self.Cx0, self.time_array, self.mi_max) 
        self.Cenz = self.enzyme_concentration()
        self.cpet = self.pet_concentration(self.Cenz, initial_pet_concentration)

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

