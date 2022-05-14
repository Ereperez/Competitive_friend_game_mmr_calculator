#A Python progam to print all combinations of given length
 
from itertools import combinations
import math
 
#get all combinations of [1, 2, 3] and length 2
 
#counter = 0
#print("Enter the total amount of players: ")
#totalPlayers = int(input())
#teamSize = int(totalPlayers/2)
 
players = []
 
#print("Players in each team: " + str(teamSize))
 
#creating an empty list
#lst = []
 
#number of elements as input
totalPlayers = int(input("Enter number of players : "))
teamSize = int(totalPlayers/2)
 
print("Enter the MMR of each player: ")
 
#iterating till the range
for i in range(0, totalPlayers):
    ele = int(input())
    players.append(ele) # adding the element
 
print (players)
 
comb = combinations(players,teamSize)
 
listOfComb = []
 
for i in list(comb):
    listOfComb += [i]
 
print("Players in each team: " + str(teamSize))
print("Total amount of combinations: " + str(len(listOfComb)))
 
combOfTeams = int(math.factorial(len(listOfComb))/(2*(math.factorial(len(listOfComb)-2))))#Total amount of combinations choose 2
print("Amount of matchups: " + str(combOfTeams))
print("------------------------------------------") 

testList = []
 
counter = 0
testList = []
mmrDiff = 0
mmrDiffList = []
maxMmrDif = 150
minMmrDif = -150
 
for i in range(len(listOfComb)):
    for j in range(len(listOfComb)):
        if i <= j or (set(listOfComb[i]) & set(listOfComb[j]) != set()):
            continue
        teamCompositions = listOfComb[i],listOfComb[j]
        mmrDiff = sum(teamCompositions[0]) - sum(teamCompositions[1])
        if mmrDiff < maxMmrDif and mmrDiff > minMmrDif:
            print(list(teamCompositions))
            counter +=1
            print("Difference MMR between teams: " + str(sum(teamCompositions[0]) - sum(teamCompositions[1])))
            print("Number of unique Team compositions: " + str(counter))
            print("sum of 1st: " + str(sum(teamCompositions[0])))
            print("sum of 2nd: " + str(sum(teamCompositions[1])))
            print("------------------------------------------") 
            mmrDiffList.append(mmrDiff)

        testList.append(teamCompositions)
        testList.append(mmrDiff)
 
print("This is the mmr difference for the different teams: ")
mmrDiffList.sort() 
print(mmrDiffList)
#print(sorted(mmrDiffList))
 
 