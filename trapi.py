import requests

BASE_URL = 'https://api.trapi.dev/'


class PlayerData:
    def __init__(self, api_key=''):
        self.api_key = api_key

    def getPlayer(self, playername):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/player/{playername}?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getPlayerStatus(self, playeruuid):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/status/{playeruuid}?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getGuild(self, guildname):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/guild/{guildname}?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getRecentGames(self, uuid):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/recentgames/{uuid}?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
class Resources:
    def __init__(self, api_key=''):
        self.api_key = api_key

    def getGames(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/resources/games/?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getAchievements(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/resources/achievements/?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getChallenges(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/resources/challenges/?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getQuests(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/resources/quests/?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getGuildsAchievements(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/resources/guilds/achievements/?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getVanityPets(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/resources/vanity/pets/?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getVanityCompanions(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/resources/vanity/companions/?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
class Skyblock:
    def __init__(self, api_key=''):
        self.api_key = api_key
        
    def getCollections(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/skyblock/collections?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getSkills(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/skyblock/skills?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getElection(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/skyblock/election?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getAuction(self, type='uuid', uuid=None, player=None, profile=None):
        try:
            if type == 'uuid':
                response = requests.get(BASE_URL + f'/v1/skyblock/auction/{type}/{uuid}?api_key=' + self.api_key)
            elif type == 'player':
                response = requests.get(BASE_URL + f'/v1/skyblock/auction/{type}/{player}?api_key=' + self.api_key)
            elif type == 'profile':
                response = requests.get(BASE_URL + f'/v1/skyblock/auction/{type}/{profile}?api_key=' + self.api_key)
            else:
                print("The type has to be <UUID/PLAYER/PROFILE>!")

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getAuctions(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/skyblock/auctions?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getAuctionsEnded(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/skyblock/auctions_ended?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getBazaar(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/skyblock/bazaar?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getProfile(self, profile=None):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/skyblock/profile/{profile}?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getProfiles(self, uuid=None):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/skyblock/profiles/{uuid}?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getMuseum(self, profile=None):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/skyblock/museum/{profile}?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getBingo(self, uuid=None):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/skyblock/bingo/{uuid}?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def getFireSales(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/skyblock/firesales/?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
class Mojang:
    def __init__(self, api_key=''):
        self.api_key = api_key

    def getProfileInfo(self, username=None):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/mojang/users/profiles/minecraft/{username}?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None

class Other:
    def __init__(self, api_key=''):
        self.api_key = api_key

    def addSums(self, num1, num2):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/add/{num1}/{num2}?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def randomWord(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/randomword/?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None
        
    def headsOrtails(self):
        try:
            # Sending a GET request to the specified URL
            response = requests.get(BASE_URL + f'/v1/h-t/?api_key=' + self.api_key)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the content of the response
                return response.text
            else:
                # Printing an error message if the request was not successful
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            # Handling any exceptions that might occur during the request
            print(f"An error occurred: {e}")
            return None