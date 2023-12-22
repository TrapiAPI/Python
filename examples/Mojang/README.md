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