import trapi

Skyblock = trapi.Skyblock("API_KEY")

data = Skyblock.getAuctionsEnded()

print(data)