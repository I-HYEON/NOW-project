from django.conf import settings
from .serializers import DepositProductsSerializerD, DepositProductsSerializerC, DepositProductsSerializer, DepositOptionsSerializer, CommentSerializer
from .models import DepositOptions, DepositProducts, Comment
from accounts.serializers import UserSerializer
from accounts.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from collections import defaultdict
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
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
    
    base_serializer = DepositProductsSerializerC(data=base_list, many=True)
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

        # 추가시킬 조건문들
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
                        q_sal |= Q(salary__lte=2000)
                    elif data_val == '2':
                        q_sal |= Q(salary__gt=2000,salary__lte=4000)
                    elif data_val == '3':
                        q_sal |= Q(salary__gt=4000,salary__lte=6000)
                    elif data_val == '4':
                        q_sal |= Q(salary__gt=6000,salary__lte=10000)
                    elif data_val == '5':
                        q_sal |= Q(salary__gt=10000)
                elif data_key == 'wealth':
                    if data_val == '1':
                        q_whl |= Q(wealth__lte=2000)
                    elif data_val == '2':
                        q_whl |= Q(wealth__gt=2000,wealth__lte=6000)
                    elif data_val == '3':
                        q_whl |= Q(wealth__gt=6000,wealth__lte=10000)
                    elif data_val == '4':
                        q_whl |= Q(wealth__gt=10000,wealth__lte=20000)
                    elif data_val == '5':
                        q_whl |= Q(wealth__gt=20000,wealth__lte=40000)
                    elif data_val == '6':
                        q_whl |= Q(wealth__gt=40000)
        q = q_gen & q_age & q_sal & q_whl & q_ten
        # 조건에 해당되는 User 쿼리
        user_filtered = User.objects.filter(q)
        # pprint(user_filtered)
        
        deposit_count = defaultdict(int)

        # 해당되는 User들을 돌면서 적금들 갯수 카운트
        for user_fil in user_filtered:
            for user in user_fil.deposit.all():
                deposit_count[user] += 1

        # 가장 많은 유저가 든 적금순으로 정렬
        result = sorted(deposit_count.items(), key=lambda x: x[1], reverse=True)
        # 결과를 Json으로 변환하는 과정
        result_data = {}
        i = 1
        for temp in result:
            temp_data = DepositProductsSerializerD(temp[0])
            result_data[i]=(temp_data.data)
            i+=1
        if i == 1:
            temp = DepositProducts.objects.all()
            result_data = DepositProductsSerializerD(temp, many=True)
            sorted_data = sorted(result_data.data, key=lambda x: x['max_intr'], reverse=True)
            return Response({0:sorted_data,1:[]}, status=status.HTTP_200_OK)
        return Response({0:[],1:result_data}, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def deposit_sign(request, fin_prdt_cd, user_pk):
    # cd에 맞는 적금 정보를 가지고옴
    deposit_info = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    # user_pk에 맞는 유저 정보를 가지고옴
    User_info = User.objects.get(pk=user_pk)
    # 만약 유저의 deposit(Manytomanyfield)에서 이미 존재한다면?
    if deposit_info in User_info.deposit.all():
        # 삭제
        User_info.deposit.remove(deposit_info)
    else:
        # 없으면 추가
        User_info.deposit.add(deposit_info)
    # 최신화 된 유저정보를 Response로 반환하기 위해 직렬화
    User_info = UserSerializer(User_info)
    # 반환
    return Response(User_info.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
@api_view(['GET','DELETE','PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serilaizer = CommentSerializer(comment)
        return Response(serilaizer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, fin_prdt_cd):
    depositproducts = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(depositproducts=depositproducts,user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)