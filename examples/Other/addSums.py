import trapi

Other = trapi.Other("API_KEY")

result = Other.addSums(1, 5)

if result:
    print("Response:")
    print(result)
else:
    print("Request failed.")