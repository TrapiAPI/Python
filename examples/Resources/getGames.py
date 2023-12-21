import trapi

Resources = trapi.Resources("API_KEY")

data = Resources.getGames()

print(data)