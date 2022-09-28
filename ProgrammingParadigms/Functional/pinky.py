def Animal(iq, species, capabilities):
    return [iq, species, capabilities]

def superiorIntelligence(animal, iq):
    animal[0] += iq
    return animal
        
def pinkify(animal):
    animal[2] = ""
    return animal

def superpowers(animal):
    if animal[1] == "elephant":
        animal[2].append("not to be afraid of mice")
    elif animal[1] == "mouse" and animal[0] > 100:
        animal[2].append("speak")
    
def anthropomorphic(animal):
    if animal[0] > 60 and "speak" in animal[2]:
        return True
    return False

def notSoSane(animal):
    pinkCounter = 0
    for ability in animal[2]:
        if pinkiesco(ability):
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

def Experiment():
    return []
        
        
