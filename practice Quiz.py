import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
print("WELCOME TO QUIZ GAME")

play = input("Do you wanna play?(s/n) ").lower()
print(play)
score = 0
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

if play != 's':
    quit()

print("Okay lets start!")




print("\n")
print("1.What is NaCl?")
print("\n")
options1 = {"1":"Hydrochloric acid", '2':"Nitrogen chloride", '3':'Sodium Chloride', '4':'Sodium chloric acid'}
for key,value in options1.items():
    print(key + ':' + value)
answer1 = input("Answer: ")
if answer1 == '3':
    print("Correct!")
    score +=1
else:
    print("stupid!")
print("\n")

print("2.Which fruit contains most vitamin C?")
print("\n")
options2 = {"1":"Apple", '2':"Water Melon", '3':'Chickoo', '4':'Orange'}
for key,value in options2.items():
    print(key + ':' + value)
answer2 = input("Answer: ")
if answer2 == '4':
    print("Correct!")
    score +=1
else:
    print("stupid!")

print("\n")

print("3.Which is the most abdundant gas found in atmosphere?")
print("\n")
options3 = {"1":"Hydrogen", '2':"Nitrogen", '3':'Oxygen', '4':'Helium'}
for key,value in options3.items():
    print(key + ':' + value)
answer3 = input("Answer: ")
if answer3 == '2':
    print("Correct!")
    score +=1
else:
    print("stupid!")
print("\n")

print("4.How many bones does a adult human has?")
print("\n")
options4 = {"1":"226", '2':"250", '3':'206', '4':'106'}
for key,value in options4.items():
    print(key + ':' + value)
answer4 = input("Answer: ")
if answer4 == '3':
    print("Correct!")
    score +=1
else:
    print("stupid!")
print("\n")
print("5.What is the normal Blood pressure of human?")
print("\n")
options5 = {"1":"120/80", '2':"180/20", '3':'150/20', '4':'80/20'}
for key,value in options5.items():
    print(key + ':' + value)
answer5 = input("Answer: ")
if answer5 == '1':
    print("Correct!")
    score +=1
else:
    print("stupid!")
print("\n")
print("6.Which of the following is found in ocean?")
print("\n")
options6 = {"1":"Metamorphic rocks", '2':"Marbles", '3':'Coral reef', '4':'granite'}
for key,value in options6.items():
    print(key + ':' + value)
answer6 = input("Answer: ")
if answer6 == '3':
    print("Correct!")
    score +=1
else:
    print("stupid!")
print("\n")
print("7.Who is the strongest of the following?")
print("\n")
options7 = {"1":"Murat", '2':"Goku", '3':'Henry Cavil', '4':'vegeta'}
for key,value in options7.items():
    print(key + ':' + value)
answer7 = input("Answer: ")
if answer7 == '1':
    print("Correct!")
    score +=1
else:
    print("stupid!")
print("\n")
print("8.What is the balancing part of the brain called?")
print("\n")
options8 = {"1":"Aorta", '2':"Nerves", '3':'Cerebrum', '4':'Cerebellum'}
for key,value in options8.items():
    print(key + ':' + value)
answer8 = input("Answer: ")
if answer8 == '4':
    print("Correct!")
    score +=1
else:
    print("stupid!")
print("\n")
print("9.Which is the strongest acid among the following?")
print("\n")
options9 = {"1":"HCl", '2':"KCl", '3':'KOH', '4':'H2SO4'}
for key,value in options9.items():
    print(key + ':' + value)
answer9 = input("Answer: ")
if answer9 == '4':
    print("Correct!")
    score +=1
else:
    print("stupid!")
print("\n")
print("10.Which is the largest organ in human body?")
print("\n")
options10 = {"1":"Brain", '2':"Stomach", '3':'Skin', '4':'Lungs'}
for key,value in options10.items():
    print(key + ':' + value)
answer10 = input("Answer: ")
if answer10 == '3':
    print("Correct!")
    score +=1
else:
    print("stupid!")
print("\n")
print("Finished !")
print("\n")
if score < 5 :
    print("You're score is low,You are stupid")
    print("\n")
    print(CLEAR_AND_RETURN)
if 5< score < 10:
    print("score:",score, "You scored well, Congratulations")
print(CLEAR_AND_RETURN)

