import random

words=["moon", "juice", "rocky", "tiger", "melon", "happy", "sunny", "apple", "eagle", "bunny", "jelly", "ocean", "beach", "piano", "frost", "giant", "zebra", "robot", "magic", "puppy", "flame", "storm", "smile", "angel", "dream", "fairy", "candy", "wings", "honey", "river", "peace", "cloud", "light", "heart", "queen", "music", "space", "crown", "dance", "stars", "earth", "swift", "grape", "cherry", "daisy", "spark", "witty", "spark", "fuzzy"]

word=random.choice(words)
print("Guess the word")

print()

guesses=" "

turns=20

while(turns):
    fail=0
    char=input("Guess a character: ")
    guesses+=char
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            fail+=1
    if fail==0:
        print("Youn win")
        print("Word is: ",word)
        break
    turns-=1
        