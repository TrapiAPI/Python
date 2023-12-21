import trapi

Resources = trapi.Resources("API_KEY")

data = Resources.getVanityPets()

print(data)