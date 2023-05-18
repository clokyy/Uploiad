#                      M3A10 String Variables Assignment
#                            LOGAN WEISGERBER
#                       COMPLETION DATE: 3/13/2023
#            

#Variable key - Defines all variables used in the project
ProgrammingExperience = "2 Years of Java, 8 months of JavaScript"
Siblings = "I am an uncle to 3 kids, 2 boys, Jackson (10) Parker (2) and one girl Abigail (5)"
Job = "Grill @ Fuddruckers"
ElementarySchool = "St. Theresa"
DogName = "Bear"
FirstName = "Logan"

#Prints the strings which are formatted to be placed where the {} in each line, they are then set to uppercase
print("Name: {}".format(FirstName).upper())
print("\n")
print("My Programming Experience Before CS20: {}".format(
    ProgrammingExperience).upper())
print("\n")
print("Elementary School: {}".format(ElementarySchool).upper())
print("\n")
print("Current Employement {}".format(Job).upper())
print("\n")
print("Personal Life: {}".format(Siblings).upper())
print("\n")
print("Pet Name: {}".format(DogName).upper())

print("\n")
print("-------------- LOWER CASE --------------")
print("\n")
# Same Strings just Lower Case

print("Name: {}".format(FirstName).lower())
print("\n")
print("My Programming Experience Before CS20: {}".format(
    ProgrammingExperience).lower())
print("\n")
print("Elementary School: {}".format(ElementarySchool).lower())
print("\n")
print("Current Employement {}".format(Job).lower())
print("\n")
print("Personal Life: {}".format(Siblings).lower())
print("\n")
print("Pet Name: {}".format(DogName).lower())
print("\n")

# Prints Joke
print("Joke:")
print("\n")
#\n creates a new line in the project to make things look neater
print("My friends call me 007 when I play Call of Duty with them. \n"+ "\n"+ "0 Kills \n0 Assists \n7 Deaths")
print("\n")

#Splitting Variables
SplitVariable = "ComputerScience20"

# C = 0 O = 1.....
print(SplitVariable[0:8].lower())
print(SplitVariable[8:15].upper())
print(SplitVariable[15:18])
