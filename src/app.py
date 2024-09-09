import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = 'https://api.api-ninjas.com/v1/passwordgenerator'
API_KEY = os.getenv('API_KEY')
header = {'X-Api-Key': API_KEY}
print(API_KEY)

def get_password(length):
    param = {'length' : length}
    response = requests.get(API_URL, headers=header, params=param)
    if response.status_code != requests.codes.ok:
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}") 
    response.raise_for_status()
    data = response.json()
    return data['random_password']


if __name__ == '__main__':
    print(get_password(8))
    