import trapi

PlayerData = trapi.PlayerData("API_KEY")

data = PlayerData.getPlayer("PLAYER_NAME")

print(data)