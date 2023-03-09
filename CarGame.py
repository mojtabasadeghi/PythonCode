status = 0

while True:
    user_input = input("> ").lower()
    if user_input == "help":
        print("""start - to start the car
stop - to stop the car
quit - to exit the game""")
    elif user_input == "start" and status == 0:
        status = 1
        print("Car started ...")
    elif user_input == "start" and status == 1:
        print("Car already started.")
    elif user_input == "stop" and status == 1:
        status = 0
        print("Car stopped.")
    elif user_input == "stop" and status == 0:
        print("Car already stop you should start it first.")
    elif user_input == "quit":
        break
    else:
        print("I don't understand that...")
