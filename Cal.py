import random

def monstrous_calculator():
    print("Welcome to the Monstrous Calculator!")
    print("I am MONSTER, your calculating companion.")
    
    while True:
        print("\nChoose your monstrous operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == '5':
            print("Farewell, mortal. MONSTER will haunt your calculations no more!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! MONSTER demands a proper selection.")
            continue

        num1 = float(input("Enter the first monstrous number: "))
        num2 = float(input("Enter the second monstrous number: "))

        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
            else:
                print("MONSTER doesn't divide by zero. Try again.")
                continue

        print(f"The monstrous result is: {result}")
        scare_factor = random.randint(1, 10)
        print(f"Beware! MONSTER's scare factor for this calculation: {scare_factor}")

monstrous_calculator()
