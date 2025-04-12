import requests

api_key = "bd6f1dd81d2f2eb8414a656ec18c6ef5"  # Replace with your API key if needed
city = "Delhi"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

# Print the status and full JSON response
print("Status Code:", response.status_code)
print("Response:", response.json())
