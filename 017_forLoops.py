# In a for loop, we will know in advance how many times the loop will need to iterate because we will be working on a collection with a predefined length.

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for sport in sport_games:
  print(sport)

# for loop: using range()

promise = "I will finish the python loops module!"

for temp in range(5):
  print(promise)

# for loop: using while

countdown = 10
while countdown >= 0:
  print(countdown)
  countdown -= 1

print("We have liftoff!")

# for loop: lists

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0
while index < length:
  print("I am learning about", python_topics[index])
  index += 1

# for loop: infinite loops (example fixes the loop)

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
index = 0
length = len(students_period_A)

while index < length:
  students_period_B.append(students_period_A[index])
  index += 1
print(students_period_B)

#  for loop: break

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"


index = 0

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    break
print("They have the dog I want!")

# for loop: continue

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
   continue
  print(age)

# for loop: nested

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  print(location)
  for scoops in location:
    scoops_sold += scoops
print(scoops_sold)

# for loop: list comprehensions

