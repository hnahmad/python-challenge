import os
import csv
import sys

voteslist = []
candidateslist =[]
uniquecandidates = []
votecounter = []
candidatepercentages=[]



csvpath = os.path.join("Resources", "election_data.csv")


with open(csvpath,newline='',encoding='UTF-8') as election_data:

    csvreader = csv.reader(election_data,delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        
        #Count the number of votes by putting voter IDs in a list (could be any row)
        
        voteslist.append(row[0])
        VoteCount = int(len(voteslist))

        #To get a complete list of candidates who received votes, we will need be able to run a test for whether a name already exits in a list. 
        #So, we will make a list of all votes again by candidate name, and then extra using not in
        #print(row)
        #print(type(row))
        #break
        if row[2] not in uniquecandidates:
                uniquecandidates.append(row[2])
                # Do Something  

    #We have a list of unique candidates.  We want to count the votes for each.  Hence, we will loop through
    #the CSV once for each candidate.  
      
    for candidate in uniquecandidates:
        #Before each loop, we want to make sure our counters are reset.
        for row in csvreader:
            candidatecount=0
            candidatepercentage=0
            #Add vote to counter when the item in the candidate "column" is the same as current candidate.
            if row[2]=candidate:
                candidatecount = candidatecount+1
            #Calculate percentage
            candidatepercentage = candidatecount / VoteCount
            #We need to store the final count and percentage before the loop starts over.       
            votecounter.append(candidatecount) 
            candidatepercentages.append(candidatepercentage)    

   #We now have three lists, one with the candidates,one with the corresponding number of votes,
   # and one with the percentages each candidate got.  To find the winner's name, we find index
   #of maximum votes in votes list, and use it to choose candidate from candidate list.

    highestvotetotal = max(votecounter)  
    indexvariable = votecounter.index(highestvotetotal)   

    winner = uniquecandidates(indexvariable)

    print("Election Results")
    print()
    totalvotesforprinting = str(VoteCount)
    print(f'Total Votes:"{totalvotesforprinting}
    print()
    for candidate in uniquecandidates:
        indextoprint=uniquecandidates.index(candidate)
        print(f'{candidate}:{votecounter(indextoprint)} ({int(100*candidatepercentages(indextoprint))})')

    print(f'Winner is ' {winner})