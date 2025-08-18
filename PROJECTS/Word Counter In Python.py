# Word Counter In Python

Context = "The streets are paved now, and  the electric companies are cutting down more and more of the shade trees-the water oaks, the maples and aaphelt like tearing silk, and even the negro womem who still take in white people's washing after the old custom, fetchand deliverit in automobiles." 

Words = Context.split()

WordCount = {}

for Word in Words:

    if Word in WordCount:

        WordCount[Word] += 1

    else:

        WordCount[Word] = 1

for Word, Count in WordCount.items():
    print(Word, ":" , Count)