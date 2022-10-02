from itertools import product

class Animal:

    def __init__(self, iq, species, capabilities):
        self.iq = iq
        self.species = species
        self.capabilities = capabilities

    def __str__(self):
        returnString = ""
        returnString += f"IQ: {self.iq}\n"
        returnString += f"Species: {self.species}\n"
        returnString += f"Capabilities: {self.capabilities}\n"
        return returnString

    def superiorIntelligence(animal, addIQ):
        animal.iq += addIQ
        
    def pinkify(animal):
        animal.capabilities = []

    def superpowers(animal):
        if animal.species == "elephant":
            animal.capabilities.append("not to be afraid of mice")
        elif animal.species == "mouse" and animal.iq > 100:
            animal.capabilities.append("speak")
        
    def anthropomorphic(animal):
        if animal.iq > 60 and "speak" in animal.capabilities:
            return True
        return False

    def notSoSane(animal):
        pinkCounter = 0
        for ability in animal.capabilities:
            if Animal.pinkiesco(ability):
                pinkCounter += 1
        if pinkCounter > 2:
            return True
        return False
    
    def pinkiesco(ability):
        abilityWords = ability.split(" ")
        if len(abilityWords) != 2:
            return False
        if abilityWords[0] != "do":
            return False
        if len(abilityWords[1]) > 4:
            return False
        totalVowelCount = (abilityWords[1].count("a") + 
                        abilityWords[1].count("e") + 
                        abilityWords[1].count("i") + 
                        abilityWords[1].count("o") + 
                        abilityWords[1].count("u"))
        if totalVowelCount != 1:
            return False
        return True

    def generateWordsUpTo(length):
        for x in range(1, length + 1):
            Animal.generateWords(x)
                
    def generateWords(length):
        vowels = ["a", "e", "i", "o", "u"]
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n','p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        if length > 4:
            return
        elif length == 1:
            for vowel in vowels:
                print(vowel)
            return
        elif length == 3 or length == 4:
            consonants = list(product(consonants, repeat = length - 1))
            for index in range(len(consonants)):
                consonants[index] = "".join(consonants[index])
        for index in range(length):
            for vowel in vowels:
                for consonant in consonants:
                    print(consonant[:index] + vowel + consonant[index:])
        
class Experiment:
    
    def __init__(self, animal, transformations, criteria):
        self.animal = animal
        self.transformations = transformations
        self.criteria = criteria
        self.resultingAnimal = None
        
    def successfulExperiment(self):
        animalCopy = self.animal
        for transformation in self.transformations:
            print(animalCopy)
            transformation(animalCopy)
        print(animalCopy)
        self.resultingAnimal = animalCopy
        return self.criteria(animalCopy)
        
class Report:
    
    def __init__(self, animals, capabilities, transformations, criteria):
        self.animals = animals
        self.capabilities = capabilities
        self.transformations = transformations
        self.criteria = criteria
        self.experiments = []
        
    def GenerateInformation(self):
        for animal in self.animals:
            individualExperiment = Experiment(animal, self.transformations, self.criteria)
            individualExperiment.successfulExperiment()
            self.experiments.append(individualExperiment)
            
    def IQReport(self):
        self.GenerateInformation()
        for experiment in self.experiments:
            for capability in self.capabilities:
                if capability in experiment.resultingAnimal.capabilities:
                    print(f"Animal: {experiment.resultingAnimal.species}; IQ: {experiment.resultingAnimal.iq}")
                    break
                
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

animalTest = Animal(17, "mouse", ["destroy the world", "make soulless plans"])

print(animalTest)

addSpecificIQ = lambda animalIQ: Animal.superiorIntelligence(animalIQ, 100)
experiment = Experiment(animalTest, [Animal.pinkify, addSpecificIQ, Animal.superpowers], Animal.anthropomorphic)
print(experiment.successfulExperiment())

Animal.generateWords(4)