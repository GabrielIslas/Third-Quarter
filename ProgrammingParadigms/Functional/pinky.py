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

    def superiorIntelligence(self, addIQ):
        self.iq += addIQ
        
    def pinkify(self):
        self.capabilities = []

    def superpowers(self):
        if self.species == "elephant":
            self.capabilities.append("not to be afraid of mice")
        elif self.species == "mouse" and self.iq > 100:
            self.capabilities.append("speak")
        
    def anthropomorphic(self):
        if self.iq > 60 and "speak" in self.capabilities:
            return True
        return False

    def notSoSane(self):
        pinkCounter = 0
        for ability in self.capabilities:
            if self.pinkiesco(ability):
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



animal = Animal(75, "elephant", ["asdsad"])
print(animal)
animal.superpowers()
print(animal)
animal.superiorIntelligence(25)
print(animal)
print(animal.anthropomorphic())
