from urllib.parse import urljoin
import json
import requests

def get_token_info(request, username, password, client_id, client_secret):
    headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": 'password',
        "username": username,
        "password": password,
        "client_id": client_id,
        "client_secret": client_secret,
    }
    zoho_invoice_url = 'http://localhost:8000/o/token/'
    response = requests.post(zoho_invoice_url, data=data)
    token_info = json.loads(response.content)
    return token_info