import requests
from config import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET

def get_facebook_access_token(app_id, app_secret):
    url = f"https://graph.facebook.com/oauth/access_token?client_id={app_id}&client_secret={app_secret}&grant_type=client_credentials"
    response = requests.get(url)
    return response.json().get('access_token')

def get_facebook_posts(query, access_token, count=100):
    url = f"https://graph.facebook.com/search?q={query}&type=post&fields=message&limit={count}&access_token={access_token}"
    response = requests.get(url)
    return [post['message'] for post in response.json()['data']]
