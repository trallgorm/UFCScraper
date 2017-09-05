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

def maxChecker(finder, newValue, newFighter):
    if newValue > finder.max:
        finder.maxFighter = textof(newFighter)
        finder.max = newValue

def minChecker(finder, newValue, newFighter):
    if newValue < finder.min:
        finder.minFighter = textof(newFighter)
        finder.min = newValue

class summaryFinder:
    words = {}

    def update(self, fighter):
        summary = textof(fighter.find('fighterSummary'))
        cleansummary = summary.replace(",", " ").replace(".", " ").replace("!", " ").replace(":", " ").lower()
        for word in cleansummary.split():
            if word in self.words:
                self.words[word] += 1
            else:
                self.words[word] = 1

    def printResults(self):
        print("The words used and how often they are used were: ")
        sortedwords = sorted(self.words.items(), key=lambda x: x[1], reverse=True)
        for word in sortedwords:
           print(word)

class weightFinder:
    #Change to have lists for fighters
    min = 999999
    max = 0
    minFighter = ""
    maxFighter = ""

    def update(self, fighter):
        weight = textof(fighter.find('fighterWeight'))
        intweight = int(weight.split(' ', 1)[0])
        if intweight > 0:
            minChecker(self, intweight, fighter)
            maxChecker(self, intweight, fighter)

    def printResults(self):
        print("The smallest fighter was " + self.minFighter.strip() + " with a weight of " + str(self.min) + " pounds")
        print("The biggest fighter was " + self.maxFighter.strip() + " with a weight of " + str(self.max) + " pounds")

class reachFinder:
    #Change to have lists for fighters
    max = 0
    maxFighter = ''

    def update(self, fighter):
        reach = textof(fighter.find('fighterReach'))
        if len(reach) > 0:
            intreach = int(reach.split('"', 1)[0])
            maxChecker(self,intreach,fighter)

    def printResults(self):
        print("The fighter with the most reach was " + self.maxFighter.strip() + " with a reach of " + str(self.max) + " inches")


class strikesFinder:
    #Change to have lists for fighters
    min = 999999
    max = 0
    minFighter = ""
    maxFighter = ""

    def update(self, fighter):
        totalstrikes = textof(fighter.find('fighterTotalStrikes'))
        if totalstrikes != '':
            punches = int(totalstrikes)
            if punches > 0:
                minChecker(self, punches, fighter)
                maxChecker(self, punches, fighter)

    def printResults(self):
        print("The fighter with the most punches was " + self.maxFighter.strip() + " with " + str(self.max) + " punches thrown")
        print("The fighter with the least punches was " + self.minFighter.strip() + " with " + str(self.min) + " punches thrown")


class recordFinder:
    #Change to have lists for fighters
    maxwins = 0
    maxWinner = ""
    totalmatches=0
    maxfights = 0
    mostActiveFighter = ''

    def update(self, fighter):
        record = textof(fighter.find('fighterRecord')).replace(",", "-").replace("(", "-").split("-")
        if len(record) > 2:
            fighterWins = int(record[0])
            fighterLosses = int(record[1])
            fighterDraws = int(record[2])
            numfights = fighterWins + fighterLosses + fighterDraws
            if fighterLosses == 0 and fighterWins > self.maxwins:
                self.maxwins = fighterWins
                self.maxwinner = textof(fighter)
            self.totalmatches = self.totalmatches + numfights
            if numfights > self.maxfights:
                self.maxfights = numfights
                self.mostActiveFighter = textof(fighter)

    def printResults(self):
        print("The fighter with the most wins and 0 losses was " + self.maxwinner.strip() + " with " + str(self.maxwins) + " wins")
        print("The fighter with the most fights was " + self.mostActiveFighter.strip() + " with " + str(self.maxfights) + " fights")

totalfighters = 0
sumf = summaryFinder()
wf = weightFinder()
rf = reachFinder()
sf = strikesFinder()
rdf = recordFinder()

for fighter in tree.findall('fighterName'):
    totalfighters = totalfighters+1

    sumf.update(fighter)
    wf.update(fighter)
    rf.update(fighter)
    sf.update(fighter)
    rdf.update(fighter)


sumf.printResults()
wf.printResults()
rf.printResults()
sf.printResults()
rdf.printResults()
print("UFC fighters have " + str(rdf.totalmatches/totalfighters) + " fights on record on average")

