from django.conf import settings
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from .models import DepositOptions, DepositProducts
from accounts.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

from django.db.models import Count, Q

DEPOSIT_BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

# Create your views here.

@api_view(['GET'])
def save_deposit(request):
    URL = DEPOSIT_BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    
    results = requests.get(URL, params=params).json()
    base_list = results['result']['baseList']
    option_list = results['result']['optionList']
    
    base_serializer = DepositProductsSerializer(data=base_list, many=True)
    if base_serializer.is_valid():
        base_serializer.save()
    else:
        Response(base_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    for option in option_list:
        option_serializer = DepositOptionsSerializer(data=option)
        if option_serializer.is_valid():
            deposit_product = DepositProducts.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
            option_serializer.save(fin_prdt_cd=deposit_product)
        else:
            Response(option_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # option list 중복 제거
    duplicate_options = (
        DepositOptions.objects
        .values('fin_prdt_cd', 'save_trm')
        .annotate(count=Count('id'))
        .filter(count__gt=1)
    )

    for duplicate in duplicate_options:
        fin_prdt_cd = duplicate['fin_prdt_cd']
        save_trm = duplicate['save_trm']
        duplicate_objects = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd, save_trm=save_trm)
        duplicate_objects.exclude(pk=duplicate_objects.first().pk).delete()

    return Response(base_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def deposit_detail(request, fin_prdt_cd):
    deposit_info = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    deposit_info_serializer = DepositProductsSerializer(deposit_info)

    deposit_detail_info = DepositOptions.objects.filter(fin_prdt_cd_id=deposit_info.id)
    deposit_detail_info_serializer = DepositOptionsSerializer(deposit_detail_info, many=True)

    serializer_data = {
        'deposit_detail' : deposit_info_serializer.data,
        'deposit_detail_options' : deposit_detail_info_serializer.data
    }

    return Response(serializer_data, status=status.HTTP_200_OK)

from django.db.models import Q
from pprint import pprint
@api_view(['POST'])
def recomend_deposit(request):
    if request.method == 'POST':
        data = request.data
        # 받은 데이터 파싱
        conversion = {
            'gen' : 'gender', 'age' : 'age', 'sal' : 'salary', 'whl' : 'wealth', 'ten' : 'tendency',
            'one' : '1', 'two' : '2', 'thr' : '3', 'fou' : '4', 'fiv' : '5', 'six' : '6',
        }
        filter_conditions = {}
        filter_conditions['gender'] = []
        filter_conditions['age'] = []
        filter_conditions['salary'] = []
        filter_conditions['wealth'] = []
        filter_conditions['tendency'] = []

        q_gen = Q()
        q_age = Q()
        q_sal = Q()
        q_whl = Q()
        q_ten = Q()

        for item in data.items():
            # print(item)
            if item[1]:
                data_key = conversion[item[0][:3]]
                data_val = conversion[item[0][4:]]
                if data_key == 'gender':
                    q_gen |= Q(gender=data_val)
                elif data_key == 'tendency':
                    q_ten |= Q(tendency=data_val)
                elif data_key == 'age':
                    if data_val == '1':
                        q_age |= Q(age__lte=20)
                    elif data_val == '2':
                        q_age |= Q(age__gt=20,age__lte=30)
                    elif data_val == '3':
                        q_age |= Q(age__gt=30,age__lte=40)
                    elif data_val == '4':
                        q_age |= Q(age__gt=40,age__lte=50)
                    elif data_val == '5':
                        q_age |= Q(age__gt=50,age__lte=60)
                    elif data_val == '6':
                        q_age |= Q(age__gt=60)
                elif data_key =='salary':
                    if data_val == '1':
                        q_sal |= Q(age__lte=20000000)
                    elif data_val == '2':
                        q_sal |= Q(age__gt=20000000,age__lte=40000000)
                    elif data_val == '3':
                        q_sal |= Q(age__gt=40000000,age__lte=60000000)
                    elif data_val == '4':
                        q_sal |= Q(age__gt=60000000,age__lte=100000000)
                    elif data_val == '5':
                        q_sal |= Q(age__gt=100000000)
                elif data_key == 'wealth':
                    if data_val == '1':
                        q_whl |= Q(age__lte=20000000)
                    elif data_val == '2':
                        q_whl |= Q(age__gt=20000000,age__lte=60000000)
                    elif data_val == '3':
                        q_whl |= Q(age__gt=60000000,age__lte=100000000)
                    elif data_val == '4':
                        q_whl |= Q(age__gt=100000000,age__lte=200000000)
                    elif data_val == '5':
                        q_whl |= Q(age__gt=200000000,age__lte=400000000)
                    elif data_val == '6':
                        q_whl |= Q(age__gt=400000000)
        q = q_gen & q_age & q_sal & q_whl & q_ten
        user_filtered = User.objects.filter(q)
        pprint(user_filtered)
        return Response(data, status=status.HTTP_200_OK)