import trapi

PlayerData = trapi.PlayerData("API_KEY")

data = PlayerData.getGuild("GUILD_NAME")

print(data)