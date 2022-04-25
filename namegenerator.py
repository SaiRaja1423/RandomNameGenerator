import sys
import random

def main():
    print("Welcome to random food generator")
    Toppings = ("chocolate", "vanilla", "strawberry", 
    "caramel", "oreo", "kitkat", "bubblegum", "rasberry", "orange", "water melon")

    Food = ("baji", "puff", "samosa", "idli", "dosa", "pizza", "burger", 
            "upma", "vada", "pie" )

    while True:
        Toppings_name = random.choice(Toppings)
        Food_name = random.choice(Food)

        print("\n\n")
        print("{}{}".format(Toppings_name,Food_name),file=sys.stderr)
        print("\n\n")
        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break
    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
