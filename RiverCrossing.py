while True:
    print("""
    Welcome!
    [1] Start
    [2] View Formula
    [3] View Rules
    [4] Credits
    [5] Exit
    """)

    options = input("Enter your choice (1/2/3/4/5) >>> ")
    if options == "1":
        adultsamt = int(input("How many adults are trying to cross the river >>> "))
        print("Lets go with 2 children.")
        print("------------------------------")
        amt1 = int(adultsamt / 4)
        steps = adultsamt * 4 + 1
        print(f"""
        Solution to: What if there were {adultsamt} adults and 2 Children.
        Steps needed = {steps}
        """)
        again = input("Do you want to do another one? ")
        if again == "yes" or "y":
            pass
        if again == "no" or "n":
            quit()

    elif options == "2":
        print("FORMULA:")
        print("------------------------------")
        print("Child 1 & Child 2 ---> Other side\nMainland          <--- Child 1\nAdult             ---> Other Side\nMainland          <--- Child 2\n")
        print("------------------------------")
        print("Multiply this by how many adults you have, 1 adult is equal to 4 steps!")
        print("------------------------------")
        print("Make sure to add this line at the end to account for both children:")
        print("Child 1 & Child 2 ---> Other side")

    elif options == "3":
        print("""
        <!> RULES <!>
        - All adults weight the same.
        - Each child weighs half as much as an adult.
        - Boat can only carry weight of one adult.
        - Adults and children can row the boat.
        - Boat must have someine in it to row!

        <!> Website <!>
        - https://nrich.maths.org/11175
        """)

    elif options == "4":
        print("""
        You can find the explanation on my website: https://www.bludenz.dev/nrich/rivercrossing
        Or the code on GitHub: https://github.com/Bludenz/NRICH/tree/main/RiverCrossing
        """)


    elif options == "5":
        quit()