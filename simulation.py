import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        '''
        Initialize the simulation 
        '''
        self.logger = Logger("simulation_log.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.newly_infected = []

        self.logger.write_metadata(
            pop_size, vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate
        )

    def _create_population(self):
        '''
        creates the initial pop
        '''
        population = []
        for i in range(self.pop_size):
            if i < self.initial_infected:
                population.append(Person(i, is_vaccinated=False, infection=self.virus))
            else:
                is_vaccinated = random.random() < self.vacc_percentage
                population.append(Person(i, is_vaccinated=is_vaccinated))
        return population

    def _simulation_should_continue(self):
        '''
        Determines if the simulation should continue.
        '''
        alive_people = [person for person in self.population if person.is_alive]
        if not alive_people or all(person.is_vaccinated for person in alive_people):
            return False
        return True

    def run(self):
        '''
        Runs Simulation
        '''
        time_step_counter = 0
        while self._simulation_should_continue():
            time_step_counter += 1
            self.time_step()
        # log final results
        alive_people = [p for p in self.population if p.is_alive]
        vaccinated_count = sum(1 for p in alive_people if p.is_vaccinated)
        dead_count = self.pop_size - len(alive_people)
        self.logger.log_final_summary(
            time_step_counter, self.pop_size, len(alive_people), dead_count, vaccinated_count
        )

    def time_step(self):
        '''
        simulates a single time step, including interactions and infection updates
        '''
        for person in self.population:
            if person.is_alive and person.infection:
                interactions = 0
                while interactions < 100:
                    random_person = random.choice(self.population)
                    if random_person.is_alive and random_person != person:
                        self.interaction(person, random_person)
                        interactions += 1
        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        '''
        handles an interaction between an infected person and another person
        '''
        if random_person.is_vaccinated or random_person.infection:
            return
        
        if random.random() < self.virus.repro_rate:
            self.newly_infected.append(random_person)

    def _infect_newly_infected(self):
        '''
        infects all people in the 'newly_infected' list
        '''
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10


    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)


    sim.run()
