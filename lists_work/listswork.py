# This script focuses on mastering sorting in python. 
cars = ['bmw', 'subaru', 'audi', 'toyota']
cars.sort() # Sorting using the sort() method
print(cars)
friends = ['Ivy', 'Emmaculate', 'Julius', 'Sandra', 'Priscah', 'Jane']

# Sorting a List Temporarily with the sorted() Function
print(sorted(friends)) # Sorting using the sorted as a argument. 
print(friends)
print(sorted(friends, key=len)) # Sorting using the len() method as the key. 
friends.sort(reverse=True) # Here the sort() method sorts in the reverse order of the alphabet
print(friends)

# Printing a List in Reverse Order
motorcycles = ['honda', 'suzuki', 'yamaha', 'ducati', 'bmw']
print(motorcycles)
motorcycles.reverse()
print(motorcycles)

# Do it yourself
places_of_interest = ['seychelles', 'maldives', 'california', 'london', 'dubai']
print(places_of_interest)
print(sorted(places_of_interest))
print(places_of_interest)
print(sorted(places_of_interest, reverse=True))
print(places_of_interest)
places_of_interest.reverse()
print(places_of_interest)
places_of_interest.sort()
print(places_of_interest)
places_of_interest.sort(reverse=True)
print(places_of_interest)

# recap
languages = ['Kiswahili', 'Spanish', 'English', 'Arabic', 'Amharic', 'German', 'Chinese']
print(len(languages))
print(sorted(languages))
print(sorted(languages, reverse=True))
languages.reverse()
print(languages)
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)
languages.sort(reverse=False)
print(languages)

# Avoiding Index Errors When Working with Lists
# print(languages[7]) # This line of code produces an error because of the off-by-one nature of indexing in lists. 
rivers = ['Gucha', 'Nzoia', 'Tana']
print(rivers[-1]) # This line of code return the last element in the list. 
mountains = []
# print(mountains[-1]) # This line produces an error. 

#Indentation errors
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title()) # This is a logical error. If indented will produce the desired output. 

# DIY 4
types_of_pizza = ['cheese', 'pepperoni', 'meat', 'veggie', 'margherita', 'hawaiian']
for type in types_of_pizza:
    print("I love " + type + " pizza. ")
print("""I remember the first time I ate pizza it was amazing. 
The first type I took was pepperoni and it was delicious. I really love pizza!
      """)

animals_with_similarities = ['dog', 'cat', 'sheep']
for animal in animals_with_similarities:
    print("A " + animal + " would make a great pet. ")
print("Any of these animals would make a great pet. ")

# Numerical lists
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
# To make the code concise
cubes = []
for number in range(1, 11):
    cubes.append(number**3)
print(cubes)
# Simple statistics with numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions
squareroots = [digit**(1/2) for digit in range(10, 110, 10)]
print(squareroots)
# Try It Yourself
for odd in range(1, 21, 2):
    print(odd)
# Cube comprehension
cube_of_no = [no**3 for no in range(1, 11)]
print(cube_of_no)

# Slicing a list
players = ['Julius', 'Chrispus', 'James', 'Fredrick', 'Joy', 'Christine']
print(players[0:2])
print(players[1:4])
print(players[:4])
print(players[0:4])
print(players[2:]) # Python returns all items from the third item through the end of the list. 
# If we want to output the last three players from the roster we can use -
print(players[-3:])
print("\nHere are the first three players in my team:")
for player in players[0:3]:
    print(player.title())

# Copying a list
my_foods = ['Pizza', 'French fries', 'Burger']
friend_foods = my_foods[:]
# If we use the syntax friend_foods = my_foods >>> The two variables will point to the same list
# and hence it will not create the two lists as intended. 
my_foods.append("Carrot cake")
friend_foods.append("Ice cream")
print("My favorite foods are: ")
print(my_foods)
print("\nMy friends' favorite foods are: ")
print(friend_foods)
