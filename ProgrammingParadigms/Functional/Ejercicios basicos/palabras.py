isVowel = lambda c: c.lower() == "a" or c.lower() == "e" or c.lower() == "i" or c.lower() == "o" or c.lower() == "u"
consonantCount = lambda word: sum(not isVowel(c) for c in word)
vowelCount = lambda word: sum(isVowel(c) for c in word)
moreConsonantsThanVowels = lambda word: consonantCount(word) > vowelCount(word) 
acronym = lambda words: "".join(word[0] for word in words.split(" "))

print(vowelCount("eaoeiauoifg"))
print(moreConsonantsThanVowels("eaoeiauoifg"))
print(moreConsonantsThanVowels("zjhxjkhkjhaeo"))
print(acronym("asdjskd kfdh weiu dsakj 2hj Asd"))