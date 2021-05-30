from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
import requests

import urllib
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .utils import get_json_val, find_colors_img, find_border_color, find_dominant_color, hex_val_color,resize_img , retrieve_image_from_url


def get_data(request):

    if request.method == "GET":
        
        src1=request.GET.get('src')
        src1=str(src1)
        src1=src1.replace(" ","%20")
        print(src1)
        dict=get_json_val(src1)
        return JsonResponse(dict)
        