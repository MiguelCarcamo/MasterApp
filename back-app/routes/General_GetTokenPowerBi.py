from flask import Blueprint, jsonify, request
import pandas as pd
import asyncio
import json
from pandas import json_normalize
import requests

main=Blueprint('General_GetTokenPowerBi_blueprint', __name__)
_loop2 = asyncio.get_event_loop()

@main.route('/')
def get_General_GetTokenPowerBi():
    try:
        url = 'https://login.microsoftonline.com/03fa6430-2a3b-4a59-b916-ffb7eb0b395c/oauth2/token'
        headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
        data = {
            'grant_type': 'password',
            'username': 'miguel.carcamo@tegraglobal.com',
            'password': 'Naruto04..',
            'client_id': '4e3ecd43-63b6-4504-a5f4-2b9639615dd0',
            'resource': 'https://analysis.windows.net/powerbi/api',
            'scope': 'openid'
        }

        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            access_token = response.json().get('access_token')
            return jsonify({'access_token': str(access_token)}), 200
        else:
            return jsonify({'access_token': str(response.text)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500