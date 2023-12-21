import trapi

Skyblock = trapi.Skyblock("API_KEY")

data = Skyblock.getCollections()

print(data)