import trapi

Skyblock = trapi.Skyblock("API_KEY")

data = Skyblock.getAuctions()

print(data)