from django.shortcuts import render
import requests
import pymongo
from pymongo import MongoClient
from django.http import JsonResponse
import json
import time

cluster=MongoClient("mongodb+srv://rashmeet:rashmeet@bitcoin.7uzqf.mongodb.net/test?retryWrites=true&w=majority")
db=cluster["test"]
collection=db['test']
response = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
res=response.json()
print(res)
res=res['rates']
collection.insert_one(res)
def index(request):
    res=collection.find_one({})
    coins=[]
    for i in res.keys():
        if(not i=='_id'):
            #print(i)
            coins.append(res[i])
    context={'coins':coins}
    return render(request,'index.html',context)

def api(request):
    data = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
    res=data.json()
    return JsonResponse(res)

