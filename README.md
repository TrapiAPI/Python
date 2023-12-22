# Overview
This API Wrapper is not a pip package and so you will need to clone the repository and run it from the repository to import the package.

# Authirection

To authenticate you need to put the following:

```python
PlayerData = PlayerData("API_KEY")
Resources = Resources("API_KEY")
Skyblock = Skyblock("API_KEY")
```

# PlayerData

## getPlayer("PlayerName")

This pulls the data of a player from the Hypixel API.

Example:

```python
import trapi

PlayerData = PlayerData("")

result = PlayerData.getPlayer("PLAYER_NAME")

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getGuild("GUILD_NAME")

This pulls the data of a guild from the Hypixel API.

Example:

```python
import trapi

PlayerData = PlayerData("")

result = PlayerData.getGuild("GUILD_NAME")

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getPlayerStatus("PLAYER_UUID")

This pulls the status of a player.

Example:

```python
import trapi

PlayerData = PlayerData("")

result = PlayerData.getPlayerStatus("PLAYER_UUID")

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getRecentGames("PLAYER_UUID")

This gets the recently played games for a given player.

Example:

```python
import trapi

PlayerData = PlayerData("")

result = PlayerData.getPlayerStatus("PLAYER_UUID")

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

# Resources

## getGames()

Gets the games list.

Example:

```python
import trapi

Resources = Resources("")

result = Resources.getGames()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getAchievements()

Gets the achievements list.

Example:

```python
import trapi

Resources = Resources("")

result = Resources.getAchievements()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getChallenges()

Gets the challanges list.

Example:

```python
import trapi

Resources = Resources("")

result = Resources.getChallenges()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getQuests()

Gets the quests list.

Example:

```python
import trapi

Resources = Resources("")

result = Resources.getQuests()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getGuildsAchievements()

Gets the Guilds Achievements.

Example:

```python
import trapi

Resources = Resources("")

result = Resources.getGuildsAchievements()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getVanityPets()

Gets the Vanity Pets.

Example:

```python
import trapi

Resources = Resources("")

result = Resources.getVanityPets()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getVanityCompanions()

Gets the Vanity Companions.

Example:

```python
import trapi

Resources = Resources("")

result = Resources.getVanityCompanions()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

# Skyblock

## getCollections()

Gets the Skyblock Collections.

Example:

```python
import trapi

Skyblock = Skyblock("")

result = Skyblock.getCollections()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getSkills()

Gets the Skyblock Skills.

Example:

```python
import trapi

Skyblock = Skyblock("")

result = Skyblock.getSkills()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getElection()

Gets the Skyblock Elections data.

Example:

```python
import trapi

Skyblock = Skyblock("")

result = Skyblock.getElection()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getAuction()

Gets the Skyblock Auction data.

Example:

```python
import trapi

Skyblock = Skyblock("")

result = Skyblock.getAuction(type='player', player='PLAYER_NAME')

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getAuctionsEnded()

Gets the Skyblock Auctions Ended data.

Example:

```python
import trapi

Skyblock = Skyblock("")

result = Skyblock.getAuctionsEnded()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getBazaar()

Gets the Skyblock Bazzaar data.

Example:

```python
import trapi

Skyblock = Skyblock("")

result = Skyblock.getBazaar()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getProfile()

Gets the Skyblock Profile data.

Example:

```python
import trapi

Skyblock = Skyblock("")

result = Skyblock.getProfile(profile="PROFILE_ID")

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getProfiles()

Gets the Skyblock Profiles data.

Example:

```python
import trapi

Skyblock = Skyblock("")

result = Skyblock.getProfiles(uuid="PLAYER_UUID")

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getMuseum()

Gets the Skyblock Museum data.

Example:

```python
import trapi

Skyblock = Skyblock("")

result = Skyblock.getMuseum(profile="PROFILE_ID")

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getBingo()

Gets the Skyblock Bingo data.

Example:

```python
import trapi

Skyblock = Skyblock("")

result = Skyblock.getBingo(uuid="UUID")

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## getFireSales()

Gets the fire sales data.

Example:

```python
import trapi

Skyblock = Skyblock("")

result = Skyblock.getFireSales()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

# Mojang

## getProfileInfo()

Gets the profile information of a user on the Mojang API.

Example:

```python
import trapi

Mojang = Mojang("")

result = Mojang.getProfileInfo("USERNAME")

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

# Other

## addSums()

Adds the sums of two numbers.

Example:

```python
import trapi

Other = Other("")

result = Other.addSums(5, 1)

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## headsOrtails()

Outputs `heads` or `tails`.

Example:

```python
import trapi

Other = Other("")

result = Other.headsOrtails()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```

## randomWord()

Outputs a random word.

Example:

```python
import trapi

Other = Other("")

result = Other.randomWord()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")
```