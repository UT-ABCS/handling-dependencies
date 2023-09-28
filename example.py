# Example of code that requires a dependency to run
# Adapted from: https://api-ninjas.com/api/quotes
import requests

category = "happiness"
api_url = "https://api.api-ninjas.com/v1/quotes?category={}".format(category)
api_key = "MYG6WHHbcStdZncDRQj1rw==yke1Qfn91X3xZSLi"
response = requests.get(api_url, headers={"X-Api-Key": api_key})

if response.status_code == requests.codes.ok:
    response = response.json()
    print("Quote: " + response[0]["quote"])
    print("Author: " + response[0]["author"])
    print("Category: " + response[0]["category"])
else:
    print("Error:", response.status_code, response.text)