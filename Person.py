import random
from Virus import Virus

class Person(object):
    ''' The simulation will contain people who will make up a population.'''

    def __init__(self, is_vaccinated, infection=None):
       
        self.is_alive = True #boolean
        self.is_vaccinated = is_vaccinated #boolean
        self.infection = infection #virus object
        
    def did_survive_infection(self):
        mortality_rate = self.infection.mortality_num
        if self.infection:
            random_float = random.randrange(0,1)
            if random_float < mortality_rate:
                self.is_alive = False
                return False
            else:
                self.is_vaccinated =  True
                self.infection = None
                return True

        