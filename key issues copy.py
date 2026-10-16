import random

n = random.randint(1, 100)
a = -1
guesses = 0

while a != n:
  guesses += 1  # Fixed increment operator
  a = int(input("Guess the number: "))  # Converted input to an integer

  if a > n:
    print("Lower number please!!")
  elif a < n:
    print("Higher number please!!")
  else:
    print(f"You guessed the number {n} correctly in {guesses} attempts!")

print("player 2's turn")

n = random.randint(1, 100)
a = -1
guesses = 0

while a != n:
  guesses += 1  # Fixed increment operator
  a = int(input("Guess the number: "))  # Converted input to an integer

  if a > n:
    print("Lower number please!!")
  elif a < n:
    print("Higher number please!!")
  else:
    print(f"You guessed the number {n} correctly in {guesses} attempts!")

print("game over...!! player with fewer {guesses} attempts wins")
