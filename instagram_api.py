import requests
from config import INSTAGRAM_APP_ID, INSTAGRAM_APP_SECRET, INSTAGRAM_ACCESS_TOKEN

def get_instagram_posts(query, access_token, count=100):
    url = f"https://graph.facebook.com/v12.0/ig_hashtag_search?q={query}&user_id={INSTAGRAM_APP_ID}&fields=id,name,media_count&access_token={access_token}"
    response = requests.get(url)
    hashtag_id = response.json()['data'][0]['id']

    url = f"https://graph.facebook.com/v12.0/{hashtag_id}/recent_media?user_id={INSTAGRAM_APP_ID}&fields=caption,media_type,media_url,permalink,thumbnail_url,timestamp&limit={count}&access_token={access_token}"
    response = requests.get(url)

    return [post['caption'] for post in response.json()['data'] if 'caption' in post]
