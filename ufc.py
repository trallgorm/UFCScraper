from xml.etree.ElementTree import Element, SubElement, tostring
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from bs4 import BeautifulSoup
def addTextToNode(node, foundNodeContent):
    if foundNodeContent is not None:
        node.text=foundNodeContent.getText().strip()

fighterLinks = []
testMode=False
root=Element('fighters')
for currentPage in range(0,29):
    print("Starting work on page " + str(currentPage))
    page = ''
    if (not testMode):
        page = urlopen("http://www.ufc.ca/fighter/Weight_Class/filterFighters?offset="+str(currentPage*20)+"&max=20&sort=lastName&order=asc")
    soup = BeautifulSoup(page)
    fighterLinksOnPage=soup.find_all('a', class_='fighter-name')
    for fighterLink in fighterLinksOnPage:
        fighterLinks.append(fighterLink['href'])
        fighterPage=''
        if (not testMode):
            fighterPage = urlopen("http://www.ufc.ca"+fighterLink['href'])
        fighterSoup =  BeautifulSoup(fighterPage)

        fighterName = SubElement(root, "fighterName")
        fighterNameContent = fighterSoup.find_all('span', class_='fighter-name')
        fighterName.text=''
        for namePlace in fighterNameContent:
            fighterName.text+=namePlace.find(text=True).strip()+' '
        print(fighterName.text)

        fighterRecord = SubElement(fighterName, "fighterRecord")
        addTextToNode(fighterRecord,fighterSoup.find('span', class_='fighter-record'))

        fighterSummary = SubElement(fighterName, "fighterSummary")
        addTextToNode(fighterSummary, fighterSoup.find(id='fighter-skill-summary'))

        fighterFrom =  SubElement(fighterName, "fighterFrom")
        addTextToNode(fighterFrom, fighterSoup.find(id='fighter-from'))

        fighterOutOf = SubElement(fighterName, "fighterOutOf")
        addTextToNode(fighterOutOf, fighterSoup.find(id='fighter-lives-in'))

        fighterAge = SubElement(fighterName, "fighterAge")
        addTextToNode(fighterAge, fighterSoup.find(id='fighter-age'))

        fighterHeight = SubElement(fighterName, "fighterHeight")
        addTextToNode(fighterHeight, fighterSoup.find(id='fighter-height'))

        fighterWeight = SubElement(fighterName, "fighterWeight")
        addTextToNode(fighterWeight, fighterSoup.find(id='fighter-weight'))

        fighterReach = SubElement(fighterName, "fighterReach")
        addTextToNode(fighterReach, fighterSoup.find(id='fighter-reach'))

        fighterLegReach = SubElement(fighterName, "fighterLegReach")
        addTextToNode(fighterLegReach, fighterSoup.find(id='fighter-leg-reach'))

        fighterTotalStrikes = SubElement(fighterName, "fighterTotalStrikes")
        #addTextToNode(fighterTotalStrikes, fighterSoup.find(id='fighter-lives-in'))

        fighterSuccessfulStrikesPercentage = SubElement(fighterName, "fighterSuccessfulStrikesPercentage")
        addTextToNode(fighterSuccessfulStrikesPercentage, fighterSoup.find(id='total-striking-graph-percent-successful'))

        fighterTakedowns = SubElement(fighterName, "fighterTakedowns")
        #addTextToNode(fighterTakedowns, fighterSoup.find(id='fighter-lives-in'))

        fighterSuccessfulTakedownsPercentage = SubElement(fighterName, "fighterSuccessfulTakedownsPercentage")
        addTextToNode(fighterSuccessfulTakedownsPercentage, fighterSoup.find(id='total-striking-graph-percent-successful'))

        fighterSuccessfulStrikes = SubElement(fighterName, "fighterSuccessfulStrikes")
        #addTextToNode(fighterSuccessfulStrikes, fighterSoup.find(id='fighter-lives-in'))

        fighterSuccessfulStandingStrikes = SubElement(fighterSuccessfulStrikes, "fighterSuccessfulStandingStrikes")
        #addTextToNode(fighterSuccessfulStandingStrikes, fighterSoup.find(id='fighter-lives-in'))

        fighterSuccessfulGroundStrikes  = SubElement(fighterSuccessfulStrikes, "fighterSuccessfulGroundStrikes")
        #addTextToNode(fighterSuccessfulGroundStrikes, fighterSoup.find(id='fighter-lives-in'))

        fighterSuccessfulClinchStrikes = SubElement(fighterSuccessfulStrikes, "fighterSuccessfulClinchStrikes")
        #addTextToNode(fighterSuccessfulClinchStrikes, fighterSoup.find(id='fighter-lives-in'))

        fighterSubmissions = SubElement(fighterName, "fighterSubmissions")
        addTextToNode(fighterSubmissions, fighterSoup.find(id='successful-submissions'))

        fighterPasses = SubElement(fighterName, "fighterPasses")
        addTextToNode(fighterPasses, fighterSoup.find(id='successful-passes'))

        fighterSweeps = SubElement(fighterName, "fighterSweeps")
        addTextToNode(fighterSweeps, fighterSoup.find(id='successful-sweeps'))

        fighterStrikesAvoidedPercentage = SubElement(fighterName, "fighterStrikesAvoidedPercentage")
        addTextToNode(fighterStrikesAvoidedPercentage , fighterSoup.find(id='striking-defense-pecentage'))

        fighterTakedownsAvoidedPercentage = SubElement(fighterName, "fighterTakedownsAvoidedPercentage")
        addTextToNode(fighterTakedownsAvoidedPercentage, fighterSoup.find(id='takedown-defense-percentage'))

        fighterOpponents = SubElement(fighterName, "fighterOpponents")
        opponents = fighterSoup.find_all('td', class_='fighter')
        for opponent in opponents:
            opponentName = SubElement(fighterOpponents, "opponentName")
            addTextToNode(opponentName, opponent.find('a'))

            fightResult = SubElement(opponentName, "fightResult")
            #addTextToNode(fightResult, fighterSoup.find(id='fighter-lives-in'))

tree = ET.ElementTree(root)
tree.write("fighters.xml")
