import trapi

Skyblock = trapi.Skyblock("API_KEY")

data = Skyblock.getProfiles(uuid="PLAYER_UUID")

print(data)