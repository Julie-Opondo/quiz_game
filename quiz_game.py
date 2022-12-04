print("Welcome to my game!")
gaming = input("You want to play my quiz game? ")

if gaming.upper() == "YES":
    name = input("What is your name?  ")
    print("Welcome to Random Quiz " + name)
else :
    print("Okay, Another Day!")

score = 0 
#question one
response = input("What year did Kenya gain independence? ")

if response == "1963":
   print("Correct!") 
   score += 1
else:
    print('Incorrect!')  
#question two
response = input("What is the capital of kenya? ")
if response.lower() == 'nairobi':
   print("Correct!") 
   score += 1
else:
    print('Incorrect!')  
#question three
response = input("What is the hightest mountain in Kenya? Mt. ").lower()
if response == "kenya":
   print("Correct!") 
   score += 1
else:
    print('Incorrect!')  
#question four
response = input("How many counties are there in Kenya? ")
if response == "47":
   print("Correct!") 
else:
    print('Incorrect!')  
#question five
response = input("When was the last general election in Kenya? ")
if response == "2022":
   print("Correct!") 
   score += 1
else:
    print('Incorrect!')          

print("Thank you for playing " + name + ". Your score is " + str(int(score/4 * 100))+ " %")
