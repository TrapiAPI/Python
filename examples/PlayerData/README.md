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