from xml.etree.ElementTree import Element, SubElement, tostring
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from bs4 import BeautifulSoup
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
        fighterName.text="test"

        fighterRecord = SubElement(fighterName, "fighterRecord")
        fighterRecordText=fighterSoup.find('span', class_='fighter-record')
        if fighterRecordText is not None:
            print(fighterRecordText.get_text())
            fighterRecord.text=fighterRecordText.get_text()

        fighterSummary = SubElement(fighterName, "fighterSummary")
        fighterSummary.text='test'#fighterSoup.find(id='fighter-skill-summary').get_text()

        fighterFrom =  SubElement(fighterName, "fighterFrom")
        fighterFrom.text="test"

        fighterOutOf = SubElement(fighterName, "fighterOutOf")
        fighterOutOf.text="test"

        fighterAge = SubElement(fighterName, "fighterAge")
        fighterAge.text="test"

        fighterHeight = SubElement(fighterName, "fighterHeight")
        fighterHeight.text="test"

        fighterReach = SubElement(fighterName, "fighterReach")
        fighterReach.text="test"

        fighterTotalStrikes = SubElement(fighterName, "fighterTotalStrikes")
        fighterTotalStrikes.text="test"

        fighterSuccessfulStrikesPercentage = SubElement(fighterName, "fighterSuccessfulStrikesPercentage")
        fighterSuccessfulStrikesPercentage.text="test"

        fighterTakedowns = SubElement(fighterName, "fighterTakedowns")
        fighterTakedowns.text="test"

        fighterSuccessfulTakedownsPercentage = SubElement(fighterName, "fighterSuccessfulTakedownsPercentage")
        fighterSuccessfulTakedownsPercentage.text="test"

        fighterSuccessfulStrikes = SubElement(fighterName, "fighterSuccessfulStrikes")
        fighterSuccessfulStrikes.text="test"

        fighterSuccessfulStandingStrikes = SubElement(fighterSuccessfulStrikes, "fighterSuccessfulStandingStrikes")
        fighterSuccessfulStandingStrikes.text="test"

        fighterSuccessfulGroundStrikes  = SubElement(fighterSuccessfulStrikes, "fighterSuccessfulGroundStrikes")
        fighterSuccessfulGroundStrikes.text="test"

        fighterSuccessfulClinchStrikes = SubElement(fighterSuccessfulStrikes, "fighterSuccessfulClinchStrikes")
        fighterSuccessfulClinchStrikes.text="test"

        fighterSubmissions = SubElement(fighterName, "fighterSubmissions")
        fighterSubmissions.text="test"

        fighterPasses = SubElement(fighterName, "fighterPasses")
        fighterPasses.text="test"

        fighterSweeps = SubElement(fighterName, "fighterSweeps")
        fighterSweeps.text="test"

        fighterStrikesAvoidedPercentage = SubElement(fighterName, "fighterStrikesAvoidedPercentage")
        fighterStrikesAvoidedPercentage.text="test"

        fighterTakedownsAvoidedPercentage = SubElement(fighterName, "fighterTakedownsAvoidedPercentage")
        fighterTakedownsAvoidedPercentage.text="test"

        fighterOpponents = SubElement(fighterName, "fighterOpponents")
        fighterOpponents.text="test"

        opponentName = SubElement(fighterOpponents, "opponentName")
        opponentName.text="test"

        fightResult = SubElement(opponentName, "fightResult")
        fightResult.text="test"

tree = ET.ElementTree(root)
tree.write("fighters.xml")
