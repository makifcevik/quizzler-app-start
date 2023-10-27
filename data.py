import requests


parameters = {
    "amount": 10,
    "category": 23,
    "type": "boolean"
}

api_data = requests.get("https://opentdb.com/api.php", params=parameters).json()
question_data = api_data["results"]  # a list containing dictionaries about question data

