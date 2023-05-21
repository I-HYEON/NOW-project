from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

import os
import sys
import urllib.request
import json
# Create your views here.
@api_view(['GET'])
def search(request,words):
    client_id = "wDitqN6NrKBFrtsSNC4E"
    client_secret = "O1g5I7MqPr"
    encText = urllib.parse.quote(words)
    url = "https://openapi.naver.com/v1/search/encyc.json?query=" + encText + "&display=24&start=1" # JSON 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        json_data = json.loads(response_body.decode('utf-8'))
        return Response(json_data,status=status.HTTP_200_OK)
    else:
        Response("BAD_REQUEST", status=status.HTTP_400_BAD_REQUEST)
    