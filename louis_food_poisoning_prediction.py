#Louis' Food Poisoning Prediction

from collections import Counter
import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.linear_model import LogisticRegression
import pickle
import statsmodels.api as sm


#subset to Las Vegas only
business_info = business_info[business_info["city"] == "Las Vegas"]

# subset reviews that experienced food poisoning, by matching words to their reviews
words = ["poison", "diarrhea", "diarrhoea", "vomit", "puking", "puked", "threw up", "throw up", "salmonella"] # don't use "sick", as only 1/2 correlated with negative review
lv_poisoned = lv_nlp[lv_nlp["text"].str.contains(("|".join(words)), case = False, na = False)]

# subset only bad reviews (nobody would give a good review to a restaurant in which they were poisoned)
lv_poisoned["stars"] = pd.to_numeric(lv_poisoned["stars"].copy())
lv_poisoned = lv_poisoned.loc[lv_poisoned["stars"] < 2.0]

lv_poisoned.count()
lv_poisoned.head()

# convert data to list (fn does not accept pandas data types)
business_id = business_info["business_id"].values.tolist()

# get unique values from poisoned_id, makes it substantially faster to compute
poisoned_id = lv_poisoned["business_id"].values.tolist()
poisoned_id = set(poisoned_id.copy())
poisoned_id = list(poisoned_id.copy())

# now count of poisoned reviews per restaurant and total reviews per restaurant
poisoned_counter = Counter(lv_poisoned["business_id"])
total_counter = Counter(lv_nlp["business_id"])

# function
def is_poisoned(a, b):
    poisoned_binary = []
    for row in a:
        if row in b:
            poisoned_count = poisoned_counter[row]
            total_count = total_counter[row]
            poisoned_binary.append(poisoned_count / total_count)
        else:
            poisoned_binary.append(0)
    return poisoned_binary

# business_info["poisoned"] = is_poisoned(business_info["business_id"], lv_poisoned2["business_id"]) # DOES NOT WORK WITH PANDAS data input
business_info["%_poisoned"] = is_poisoned(business_id, poisoned_id)

print(business_info["%_poisoned"])


# create dummies for different cuisines
df = pd.get_dummies(business_info["Cuisine"], columns = ["Cuisine"])
df.head()
business_info2 = business_info.copy()
business_info2 = pd.concat([business_info, df], axis = 1)

business_info2.iloc[:,63:74]
business_info_names = business_
print(business_info2.columns.to_list())

# build logistic regression
train = business_info2.sample(100)

y_train = train[["%_poisoned"]].astype(float)
x_train = train[['American', 'Asian Fusion', 'Chinese', 'Coffee & Tea', 'Fast Food', 'Indian', 'Italian', 'Japanese', 'Mediterranean', 'Mexican',
                 'Others', 'Seafood', 'Thai', 'Vietnamese']].astype(float)

smlogreg = sm.Logit(y_train, x_train).fit()
smlogreg.summary()












# some more cleaning
business_info["attributes.RestaurantsTakeOut"].isnull().any()
business_info["attributes.RestaurantsTakeOut"].isnull().sum()

business_info["attributes.BusinessAcceptsCreditCards"] = business_info["attributes.BusinessAcceptsCreditCards"].astype(bool)
business_info["attributes.BusinessAcceptsCreditCards"] = business_info["attributes.BusinessAcceptsCreditCards"].astype(int)

business_info["attributes.RestaurantsTakeOut"] = business_info["attributes.RestaurantsTakeOut"].astype(bool)
business_info["attributes.RestaurantsTakeOut"] = business_info["attributes.RestaurantsTakeOut"].astype(int)

business_info["attributes.RestaurantsTakeOut"].replace({NaN: False})
business_info["attributes.RestaurantsTakeOut"].replace({False: 0, True: 1}, inplace=True)



