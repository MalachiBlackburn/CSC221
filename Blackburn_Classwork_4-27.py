##This program uses the pet class
import car

def main():
    ##local variables
    car_year_model = ""
    car_make = ""
    car_speed = 0


    car_year_model = int(input("Enter the model year of the car: "))
    car_make = input("Enter the make of the car: ")
    car_speed = int(input("Enter the car's speed: "))

    ##Create an instance of the pet class

    mycar = car.Car(car_year_model, car_make, car_speed)

    ## Display pet Info

    print("Here is your pet's name:", mycar.get_year_model())
    print("Here is your pet's type:", mycet.get_make())
    print("Here is your pet's age:", mycet.get_speed())
    












main()
