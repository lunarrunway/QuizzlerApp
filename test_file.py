import requests


data = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")

question_data = data.json()['results']
print(question_data)
