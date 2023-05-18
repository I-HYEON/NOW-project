from django.conf import settings
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from .models import DepositOptions, DepositProducts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests


DEPOSIT_BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

# Create your views here.

@api_view(['GET'])
def save_deposit(request):
    URL = DEPOSIT_BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo':1
    
    }
    results = requests.get(URL, params=params).json()
    
    result = results['result']['baseList']
    serializer = DepositProductsSerializer(data=result, many=True)
    
    if serializer.is_valid():
        serializer.save()
    else:
        Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    for result in results['result']['optionList']:
        serializer = DepositOptionsSerializer(data=result)
        if serializer.is_valid():
            temp = serializer.save(fin_prdt_cd=DepositProducts.objects.get(fin_prdt_cd=result['fin_prdt_cd']))
            temp.save()
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('message : okay')