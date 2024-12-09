class Logger(object):
    def __init__(self, file_name):
        '''
        initialize the logger
        '''
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
       '''
       log the metadata
       '''
       with open(self.file_name, 'w') as log_file:
           log_file.write(f"Simulation Metadata:\n")
           log_file.write(f"Population Size: {pop_size}\n")
           log_file.write(f"Vaccination Percentage: {vacc_percentage}\n")
           log_file.write(f"Virus Name: {virus_name}\n")
           log_file.write(f"Mortality Rate: {mortality_rate}\n")
           log_file.write(f"Basic Reproduction Number: {basic_repro_num}\n")
           log_file.write(f"===========================================\n\n")

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        '''
        log detail of interactions
        '''
        with open(self.file_name, 'a') as log_file:
            log_file.write(f"Step {step_number} - Interactions:\n")
            log_file.write(f"Total Interactions: {number_of_interactions}\n")
            log_file.write(f"New Interactions: {number_of_new_infections}\n")
            log_file.write(f"============================================\n\n")

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        '''
        log the survival and fatalities 
        '''
        with open(self.file_name, 'a') as log_file:
            log_file.write(f"Step {step_number} - Infection Survival:\n")
            log_file.write(f"Current Population: {population_count}\n")
            log_file.write(f"New Fatalities: {number_of_new_fatalities}\n")
            log_file.write(f"==========================================\n\n")

    def log_step_summary(self, step_number, population_size, num_alive, num_dead, num_vaccinated):
        '''
        log summary of the current simulation
        '''
        with open(self.file_name, 'a') as log_file:
            log_file.write(f"Step {step_number} - summary:\n")
            log_file.write(f"Population Size: {population_size}\n")
            log_file.write(f"Alive: {num_alive}\n")
            log_file.write(f"Dead: {num_dead}\n")
            log_file.write(f"Vaccinated: {num_vaccinated}\n")
            log_file.write(f"========================================\n\n")

    def log_final_summary(self, total_steps, population_size, num_alive, num_dead, num_vaccinated):
        '''
        log final summary of simulation results
        '''
        with open(self.file_name, 'a') as log_file:
            log_file.write(f"Simulation Complete:\n")
            log_file.write(f"Total Steps: {total_steps}\n")
            log_file.write(f"Final Population Size: {population_size}\n")
            log_file.write(f"Alive: {num_alive}\n")
            log_file.write(f"Dead: {num_dead}\n")
            log_file.write(f"Vaccinated: {num_vaccinated}\n")
            log_file.write(f"========================================\n\n")
