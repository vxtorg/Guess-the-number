
guess = 0 
tries = 0


while guess != 6 and tries < 5:
  guess = int(input('Guess the number : '))
  tries += 1
if guess == 0:
  print("You got it")
else:
  print("more lucky next time!")