print("Quiz Game")
player=input("Do you want to play?")
if(player=="yes"):
    print("Lets play")
    score=0
    qn=input("Who invented Computer?")
    qn.lower()
    if(qn=="charles babbage"):
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    qn=input("1024 Kilobytes is equal to ___ MB?")
    if(qn=="1"):
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    qn=input("Brain of computer is?")
    qn.lower()
    if(qn=="cpu"):
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    qn=input("Who is known as Father of Indian Constitution?")
    qn.lower()
    if(qn=="ambedkar"):
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    qn=input("Which is the most sensitive organ in our body?")
    qn.lower()
    if(qn=="skin"):
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    qn=input("Smallest state of India is?")
    qn.lower()
    if(qn=="goa"):
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    qn=input("Fastest animal on earth is?")
    qn.lower()
    if(qn=="cheetah"):
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    qn=input("Which is the animal referred as the ship of the desert?")
    qn.lower()
    if(qn=="camel"):
        print("Correct")
        score+=1
    else:
        print("Incorrect")
else:
    quit()
print("Game over,Your score is:",score)
if(score=="8"):
    print("You have won")

    
