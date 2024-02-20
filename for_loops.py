print("Welcome")
user=int(input("Which code would you like to run? Choose a number between 1 and 10:"))
if user==1:
    for count in range(1,1001):
        print(count)

if user==2:
    for count in range(1,1001, 2):
        print(count)

if user==3:
    for count in range (0,1000):
        if count % 3==0:
            print(count)

if user==4:
    for count in range(1,1000):
        if count % 3 == 0:
            print(count)
        elif count % 5==0:
            print(count)

if user==5:
    user= int(input("Enter a number greater than 200:"))
    for count in range(user):
        if count % 11==0:
            print(count)
        elif count % 13==0:
            print(count)

if user==6:
    user= str(input("Enter a word:"))
    for L in range (len (user)):
        print ((user[L]))

if user==7:
    user= str(input("Enter a sentence. The sentence must be longer than 10 letters:"))
    for l in range(0, len(user), 2):
        print(user[l])

if user==8:
    import random
    print("This is a dice rolling simulator. A die will be rolled 1000 times. The output values are shown below:")
    ones=0
    twos=0
    threes=0
    fours=0
    fives=0
    sixes=0
    for roll in range(1000):
        dice=random.randint(1,6)
        if dice==1:
            ones+=1
        elif dice ==2:
            twos+=1
        elif dice==3:
             threes+=1
        elif dice==4:
            fours+=1
        elif dice==5:
            fives+=1
        elif dice==6:
            sixes+=1
    print (f"{ones} 1s, {twos} 2s, {threes} 3s, {fours} 4s, {fives} 5s, and {sixes} 6s were rolled")

if user==9:
   user=int(input("Enter any number:"))
   for i in range (1,user):
        if user % i == 0:
            print (f"{user} is not a prime number.")
            break
        else:
            print(f"{user} is a prime number.")

if user== 10:
    print("This program will print all prime numbers less than 1000.")
    for count in range (1001):
        for i in range(2, count):
            if count % i==0:
                break
        else:
            print (count)