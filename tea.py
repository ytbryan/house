#tea making simulator
import time

def boil_water():
    print("Boiling water...")
    time.sleep(3)
    print("Water is boiling.")

def add_teabag():
    print("Adding a tea bag...")
    time.sleep(2)
    print("Tea bag added.")

def steep_tea():
    print("Steeping the tea...")
    time.sleep(3)
    print("Tea is ready.")

def add_milk_and_sugar():
    print("Adding milk and sugar...")
    time.sleep(2)
    print("Tea is now ready to drink.")

def make_tea():
    boil_water()
    add_teabag()
    steep_tea()
    add_milk_and_sugar()

def main():
    print("Welcome to the Tea Making Simulator!")
    while True:
        print("\nOptions:")
        print("1. Make tea")
        print("2. Quit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            make_tea()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
