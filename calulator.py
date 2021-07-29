while True:
    input ("***********Welcome To The Calculator*********")
    input ("for your infomation you cant use words or letters")



    while True:
        while True:
            numb_1 = int(input("what is your first number: "))
            if numb_1 >=0:
                break
            elif numb_1 <=0:
                break
            else:
                print ("invalid number")
                    
        while True:
            numb_2 = int(input("What is your second number: "))
            if numb_2 >=0:
                break
            elif numb_2 <=0:
                break
            else:
                print ("invalid number")

        while True:
            action = input("What is the fuction you wish to use: ")
            if action == "+" :
                answer = numb_1 + numb_2
                print (answer)
                break
            
            elif action == "-" :
                answer = numb_1 - numb_2
                print (answer)
                break
            
            elif action == "*" :
                answer = numb_1 * numb_2
                print (answer)
                break
            elif action == "/" :
                answer = numb_1 / numb_2
                print (answer)
                break

            else:
                print ("invalid function")
        repeat = input ("would you like to restart: ").upper()
        if repeat == "N" or "NO"
    break
