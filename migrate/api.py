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

    countries = ["Trump_Tower_(New_York_City)", "United_States", "United_States", "Iraq", "United_States", "Iraq", "Greece",
           "Iraq", "Iraq", "Washington,_D.C.", "Hawaii", "Iraq", "United_States", "Hawaii", "United_States", "China",
           "Iraq", "Iran", "Old_Country_Road", "Westbury,_New_York", "New_York", "United_States", "Egypt",
           "Washington,_D.C.", "United_States", "Iran", "Egypt", "Washington,_D.C.", "United_States", "Iran", "Israel",
           "United_States", "Canada", "China", "Europe", "United_States", "Europe", "China", "Iran", "Libya", "China",
           "United_States", "China", "Israel", "United_States", "White_House", "Afghanistan", "Washington_(state)",
           "Mexico", "Italy", "Italy", "Mexico", "United_States", "China", "China", "United_States", "United_States",
           "Orlando,_Florida", "United_States", "Washington,_D.C.", "United_States", "Mexico", "Israel",
           "Palestinian_National_Authority", "United_States", "United_States", "China", "Libya", "Iraq_War",
           "Afghanistan", "United_States", "Afghanistan", "Iraq_War", "Washington,_D.C.", "Martha's_Vineyard",
           "United_States", "United_States", "China", "United_States", "United_States", "United_States",
           "United_States", "China", "Iran", "Iraq", "United_States", "Federal_government_of_the_United_States",
           "Newtown,_Connecticut", "Sandy_Hook_Elementary_School_shooting", "Connecticut", "Asia", "United_Kingdom",
           "Trump_National_Doral_Miami", "Scotland", "Scotland", "United_Kingdom", "Scotland", "United_Kingdom",
           "Scotland", "Scotland", "United_States", "United_States", "Scotland", "Egypt", "Iraq_War", "Afghanistan",
           "Afghanistan", "China", "2012_Benghazi_attack", "2012_Benghazi_attack", "LaGuardia_Airport",
           "Washington,_D.C.", "2012_Benghazi_attack", "New_York", "New_Jersey", "Detroit", "Philadelphia",
           "United_States", "Trump_Tower_(New_York_City)", "China", "United_States", "Benghazi", "China", "China",
           "United_States", "New_York", "Florida", "New_York_City", "New_York", "Libya", "United_States", "Benghazi",
           "Ohio", "China", "2012_Benghazi_attack", "United_States", "2012_Benghazi_attack", "Fort_Hood",
           "Trump_World_Tower", "Washington,_D.C.", "United_States", "United_States", "United_States", "United_States",
           "Libya", "China", "Libya", "2012_Benghazi_attack", "Libya", "Benghazi", "United_States", "Libya",
           "Bain_%26_Company", "Colorado", "United_States", "United_Kingdom", "Scotland", "Saudi_Arabia", "China",
           "Libya", "Libya", "United_States", "United_States", "United_States", "China", "Iran", "Libya", "Greece",
           "United_States", "Mexico", "United_States", "Libya", "United_States", "Iraq", "Libya", "Washington,_D.C.",
           "Scotland", "Fifth_Avenue", "Iran", "Libya", "United_States", "2012_Benghazi_attack", "Canada", "China",
           "Egypt", "United_States", "Middle_East", "London", "Japan", "China", "United_States", "United_States",
           "Egypt", "United_States", "Iran", "Libya", "Egypt", "Iraq", "Libya", "Libya", "Libya", "United_States",
           "Afghanistan", "Chicago", "Chicago", "Germany", "United_States", "United_States", "United_States", "France",
           "United_States", "China", "China", "Tampa,_Florida", "United_States", "Russia", "Empire_State_Building",
           "Sinai_Peninsula", "Camp_David", "China", "United_States", "California", "North_Carolina",
           "Charlotte,_North_Carolina", "United_States", "Afghanistan", "United_States", "Iran", "Iran", "Chicago",
           "United_States", "China", "United_States", "China", "Tucson,_Arizona", "United_States", "United_States",
           "China", "China", "United_States", "United_States", "Keystone_Pipeline", "China", "United_States", "Canada",
           "Saudi_Arabia", "United_States", "United_States", "Colorado", "United_States", "Aspen,_Colorado", "Kenya",
           "Colorado", "United_States", "United_States", "Bill_Clinton", "United_States", "Sarasota_County,_Florida",
           "Cuba", "Iran", "New_York_City", "China", "Egypt", "United_States", "China", "Syria", "Euro",
           "United_States", "Miss_Pennsylvania", "Greece", "United_States", "Boston", "United_States", "Saudi_Arabia",
           "Euro", "United_States", "United_States", "United_States", ".nyc", "China", "Philippines", "United_States",
           "United_Kingdom", "United_States", "Georgetown_University", "China", "France", "United_States", "China",
           "Guantanamo_Bay_detention_camp", "New_York_City", "China", "United_States", "United_States", "Scotland",
           "United_States", "United_States", "United_States", "China", "United_States", "China", "United_States",
           "Palm_Beach_County,_Florida", "United_States", "Saudi_Arabia", "China", "China", "United_States", "China",
           "China", "United_States", "Saudi_Arabia", "United_States", "United_States", "United_States", "Texas",
           "Afghanistan", "United_States", "Afghanistan", "United_States", "California", "China", "Israel", "Iran",
           "Iran", "China", "United_States", "Iran", "Israel", "Afghanistan", "United_States", "United_Kingdom",
           "United_States", "Afghanistan", "Iran", "United_States", "United_States", "United_States", "United_States",
           "United_States", "Canada", "China", "Keystone_Pipeline", "Pacific_Ocean", "Israel", "West", "China",
           "United_States", "United_States", "United_States", "Iran", "China", "United_States", "China", "Florida",
           "Egypt", "China", "United_States", "United_States", "Keystone_Pipeline", "Strait_of_Hormuz",
           "Keystone_Pipeline", "United_States", "United_States", "Israel", "Iran", "Walt_Disney_World", "China",
           "United_States", "Bain_Capital", "Iran", "Tehran", "Trump_Tower_(New_York_City)", "Fifth_Avenue",
           "United_States", "Russia", "Iran", "United_States", "United_States", "Strait_of_Hormuz", "Iraq",
           "United_States_presidential_election_in_Iowa,_2012", "Antarctica", "Scotland", "Israel", "Egypt",
           "United_States", "South_Africa", "Aberdeen", "New_York", "Scotland", "South_Africa", "Aberdeen", "Boston",
           "New_York", "California", "United_States", "New_York", "United_Kingdom", "Ontario", "Scotland", "Scotland",
           "Iran", "Iran", "Iran", "Syria", "Arizona", "Oklahoma", "Texas", "Afghanistan", "United_States",
           "United_States", "United_States", "Oval_Office", "United_States", "Colombia", "United_States", "New_York",
           "Iran", "America_(2009_film)", "Sahara", "Germany", "Scotland", "United_States", "Benghazi", "Scotland",
           "Scotland", "Iraq", "China", "Iran", "Hindenburg_disaster", "Saudi_Arabia", "Syria", "United_States",
           "New_York_(magazine)", "United_States", "United_States", "Canada", "Washington,_D.C.", "United_States",
           "Washington,_D.C.", "United_States", "United_States", "Shopping_mall", "United_States", "Doral,_Florida",
           "Miami", "Scotland", "United_States", "North_Carolina", "Nebraska", "Washington,_D.C.", "Spain",
           "Washington,_D.C.", "United_States", "Iran", "Iran", "Africa", "Iran", "Washington_Navy_Yard", "Russia",
           "United_States", "Washington_Navy_Yard", "North_Korea", "Yongbyon_Nuclear_Scientific_Research_Center",
           "Syria", "New_Jersey", "Syria", "Detroit", "Russia", "United_States", "Germany", "World_Trade_Center_site",
           "Russia", "United_States", "Benghazi", "Syria", "Jacksonville_Jaguars", "Syria", "Iraq", "Russia",
           "United_States", "Syria", "Syria", "Syria", "Russia", "China", "Syria", "Syria", "Mediterranean_Sea",
           "Syria", "Syria", "Iraq", "Syria", "Syria", "Syria", "Iran", "Syria", "United_States", "Syria",
           "United_States", "Syria", "Syria", "Syria", "Columbia,_South_Carolina", "South_Carolina", "United_States",
           "Syria", "United_States", "Syria", "United_States", "Syria", "Syria", "United_States", "Syria",
           "Winston_Churchill", "United_Kingdom", "Syria", "Syria", "United_Kingdom", "Syria", "United_States", "Syria",
           "New_York_City", "Syria", "Russia", "Syria", "Syria", "United_States", "United_States", "Iraq", "Iran",
           "Wall_Street", "New_York", "Macy's", "New_York_City", "Russia", "America_(2009_film)", "China",
           "New_York_City", "Chicago", "United_States", "Egypt", "United_States", "Texas", "Scotland", "Scotland",
           "Scotland", "Benghazi", "Iraq", "Benghazi", "Spring_(hydrology)", "United_States", "United_States", "Russia",
           "Detroit", "New_York_City", "United_States", "Aberdeen", "Scotland", "Europe", "Spain", "Scotland",
           "Detroit", "United_States", "Iraq", "Detroit", "United_States", "New_York_City", "Florida", "Brazil",
           "Moscow", "United_States", "Egypt", "Mark_Cuban", "Scotland", "Miss_Pennsylvania", "New_York_City",
           "Louisiana", "South_Africa", "Uganda", "Africa", "United_States", "Egypt", "United_States", "Arizona",
           "Africa", "Africa", "Cuba", "New_York_City", "China", "United_States", "United_States", "China",
           "United_States", "United_States", "United_States", "China", "United_States", "Miss_USA", "Miss_Utah",
           "2012_Benghazi_attack", "Las_Vegas", "Syria", "Syria", "United_States", "United_States", "China", "Miss_USA",
           "Miss_Alabama", "China", "Macy's", "New_Jersey", "New_York_City", "Park", "Trump_National_Doral_Miami",
           "Miami", "Aberdeen", "United_States", "United_Kingdom", "United_States", "Chicago", "United_States",
           "Scotland", "United_States", "New_York_City", "2012_Benghazi_attack", "Watergate_scandal",
           "2012_Benghazi_attack", "2012_Benghazi_attack", "Chinese_language", "JFK_(film)", "Macy's", "Boston", "Park",
           "Park", "Upstate_New_York", "Scotland", "Iowa", "Afghanistan", "United_States", "Macy's", "Iraq", "Aberdeen",
           "Scotland", "Pan_Am_Flight_103", "Park", "Park", "Parking_lot", "Boston", "New_York_City", "Boston",
           "Boston", "Boston", "Boston", "Boston", "Boston", "Boston", "Boston", "Washington,_D.C.", "United_States",
           "Boston", "Boston", "Afghanistan", "Cuba", "United_States", "Boston", "Boston", "New_York_City",
           "South_Korea", "United_States", "North_Korea", "Indiana", "Scotland", "Seoul", "South_Korea", "North_Korea",
           "Iraq_War", "United_States", "United_States", "Aurora,_Colorado", "Colorado", "Spain",
           "Trump_National_Doral_Miami", "Miami", "China", "Scotland", "China", "Middle_East", "Scotland", "China",
           "China", "China", "United_States", "Aberdeen", "Canada", "Scotland", "Cyprus", "Aberdeen", "United_States",
           "China", "Cyprus", "New_York_City", "Board_of_directors", "Iraq", "Washington,_D.C.", "Cuba", "Iraq",
           "Scotland", "Board_of_directors", "Western_European_Summer_Time", "Temple_Mount",
           "West_Coast_of_the_United_States", "Afghanistan", "United_States", "China", "Scotland", "Detroit", "China",
           "United_States", "Washington,_D.C.", "China", "Macy's", "United_States", "United_States", "Washington,_D.C.",
           "Egypt", "United_States", "Wharton_School_of_the_University_of_Pennsylvania", "United_States",
           "New_York_City", "China", "United_States", "Scotland", "Scotland", "United_States", "United_States",
           "Afghanistan", "United_States", "Egypt", "Afghanistan", "United_States", "United_States", "Iraq",
           "Afghanistan", "New_Jersey", "United_States", "United_Kingdom", "United_States", "United_States", "Israel",
           "Middle_East", "United_States", "United_States", "United_States", "World_Trade_Center_(1973%E2%80%932001)",
           "World_Trade_Center_(1973%E2%80%932001)", "World_Trade_Center_(1973%E2%80%932001)", "America_(2009_film)",
           "Afghanistan", "Washington,_D.C.", "United_States", "United_States", "United_States", "New_York_City",
           "Iraq", "United_States", "Washington,_D.C.", "Maryland", "Florida", "Guantanamo_Bay_detention_camp",
           "United_States", "Iraq", "Washington,_D.C.", "Iraq", "Israel", "Iran", "United_States", "New_York_City",
           "Saudi_Arabia", "West_Africa", "West_Africa", "New_York_City", "United_States", "West_Africa",
           "United_States", "United_States", "West_Africa", "United_States", "United_States", "United_States", "Mexico",
           "United_States", "LaGuardia_Airport", "Mexico", "United_States", "United_States", "United_States", "Africa",
           "United_States", "West_Africa", "Russell_Simmons", "Iowa", "Africa", "West_Africa", "United_States",
           "General_Motors_Building_(Manhattan)", "West_Africa", "United_States", "West_Africa", "Iraq",
           "United_States", "Iowa", "West_Africa", "United_States", "United_States", "West_Africa", "West_Africa",
           "Liberia", "United_States", "West_Africa", "United_States", "West_Africa", "Mexico", "United_States",
           "Israel", "West_Africa", "West_Africa", "United_States", "United_States", "White_House", "Syria",
           "Washington,_D.C.", "West_Africa", "West_Africa", "United_States", "Hong_Kong", "Central_Park",
           "United_Kingdom", "Oklahoma", "United_States", "Mexico", "United_States", "Briarcliff_Manor,_New_York",
           "United_States", "Syria", "Iraq", "Syria", "Africa", "Mexico", "Africa", "Atlantic_City,_New_Jersey",
           "United_States", "Atlantic_City,_New_Jersey", "America_(2009_film)", "United_States", "Saudi_Arabia",
           "Atlantic_City,_New_Jersey", "Mexico", "Miami_metropolitan_area", "United_States", "Vietnam_War",
           "United_States", "United_States", "Africa", "United_States", "Iraq_War", "United_States", "West_Africa",
           "Briarcliff_Manor,_New_York", "Westchester_County,_New_York", "Iraq", "United_States", "Iraq", "Africa",
           "United_States", "Iraq", "United_States", "Baghdad", "United_States", "Scotland", "Scotland",
           "Atlantic_City,_New_Jersey", "West_Virginia", "Washington,_D.C.", "Scotland", "United_States",
           "New_York_City", "United_States", "United_States", "United_States", "United_States",
           "Atlantic_City,_New_Jersey", "United_States", "United_States", "Atlantic_City,_New_Jersey", "United_States",
           "Mexico", "Asia", "Europe", "United_States", "Mexico", "Mexico", "United_States", "Mexico", "Mexico",
           "United_States", "United_States", "Chicago", "Scotland", "Iraq", "Iraq", "United_States", "Syria", "Iraq",
           "Iran", "Illinois", "Benghazi", "Mexico", "Afghanistan", "Iraq", "New_York", "United_States", "Mexico",
           "United_States", "Sint_Maarten", "Sint_Maarten", "United_States", "2012_Benghazi_attack", "Iraq",
           "United_States", "Chicago", "Syria", "Iraq", "Pinehurst_Resort", "Pinehurst_Resort", "Pinehurst_Resort",
           "Iraq", "United_States", "Alternating_current", "Iraq", "Iraq", "Iraq", "United_States", "White_House",
           "Iraq", "United_States", "Iraq", "Pakistan", "Afghanistan", "United_States", "Afghanistan", "Iraq_War",
           "United_States", "United_States", "United_States", "Israel", "Middle_East", "United_States", "United_States",
           "United_States", "United_States", "United_States", "Benghazi", "United_States", "United_States",
           "United_States", "Russia", "United_States", "United_States", "Manhattan", "North_Korea", "Miss_Pennsylvania",
           "United_States", "Italy", "United_States", "Pound_sterling", "United_States", "Japan", "South_Korea",
           "United_States", "New_York_City", "Iraq", "Iran", "China", "Iraq", "Washington,_D.C.", "Colorado",
           "Fort_Knox", "Moscow", "Brooklyn", "Russia", "United_States", "United_States", "Scotland", "Ireland",
           "Atlantic_Ocean", "Republic_of_Ireland", "Lake_Tahoe", "United_States", "Southern_California", "Russia",
           "Vancouver", "United_Kingdom", "Manhattan", "Netherlands", "Russia", "China", "Russia", "California",
           "New_York", "Scotland", "Aberdeen", "White_House", "Russia", "Kanye_West", "United_States", "Russia",
           "United_States", "Ukraine", "United_States", "Columbia_University", "New_York", "New_York_City",
           "New_York_City", "United_States", "Iraq", "Iran", "United_States", "America_(2009_film)", "Florida", "China",
           "New_York", "Florida", "Miami", "Florida", "South_Africa", "Pan_Am_Flight_103", "New_Hampshire",
           "Buffalo,_New_York", "New_York", "Republic_of_Ireland", "Scotland", "Russia", "Trump_National_Doral_Miami",
           "United_States", "Italy", "Atlanta", "Texas", "Florida", "World_Trade_Center_(1973%E2%80%932001)",
           "New_York", "New_York", "Scotland", "New_York", "New_York_City", "Scotland", "Iraq", "Iraq", "Iowa", "Iowa",
           "Council_Bluffs,_Iowa", "United_States", "Virginia", "2012_Benghazi_attack", "2012_Benghazi_attack",
           "Europe", "United_States", "Veterans_Health_Administration", "United_States", "United_States", "Afghanistan",
           "Lindsey_Graham", "United_States_presidential_election_in_Iowa,_2012", "Iraq", "Monmouth_University", "Iowa",
           "Pennsylvania", "United_Kingdom", "Israel", "United_States", "Philadelphia", "Iowa", "United_States",
           "United_States", "United_States", "United_States", "Iowa", "United_States", "New_York_City", "United_States",
           "United_States", "United_States", "San_Bernardino,_California", "Manassas,_Virginia", "Virginia",
           "California", "California", "United_States", "United_States", "Ohio", "Columbus,_Ohio", "Ohio", "Louisiana",
           "United_States", "New_York_City", "Ohio", "West_Virginia", "United_States", "New_York_City", "Ohio", "Ohio",
           "Paris", "Paris", "Baltimore", "Paris", "Paris", "China", "Illinois", "United_States", "Carson,_California",
           "United_States", "Hispanic_and_Latino_Americans", "New_York_City", "Norfolk", "China", "Russia",
           "United_States", "Mexico", "United_States", "Iowa", "Washington,_D.C.", "United_States",
           "Carson,_California", "United_States", "Mexico", "America_(2009_film)", "United_States", "Iraq",
           "Ur_(cuneiform)", "Middle_East", "Iraq", "New_Hampshire", "World_Trade_Center_(1973%E2%80%932001)",
           "Maryland", "Iraq", "Russia", "China", "United_States", "L.V._(singer)",
           "St._Jude_Children's_Research_Hospital", "Washington,_D.C.", "United_States", "Roseburg,_Oregon", "Oregon",
           "United_States", "United_States", "United_States", "Florida", "Iraq_War", "New_York", "United_States",
           "America_(2009_film)", "White_House", "Washington,_D.C.", "United_States_Capitol", "United_States",
           "Washington,_D.C.", "Washington,_D.C.", "Iran", "United_States_Capitol", "Dallas", "Washington,_D.C.",
           "Iran", "Washington,_D.C.", "United_States_Capitol", "United_States", "New_York_City", "United_States",
           "Denali_Borough,_Alaska", "Ohio", "Wisconsin", "New_York", "United_States", "Asia", "White_House", "Iraq",
           "United_States", "Atlanta", "Public_relations", "Scotland", "United_States", "Boston", "Washington,_D.C.",
           "Wisconsin", "Washington,_D.C.", "Wisconsin", "Iowa", "Arizona", "United_States", "United_States",
           "New_York_(magazine)", "United_States", "Personal_computer", "Phoenix,_Arizona", "United_States",
           "United_States_Naval_Academy", "Iran", "Las_Vegas", "New_York_City", "United_States", "Iran",
           "United_States", "United_States", "United_States", "United_States", "Michigan", "Mexico", "Mexico",
           "United_States", "Mexico", "Mexico", "United_States", "Convention_center", "Phoenix,_Arizona",
           "Phoenix,_Arizona", "United_States", "Phoenix,_Arizona", "United_States", "United_States", "Mexico",
           "San_Francisco", "United_States", "San_Francisco", "California", "United_States", "Mexico", "Mexico",
           "United_States", "Chicago", "Hispanic_and_Latino_Americans", "United_States", "New_York", "Mexico",
           "United_States", "Mexico", "United_States", "Israel", "United_States", "Mexico", "United_States", "Miss_USA",
           "Hollywood", "America_(2009_film)", "Boston", "Rhode_Island", "United_States", "Mexico", "United_States",
           "United_States", "Mexico", "Mexico", "United_States", "United_States", "United_States", "United_States",
           "United_States", "United_States", "Mexico", "United_States", "Iraq", "United_States", "Iraq",
           "South_Carolina", "United_States", "Iraq", "United_States", "Pennsylvania", "Coralville,_Iowa",
           "United_States", "United_States", "New_York_City", "United_States", "Ohio", "Japan", "China",
           "United_States", "United_States", "Iraq", "Iraq_War", "Iraq", "United_States", "Philadelphia", "Iraq_War",
           "United_States", "Africa", "Mississippi", "Zimbabwe", "United_States", "United_States", "Aberdeen",
           "United_States", "United_States", "Baltimore", "Baltimore", "Baltimore", "United_States", "Baltimore",
           "Baltimore", "China", "Florida", "United_States", "Japan", "Nashua,_New_Hampshire", "President",
           "New_Hampshire", "Washington,_D.C.", "Iran", "United_States", "Mexico", "Iran", "United_States", "Iran",
           "Iran", "United_States", "Iran", "United_States", "Iran", "United_States", "United_States", "United_States",
           "Trump_National_Doral_Miami", "Mexico", "United_States", "Mexico", "United_States", "Iran",
           "Doonbeg_(Killard)", "United_States", "United_States", "Kenya", "Kenya", "Medford,_Oregon", "Kenya",
           "United_States", "United_States_presidential_election_in_Iowa,_2012", "New_York_City", "Scotland",
           "South_Carolina", "Atlantic_City,_New_Jersey", "France", "Paris", "Guantanamo_Bay_detention_camp", "Paris",
           "Paris", "Kenya", "Kenya", "Kenya", "Iran", "Israel", "United_States", "Germany", "Turkey", "Germany",
           "Switzerland", "China", "Russia", "White_House", "Russia", "Pennsylvania", "Wisconsin", "Indiana", "Mexico",
           "Southeastern_United_States", "Somalia", "United_States", "Virginia", "New_Hampshire", "California",
           "Kentucky", "Mexico", "Australia", "New_Zealand", "Russia", "China", "Saudi_Arabia", "Japan",
           "United_Kingdom", "Utah", "Florida", "Cuba", "Venezuela", "United_States", "Reno,_Nevada", "Nevada",
           "United_States", "United_States", "North_Carolina", "Iowa", "Bill_Clinton", "Arizona", "New_Hampshire",
           "Dallas", "Mosul", "United_States", "United_States", "Maine", "Mosul", "Benghazi", "United_States",
           "Second_Amendment_to_the_United_States_Constitution", "United_States", "Wisconsin", "Hillary_Clinton",
           "New_Hampshire", "North_Carolina", "Cuba", "United_States", "State_of_Palestine", "Israel", "United_States",
           "Indiana", "2012_Benghazi_attack", "Iraq", "United_States", "Mosul", "Wall_Street", "United_States",
           "New_Jersey", "Syria", "Libya", "Iraq", "Russia", "Benghazi", "Asia", "Washington,_D.C.",
           "Washington_(state)", "Middle_East", "Ohio", "Charlotte,_North_Carolina", "Charlotte,_North_Carolina",
           "High_Point,_North_Carolina", "North_Carolina", "New_York", "New_Jersey", "Minnesota", "United_States",
           "Iraq_War", "Bill_Clinton", "China", "Syria", "Mexico", "Mexico", "Mexico", "Washington,_D.C.", "Chicago",
           "Italy", "Myanmar", "United_States", "Texas", "United_States", "United_States", "United_States",
           "United_States", "United_States", "Crimea", "United_States", "United_States", "United_States",
           "United_States", "United_States", "United_States", "United_States", "United_States", "United_States",
           "United_States", "United_States", "United_States", "Iran", "Iran", "United_States",
           "Mechanicsburg,_Pennsylvania", "Pennsylvania", "Iraq", "Johnstown,_Pennsylvania", "Pennsylvania",
           "United_States", "United_States", "United_States", "Syria", "France", "United_States", "United_States",
           "United_States", "United_States", "Florida", "Pennsylvania", "Pennsylvania", "Philadelphia", "United_States",
           "United_States", "Baton_Rouge,_Louisiana", "Cleveland", "United_States", "Nice", "France", "Nice", "France",
           "France", "Israel", "United_States", "Miami", "Dallas", "Atlantic_City,_New_Jersey", "Airport",
           "Convention_center", "United_States", "Baghdad", "Bangladesh", "Cleveland", "Israel", "State_of_Palestine",
           "United_States", "Israel", "State_of_Palestine", "United_States", "United_States", "United_States",
           "Bill_Clinton", "U.S._Immigration_and_Customs_Enforcement", "United_Kingdom", "West_Virginia",
           "Orlando,_Florida", "Dallas", "Texas", "Saudi_Arabia", "New_Hampshire", "Orlando,_Florida",
           "Orlando,_Florida", "Los_Angeles", "Florida", "Orlando,_Florida", "Elkhart,_Indiana", "Benghazi", "Texas",
           "Royce_da_5'9%22", "Pearl_Harbor", "Japan", "United_States", "Syria", "New_Mexico", "Mexico",
           "United_States", "United_States", "Syria", "Iraq", "Libya", "United_States", "United_States", "China",
           "United_States", "United_States", "Massachusetts", "United_States", "United_States", "Las_Vegas_Strip",
           "United_States", "Connecticut", "New_York_City", "Colorado", "Colorado", "New_York_City", "New_York_City",
           "Wisconsin", "United_States", "Wisconsin", "United_States", "Wisconsin", "Guantanamo_Bay_detention_camp",
           "United_States", "Pakistan", "United_States", "Paris", "Brussels", "Europe", "United_States", "Syria",
           "Europe", "United_States", "Brussels", "Cleveland", "Brussels", "Washington,_D.C.", "Cuba", "Brussels",
           "Cuba", "Brussels", "Arizona", "Florida", "Ohio", "Mexico", "Ohio", "Mexico", "United_States", "Ohio",
           "Ohio", "United_States", "Chicago", "Florida", "Florida", "Ohio", "Mexico", "United_States", "Florida",
           "Kentucky", "Virginia", "Florida", "South_Carolina", "Washington,_D.C.", "Florida", "Florida",
           "Washington,_D.C.", "Florida", "United_States", "Washington,_D.C.", "United_States", "Texas", "Nevada",
           "Iowa", "Tennessee", "West_Hollywood,_California", "South_Carolina", "Holy_See", "Nevada", "United_States",
           "South_Carolina", "North_Augusta,_South_Carolina", "Canada", "United_States", "South_Carolina", "Iraq_War",
           "New_Hampshire", "Washington,_D.C.", "Iowa", "New_Hampshire", "United_States", "Iowa", "Canada",
           "White_House", "Canada", "United_States", "Illinois", "Iowa", "Oklahoma", "United_States", "Ames,_Iowa",
           "Iowa", "Wall_Street", "New_York_City", "New_York_City", "United_States", "United_States", "Iowa", "Cosby",
           "Paris", "Germany", "Canada", "New_Hampshire", "Germany", "Morocco", "Israel", "United_States",
           "United_States", "Florida", "Syria", "Ukraine", "Crimea", "Russia", "United_States", "Paris", "Louvre",
           "United_States", "France", "Australia", "Mexico", "Chicago", "Oval_Office", "Guantanamo_Bay_detention_camp",
           "United_States", "Europe", "Middle_East", "Nazi_Germany", "Europe", "Chicago", "Russia",
           "Great_Wall_of_China", "Mexico", "Hollywood", "Russia", "United_States", "Australia", "United_States",
           "United_States", "Mexico", "United_States", "Mexico", "California", "United_States", "Russia",
           "United_States", "United_States", "Boston", "Russia", "United_States"]

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
    out = []
    values = []
    for k,v in dingle.iteritems():
        if v > 4 and k is not "United_States":
            values.append(v)
    print values

    for k, v in dingle.iteritems():
        if v > 4 and k is not "United_States":
            out.append(it(k.replace("_", " "), float((v-min(values))/float((max(values)-min(values))))))

    out = sorted(out, key=lambda x: x.times)
    n = []
    for o in out:
        n.append((o.name, o.times))
    return JsonResponse({"d": n})

class it():

    def __init__(self, name,t):
        self.name = name
        self.times = t





