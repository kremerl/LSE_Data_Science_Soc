#Louis' Food Poisoning Prediction

from collections import Counter

#subset to Las Vegas only
business_info = business_info[business_info["city"] == "Las Vegas"]

# subset reviews that experienced food poisoning, by matching words to their reviews
words = ["poison", "diarrhea", "diarrhoea", "vomit", "puking", "puked", "threw up", "throw up", "salmonella"] # don't use "sick", as only 1/2 correlated with negative review
lv_poisoned = lv_nlp[lv_nlp["text"].str.contains(("|".join(words)), case = False, na = False)]

# subset only bad reviews (nobody would give a good review to a restaurant in which they were poisoned)
lv_poisoned["stars"] = pd.to_numeric(lv_poisoned["stars"]) # REMOVE once dataset is cleaned
lv_poisoned = lv_poisoned.loc[lv_poisoned["stars"] < 3.0]

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









# debugging leftovers (keep for now)
poisoned_id[0:3]
full_id[0:3]
full_id

z = ["oranges", "apples", "pears", "peaches"]
for x in z:
    print(x)

pd.Series(z)


#other stuff
# function that returns 1 if poisened and 0 otherwise (works by matching business_id of total dataset to business_id of poisened dataframe)
def is_poisoned(a, b):
    new_variable = []
    for row in a:
        if row in b:
            new_variable.append(1) #append is like [row/i] in R (to iterate over outcome variable)
        else:
            new_variable.append(0)
    return new_variable

# prototype of fn
one = ["abc123", "bcd234", "cde345"]
two = ["xyz", "xyz2", "abc123", "abc123"]
is_poisoned(one,two)
