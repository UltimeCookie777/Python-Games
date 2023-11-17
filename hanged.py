import os
maxAttempts, attempts, mot = 8, 0, [c for c in input("Mot à trouver : ").lower()]
guess = ["-"] * len(mot)
os.system('cls')
while not(guess == mot) and not(attempts == maxAttempts):
    lettre, attempts = input("Lettre : ").lower(), attempts+1
    for idx, val in enumerate(mot):
        guess[idx] = lettre if lettre == val else guess[idx]
    print(guess)
print("Tu es réussi, le mot était " + "".join(mot) if guess==mot else "Perdu ! Le mot était "+ "".join(mot))