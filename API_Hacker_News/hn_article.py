import requests
import json

# Вызов API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Анализ структуры данных.
response_dicts = r.json()
readable_file = 'readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dicts, f, indent=4)

print(response_dicts)







