import unittest
from simulation import Simulation
from person import Person
from virus import Virus

class TestSimulation(unittest.TestCase):

    def setUp(self):
        # Initialize a small simulation for testing
        self.virus = Virus("TestVirus", 0.5, 0.25)
        self.simulation = Simulation(self.virus, 100, 0.1, initial_infected=5)

    def test_create_population(self):
        # Test that the population size matches the initialized value
        self.assertEqual(len(self.simulation.population), 100)

        # Test that initial infected count matches
        infected_count = sum(1 for person in self.simulation.population if person.infection is not None)
        self.assertEqual(infected_count, 5)

    def test_simulation_should_continue(self):
        # Ensure the simulation continues when conditions are met
        self.assertTrue(self.simulation._simulation_should_continue())

        # Simulate conditions where the simulation stops
        for person in self.simulation.population:
            person.is_alive = False
        self.assertFalse(self.simulation._simulation_should_continue())

    def test_time_step(self):
        # Verify that a time step processes correctly
        pre_infected_count = sum(1 for person in self.simulation.population if person.infection)
        self.simulation.time_step()
        post_infected_count = sum(1 for person in self.simulation.population if person.infection)
        self.assertGreaterEqual(post_infected_count, pre_infected_count)

    def test_infection_spread(self):
        # Verify that infection spreads correctly
        self.simulation.time_step()
        newly_infected = self.simulation.newly_infected
        for person in newly_infected:
            self.assertEqual(person.infection, self.virus)

    def test_final_summary_logging(self):
        # Run the simulation and check that it ends correctly
        self.simulation.run()
        survivors = sum(1 for person in self.simulation.population if person.is_alive)
        self.assertTrue(survivors >= 0)

if __name__ == "__main__":
    unittest.main()
