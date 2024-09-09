name = input("Enter your name: ")
print("\n")
print("Welcome",name,"Lets start!")

print("\n")

level1 = input("You are in a jungle and you found a cave. Would you like to explore it? (y/n): ").lower()
print("\n")
if level1 == 'y':
    print("You entered the cave and its cold and dark. what would you do")
    ques1 =  {"1":"Use rocks and wood to ignite fire","2":"Continue in dark"}
    for key,value in ques1.items():
        print(key,":",value)
    ans1 = input("Ans: ")
    print("\n")
    if ans1 == '1':
        print("Yay! Now you can see the Treasure map on cave walls","\n","LEVEL 1 COMPLETE")
    else:
        print("You died of cold","\n","GAME OVER")
else:
    print("Good bye")

print("\n")
level2 =  input("You are following the treasure map, Now you encountered two paths. Which direction would you go (R/L) ?: ").lower()
print("\n")
if level2 == "r":
    print("In the right direction You came across a vertical wall")
    ques2 = input("You wanna climb or quit? (climb/Quit)").lower()
    if ques2 == 'climb':
        print("Well done Tiger!,LEVEL TWO COMPLETE")
    else:
        print('Game Over')
    print("\n")
else:
    print("In the left direction You came across a river")
    ques3 =input("You wanna swim through it (swim/quit)? ").lower()
    if ques3 == "swim":
        print("Well done Tiger!,LEVEL TWO COMPLETE")
    else:
        print('Game Over')
    print("\n")

level3 = input("You reached the Room where the treasure is hidden, But you need to explode the place to get the treasure. Can you do it or Quit? (Can do/Quit): ").lower()

if level3 =="can do":
    print("Great! Now you have a bomb in your bag pack, you set up the bomb and Choose a place to hide or else you'll die in explosion")
    print("\n")
    ques4 = {"1":"Hide nearby bomb","2":"Hide behind the room ","3":"Hide above the room","4":"Go a big distance away and hide somewhere far from the bomb"}
    for key,value in ques4.items():
        print(key," ",value)
        print("\n")
    ans4 = input("ans: ")
    if ans4 == "4":
        print("Phew!","Bomb Exploded!","You are alive")
        print("\n")
        print("CONGRATULATIONS YOU WON A LOT OF TREASURE! GAME FINISHED!")
    else:
        print("OMG! Bomb Exploded!","But you are injured! GAMEOVER MAN")
        print("\n")
else:
    print("Game over!")