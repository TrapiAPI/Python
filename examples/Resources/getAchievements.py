import trapi

Resources = trapi.Resources("API_KEY")

data = Resources.getAchievements()

print(data)