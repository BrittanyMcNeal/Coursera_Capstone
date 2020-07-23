import pandas as pd
import numpy as np
import json
import requests
from pandas.io.json import json_normalize
import matplotlib.cm as cm
import matplotlib.colors as colors
from sklearn.cluster import KMeans
import folium 
from pandas import ExcelWriter
from pandas import ExcelFile # Here we are downloading everything we will probably need

# Webscraped and saved information as a excel file
canada_df = pd.read_excel('Canada.xlsx', sheet_name='Sheet1')

#Here we are making sure our program is going to ignore anything "not assigned" and group things approprately


canada_dropNotAssigned = canada_df[canada_df.Borough != 'Not assigned'].reset_index(drop=True)

canada_grouped = canada_dropNotAssigned.groupby(['Postal Code','Borough'], as_index=False).agg(lambda x: ','.join(x))

mask = canada_grouped['Neighbourhood'] == "Not assigned"
canada_grouped.loc[mask, 'Neighbourhood'] = canada_grouped.loc[mask, 'Borough']

#using .shape
print (canada_grouped.shape)
print (canada_grouped)

(103, 3)
    Postal Code      Borough                                      Neighbourhood
0           M1B  Scarborough                                     Malvern, Rouge
1           M1C  Scarborough             Rouge Hill, Port Union, Highland Creek
2           M1E  Scarborough                  Guildwood, Morningside, West Hill
3           M1G  Scarborough                                             Woburn
4           M1H  Scarborough                                          Cedarbrae
..          ...          ...                                                ...
98          M9N         York                                             Weston
99          M9P    Etobicoke                                          Westmount
100         M9R    Etobicoke  Kingsview Village, St. Phillips, Martin Grove ...
101         M9V    Etobicoke  South Steeles, Silverstone, Humbergate, Jamest...
102         M9W    Etobicoke                Northwest, West Humber - Clairville
