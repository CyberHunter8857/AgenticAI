import requests, json

username= input("Enter Your Github Username: ")


url= f"https://api.github.com/users/{username}"


try:
    response= requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    exit()

if response.status_code==200:
    data= response.json()
    print(f"\nName:{data['name']}")
    print(f"Username:{data['login']}")
    print(f"Bio:{data['bio']}")
    print(f"Followers:{data['followers']}")
    print(f"Following:{data['following']}")
    print(f"Ratio:{data['followers']/data['following'] if data['following'] != 0 else 'N/A'}")
    print(f"Public Repositories:{data['public_repos']}")
    print(f"ProfileUrl:{data['html_url']}")
else:
    print("User not found.")
