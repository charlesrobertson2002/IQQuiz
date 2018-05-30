score = 0
ready = int(input("This is a free 110% accurate IQ quiz answer all of the questions as best as you can good luck type 1 and hit enter to start: " ))
print" "
if ready == 1:
	
	print "Which of these numbers fit the pattern 1, 8, 27, 64, 125, ?: "
	print "1: 169"
	print "2: 216"
	print "3: 147"
	print "4: 238"
question1 = int(input("Type in the number to the left of your answer then hit enter: " ))
print " "
if question1 ==2:
	print "You are correct the pattern is cubes and the cube of 6 is 216"
	score = score+1
elif question1 == 1 or 4 or 3:
	print "Wrong answer better luck next time"
else: 
	print "Invalid answer try typing in the number to the left of the answer you want on the next question"
print " "
print "Which of these is the correct definition of lackadaisical: "
print "1: To be Extremly Energized"
print "2: To Mess up Something"
print "3: To Lack Enthusiasm"
print "4: To Like Flowers"
question2 = int(input("Type in the number to the left of your answer then hit enter: " ))
print " "
if question2 ==3:
	print "You are correct lackadaisical means to lak enthusiasm"
	score = score+1
elif question2 == 1 or 4 or 2:
	print "Wrong answer better luck next time"
else: 
	print "Invalid answer try typing in the number to the left of the answer you want on the next question"
print " "	
print "What is Newton's second law: "
print "1: Force = mass times acceleration"
print "2: E=mc^2"
print "3: For every action there is an equal but opposite eaction "
print "4: An object at rest stays at rest and an object in motion stays in motion with the same speed and in the same direction unless acted upon by an unbalanced force."
question3 = int(input("Type in the number to the left of your answer then hit enter: "))
print " "
if question3 ==1:
	print "You are correct Newton's second law is Force = mass times acceleration"
	score = score+1
elif question3 == 2 or 4 or 3:
	print "Wrong answer better luck next time"
else: 
	print "Invalid answer try typing in the number to the left of the answer you want on the next question"
print " "	
print "Which number logically follows this series 4,6,9,6,14,6,? " 
print "1: 6"
print "2: 17"
print "3: 19 "
print "4: 21"
question4 = int(input("Type in the number to the left of your answer then hit enter: "))
print " "
if question4 ==3:
	print "You are correct the pattern is a number than 6 then the first number plus 5 and so on and so forth."
	score = score+1
elif question4 == 1 or 4 or 2:
	print "Wrong answer better luck next time"
else: 
	print "Invalid answer try typing in the number to the left of the answer you want on the next question"

print " "
print "Which conclusion follows the statements.  None of the money collectors are engineers.  All of the drones are money collectors. " 
print "1: All money collectors are engineers"
print "2: Engineers are not drones"
print "3: No money collectors are drones"
print "4: Some drones are engineers"
question5 = int(input("Type in the number to the left of your answer then hit enter: "))
print " "
if question5 ==2:
	print "You are correct the logical conclusion is that engineers are not drones."
	score = score+1
elif question5 == 1 or 4 or 3:
	print "Wrong answer better luck next time"
else: 
	print "Invalid answer try typing in the number to the left of the answer you want on the next question"	

print " "
print "Wire is to electricity as Pipe is to ? "
print "1: Tube"
print "2: Cord"
print "3: Dogs "
print "4: Water"
question6 = int(input("Type in the number to the left of your answer then hit enter: "))
print " "
if question6 ==4:
	print "You are correct electricity flows through wires and water flows through pipes."
	score = score+1
elif question6 == 1 or 3 or 2:
	print "Wrong answer better luck next time"
else: 
	print "Invalid answer try typing in the number to the left of the answer you want on the next question"

print " "
print "Which answer is the opposite meaning of the word shame "
print "1: Pride"
print "2: Greed"
print "3: Luck"
print "4: Joy"
question7 = int(input("Type in the number to the left of your answer then hit enter: "))
print " "
if question7 ==1:
	print "You are correct the opposite of shame is pride."
	score = score+1
elif question7 == 3 or 4 or 2:
	print "Wrong answer better luck next time"
else: 
	print "Invalid answer try typing in the number to the left of the answer you want on the next question"

print " "
print "Which of these numbers fit the pattern 2, 6, 24, 120, 720, ? "
print "1: 3240"
print "2: 2360"
print "3: 5040"
print "4: 1334"
question8 = int(input("Type in the number to the left of your answer then hit enter: "))
print " "
if question8 ==3:
	print "You are correct the Nth term in this pattern is N!."
	score = score+1
elif question8 == 1 or 4 or 2:
	print "Wrong answer better luck next time"
else: 
	print "Invalid answer try typing in the number to the left of the answer you want on the next question"

print " "
print "What do these numbers have in common 3, 13, 37, 53, 61 "
print "1: They all add up to 200"
print "2: They are all composite numbers"
print "3: They are multiples of 3"
print "4: They are prime numbers"
question9 = int(input("Type in the number to the left of your answer then hit enter: "))
print " "
if question9 ==4:
	print "You are correct they are all prime numbers"
	score = score+1
elif question9 == 1 or 3 or 2:
	print "Wrong answer better luck next time"
else: 
	print "Invalid answer try typing in the number to the left of the answer you want on the next question"

print " "
print "Which of these numbers fit the pattern 2, 6, 24, 120, 720, ? "
print "1: 3240"
print "2: 2360"
print "3: 5040"
print "4: 1334"
question10 = int(input("Type in the number to the left of your answer then hit enter: "))
print " "
if question10 ==3:
	print "You are correct the Nth term in this pattern is N!."
	score = score+1
elif question10 == 1 or 4 or 2:
	print "Wrong answer better luck next time"
else: 
	print "Invalid answer try typing in the number to the left of the answer you want on the next question"

print " "
print "Your IQ is " + str((score * 10 + 50)) + "."

