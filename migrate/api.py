# -*- coding: utf-8 -*-
from django.http import JsonResponse
import urllib2
import json
from operator import itemgetter
import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def add(request):
    return get_data(request)

def countInfo():

    countries = ("Trump Tower (New York City)", "Iraq", "Iraq", "Greece",
           "Iraq", "Iraq", "Washington, D.C.", "Hawaii", "Iraq", "Hawaii", "China",
           "Iraq", "Iran", "Old Country Road", "Westbury, New York", "New York", "Egypt",
           "Washington, D.C.", "Iran", "Egypt", "Washington, D.C.", "Iran", "Israel",
            "Canada", "China", "Europe", "Europe", "China", "Iran", "Libya", "China",
            "China", "Israel", "White House", "Afghanistan", "Washington (state)",
           "Mexico", "Italy", "Italy", "Mexico", "China", "China",
           "Orlando, Florida", "Washington, D.C.", "Mexico", "Israel",
           "Palestinian National Authority", "China", "Libya", "Iraq War",
           "Afghanistan", "Afghanistan", "Iraq War", "Washington, D.C.", "Martha's Vineyard",
            "China",
            "China", "Iran", "Iraq", "Federal government of the United States",
           "Newtown, Connecticut", "Sandy Hook Elementary School shooting", "Connecticut", "Asia", "United Kingdom",
           "Trump National Doral Miami", "Scotland", "Scotland", "United Kingdom", "Scotland", "United Kingdom",
           "Scotland", "Scotland", "Scotland", "Egypt", "Iraq War", "Afghanistan",
           "Afghanistan", "China", "2012 Benghazi attack", "2012 Benghazi attack", "LaGuardia Airport",
           "Washington, D.C.", "2012 Benghazi attack", "New York", "New Jersey", "Detroit", "Philadelphia",
            "Trump Tower (New York City)", "China", "Benghazi", "China", "China",
            "New York", "Florida", "New York City", "New York", "Libya", "Benghazi",
           "Ohio", "China", "2012 Benghazi attack", "2012 Benghazi attack", "Fort Hood",
           "Trump World Tower", "Washington, D.C.",
           "Libya", "China", "Libya", "2012 Benghazi attack", "Libya", "Benghazi", "Libya",
           "Bain %26 Company", "Colorado", "United Kingdom", "Scotland", "Saudi Arabia", "China",
           "Libya", "Libya", "China", "Iran", "Libya", "Greece",
            "Mexico", "Libya", "Iraq", "Libya", "Washington, D.C.",
           "Scotland", "Fifth Avenue", "Iran", "Libya", "2012 Benghazi attack", "Canada", "China",
           "Egypt", "Middle East", "London", "Japan", "China",
           "Egypt", "Iran", "Libya", "Egypt", "Iraq", "Libya", "Libya", "Libya",
           "Afghanistan", "Chicago", "Chicago", "Germany", "France",
            "China", "China", "Tampa, Florida", "Russia", "Empire State Building",
           "Sinai Peninsula", "Camp David", "China", "California", "North Carolina",
           "Charlotte, North Carolina", "Afghanistan", "Iran", "Iran", "Chicago",
            "China", "China", "Tucson, Arizona",
           "China", "China", "Keystone Pipeline", "China", "Canada",
           "Saudi Arabia", "Colorado", "Aspen, Colorado", "Kenya",
           "Colorado", "Bill Clinton", "Sarasota County, Florida",
           "Cuba", "Iran", "New York City", "China", "Egypt", "China", "Syria", "Euro",
            "Miss Pennsylvania", "Greece", "Boston", "Saudi Arabia",
           "Euro", ".nyc", "China", "Philippines",
           "United Kingdom", "Georgetown University", "China", "France", "China",
           "Guantanamo Bay detention camp", "New York City", "China", "Scotland",
            "China", "China",
           "Palm Beach County, Florida", "Saudi Arabia", "China", "China", "China",
           "China", "Saudi Arabia", "Texas",
           "Afghanistan", "Afghanistan", "California", "China", "Israel", "Iran",
           "Iran", "China", "Iran", "Israel", "Afghanistan", "United Kingdom",
            "Afghanistan", "Iran",
            "Canada", "China", "Keystone Pipeline", "Pacific Ocean", "Israel", "West", "China",
            "Iran", "China", "China", "Florida",
           "Egypt", "China", "Keystone Pipeline", "Strait of Hormuz",
           "Keystone Pipeline", "Israel", "Iran", "Walt Disney World", "China",
            "Bain Capital", "Iran", "Tehran", "Trump Tower (New York City)", "Fifth Avenue",
            "Russia", "Iran", "Strait of Hormuz", "Iraq",
           "United States presidential election in Iowa, 2012", "Antarctica", "Scotland", "Israel", "Egypt",
            "South Africa", "Aberdeen", "New York", "Scotland", "South Africa", "Aberdeen", "Boston",
           "New York", "California", "New York", "United Kingdom", "Ontario", "Scotland", "Scotland",
           "Iran", "Iran", "Iran", "Syria", "Arizona", "Oklahoma", "Texas", "Afghanistan",
            "Oval Office", "Colombia", "New York",
           "Iran", "America (2009 film)", "Sahara", "Germany", "Scotland", "Benghazi", "Scotland",
           "Scotland", "Iraq", "China", "Iran", "Hindenburg disaster", "Saudi Arabia", "Syria",
           "New York (magazine)", "Canada", "Washington, D.C.",
           "Washington, D.C.", "Shopping mall", "Doral, Florida",
           "Miami", "Scotland", "North Carolina", "Nebraska", "Washington, D.C.", "Spain",
           "Washington, D.C.", "Iran", "Iran", "Africa", "Iran", "Washington Navy Yard", "Russia",
            "Washington Navy Yard", "North Korea", "Yongbyon Nuclear Scientific Research Center",
           "Syria", "New Jersey", "Syria", "Detroit", "Russia", "Germany", "World Trade Center site",
           "Russia", "Benghazi", "Syria", "Jacksonville Jaguars", "Syria", "Iraq", "Russia",
            "Syria", "Syria", "Syria", "Russia", "China", "Syria", "Syria", "Mediterranean Sea",
           "Syria", "Syria", "Iraq", "Syria", "Syria", "Syria", "Iran", "Syria", "Syria",
            "Syria", "Syria", "Syria", "Columbia, South Carolina", "South Carolina",
           "Syria", "Syria", "Syria", "Syria", "Syria",
           "Winston Churchill", "United Kingdom", "Syria", "Syria", "United Kingdom", "Syria", "Syria",
           "New York City", "Syria", "Russia", "Syria", "Syria", "Iraq", "Iran",
           "Wall Street", "New York", "Macy's", "New York City", "Russia", "America (2009 film)", "China",
           "New York City", "Chicago", "Egypt", "Texas", "Scotland", "Scotland",
           "Scotland", "Benghazi", "Iraq", "Benghazi", "Spring (hydrology)", "Russia",
           "Detroit", "New York City", "Aberdeen", "Scotland", "Europe", "Spain", "Scotland",
           "Detroit", "Iraq", "Detroit", "New York City", "Florida", "Brazil",
           "Moscow", "Egypt", "Mark Cuban", "Scotland", "Miss Pennsylvania", "New York City",
           "Louisiana", "South Africa", "Uganda", "Africa", "Egypt", "Arizona",
           "Africa", "Africa", "Cuba", "New York City", "China", "China",
            "China", "Miss USA", "Miss Utah",
           "2012 Benghazi attack", "Las Vegas", "Syria", "Syria", "China", "Miss USA",
           "Miss Alabama", "China", "Macy's", "New Jersey", "New York City", "Park", "Trump National Doral Miami",
           "Miami", "Aberdeen", "United Kingdom", "Chicago",
           "Scotland", "New York City", "2012 Benghazi attack", "Watergate scandal",
           "2012 Benghazi attack", "2012 Benghazi attack", "Chinese language", "JFK (film)", "Macy's", "Boston", "Park",
           "Park", "Upstate New York", "Scotland", "Iowa", "Afghanistan", "Macy's", "Iraq", "Aberdeen",
           "Scotland", "Pan Am Flight 103", "Park", "Park", "Parking lot", "Boston", "New York City", "Boston",
           "Boston", "Boston", "Boston", "Boston", "Boston", "Boston", "Boston", "Washington, D.C.",
           "Boston", "Boston", "Afghanistan", "Cuba", "Boston", "Boston", "New York City",
           "South Korea", "North Korea", "Indiana", "Scotland", "Seoul", "South Korea", "North Korea",
           "Iraq War", "Aurora, Colorado", "Colorado", "Spain",
           "Trump National Doral Miami", "Miami", "China", "Scotland", "China", "Middle East", "Scotland", "China",
           "China", "China", "Aberdeen", "Canada", "Scotland", "Cyprus", "Aberdeen",
           "China", "Cyprus", "New York City", "Board of directors", "Iraq", "Washington, D.C.", "Cuba", "Iraq",
           "Scotland", "Board of directors", "Western European Summer Time", "Temple Mount",
           "West Coast of the United States", "Afghanistan", "China", "Scotland", "Detroit", "China",
            "Washington, D.C.", "China", "Macy's", "Washington, D.C.",
           "Egypt", "Wharton School of the University of Pennsylvania",
           "New York City", "China", "Scotland", "Scotland",
           "Afghanistan", "Egypt", "Afghanistan", "Iraq",
           "Afghanistan", "New Jersey", "United Kingdom", "Israel",
           "Middle East", "World Trade Center (1973%E2%80%932001)",
           "World Trade Center (1973%E2%80%932001)", "World Trade Center (1973%E2%80%932001)", "America (2009 film)",
           "Afghanistan", "Washington, D.C.", "New York City",
           "Iraq", "Washington, D.C.", "Maryland", "Florida", "Guantanamo Bay detention camp",
            "Iraq", "Washington, D.C.", "Iraq", "Israel", "Iran", "New York City",
           "Saudi Arabia", "West Africa", "West Africa", "New York City", "West Africa",
            "West Africa", "Mexico",
            "LaGuardia Airport", "Mexico", "Africa",
            "West Africa", "Russell Simmons", "Iowa", "Africa", "West Africa",
           "General Motors Building (Manhattan)", "West Africa", "West Africa", "Iraq",
            "Iowa", "West Africa", "West Africa", "West Africa",
           "Liberia", "West Africa", "West Africa", "Mexico",
           "Israel", "West Africa", "West Africa", "White House", "Syria",
           "Washington, D.C.", "West Africa", "West Africa", "Hong Kong", "Central Park",
           "United Kingdom", "Oklahoma", "Mexico", "Briarcliff Manor, New York",
            "Syria", "Iraq", "Syria", "Africa", "Mexico", "Africa", "Atlantic City, New Jersey",
            "Atlantic City, New Jersey", "America (2009 film)", "Saudi Arabia",
           "Atlantic City, New Jersey", "Mexico", "Miami metropolitan area", "Vietnam War",
            "Africa", "Iraq War", "West Africa",
           "Briarcliff Manor, New York", "Westchester County, New York", "Iraq", "Iraq", "Africa",
            "Iraq", "Baghdad", "Scotland", "Scotland",
           "Atlantic City, New Jersey", "West Virginia", "Washington, D.C.", "Scotland",
           "New York City",
           "Atlantic City, New Jersey", "Atlantic City, New Jersey",
           "Mexico", "Asia", "Europe", "Mexico", "Mexico", "Mexico", "Mexico",
            "Chicago", "Scotland", "Iraq", "Iraq", "Syria", "Iraq",
           "Iran", "Illinois", "Benghazi", "Mexico", "Afghanistan", "Iraq", "New York", "Mexico",
            "Sint Maarten", "Sint Maarten", "2012 Benghazi attack", "Iraq",
            "Chicago", "Syria", "Iraq", "Pinehurst Resort", "Pinehurst Resort", "Pinehurst Resort",
           "Iraq", "Alternating current", "Iraq", "Iraq", "Iraq", "White House",
           "Iraq", "Iraq", "Pakistan", "Afghanistan", "Afghanistan", "Iraq War",
            "Israel", "Middle East",
            "Benghazi",
            "Russia", "Manhattan", "North Korea", "Miss Pennsylvania",
            "Italy", "Pound sterling", "Japan", "South Korea",
            "New York City", "Iraq", "Iran", "China", "Iraq", "Washington, D.C.", "Colorado",
           "Fort Knox", "Moscow", "Brooklyn", "Russia", "Scotland", "Ireland",
           "Atlantic Ocean", "Republic of Ireland", "Lake Tahoe", "Southern California", "Russia",
           "Vancouver", "United Kingdom", "Manhattan", "Netherlands", "Russia", "China", "Russia", "California",
           "New York", "Scotland", "Aberdeen", "White House", "Russia", "Kanye West", "Russia",
            "Ukraine", "Columbia University", "New York", "New York City",
           "New York City", "Iraq", "Iran", "America (2009 film)", "Florida", "China",
           "New York", "Florida", "Miami", "Florida", "South Africa", "Pan Am Flight 103", "New Hampshire",
           "Buffalo, New York", "New York", "Republic of Ireland", "Scotland", "Russia", "Trump National Doral Miami",
            "Italy", "Atlanta", "Texas", "Florida", "World Trade Center (1973%E2%80%932001)",
           "New York", "New York", "Scotland", "New York", "New York City", "Scotland", "Iraq", "Iraq", "Iowa", "Iowa",
           "Council Bluffs, Iowa", "Virginia", "2012 Benghazi attack", "2012 Benghazi attack",
           "Europe", "Veterans Health Administration", "Afghanistan",
           "Lindsey Graham", "United States presidential election in Iowa, 2012", "Iraq", "Monmouth University", "Iowa",
           "Pennsylvania", "United Kingdom", "Israel", "Philadelphia", "Iowa",
            "Iowa", "New York City",
            "San Bernardino, California", "Manassas, Virginia", "Virginia",
           "California", "California", "Ohio", "Columbus, Ohio", "Ohio", "Louisiana",
            "New York City", "Ohio", "West Virginia", "New York City", "Ohio", "Ohio",
           "Paris", "Paris", "Baltimore", "Paris", "Paris", "China", "Illinois", "Carson, California",
            "Hispanic and Latino Americans", "New York City", "Norfolk", "China", "Russia",
            "Mexico", "Iowa", "Washington, D.C.",
           "Carson, California", "Mexico", "America (2009 film)", "Iraq",
           "Ur (cuneiform)", "Middle East", "Iraq", "New Hampshire", "World Trade Center (1973%E2%80%932001)",
           "Maryland", "Iraq", "Russia", "China", "L.V. (singer)",
           "St. Jude Children's Research Hospital", "Washington, D.C.", "Roseburg, Oregon", "Oregon",
            "Florida", "Iraq War", "New York",
           "America (2009 film)", "White House", "Washington, D.C.", "United States Capitol",
           "Washington, D.C.", "Washington, D.C.", "Iran", "United States Capitol", "Dallas", "Washington, D.C.",
           "Iran", "Washington, D.C.", "United States Capitol", "New York City",
           "Denali Borough, Alaska", "Ohio", "Wisconsin", "New York", "Asia", "White House", "Iraq",
            "Atlanta", "Public relations", "Scotland", "Boston", "Washington, D.C.",
           "Wisconsin", "Washington, D.C.", "Wisconsin", "Iowa", "Arizona",
           "New York (magazine)", "Personal computer", "Phoenix, Arizona",
           "United States Naval Academy", "Iran", "Las Vegas", "New York City", "Iran",
            "Michigan", "Mexico", "Mexico",
            "Mexico", "Mexico", "Convention center", "Phoenix, Arizona",
           "Phoenix, Arizona", "Phoenix, Arizona", "Mexico",
           "San Francisco", "San Francisco", "California", "Mexico", "Mexico",
            "Chicago", "Hispanic and Latino Americans", "New York", "Mexico",
            "Mexico", "Israel", "Mexico", "Miss USA",
           "Hollywood", "America (2009 film)", "Boston", "Rhode Island", "Mexico",
            "Mexico", "Mexico",
            "Mexico", "Iraq", "Iraq",
           "South Carolina", "Iraq", "Pennsylvania", "Coralville, Iowa",
            "New York City", "Ohio", "Japan", "China",
            "Iraq", "Iraq War", "Iraq", "Philadelphia", "Iraq War",
            "Africa", "Mississippi", "Zimbabwe", "Aberdeen",
            "Baltimore", "Baltimore", "Baltimore", "Baltimore",
           "Baltimore", "China", "Florida", "Japan", "Nashua, New Hampshire", "President",
           "New Hampshire", "Washington, D.C.", "Iran", "Mexico", "Iran", "Iran",
           "Iran", "Iran", "Iran",
           "Trump National Doral Miami", "Mexico", "Mexico", "Iran",
           "Doonbeg (Killard)", "Kenya", "Kenya", "Medford, Oregon", "Kenya",
            "United States presidential election in Iowa, 2012", "New York City", "Scotland",
           "South Carolina", "Atlantic City, New Jersey", "France", "Paris", "Guantanamo Bay detention camp", "Paris",
           "Paris", "Kenya", "Kenya", "Kenya", "Iran", "Israel", "Germany", "Turkey", "Germany",
           "Switzerland", "China", "Russia", "White House", "Russia", "Pennsylvania", "Wisconsin", "Indiana", "Mexico",
           "Southeastern United States", "Somalia", "Virginia", "New Hampshire", "California",
           "Kentucky", "Mexico", "Australia", "New Zealand", "Russia", "China", "Saudi Arabia", "Japan",
           "United Kingdom", "Utah", "Florida", "Cuba", "Venezuela", "Reno, Nevada", "Nevada",
            "North Carolina", "Iowa", "Bill Clinton", "Arizona", "New Hampshire",
           "Dallas", "Mosul", "Maine", "Mosul", "Benghazi",
           "Second Amendment to the United States Constitution", "Wisconsin", "Hillary Clinton",
           "New Hampshire", "North Carolina", "Cuba", "State of Palestine", "Israel",
           "Indiana", "2012 Benghazi attack", "Iraq", "Mosul", "Wall Street",
           "New Jersey", "Syria", "Libya", "Iraq", "Russia", "Benghazi", "Asia", "Washington, D.C.",
           "Washington (state)", "Middle East", "Ohio", "Charlotte, North Carolina", "Charlotte, North Carolina",
           "High Point, North Carolina", "North Carolina", "New York", "New Jersey", "Minnesota",
           "Iraq War", "Bill Clinton", "China", "Syria", "Mexico", "Mexico", "Mexico", "Washington, D.C.", "Chicago",
           "Italy", "Myanmar", "Texas",
            "Crimea",

            "Iran", "Iran",
           "Mechanicsburg, Pennsylvania", "Pennsylvania", "Iraq", "Johnstown, Pennsylvania", "Pennsylvania",
            "Syria", "France",
            "Florida", "Pennsylvania", "Pennsylvania", "Philadelphia",
            "Baton Rouge, Louisiana", "Cleveland", "Nice", "France", "Nice", "France",
           "France", "Israel", "Miami", "Dallas", "Atlantic City, New Jersey", "Airport",
           "Convention center", "Baghdad", "Bangladesh", "Cleveland", "Israel", "State of Palestine",
            "Israel", "State of Palestine",
           "Bill Clinton", "U.S. Immigration and Customs Enforcement", "United Kingdom", "West Virginia",
           "Orlando, Florida", "Dallas", "Texas", "Saudi Arabia", "New Hampshire", "Orlando, Florida",
           "Orlando, Florida", "Los Angeles", "Florida", "Orlando, Florida", "Elkhart, Indiana", "Benghazi", "Texas",
           "Royce da 5'9%22", "Pearl Harbor", "Japan", "Syria", "New Mexico", "Mexico",
            "Syria", "Iraq", "Libya", "China",
            "Massachusetts", "Las Vegas Strip",
            "Connecticut", "New York City", "Colorado", "Colorado", "New York City", "New York City",
           "Wisconsin", "Wisconsin", "Wisconsin", "Guantanamo Bay detention camp",
            "Pakistan", "Paris", "Brussels", "Europe", "Syria",
           "Europe", "Brussels", "Cleveland", "Brussels", "Washington, D.C.", "Cuba", "Brussels",
           "Cuba", "Brussels", "Arizona", "Florida", "Ohio", "Mexico", "Ohio", "Mexico", "Ohio",
           "Ohio", "Chicago", "Florida", "Florida", "Ohio", "Mexico", "Florida",
           "Kentucky", "Virginia", "Florida", "South Carolina", "Washington, D.C.", "Florida", "Florida",
           "Washington, D.C.", "Florida", "Washington, D.C.", "Texas", "Nevada",
           "Iowa", "Tennessee", "West Hollywood, California", "South Carolina", "Holy See", "Nevada",
           "South Carolina", "North Augusta, South Carolina", "Canada", "South Carolina", "Iraq War",
           "New Hampshire", "Washington, D.C.", "Iowa", "New Hampshire", "Iowa", "Canada",
           "White House", "Canada", "Illinois", "Iowa", "Oklahoma", "Ames, Iowa",
           "Iowa", "Wall Street", "New York City", "New York City", "Iowa", "Cosby",
           "Paris", "Germany", "Canada", "New Hampshire", "Germany", "Morocco", "Israel",
            "Florida", "Syria", "Ukraine", "Crimea", "Russia", "Paris", "Louvre",
            "France", "Australia", "Mexico", "Chicago", "Oval Office", "Guantanamo Bay detention camp",
            "Europe", "Middle East", "Nazi Germany", "Europe", "Chicago", "Russia",
           "Great Wall of China", "Mexico", "Hollywood", "Russia", "Australia",
            "Mexico", "Mexico", "California", "Russia",
            "Boston", "Russia")

    country = {}
    for i in countries:
        if i not in country:
            country[i] = 1
        else:
            country[i] += 1
    return country

def get_data(request):

    words = []
    for i in range(9, 18):
        if i is 9:
            url = 'http://www.trumptwitterarchive.com/data/realdonaldtrump/200{0}.json'.format(i)
        else:
            url = 'http://www.trumptwitterarchive.com/data/realdonaldtrump/20{0}.json'.format(i)

        serialized_data = urllib2.urlopen(url).read()

        d = json.loads(serialized_data)

        for x in range(0, len(d)-1):
            str1 = d[x]['text']
            str2 = str1.replace("\n", "")
            words.append(str2)

    word_dict = {}
    stuff = []
    url = 'https://raw.githubusercontent.com/uwescience/datasci_course_materials/master/assignment1/AFINN-111.txt'
    serialized_data = urllib2.urlopen(url).readlines()
    for line in serialized_data:
        x = line.split()
        if len(x) > 2:
            temp = x[0] + " " + x[1]
            word_dict[temp] = x[2]
        elif len(x) is 2:
            word_dict[x[0]] = x[1]

    for line in words:
        total = 0
        x = line.split()
        for i in range(0, len(x) - 1):
            if x[i] in word_dict:
                total += int(word_dict[x[i]])
        if total < 0:
            stuff.append((line, total))

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




