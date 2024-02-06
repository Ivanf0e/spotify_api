from requests import post, get, put
import json

CLIENT_ID, CLIENT_SECRET = open('spotify_env.txt').read().split('\n')

user = post('https://accounts.spotify.com/api/token',{
    'grant_type': 'client_credentials',
    'refresh_token': 'refreshToken',
    'scope': 'playlist-read-private user-top-read user-read-private user-read-email',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET},
    headers={'Content-Type': 'application/x-www-form-urlencoded'}).json()
token = user['access_token']

result = get(
#     'https://api.spotify.com/v1/me/playlists',
    'https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg',
#     'https://api.spotify.com/v1/me',
    headers={'Authorization': f'Bearer {token}'})

print(result.json())