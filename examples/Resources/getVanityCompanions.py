import trapi

Resources = trapi.Resources("API_KEY")

data = Resources.getVanityCompanions()

print(data)