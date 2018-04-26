##This program uses the pet class
import pet

def main():
    ##local variables
    pet_name = ""
    pet_type = ""
    pet_age = 0


    pet_name = input("Enter the pet's name: ")
    pet_type = input("Enter the type of pet: ")
    pet_age = int(input("Enter the pet's age: "))

    ##Create an instance of the pet class

    mypet = pet.Pet(pet_name, pet_type, pet_age)

    ## Display pet Info

    print("Here is your pet's name:", mypet.get_name())
    print("Here is your pet's type:", mypet.get_animal_type())
    print("Here is your pet's age:", mypet.get_age())
    












main()
