# import packages and your csv in this file

import numpy as np
import pandas as pd
import regex as re
import json, tqdm, string



# Louis: import business_info csv and convert to dataframe
business_info = pd.read_csv("/Users/louiskremer/Desktop/github/yelp_data_local/business_info.csv", delimiter = ",", header = 0, dtype = str)

# Louis: import LV data
lv_nlp = pd.read_csv("/Users/louiskremer/Desktop/github/yelp_data_local/lv_nlp.csv", delimiter = ",", header = 0, dtype = str)

# convert into dataframes
business_info = pd.DataFrame(business_info)
lv_nlp = pd.DataFrame(lv_nlp)




