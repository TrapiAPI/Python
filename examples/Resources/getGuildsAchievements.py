import trapi

Resources = trapi.Resources("API_KEY")

data = Resources.getGuildsAchievements()

print(data)