import random
while True:
    number = random.randint(1, 100)
    tries = 10
    tried = set()
    while tries > 0:
        user_input = input(f"Enter your guess: ").strip()            
        guess = int(user_input)
        
        if guess < 1 or guess > 100:
            print("Out of range! Numbers must be between 1 and 100")
            continue
        if guess in tried:
            print(f"You already guessed {guess} before. Try a different number! (This does not count as a try)")
            continue
        tried.add(guess)
        tries -= 1      
        if guess == number:
            print(f"Congratulations!")
            if tries > 0:
                number = random.randint(1, 100)
                tried.clear() 
                print(f"New game started! You have {tries} tries to guess the new number.")
            else:
                print("LOSE")
                break
        else:
            if guess < number:
                print("too low!")
            else:
                print("too high!")
            if tries == 0:
                print(f"Out of tries!")        
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again not in ('y', 'yes'):
        print("Thanks for playing! Goodbye.")
        break