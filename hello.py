initialCoffee=3
initialJuice=2
while True:
    if initialCoffee==0 and initialJuice==0:
        print("All sold out. Thank you for using \"Hello Cafe\".")
        break
    elif initialCoffee>0 or initialJuice>0:
        print("**************")
        print("Hello Cafe")
        print("**************")
        print("1. Coffee")
        print("2. Juice")
        menuSelect=input("Please make a selection:") 
        if menuSelect=="1":
            if initialCoffee==0:
                print("There is no left coffee.")
            elif initialCoffee>0:
                print("You choose coffee.")
                while True:
                    coffeeQuantity=int(input("Please give a quantity."))
                    if coffeeQuantity<=initialCoffee:
                        print("Here it is.")
                        initialCoffee -=coffeeQuantity
                        break
                    elif coffeeQuantity>initialCoffee:
                        print("There is only {} left.".format(initialCoffee))
                        continue
        if menuSelect=="2":
            if initialJuice==0:
                print("There is no left juice.")
            elif initialJuice>0:
                print("You choose juice.")
                while True:
                    juiceQuantity=int(input("Please give a quantity."))
                    if juiceQuantity<=initialJuice:
                        print("Here it is.")
                        initialJuice -=juiceQuantity
                        break
                    elif juiceQuantity>initialJuice:
                        print("There is only {} left.".format(initialJuice))
                        continue
    
        
  
            
    

    
