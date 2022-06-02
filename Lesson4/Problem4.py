from time import sleep

cars = ["Volvo", "Toyota", "Honda", "BMW", "Mercedes", "Jeep"]
rooms = ["room1", "room2", "room3", "room4", "room5", "room6"]


def checkRooms():
    # Checking if the model is available
    if model in cars:
        model_room = rooms[cars.index(model)]
        print(model + " is available, in " + model_room)
    else:
        print("The car is not available")
while True:
    model = input("Enter car model: ")
    print("Loading cars...")
    sleep(1.5)
    checkRooms()