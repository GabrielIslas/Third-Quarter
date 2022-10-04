from itertools import product # Used to create the combinations of letters
# Animal class
Animal = lambda iq, species, capabilities: (iq, species, capabilities)

superiorIntelligence = lambda animal, addIQ: (animal[0] + addIQ, animal[1], animal[2])

pinkify = lambda animal: (animal[0], animal[1], [])

def superpowers(animal):
    if animal[1] == "elephant":
        return (animal[0], animal[1], animal[2].append("not to be afraid of mice"))
    elif animal[1] == "mouse" and animal[0] > 100:
        return (animal[0], animal[1], animal[2].append("speak"))
    else:
        return animal

anthropomorphic = lambda animal: True if animal[0] > 60 and "speak" in animal[1] else False

def pinkiesco(ability):
    abilityWords = ability.split(" ") # Divide ability into list based on whitespace
    if len(abilityWords) != 2: # Check that there is only two words
        return False
    if abilityWords[0] != "do": # Check that the first word is "do"
        return False
    if len(abilityWords[1]) > 4: # Check that the second word is 4 letters or less
        return False
    totalVowelCount = (abilityWords[1].count("a") +  # Counting vowels on the word
                    abilityWords[1].count("e") + 
                    abilityWords[1].count("i") + 
                    abilityWords[1].count("o") + 
                    abilityWords[1].count("u"))
    if totalVowelCount != 1: # Check if there is only one vowel
        return False
    return True

pinkCount = lambda animal: sum(map(pinkiesco, animal[2]))

notSoSane = lambda animal: pinkCount(animal) > 2

def generateWords(length):
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n','p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    if length > 4: # Pinkiesco words are 4 letters or less
        return
    elif length == 1: # One letter pinkiesco words are one vowel
        for vowel in vowels:
            print(vowel)
        return
    elif length == 3 or length == 4: # Get consonant combinations for words of 3 and 4
        consonants = list(product(consonants, repeat = length - 1)) # Cartesian product of letters
        for index in range(len(consonants)):
            consonants[index] = "".join(consonants[index]) # Convert tuples into strings
    for index in range(length): # Combine vowels with consonants
        for vowel in vowels: 
            for consonant in consonants:
                print(consonant[:index] + vowel + consonant[index:])

def generateWordsUpTo(length):
        for x in range(1, length + 1):
            generateWords(x)

# Experiment class   
class Experiment:
    # Constructor, takes an animal, a list of transformation functions, and a criteria function
    def __init__(self, animal, transformations, criteria):
        self.animal = animal
        self.transformations = transformations
        self.criteria = criteria
        self.resultingAnimal = None
    # Function that executes experiment
    def successfulExperiment(self):
        animalCopy = self.animal
        for transformation in self.transformations: # Apply functions as transformations
            print(animalCopy)
            transformation(animalCopy)
        print(animalCopy)
        self.resultingAnimal = animalCopy # Save resulting animal for future use
        return self.criteria(animalCopy)
# Report class  
class Report:
    # Report constructor, takes a list of animals, a list of capabilities of interest, a list of transformations and a criteria function
    def __init__(self, animals, capabilities, transformations, criteria):
        self.animals = animals
        self.capabilities = capabilities
        self.transformations = transformations
        self.criteria = criteria
        self.experiments = []
    # This function generates the resulting animal for each individual experiment in the report
    def GenerateInformation(self):
        for animal in self.animals:
            individualExperiment = Experiment(animal, self.transformations, self.criteria)
            individualExperiment.successfulExperiment()
            self.experiments.append(individualExperiment)
    # IQ report, check if any of the capabilities is in the resulting animals  
    def IQReport(self):
        self.GenerateInformation()
        for experiment in self.experiments:
            for capability in self.capabilities:
                if capability in experiment.resultingAnimal.capabilities:
                    print(f"Animal: {experiment.resultingAnimal.species}; IQ: {experiment.resultingAnimal.iq}")
                    break
    # Species report, check if all the capabilities are in the resulting animals
    def speciesReport(self):
        self.GenerateInformation()
        for experiment in self.experiments:
            capabilityCounter = 0
            for capability in self.capabilities:
                if capability not in experiment.resultingAnimal.capabilities:
                    break
                else:
                    capabilityCounter += 1
            if capabilityCounter == len(self.capabilities):
                print(f"Animal: {experiment.resultingAnimal.species}")
    # Capacities report, check if none of the capabilities are in the resulting animals
    def capacitiesReport(self):
        self.GenerateInformation()
        for experiment in self.experiments:
            hasCapability = False
            for capability in self.capabilities:
                if capability in experiment.resultingAnimal.capabilities:
                    hasCapability = True
                    break
            if not hasCapability:
                print(f"Animal: {experiment.resultingAnimal.species}; No. Capacities: {len(experiment.resultingAnimal.capabilities)}")
# Create test animal
animalTest = Animal(17, "mouse", ["destroy the world", "make soulless plans"])

print(animalTest)
# Lambda function that adds an specific amount of IQ
addSpecificIQ = lambda animalIQ: Animal.superiorIntelligence(animalIQ, 100)
