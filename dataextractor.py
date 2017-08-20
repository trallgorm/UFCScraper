#cool stats
#most used words in summary
#funny summaries
#Most active city
#Person with highest amount of punches thrown
#person with highest amount of takedowns
#person with greatest amount of punches with 100% accuracy?
#person with most fights
#average amount of fights
#fighter with lowest weight
#fighter with highest weight
#longest loss streak
#longest win streak

import xml.etree.ElementTree
tree = xml.etree.ElementTree.parse('fighters.xml').getroot()

def textof(node):
    if node is None or node.text==None:
        return ''
    else:
        return node.text

words={}

for fighter in tree.findall('fighterName'):
    summary = textof(fighter.find('fighterSummary'))
    cleansummary = summary.replace(","," ").lower()
    for word in cleansummary.split():
        if word in words:
            words[word]+=1
        else:
            words[word]=1

sortedwords = sorted(words.items(), key=lambda x: x[1],reverse=True)
for word in sortedwords:
    print(word)