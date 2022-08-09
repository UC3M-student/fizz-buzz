import sys

x = 3
lst = list(range(1,101,1))
lst = list(map(str,lst))


while True:
    for i in range(1,101,1):
        asked_question = input("Please enter the following number -> ")
        
        if i%3 ==0:
            if asked_question == "fizz":
                continue
            else:
                while True:
                    x-=1
                    print("This is not the answer we were looking for. You have",x,"more lifes")
                    if x == 0:
                        print("You lost all lifes. Please try again")
                        sys.exit()
                    asked_question2 = input("Please enter the following number -> ")
                    if asked_question2 == "fizz":
                        break
        elif i%5 ==0:
            if asked_question == "buzz":
                continue
            else:
                while True:
                    x-=1
                    print("This is not the answer we were looking for. You have",x,"more lifes")
                    if x == 0:
                        print("You lost all lifes. Please try again")
                        sys.exit()
                    asked_question2 = input("Please enter the following number -> ")
                    if asked_question2 == "buzz":
                        break    
                    
        elif i%5 == 0 and i%3 ==0:
            if asked_question == "fizz buzz":
                continue
            else:
                while True:
                    x-=1
                    print("This is not the answer we were looking for. You have",x,"more lifes")
                    if x == 0:
                        print("You lost all lifes. Please try again")
                        sys.exit()
                    asked_question2 = input("Please enter the following number -> ")
                    if asked_question2 == "fizz-buzz":
                        break 
        else:
            asked_question = int(asked_question)
            if i != asked_question:
                while True:
                    x-=1
                    print("This is not the answer we were looking for. You have",x,"more lifes")
                    if x == 0:
                        print("You lost all lifes. Please try again")
                        sys.exit()
                    asked_question2 = input("Please enter the following number -> ")
                    if asked_question2 == i:
                        break
