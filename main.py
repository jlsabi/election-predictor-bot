from config import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET, INSTAGRAM_ACCESS_TOKEN
from twitter_api import authenticate, get_tweets
from facebook_api import get_facebook_access_token, get_facebook_posts
from instagram_api import get_instagram_posts
from data_processing import create_dataframe
from prediction_model import predict_election

api = authenticate()

query = 'election'
tweets = get_tweets(api, query)

facebook_access_token = get_facebook_access_token(FACEBOOK_APP_ID, FACEBOOK_APP_SECRET)
facebook_posts = get_facebook_posts(query, facebook_access_token)

instagram_posts = get_instagram_posts(query, INSTAGRAM_ACCESS_TOKEN)

all_posts = tweets + facebook_posts + instagram_posts
posts_df = create_dataframe(all_posts)
#make sure to edit the candidate11 and candidate22
candidate1 = 'candidate11'
candidate2 = 'candidate22'

prediction = predict_election(posts_df, candidate1, candidate2)
print(prediction)
