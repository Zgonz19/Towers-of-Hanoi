# COSC 3320, Towers of Hanoi, Assignment 1
# Gonzalo Zepeda, ID: 1561524

# when called, printMove function prints the current move as long as the parameters
# entered correspond to the solution.
# notable parameters: which disk is moving, disk location, disk destination, number of moves so far
def printMove(disk, source, dest, currentStep):                                   
	print("Move number " + str(currentStep) + ": Move disk " + str(disk) + " from " + str(source) +
        " to " + str(dest))
	
# the hanoi function is the main recursive function of the program
# notable parameters: how many disks there are, the 5 pegs, the current move
# once called, this function will call itself until all disks are in the destination peg
def hanoi(numOfDisks, Start, source, dest, aux, last, current,r):
	numOfDisks = int(numOfDisks)
	if numOfDisks == 1: 
		printMove(numOfDisks, source, aux, current)
		current+=1 
		printMove(numOfDisks, aux, dest, current) 
		current+=1

	elif numOfDisks == 2:
		printMove(numOfDisks-1, source, aux, current) 
		current+=1 
		printMove(numOfDisks-1, aux, dest, current)
		current+=1
		if current == 4:
			printMove(numOfDisks, Start, source, current)
			current+=1
		printMove(numOfDisks, source, aux, current) 
		current+=1
		printMove(numOfDisks-1, dest, aux, current) 
		current+=1 
		printMove(numOfDisks-1, aux, source, current) 
		current+=1 
		printMove(numOfDisks, aux, dest, current) 
		current+=1
		if r == 2:
			printMove(2, dest, last, current) 
			current+=1;
		printMove(numOfDisks-1, source, aux, current)
		current+=1 
		printMove(numOfDisks-1, aux, dest, current) 
		current+=1;

	elif numOfDisks > 2:
		current = hanoi(numOfDisks-1, Start, source, dest, aux, last, current, r)
		if(hasItMoved[numOfDisks]!=1):
			printMove(numOfDisks, Start, source, current) 
			current+=1
			hasItMoved[numOfDisks]=1
		printMove(numOfDisks, source, aux, current) 
		current+=1
		current = hanoi(numOfDisks-1,Start, dest, source, aux,last, current, r)
		printMove(numOfDisks, aux, dest, current) 
		current+=1
		if(toDest[numOfDisks+1]!=0):
			printMove(numOfDisks, dest, last, current) 
			current+=1
			toDest[numOfDisks]=1
		if(numOfDisks == r):
			r-=1
		current = hanoi(numOfDisks-1, Start,source, dest, aux,last, current, r)
	return current;				 	 	 	
	
# the hanoiInit function is only called once to initiate our program. 
# within hanoiInit is the first call to our recursive hanoi function.
def hanoiInit(numOfDisks, start, source, dest, aux, last, current, r): 
	printMove(1, start, source, current)                           
	current+=1
	current = hanoi(n,"Start","Aux1","Aux3","Aux2","Dest",current,r)
	printMove(1, dest, last, current) 
	current+=1  

current=1
hasItMoved = [None]*12
toDest = [None]*12
n = input("How many disks are we solving for? ")
r = int(n)

hanoiInit(n,"Start","Aux1","Aux3","Aux2","Dest",current,r)




