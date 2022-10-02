from itertools import product # Used to create the combinations of letters
# Animal class
class Animal:
    # Constructor
    def __init__(self, iq, species, capabilities):
        self.iq = iq
        self.species = species
        self.capabilities = capabilities
    # Print function
    def __str__(self):
        returnString = ""
        returnString += f"IQ: {self.iq}\n"
        returnString += f"Species: {self.species}\n"
        returnString += f"Capabilities: {self.capabilities}\n"
        return returnString
    # Adding IQ to animal
    def superiorIntelligence(animal, addIQ):
        animal.iq += addIQ
    # Removing capabilities from animal
    def pinkify(animal):
        animal.capabilities = []
    # Give superpowers to animal
    def superpowers(animal):
        if animal.species == "elephant":
            animal.capabilities.append("not to be afraid of mice")
        elif animal.species == "mouse" and animal.iq > 100:
            animal.capabilities.append("speak")
    # Check if anthropomorphic
    def anthropomorphic(animal):
        if animal.iq > 60 and "speak" in animal.capabilities:
            return True
        return False
    # Check if theres more than 2 pinkiesco abilities
    def notSoSane(animal):
        pinkCounter = 0
        for ability in animal.capabilities:
            if Animal.pinkiesco(ability):
                pinkCounter += 1
        if pinkCounter > 2:
            return True
        return False
    # Pinkiesco check
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
    # Generate words from length 1 to length x
    def generateWordsUpTo(length):
        for x in range(1, length + 1):
            Animal.generateWords(x)
    # Generate words of length x         
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
# Creating experiment, passing functions as arguments example
experiment = Experiment(animalTest, [Animal.pinkify, addSpecificIQ, Animal.superpowers], Animal.anthropomorphic)
print(experiment.successfulExperiment())
# Remove comment to test the word generator
# Animal.generateWordsUpTo(4)