# import random

# list_numbers = list((1, 2, 3, 4, 5, 6))
# list_names = [
#'Emmanuel', 'José', 'Luis', 'Alejandro', 'Yamil', 'Natalia', 'Tamara', 'Jhonatan', 'Fernanda', 'Jasive', 'Kenia', 'Cinthia', 'Rodrigo', 'Daniel'
# ]
# list_objects = ["Hola", 2, True]

# list_numbers.append(7)
# list_names.append('Paco')
# print(list_numbers)
# print(list_names)

# list_names = ['Fernanda',  'Melisa del Carmen', 'José', 'Miriam Janet',
#              'Natalia', 'Tamara', 'Jasive', 'Gabriel', 'Jonathan Palacios (Emmanuel)',
#              'Kenia', 'Rodrigo', 'Luis', 'Yamil', 'Cinthia Melisa', 'Miguel'
# ]

# my_file =open("Lista_20_Enero.txt", "r")
# list_names = my_file.read()
# names_into_list = list_names.split("\n")
# random_name = random.choice(names_into_list)
# print(random_name)

#import random

# h_or_t = [1, 0]
#
# choice = random.choice(h_or_t)
#
# if choice == 1:
#     print("Heads")
# else:
#     print("Tails")

# Import the random module here

# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# import random
# persons = len(names)
# ran_person = (random.randint(0, persons-1))
# payer = (names[ran_person])
#
# print(str(payer) + " is going to buy the meal today!")

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️", "️⬜️", "️⬜️"]
# row2 = ["⬜️", "⬜️", "️⬜️"]
# row3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# # first convert your int into a string
# str_digit = str(position)
# # then separate this with a for loop, while converting
# # every substring back into an integer, saved on a list
# list_digit = [int(i) for i in str_digit]
# #separate these two digits into column and row (just to avoid confusion, these two can be written directly on the index)
# el_1_column = int(list_digit[0])
# el_2_row = int(list_digit[1])
# # since position in a list starts in 0, make sure to put a minus 1 on the position introduced by the user.
# map[el_2_row - 1][el_1_column - 1] = 'X'
#
# # Write your code above this row 👆
#
# # # 🚨 Don't change the code below 👇
# # print(f"{row1}\n{row2}\n{row3}")
# #
# import random
# user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n")
#
# scissors = '''
#         _______
#     ---'   ____)____
#               ______)
#            __________)
#           (____)
#     ---.__(___)
#     '''
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#         _______
#     ---'   ____)____
#               ______)
#               _______)
#              _______)
#     ---.__________)
#     '''
#
# srp = [scissors, rock, paper]
# comp_list = ["Rock", "Paper", "Scissors"]
#
# if user_choice == "0":
#     hand_choice = comp_list[0]
#     print(srp[1])
# elif user_choice == "1":
#     hand_choice = comp_list[1]
#     print(srp[2])
# elif user_choice == "2":
#     hand_choice = comp_list[2]
#     print(srp[0])
# else:
#     hand_choice = "Invalid number."
#
# comp_choice = str(random.choice(comp_list))
# if comp_choice == comp_list[0]:
#     print("Computer chose: " + str(srp[1]))
# elif comp_choice == comp_list[1]:
#     print("Computer chose: " + str(srp[2]))
# elif comp_choice == comp_list[2]:
#     print("Computer chose: " + str(srp[0]))
# else:
#     print("")
#
# print(hand_choice)
# print(comp_choice)
#
# if hand_choice == comp_choice:
#     print("It's a draw.")
# elif hand_choice == "Scissors" and comp_choice == "Rock":
#     print("You lost.")
#     print("Better luck next time, loser.")
# elif hand_choice == "Rock" and comp_choice == "Scissors":
#     print("You win.")
#     print("Congratulations or whatever.")
# elif hand_choice == "Scissors" and comp_choice == "Paper":
#     print("You win.")
#     print("Congratulations or whatever.")
# elif hand_choice == "Rock" and comp_choice == "Paper":
#     print("You lost.")
#     print("Better luck next time, loser.")
# elif hand_choice == "Paper" and comp_choice == "Rock":
#     print("You win.")
#     print("Congratulations or whatever.")
# elif hand_choice == "Paper" and comp_choice == "Scissors":
#     print("You lost.")
#     print("Better luck next time, loser.")
# else:
#     print("Invalid game.")


# number = 0
# while number != 10:
#     number += 1
#     print(number)

# #create list of files
# my_files = ["file1.txt", "file2.txt", "file3.txt"]
# #open a new file in write mode, which will work as your final file
# with open('file6.txt', 'w') as outfile:
# # iterate through the elements of the list
#     for i in my_files:
# #open each file in the list of my_files in read mode
#         with open(i) as infile:
# #read the data from the three files and write them in the final file
#             outfile.write(infile.read())
# #add \n to skip line between each files
#         outfile.write("\n")

import openpyxl
import pycountry
import random
from openpyxl import Workbook
wb = Workbook()
# grab the active worksheet
ws = wb.active
#open the list in .txt and create a list
my_file = open("Lista_20_Enero.txt", "r")
list_names = my_file.read()
names_into_list = list_names.split("\n")
#print(names_into_list)

#create an empty list and then save each country name into this new list
results = []
for country in pycountry.countries:
    results.append(country.name)

#print(results)

#shuffle the order from the list names, so it will be MORE RANDOM
temp_list= [x.split(",") for x in names_into_list]
random.shuffle(nlist := temp_list)

#print(nlist)


res = []
lott_value = 1000000
lott_list = []
rand_value = 0
#While the lottery award is bigger than 0, get a random value between 0 and that lottery value. Then add that value to
#a new list for lotterie values. Then substract that value from the bigger prize. What's left of the price will enter
#the loop and do the same: while the remaining lottery price is bigger than 0, get a random numb and substract from the
#price until 0.
lott_sum = 0
while lott_value > 0:
    rand_value = random.randint(0, lott_value)
    lott_list = lott_list + [rand_value]
    lott_value = lott_value - rand_value
    lott_sum = lott_sum + rand_value
print(lott_sum)
print(lott_list)

for ele_nlist, ele_lott_list in zip(nlist, lott_list):
    ele_nlist.append(ele_lott_list)

print(nlist)
final_list = []

#to this list with people and rewards, add a random country
for i in nlist:
    final_list = final_list + [i + [random.choice(results)]]

headers = ['Names', 'Money', 'Country']
final_list.insert(0,headers)
#print(res)
#print(final_list)
# Rows can also be appended
for col in final_list:
    ws.append(col)

# Save the file
wb.save("sample2.xlsx")