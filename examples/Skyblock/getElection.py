import trapi

Skyblock = trapi.Skyblock("API_KEY")

data = Skyblock.getElection()

print(data)