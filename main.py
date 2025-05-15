import random 
from faker import Faker
fake = Faker()

randomNumber = random.randint(1,100)

print("Welcome to the username generator!")

choice  = input("Do you want to use your real name? (yes/no): ").lower()

if choice == "yes":
    username = input("Please enter your first and last name: ")
    username = username + str(randomNumber)
elif choice == "no":
    username = fake.name() + str(randomNumber)
    
username = username.replace(" ", "_")

print("Your unique username is: ", username)

