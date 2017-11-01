

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
        print("Adding fighter: " + fighterName.text)

        fighterRecord = SubElement(fighterName, "fighterRecord")
        addTextToNode(fighterRecord,fighterSoup.find('span', class_='fighter-record'))

        wins=0
        losses=0
        if len(fighterRecord.text) > 2:
            wins= (int(fighterRecord.text.replace(",", "-").replace("(", "-").split("-")[0]))
            losses = (int(fighterRecord.text.replace(",", "-").replace("(", "-").split("-")[1]))

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

        maxNumbers = fighterSoup.find_all('div', class_='max-number')
        fighterTotalStrikes = SubElement(fighterName, "fighterTotalStrikes")
        if len(maxNumbers)>0:
            addTextToNode(fighterTotalStrikes, maxNumbers[0])

        fighterSuccessfulStrikesPercentage = SubElement(fighterName, "fighterSuccessfulStrikesPercentage")
        addTextToNode(fighterSuccessfulStrikesPercentage, fighterSoup.find(id='total-striking-graph-percent-successful'))

        fighterTakedowns = SubElement(fighterName, "fighterTakedowns")
        if len(maxNumbers) > 1:
            addTextToNode(fighterTakedowns, maxNumbers[2])

        fighterSuccessfulTakedownsPercentage = SubElement(fighterName, "fighterSuccessfulTakedownsPercentage")
        addTextToNode(fighterSuccessfulTakedownsPercentage, fighterSoup.find(id='total-striking-graph-percent-successful'))

        fighterSuccessfulStrikes = SubElement(fighterName, "fighterSuccessfulStrikes")
        addTextToNode(fighterSuccessfulStrikes, fighterSoup.find(id='types-of-successful-strikes-graph-maximum'))

        strikesgraph = fighterSoup.find(id='types-of-successful-strikes-graph')

        fighterSuccessfulStandingStrikes = SubElement(fighterSuccessfulStrikes, "fighterSuccessfulStandingStrikes")
        if strikesgraph is not None:
            standing = strikesgraph.find('div', class_='red-text-bar')
            if standing is not None:
                addTextToNode(fighterSuccessfulStandingStrikes,  standing.find('div', class_='bar-text'))

        fighterSuccessfulGroundStrikes  = SubElement(fighterSuccessfulStrikes, "fighterSuccessfulGroundStrikes")
        if strikesgraph is not None:
            ground = strikesgraph.find('div', class_='dark-red-text-bar')
            if ground is not None:
                addTextToNode( fighterSuccessfulGroundStrikes,  ground.find('div', class_='bar-text'))

        fighterSuccessfulClinchStrikes = SubElement(fighterSuccessfulStrikes, "fighterSuccessfulClinchStrikes")
        if strikesgraph is not None:
            clinch = strikesgraph.find('div', class_='grey-text-bar')
            if clinch is not None:
                addTextToNode( fighterSuccessfulClinchStrikes,  clinch.find('div', class_='bar-text'))


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
        fights = fighterSoup.find_all('tr', class_='fight')



        for fight in fights:
            opponentName = SubElement(fighterOpponents, "opponentName")
            fighter = fight.find('td', class_='fighter')
            if fighter is not None:
                addTextToNode(opponentName, fighter.find('a'))

            fightResult = SubElement(opponentName, "fightResult")
            result = fight.find('td', class_='result')
            if result is not None:
                if(result.find('div', class_='win') is not None or result.find('div', class_='title-fight') is not None or result.find('div', class_='non-ufc-title-fight-win') is not None):
                    fightResult.text = 'Win'
                    wins-=1
                if (result.getText().strip()=="Loss" or result.find('div', class_='title-fight-lose') is not None or result.find('div', class_='non-ufc-title-fight-lose') is not None):
                    fightResult.text = 'Loss'
                    losses-=1
                if (result.getText().strip() == "NO CONTEST"):
                    fightResult.text = "NO CONTEST"

            winsAtTheTimeOfFight = SubElement(opponentName, "fighterWinsPriorToFight")
            winsAtTheTimeOfFight.text = str(wins)

            lossesAtTheTimeOfFight = SubElement(opponentName, "fighterLossesPriotToFight")
            lossesAtTheTimeOfFight.text = str(losses)

            dateOfFight = SubElement(opponentName, "dateOfFight")
            event = fight.find('td', class_='event').find('div').next_sibling.strip()
            dateOfFight.text = event

tree = ET.ElementTree(root)
tree.write("fighters.xml")
