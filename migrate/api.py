# -*- coding: utf-8 -*-
from django.http import JsonResponse
import urllib2
import json
import pickle
import os
from operator import itemgetter
import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def add(request):
    return get_data(request)

def countInfo():

    countries = ['Iraq', 'Iraq', 'Greece', 'Iraq', 'Iraq', 'Iraq', 'China', 'Iraq', 'Egypt', 'Egypt', 'Israel', 'Canada', 'China', 'China', 'China', 'China', 'Israel', 'Afghanistan', 'Mexico', 'Italy', 'Italy', 'Mexico', 'China', 'China', 'Mexico', 'Israel', 'China', 'Afghanistan', 'Afghanistan', 'China', 'China', 'Iraq', 'United Kingdom', 'United Kingdom', 'United Kingdom', 'Egypt', 'Afghanistan', 'Afghanistan', 'China', 'China', 'China', 'China', 'China', 'China', 'United Kingdom', 'Saudi Arabia', 'China', 'China', 'Greece', 'Mexico', 'Iraq', 'Canada', 'China', 'Egypt', 'Japan', 'China', 'Egypt', 'Egypt', 'Iraq', 'Afghanistan', 'Germany', 'France', 'China', 'China', 'China', 'Afghanistan', 'China', 'China', 'China', 'China', 'China', 'Canada', 'Saudi Arabia', 'Kenya', 'Cuba', 'China', 'Egypt', 'China', 'Greece', 'Saudi Arabia', 'China', 'Philippines', 'United Kingdom', 'China', 'France', 'China', 'China', 'China', 'China', 'Saudi Arabia', 'China', 'China', 'China', 'China', 'Saudi Arabia', 'Afghanistan', 'Afghanistan', 'China', 'Israel', 'China', 'Israel', 'Afghanistan', 'United Kingdom', 'Afghanistan', 'Canada', 'China', 'Israel', 'China', 'China', 'China', 'Egypt', 'China', 'Israel', 'China', 'Iraq', 'Antarctica', 'Israel', 'Egypt', 'South Africa', 'South Africa', 'United Kingdom', 'Afghanistan', 'Colombia', 'Germany', 'Iraq', 'China', 'Saudi Arabia', 'Canada', 'Spain', 'Germany', 'Iraq', 'China', 'Iraq', 'United Kingdom', 'United Kingdom', 'Iraq', 'China', 'Egypt', 'Iraq', 'Spain', 'Iraq', 'Brazil', 'Egypt', 'South Africa', 'Uganda', 'Egypt', 'Cuba', 'China', 'China', 'China', 'China', 'China', 'United Kingdom', 'Afghanistan', 'Iraq', 'Afghanistan', 'Cuba', 'Spain', 'China', 'China', 'China', 'China', 'China', 'Canada', 'Cyprus', 'China', 'Cyprus', 'Iraq', 'Cuba', 'Iraq', 'Afghanistan', 'China', 'China', 'China', 'Egypt', 'China', 'Afghanistan', 'Egypt', 'Afghanistan', 'Iraq', 'Afghanistan', 'United Kingdom', 'Israel', 'Afghanistan', 'Iraq', 'Iraq', 'Iraq', 'Israel', 'Saudi Arabia', 'Mexico', 'Mexico', 'Iraq', 'Liberia', 'Mexico', 'Israel', 'Hong Kong', 'United Kingdom', 'Mexico', 'Iraq', 'Mexico', 'Saudi Arabia', 'Mexico', 'Iraq', 'Iraq', 'Iraq', 'Mexico', 'Mexico', 'Mexico', 'Mexico', 'Mexico', 'Iraq', 'Iraq', 'Iraq', 'Mexico', 'Afghanistan', 'Iraq', 'Mexico', 'Iraq', 'Iraq', 'Iraq', 'Iraq', 'Iraq', 'Iraq', 'Iraq', 'Iraq', 'Pakistan', 'Afghanistan', 'Afghanistan', 'Israel', 'Italy', 'Japan', 'Iraq', 'China', 'Iraq', 'Ireland', 'United Kingdom', 'Netherlands', 'China', 'Ukraine', 'Iraq', 'China', 'South Africa', 'Italy', 'Iraq', 'Iraq', 'Afghanistan', 'Iraq', 'United Kingdom', 'Israel', 'China', 'China', 'Mexico', 'Mexico', 'Iraq', 'Iraq', 'Iraq', 'China', 'Iraq', 'Mexico', 'Mexico', 'Mexico', 'Mexico', 'Mexico', 'Mexico', 'Mexico', 'Mexico', 'Mexico', 'Israel', 'Mexico', 'Mexico', 'Mexico', 'Mexico', 'Mexico', 'Iraq', 'Iraq', 'Iraq', 'Japan', 'China', 'Iraq', 'Iraq', 'Zimbabwe', 'China', 'Japan', 'Mexico', 'Mexico', 'Mexico', 'Kenya', 'Kenya', 'Kenya', 'France', 'Kenya', 'Kenya', 'Kenya', 'Israel', 'Germany', 'Turkey', 'Germany', 'Switzerland', 'China', 'Mexico', 'Somalia', 'Mexico', 'Australia', 'New Zealand', 'China', 'Saudi Arabia', 'Japan', 'United Kingdom', 'Cuba', 'Venezuela', 'Cuba', 'Israel', 'Iraq', 'Iraq', 'China', 'Mexico', 'Mexico', 'Mexico', 'Italy', 'Myanmar', 'Iraq', 'France', 'France', 'France', 'France', 'Israel', 'Bangladesh', 'Israel', 'Israel', 'United Kingdom', 'Saudi Arabia', 'Japan', 'Mexico', 'Iraq', 'China', 'Pakistan', 'Cuba', 'Cuba', 'Mexico', 'Mexico', 'Mexico', 'Canada', 'Canada', 'Canada', 'Germany', 'Canada', 'Germany', 'Morocco', 'Israel', 'Ukraine', 'France', 'Australia', 'Mexico', 'Mexico', 'Australia', 'Mexico', 'Mexico']

    country = {}
    for i in countries:
        if i not in country:
            country[i] = 1
        else:
            country[i] += 1
    return country

def get_data(request):

    # words = []
    # for i in range(9, 18):
    #     if i is 9:
    #         url = 'http://www.trumptwitterarchive.com/data/realdonaldtrump/200{0}.json'.format(i)
    #     else:
    #         url = 'http://www.trumptwitterarchive.com/data/realdonaldtrump/20{0}.json'.format(i)
    #
    #     serialized_data = urllib2.urlopen(url).read()
    #
    #     d = json.loads(serialized_data)
    #
    #     for x in range(0, len(d)-1):
    #         str1 = d[x]['text']
    #         str2 = str1.replace("\n", "")
    #         words.append(str2)
    #
    # word_dict = {}
    # stuff = []
    # url = 'https://raw.githubusercontent.com/uwescience/datasci_course_materials/master/assignment1/AFINN-111.txt'
    # serialized_data = urllib2.urlopen(url).readlines()
    # for line in serialized_data:
    #     x = line.split()
    #     if len(x) > 2:
    #         temp = x[0] + " " + x[1]
    #         word_dict[temp] = x[2]
    #     elif len(x) is 2:
    #         word_dict[x[0]] = x[1]
    #
    # for line in words:
    #     total = 0
    #     x = line.split()
    #     for i in range(0, len(x) - 1):
    #         if x[i] in word_dict:
    #             total += int(word_dict[x[i]])
    #     if total < 0:
    #         stuff.append((line, total))

    # send = []
    # for i in stuff:
    #     url = "https://language.googleapis.com/v1beta1/documents:analyzeEntities?fields=entities"
    #     d = {"document": {"content": i[0], "type": "PLAIN_TEXT"}}
    #     para = {"key": "AIzaSyD_p-5BoL5cMsRXUdHpy2C4bUD7KdpGk3k"}
    #     r = requests.post(url, params=para, json=d)
    #     data = json.loads(r.text)
    #     lis = data[u'entities']
    #     for dic in lis:
    #         if dic[u'type'] == "LOCATION":
    #             if u'metadata' in dic:
    #                 if u'wikipedia_url' in dic[u'metadata']:
    #                     send.append(dic[u'metadata'][u'wikipedia_url'].split('/')[-1])

    dingle = countInfo()
    out = {}
    values = []
    for k,v in dingle.iteritems():
        if v > 4:
            values.append(v)

    for k, v in dingle.iteritems():
        if v > 4:
            out[k] = (v-min(values))/float((max(values)-min(values)))

    return JsonResponse({"d": out})


def visa(request):

    from_c = request.GET['from']

    pwd = os.path.dirname(__file__)

    f = open( pwd +'/cleaner.p', 'rb')
    dct = pickle.load(f)
    f.close()
    ret = []
    if from_c in dct:
        ret = dct[from_c]
    return JsonResponse({'d': ret})


