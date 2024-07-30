import requests
import json
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

# Your application credentials
def get_pic(login):
    UID = "u-s4t2ud-c19fa334c4a5d14748060c70f39ea875b2b41bf5d57268be7fcfb3755ef43b7b"
    SECRET = "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"
    API_BASE_URL = "https://api.intra.42.fr"

    # Create a client with your credentials
    client = BackendApplicationClient(client_id=UID)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=f"{API_BASE_URL}/oauth/token", client_id=UID, client_secret=SECRET)

    # Now, you can fetch data using the obtained access token
    response = oauth.get(f"{API_BASE_URL}/v2/users/" + login )
    data = response.json()

    # Assuming 'data' contains the JSON response
    medium_image_url = data["image"]["versions"]["medium"]
    emailuu = data["email"]
    print(emailuu)
    print(json.dumps(data, indent=4))
    print(medium_image_url)
    return medium_image_url

get_pic("isalama")