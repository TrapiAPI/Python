import trapi

PlayerData = trapi.PlayerData("API_KEY")

data = PlayerData.getPlayerStatus("PLAYER_UUID")

print(data)