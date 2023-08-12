from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
additional_headers = {'X-API-KEY': os.getenv('API_KEY')}
DEFAULT_URL = 'https://www.bungie.net'
s = requests.Session()

class api:
    def request(self, upurl):
        request = s.get(url = upurl, headers=additional_headers)
        try:
            return json.loads(request.text)
        except:
            print(request.reason)

    def SearchByBungieName(self, displayName, displayNameCode):
        info = json.loads(requests.post(url= "https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayerByBungieName/All/" , headers=additional_headers, json={
                  'displayName': displayName,
                  'displayNameCode': displayNameCode}).text)
        
        return info
    
    def GetLinkedProfiles(self, membershipId, getAllMemberships, membershipType = '-1'):
        url = DEFAULT_URL + '/Platform/Destiny2/{}/Profile/{}/LinkedProfiles/?getAllMemberships={}'
        url = url.format(membershipType, membershipId, getAllMemberships)
        return self.request(url)

    def GetProfile(self, membershipType, membershipId, components):
        url = DEFAULT_URL + '/Platform/Destiny2/{}/Profile/{}/?components={}'
        url = url.format(membershipType, membershipId, components)
        return self.request(url)

    def GetCharacter(self, membershipType, membershipId, characterId, components):
        url = DEFAULT_URL + '/Platform/Destiny2/{}/Profile/{}/Character/{}/?components={}'
        url = url.format(membershipType, membershipId, characterId, components)
        return self.request(url)
    
    def GetHistoricalStats(self, membershipType, membershipId, characterId, modes, dayend= '', daystart = '', groups = '', periodType = ''):
        url = DEFAULT_URL + '/Platform/Destiny2/{}/Account/{}/Character/{}/Stats/?groups={}&dayend={}&daystart={}&modes={}&periodType={}'
        url = url.format(membershipType, membershipId, characterId, groups, dayend, daystart, modes, periodType)
        return self.request(url)

    def GetHistoricalStatsForAccount(self, membershipType, destinyMembershipId):
        url = DEFAULT_URL + '/Platform/Destiny2/{}/Account/{}/Stats/'
        url = url.format(membershipType, destinyMembershipId)
        return self.request(url)
    
    def GetActivityHistory(self, membershipType, destinyMembershipId, characterId, count = 1, mode = 'None', page = 0):
        url = DEFAULT_URL + '/Platform/Destiny2/{}/Account/{}/Character/{}/Stats/Activities/?count={}&mode={}&page={}'
        url = url.format(membershipType, destinyMembershipId, characterId, count, mode, page)
        return self.request(url)
    
    def GetUniqueWeaponHistory(self, membershipType, destinyMembershipId, characterId):
        url = DEFAULT_URL + '/Platform/Destiny2/{}/Account/{}/Character/{}/Stats/UniqueWeapons/'
        url = url.format(membershipType, destinyMembershipId, characterId)
        return self.request(url)
    
    def GetDestinyAggregateActivityStats(self, membershipType, destinyMembershipId, characterId):
        url = DEFAULT_URL + '/Platform/Destiny2/{}/Account/{}/Character/{}/Stats/AggregateActivityStats/'
        url = url.format(membershipType, destinyMembershipId, characterId)
        return self.request(url)
    
class stats(api):
    def __init__(self, info):
        self.info = info

    def getKills(self):
        return int(self.info['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['kills']['basic']['value'])
    
    def getOpponentsDefeated(self):
        return int(self.info['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['opponentsDefeated']['basic']['value'])
    
    def getDeaths(self):
        return int(self.info['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['deaths']['basic']['value'])
    
    def getAssists(self):
        return int(self.info['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['assists']['basic']['value'])
    
    def getKD(self):
        return round(self.info['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['killsDeathsRatio']['basic']['value'], 2)
    
    def getKDA(self):
        return round(self.info['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['killsDeathsAssists']['basic']['value'], 2)
    
    def getEfficiency(self):
        return round(self.info['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['efficiency']['basic']['value'], 2)
    
    def getPrecisionKills(self):
        return int(self.info['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['precisionKills']['basic']['value'])
    
    def getMostKills(self):
        return int(self.info['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['bestSingleGameKills']['basic']['value'])
    
    def getHighestKillstreak(self):
        return int(self.info['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['longestKillSpree']['basic']['value'])
    
    def getRevives(self):
        return int(self.info['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['resurrectionsPerformed']['basic']['value'])
    
    def getTimePlayed(self):
        return str(round((self.info['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['secondsPlayed']['basic']['value'])/3600, 2)) + ' h'
    
    
