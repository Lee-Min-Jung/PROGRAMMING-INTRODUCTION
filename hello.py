initialCoffee=3
initialJuice=2
while True:
    if initialCoffee==0 and initialJuice==0:
        print("all sold out")
        break
    elif initialCoffee>0 or initialJuice>0:
        print("**************")
        print("Hello Cafe")
        print("**************")
        print("1. Coffee")
        print("2. Juice")
        menuSelect=input("Make a select") 
        if menuSelect=="1":
            if initialCoffee==0:
                print("There is no left")
            elif initialCoffee>0:
                print("You choose coffee")
                while True:
                    quantitySelectOfCoffee=int(input("Give a quantity"))
                    if quantitySelectOfCoffee<=initialCoffee:
                        print("Here it is")
                        initialCoffee -=quantitySelectOfCoffee
                        break
                    elif quantitySelectOfCoffee>initialCoffee:
                        print("There is only {} left.".format(initialCoffee))
                        continue
        if menuSelect=="2":
            if initialJuice==0:
                print("There is no left")
            elif initialJuice>0:
                print("You choose juice")
                while True:
                    quantitySelectOfJuice=int(input("Give a quantity"))
                    if quantitySelectOfJuice<=initialJuice:
                        print("Here it is")
                        initialJuice -=quantitySelectOfJuice
                        break
                    elif quantitySelectOfJuice>initialJuice:
                        print("There is only {} left.".format(initialJuice))
                        continue
    
        
  
            
    

    
