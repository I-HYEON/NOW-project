from django.conf import settings
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, CommentSerializer
from .models import DepositOptions, DepositProducts, Comment
from accounts.models import User
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

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

@api_view(['POST'])
def recomend_deposit(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        
        return Response(data, status=status.HTTP_200_OK)
    

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
def comment_create(request, depositproducts_pk):
    depositproducts = get_object_or_404(DepositProducts, pk=depositproducts_pk)
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(depositproducts=depositproducts)
        return Response(serializer.data, status=status.HTTP_201_CREATED)