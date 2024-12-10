class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        with open(self.file_name, 'a') as log_file:
            log_file.write("\n--- New Simulation ---\n")
            log_file.write(
                f"Population Size: {pop_size}\n"
                f"Vaccination Percentage: {vacc_percentage}\n"
                f"Virus: {virus_name}\n"
                f"Mortality Rate: {mortality_rate}\n"
                f"Reproduction Rate: {basic_repro_num}\n\n"
            )

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        with open(self.file_name, 'a') as log_file:
            log_file.write(
                f"Step {step_number}:\n"
                f"Interactions: {number_of_interactions}\n"
                f"New Infections: {number_of_new_infections}\n\n"
            )

    def log_final_summary(self, steps, pop_size, living, dead, vaccinated):
        with open(self.file_name, 'a') as log_file:
            log_file.write("\n--- Simulation End ---\n")
            log_file.write(
                f"Steps Taken: {steps}\n"
                f"Final Population Size: {pop_size}\n"
                f"Living: {living}\n"
                f"Dead: {dead}\n"
                f"Vaccinated: {vaccinated}\n\n"
            )
