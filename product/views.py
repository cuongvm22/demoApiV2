from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from services import services

@api_view(["GET"])
def getProduct(request,productId):
    try:
        # reuturn a contain object
        result = {}
        # get product from database
        product = services.getProductById(productId)
        # convert product to dict 
        result = product[0].__dict__
        # remove error data when convert to json
        del result['_state']
        # convert int to str
        for k,v in result.items():
            result[k] = str(v)
            # result[k] = str(v).replace('\\n', '\\\\n')
        # convert result to json
        result = JsonResponse(result,json_dumps_params={'indent': 2,'ensure_ascii':False},safe=False)
        return result
  
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

