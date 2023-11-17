import os
attempts, mot = 0, [c for c in input("Word to find : ").lower()]
guess, maxAttempts = ["-"] * len(mot), 9 + len(set(mot))
os.system('cls')
while not(guess == mot) and not(attempts == maxAttempts):
    letter, attempts = input("Letter : ").lower(), attempts+1
    for idx, val in enumerate(mot):
        guess[idx] = letter if letter == val else guess[idx]
    print(guess)
print("You won ! the word was " + "".join(mot) if guess==mot else "Lost ! The word was "+ "".join(mot))