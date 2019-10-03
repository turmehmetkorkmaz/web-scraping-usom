# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:23:31 2019

@author: TORTUMLU
"""

'''
from bs4 import BeautifulSoup as soup
import urllib.request
from elasticsearch import Elasticsearch
from datetime import datetime

def make_soup(url):
    page=urllib.request.urlopen(url)
    soupdata=soup(page,"html.parser")
    return soupdata

#following to six line was wrote for elasticsearch.

ES_HOST = {"host" : "localhost", "port" : 9200}
INDEX_NAME = 'usom'
TYPE_NAME = 'zararli-baglantilar'
ID_FIELD = 'id'
bulk_data = []
header=["ID","URL","AÇIKLAMA","KAYNAK","TARİH"]

i=0;date=[]
n=2 #Default i took 20 pages, but you can make it more or les.
#This loop for pagination
for p in list(range(1,n)):
    string_version=str(p)
    soupd= make_soup("https://www.usom.gov.tr/zararli-baglantilar/"+string_version+".html")
    for record in soupd.findAll("tr"):
        data_dict = {}

        for rows in record.findAll("td"):
            if i%5==0:
                data_dict[header[i%5]]=rows.text
                idd=rows.text
            if i%5==1:
                data_dict[header[i%5]]=rows.text
            if i%5==2:
                data_dict[header[i%5]]=rows.text
            if i%5==3:
                 data_dict[header[i%5]]=rows.text
            if i%5==4:
                data_dict[header[i%5]]= datetime.strptime(rows.text, '%Y-%m-%d ')#i took date as date value.
            i=i+1

            #with the "i" value, my purpose was to control table values(td)
        op_dict = {
            "index": {
                "_index": INDEX_NAME,
                "_type": TYPE_NAME,
                "_id": idd
            }
        }
        bulk_data.append(op_dict)
        bulk_data.append(data_dict)

# create ES client, create index, if its name exist i deleted the previous one.
es = Elasticsearch(hosts=[ES_HOST])
if es.indices.exists(INDEX_NAME):
    print("deleting '%s' index..." % (INDEX_NAME))
    res = es.indices.delete(index=INDEX_NAME)
    print(" response: '%s'" % (res))

# since we are running locally, use one shard and no replicas
request_body = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    }
}
print("creating '%s' index..." % (INDEX_NAME))
res = es.indices.create(index=INDEX_NAME, body=request_body)
print(" response: '%s'" % (res))

# bulk index the data
print("bulk indexing...")
res = es.bulk(index=INDEX_NAME, body=bulk_data, refresh=True)
'''

# Import Elasticsearch package
from elasticsearch import Elasticsearch
INDEX_NAME="html_status_2"
ES_HOST = {"host" : "10.0.0.47", "port" : 9200}
es = Elasticsearch(hosts=[ES_HOST])
request_body = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    }
}

if es.indices.exists(INDEX_NAME):
    print("deleting '%s' index..." % (INDEX_NAME))
    res = es.indices.delete(index=INDEX_NAME)
    print(" response: '%s'" % (res))

# Connect to the elastic cluster
#res = es.indices.create(index=INDEX_NAME, body=request_body)