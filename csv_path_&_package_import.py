# import packages and your csv in this file

import numpy as np
import pandas as pd
import json
import tqdm


# import csv and convert to dataframe
business_info = pd.read_csv("/Users/louiskremer/Desktop/github/yelp_data_local/business_info.csv", delimiter = ",", header = 0, dtype = str)
business_info = pd.DataFrame(business_info)




