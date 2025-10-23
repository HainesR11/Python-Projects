credit = 0  # declares the value of credits
# '%.3sf' % 0.0
# '5.00'

print("you have £", credit)  # shows the amount of credits already
input("press enter to continue")

twix = 1.00  # declares the price of twix
coke = 1.25  # declares the price of coke
ready_salted_crips = 1.50  # declares the price of ready salted crips
maltesers = 1.30  # declares the price of maltesers
dairy_milk_chocolate = 1.20  # declares the price of dairy milk
walkers_ready_salted_crips = 1.50  # declares the price of walkers ready salted crips
fanta = 0.90  # declares the price of fanta
vimto_drink = 0.80  # declares the price of vimto
water = 0.40  # declares the price of water
snickes = 1.00  # declares the price of snickers

while True:  # this shows a continuous loop
    action = int(
        input("press 1 to input change, 2 to choose product or 3 to collect change: ")
    )  # this tells the user to input a number for the different optiones

    if (
        action == 1
    ):  # this shows that if the chooses action one it follows the code in action one
        try:
            addcredit = int(
                input("how much do you require: £ ")
            )  # this tells the user to input a number of credits
            credit = (
                credit + addcredit
            )  # this adds up the remaining credits to the added credits
            print(
                "your credit is £", credit
            )  # this tells the user the amount of credits

        except:
            print("this is not a valid amount.... please try again")

    elif (
        action == 2
    ):  # this shows that if the chooses action two it follows the code in action two
        print(
            "what would you like to buy\n twix for £1.00\n coke for £1.25\n ready salted crips for £1.50\n maltesers for £1.30\n dairy milk for £1.20\n walkers ready salted crisps for £1.50"
        )  # this tells the user to input a secific type of food or drink they would like to vend
        vend = input(
            "selection: "
        ).lower()  # this declare that all lettersd are lower cast and to put in a selection

        if vend == "twix":  # declares the producted vended
            if credit < 1:
                print("insufficient credit")  # allws the user not to go over the limit
            else:
                print(vend, "vended")  # tells the user the product has been vended
                credit = (
                    credit - twix
                )  # takes away the product price from the credit remaining
                print(
                    "your credit is £", credit
                )  # shows the amount the credits remaining

        elif vend == "coke":  # declares the producted vended

            if credit < 1.25:
                print("insufficient credit")  # allws the user not to go over the limit
            else:
                print(vend, "vended")  # tells the user the product has been vended
                credit = (
                    credit - coke
                )  # takes away the product price from the credit remaining
                print(
                    "your credit is £", credit
                )  # shows the amount the credits remaining

        elif vend == "ready_salted_crips":  # declares the producted vended

            if credit < 1.50:
                print("insufficient credit")  # allws the user not to go over the limit
            else:
                print(vend, "vended")  # tells the user the product has been vended
                credit = (
                    credit - ready_salted_crips
                )  # takes away the product price from the credit remaining
                print(
                    "your credit is £", credit
                )  # shows the amount the credits remaining

        elif vend == "maltesers":  # declares the producted vended

            if credit < 1.30:
                print("insufficient credit")  # allws the user not to go over the limit
            else:
                print(vend, "vended")  # tells the user the product has been vended
                credit = (
                    credit - maltesers
                )  # takes away the product price from the credit remaining
                print(
                    "your credit is £", credit
                )  # shows the amount the credits remaining

        elif vend == "snickes":  # declares the producted vended

            if credit < 1:
                print("insufficient credit")  # allws the user not to go over the limit
            else:
                print(vend, "vended")  # tells the user the product has been vended
                credit = (
                    credit - snickes
                )  # takes away the product price from the credit remaining
                print(
                    "your credit is £", credit
                )  # shows the amount the credits remaining

        elif vend == "dairy_milk_chocolate":  # declares the producted vended

            if credit < 1.20:
                print("insufficient credit")  # allws the user not to go over the limit
            else:
                print(vend, "vended")  # tells the user the product has been vended
                credit = (
                    credit - dairy_milk_chocolate
                )  # takes away the product price from the credit remaining
                print(
                    "your credit is £", credit
                )  # shows the amount the credits remaining

        elif vend == "walkers_ready_salted_crips":  # declares the producted vended

            if credit < 1.50:
                print("insufficient credit")  # allws the user not to go over the limit
            else:
                print(vend, "vended")  # tells the user the product has been vended
                credit = (
                    credit - walkers_ready_salted_crips
                )  # takes away the product price from the credit remaining
                print(
                    "your credit is £", credit
                )  # shows the amount the credits remaining

        elif vend == "vimto_drink":  # declares the producted vended

            if credit < 0.90:
                print("insufficient credit")  # allws the user not to go over the limit
            else:
                print(vend, "vended")  # tells the user the product has been vended
                credit = (
                    credit - vimto_drink
                )  # takes away the product price from the credit remaining
                print(
                    "your credit is £", credit
                )  # shows the amount the credits remaining

        elif vend == "fanta":  # declares the producted vended

            if credit < 0.80:
                print("insufficient credit")  # allws the user not to go over the limit
            else:
                print(vend, "vended")  # tells the user the product has been vended
                credit = (
                    credit - fanta
                )  # takes away the product price from the credit remaining
                print(
                    "your credit is £", credit
                )  # shows the amount the credits remaining

        elif vend == "water":  # declares the producted vended

            if credit < 0.40:
                print("insufficient credit")  # allws the user not to go over the limit
            else:
                print(vend, "vended")  # tells the user the product has been vended
                credit = (
                    credit - fanta
                )  # takes away the product price from the credit remaining
                print(
                    "your credit is £", credit
                )  # shows the amount the credits remaining

        else:
            print(
                "ivalid selection"
            )  # if not one of the options then it will print this

    elif (
        action == 3
    ):  # this shows that if the chooses action three it follows the code in action three
        print("your change is £", credit)  # this show the amount of change givern back
        credit = 0  # this changes back the credits to 0
        break  # this shows that the lopp wants to end

    else:  # this shows that any other number that the user type will go to this part of coding
        print("invalid selection")  # it will print this

print("enjoy")  # tell the user to enjoy the selection
