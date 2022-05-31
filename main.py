import json
import requests
import re
import google.auth
import google.auth.transport.requests
from flask import jsonify

creds, project = google.auth.default()

def refAccessToken(creds):    
    auth_req = google.auth.transport.requests.Request()
    creds.refresh(auth_req)
    authToken = creds.token
    return authToken

def response_get_Data(authToken,url):
    headers = {
       "Accept": "application/json",
       "Authorization": "Bearer "+authToken
     }
    response = requests.request(
       "GET",
       url,
       headers=headers
     ) 
    response = response.text.replace("u'", "'")
    return response

def response_post_Data(authToken,url):
    headers = {
       "Accept": "application/json",
       "Authorization": "Bearer "+authToken
     }
    response = requests.request(
       "POST",
       url,
       headers=headers
     ) 
    response = response.text.replace("u'", "'")
    return response  

def get_organisations(request):
    org_list = []
    project_url="https://cloudresourcemanager.googleapis.com/v1beta1/organizations:search"
    authToken = refAccessToken(creds)
    resp = response_post_Data(authToken,project_url)
    org_list = json.loads(resp)
    print(org_list)
    #return org_list

    
