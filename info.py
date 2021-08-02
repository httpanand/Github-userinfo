import requests
from pprint import pprint

username = "httpanand"
api = f"https://api.github.com/users/{username}"
user_data = requests.get(api).json()


name = user_data["name"]
website = user_data["blog"]
location = user_data["location"]
email = user_data["email"]
public_repos = user_data["public_repos"]
public_gists = user_data["public_gists"]
followers = user_data["followers"]
following = user_data["following"]
createdate = user_data["created_at"]


print("\nUser:", username)
print("\nName:", name)
print("\nWebsite:", website)
print("\nLocation:", location)
print("\nEmail:", email)
print("\nTotal Public repositories:", public_repos)
print("\nTotal Public Gists:", public_gists)
print("\nTotal followers:", followers)
print("\nTotal following:", following)
print("\nDate Created:", createdate)
