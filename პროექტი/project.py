def new_acc():  #register code
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    email =  input("Enter your Email: ")
    password = input("Enter password: ")
    password_confirm = input("confirm password: ")
    while password != password_confirm:
        input("Confirm password: ")
        break


new_acc()
def withdraww():
        #deposit, withdraw & start again (or exit) code
        deposit = int(input("How much do you want to deposit: "))
        on_card = deposit
        print("You have",on_card,"dollars on card" )
  #Deposit code
        print("you have", on_card, "dollars on card")
    #withdraw code
        if on_card >= 0:
                withdraw = int(input("how much do you want to withdraw: "))
                if withdraw <= on_card:
                        on_card = on_card - withdraw
                        print("you have", on_card, "dollars on card")
                        print("You have successfully withdrawed", withdraw, "dollars from card.")
                else:
                      print("you don't have enough money on card.")
                      
                exit = input("do you want to exit? ")
                while exit == "yes":
                      print("bye")
                      break
                if exit == "no":
                      withdraww()
                      
                              


        




withdraww()

        


        


