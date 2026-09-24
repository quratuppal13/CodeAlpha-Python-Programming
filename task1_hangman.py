import random

words = ["python", "coding", "intern", "github", "system"]
selected_word = random.choice(words)
guessed_letters = []
attempts = 6

print("--- WELCOME TO CODEALPHA HANGMAN GAME ---")

while attempts > 0:
    display = [letter if letter in guessed_letters else "_" for letter in selected_word]
    print("\nWord to guess: " + " ".join(display))
    print(f"Remaining attempts: {attempts}")
    
    if "_" not in display:
        print("🎉 Congratulations! You guessed the word correctly!")
        break
        
    guess = input("Guess a single letter: ").lower().strip()
    
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Invalid input! Please enter exactly one alphabetical letter.")
        continue
        
    if guess in guessed_letters:
        print("⚠️ You have already guessed that letter. Try another one!")
        continue
        
    guessed_letters.append(guess)
    
    if guess in selected_word:
        print("✅ Correct guess!")
    else:
        print("❌ Wrong guess!")
        attempts -= 1

if attempts == 0:
    print(f"\n💀 Game Over! The correct word was: '{selected_word}'")
