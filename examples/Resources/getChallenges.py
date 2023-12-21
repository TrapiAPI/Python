import trapi

Resources = trapi.Resources("API_KEY")

data = Resources.getChallenges()

print(data)