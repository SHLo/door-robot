import requests

URL = 'https://door-robot-default-rtdb.firebaseio.com/'

# For anonymous sign in, **TODO** Change the key below to be the API key of your Firebase project (Project Settings > Web API Key).
AUTH_URL = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyBilFmMjrGI0TVhZ5h_gDvoO4PKzx-WDgs';
headers = {'Content-type': 'application/json'}
auth_req_params = {'returnSecureToken':'true'}

connection = requests.Session()
connection.headers.update(headers)
auth_request = connection.post(url=AUTH_URL, params=auth_req_params)
auth_info = auth_request.json()
auth_params = {'auth': auth_info['idToken']}


def update_db(key, value):
    url = f'{URL}{key}.json'
    # Post the data to the database
    post_request = connection.put(url=url,
            data=value, params=auth_params)
    # Make sure data is successfully sent
    print('data sent: ' + str(post_request.ok))