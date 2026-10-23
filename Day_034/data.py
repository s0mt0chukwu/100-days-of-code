import requests

parameters = {
    "amount": "10",
    "type": "boolean",
    "category": 18,
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get("https://opentdb.com/api.php", params=parameters, headers=headers)

response.raise_for_status()
data = response.json()
question_data = data["results"]