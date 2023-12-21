import trapi

PlayerData = trapi.PlayerData("API_KEY")

data = PlayerData.getRecentGames("PLAYER_UUID")

print(data)