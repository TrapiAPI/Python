import trapi

Skyblock = trapi.Skyblock("API_KEY")

data = Skyblock.getProfile(profile="PROFILE_ID")

print(data)