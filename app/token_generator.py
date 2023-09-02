import requests, os
from dotenv import load_dotenv, find_dotenv

def create_access_token(client_id, client_secret, region = 'us'):
    data = { 'grant_type': 'client_credentials' }
    response = requests.post('https://%s.battle.net/oauth/token' % region, data=data, auth=(client_id, client_secret))
    return response.json()

load_dotenv(find_dotenv())
client_id = os.environ.get('BLIZZARD_API_CLIENT_ID')
client_secret = os.environ.get('BLIZZARD_API_CLIENT_SECRET')

response = create_access_token(client_id, client_secret)
print(response)