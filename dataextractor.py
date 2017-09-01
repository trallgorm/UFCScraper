#cool stats
#most used words in summary
#funny summaries
#Most active city
#Person with highest amount of punches thrown
#person with highest amount of takedowns
#person with greatest amount of punches with 100% accuracy?
#person with most fights according to record
#person with most fights
#average amount of fights
#fighter with lowest weight
#fighter with highest weight
#longest loss streak
#longest win streak
#longest reach

import xml.etree.ElementTree
tree = xml.etree.ElementTree.parse('fighters.xml').getroot()

def textof(node):
    if node is None or node.text==None:
        return ''
    else:
        return node.text

words={}
minweight = 999999
maxweight=0
smallestFighter=''
biggestFighter=''
maxpunches=0
punchiestFighter=''
minpunches=9999999
pussyhands=''
maxfights=0
mostActiveFighter=''
totalmatches = 0
totalfighters = 0
maxwins = 0
maxwinner = ''
maxreach = 0
maxreacher = ''

for fighter in tree.findall('fighterName'):
    totalfighters = totalfighters+1
    summary = textof(fighter.find('fighterSummary'))
    cleansummary = summary.replace(","," ").lower()
    for word in cleansummary.split():
        if word in words:
            words[word]+=1
        else:
            words[word]=1

    weight = textof(fighter.find('fighterWeight'))
    intweight = int(weight.split(' ', 1)[0])
    if intweight>0:
        if intweight<minweight:
            minweight=intweight
            smallestFighter=textof(fighter)
        if intweight>maxweight:
            maxweight=intweight
            biggestFighter=textof(fighter)

    reach = textof(fighter.find('fighterReach'))
    if len(reach)>0:
        intreach = int(reach.split('"', 1)[0])
        if intreach > maxreach:
            maxreach = intreach
            maxreacher = textof(fighter)

    totalstrikes = textof(fighter.find('fighterTotalStrikes'))
    if totalstrikes!='':
        punches = int(totalstrikes)
        if punches > 0:
            if punches < minpunches:
                minpunches = punches
                pussyhands = textof(fighter)
            if punches > maxpunches:
                maxpunches = punches
                punchiestFighter = textof(fighter)


    record = textof(fighter.find('fighterRecord')).replace(",","-").replace("(","-").split("-")
    if len(record) > 2:
        fighterWins = int(record[0])
        fighterLosses = int(record[1])
        fighterDraws = int(record[2])
        numfights = fighterWins + fighterLosses + fighterDraws
        if fighterLosses == 0 and fighterWins>0:
            maxwins=fighterWins
            maxwinner = textof(fighter)
        totalmatches = totalmatches+numfights
        if numfights > maxfights:
            maxfights = numfights
            mostActiveFighter = textof(fighter)
sortedwords = sorted(words.items(), key=lambda x: x[1],reverse=True)
#for word in sortedwords:
#   print(word)
#print(minweight)
#print(smallestFighter)
#print(maxweight)
#print(biggestFighter)

print(minpunches)
print(pussyhands)
print(maxpunches)
print(punchiestFighter)
print(maxfights)
print(mostActiveFighter)
print(totalmatches/totalfighters)
print(maxwins)
print(maxwinner)
print(maxreach)
print(maxreacher)
