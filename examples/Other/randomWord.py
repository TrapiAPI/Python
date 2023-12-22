import trapi

Other = trapi.Other("API_KEY")

result = Other.randomWord()

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")