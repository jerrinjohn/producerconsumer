import itertools as it
import pandas as pd
hashmap = {
  100:	["XLON", "XJSE","NYSE","NASDAQ","XSTO", "XTSE"],
  54 : [1,2,3,4,5,6,7,8,9],
  40: [1,2,3,4,6,7,8,9,"D","E","G","I","J","K","L","M","P"],
  59: [0,1,2,3,4,5,6],
  21: [1,2,3],
  38: [0.1,123,1000000],
  44: [0.01,100.1,1000000],
  18: [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W"],
  55: ["A","B","C","D","E","F"],
}
leftPad = "8=FIX.4.2|9=145|35=D|34=4|49=ABC_DEFG01|52=20090323-15:40:29|56=CCG|115=XYZ|11=NF 0542/03232009|60=20090323-15:40:29"
rightPad = "10=139"

def createMessages(leftPad, rightPad, hashmap):
    dict_combinations = findCombos(hashmap)
    all_poss = sorted(dict_combinations)
    all_combinations = list(it.product(*(dict_combinations[possibility] for possibility in all_poss)))
    print(len(list(all_combinations)))
    messages = []
    for i in range(0, len(all_combinations)):
        messages.append([leftPad + "|"+ "11="+str(i)+"|" + "|".join(all_combinations[i])+"|" + rightPad ])
    df = pd.DataFrame(messages)
    df.to_csv("3million_messages.csv")
        # f.write(message)
        # f.close()

def findCombos(hashmap):
    all_combinations = {}
    for i in hashmap:
        all_combinations[i] = createCombinations(i, hashmap[i])
    return all_combinations
        

def createCombinations(number, array):
    possibleCombinations = []
    for i in range(0, len(array)):
        combo =  str(number)+"="+str(array[i])
        possibleCombinations.append(combo)
    return possibleCombinations


if __name__ == '__main__': 
    createMessages(leftPad, rightPad,hashmap)