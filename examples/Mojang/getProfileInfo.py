import trapi

Mojang = trapi.Mojang("API_KEY")

data = Mojang.getProfileInfo("USERNAME")

print(data)