import trapi

Resources = trapi.Resources("API_KEY")

data = Resources.getQuests()

print(data)