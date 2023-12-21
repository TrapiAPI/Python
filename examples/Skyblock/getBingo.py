import trapi

Skyblock = trapi.Skyblock("API_KEY")

data = Skyblock.getBingo(uuid="PLAYER_UUID")

print(data)