# Python List Methods
# .count() = list method to count the number of occurrences of an element in a list
# .insert() = list method to insert an element into a specific index of the list
# .pop() = list method to remove an element from a specific index or from the end of the list
# range() = built-in Python function to create a sequence of integers
# len() = built-in Python function to get the length of a list
# .sort() / .sorted() = method and a built-in function to sort a list
# Exmaple syntax for methods: list.method(input)
# Example syntax for a built-in function: builtinfunction(input)

# .insert(): expects two inputs, first numerical index, second desired value

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
front_display_list.insert(0,"Pineapple")
print(front_display_list)

# .pop(): index of the element you want to remove

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
data_science_topics.pop(-1)
data_science_topics.pop(3)
print(data_science_topics)

# range(): creates a range object

number_list = range(0,9)
print(list(number_list))
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
zero_to_seven = range(0,8)
print(list(zero_to_seven))
# [0, 1, 2, 3, 4, 5, 6, 7]
print(zero_to_seven)
# range(0,8) --> specify it's a list as above

# example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9)
my_list = range(2,9)
print(list(my_list))
# [2,3,4,5,6,7,8]

# example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number
my_range2 = range(2,9,2)
print(list(my_range2))
# [2,4,6,8]

# example, we’ll start at 1 and skip in increments of 10 between each number until we get to 99 (one before 100)
my_range3 = range(1,100,10)
print(list(my_range3))
# [1,11,21,31,41,51,61,71,81,91]

range_five_three = range(5, 15, 3)
range_diff_five = range(0,40,5)

# len(): use to find the length of a list

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)

# Your code below: 
long_list_len = len(long_list)
print(long_list_len)
big_range_length = len(big_range)
print(big_range_length)

# Slicing Lists

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

# Your code below: 
print(beginning)

middle = suitcase[2:4]
print(middle)

# Slicing by element

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 
last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

# .count(): count occurrences of element

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count("Jake")
print(jake_votes)

# .sort(): sorts the list in place

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)

# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
print(names)

# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = sorted(cities, reverse=True)
print(sorted_cities)

# sorted(): list as an arguement, rather than being called on the list; generates a new list rather than modifying the one that already exists

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games)
print(games_sorted)

# Review

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)

first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[0:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10,"19th Century Bed Frame")
inventory.sort()
print(inventory)