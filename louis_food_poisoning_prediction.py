#Louis' Food Poisoning Prediction

# subset reviews that experienced food poisoning, by matching words to their reviews
words = ["poison", "diarrhea", "diarrhoea", "vomit", "puking", "puked", "threw up", "throw up", "salmonella"] # don't use "sick", as only 1/2 correlated with negative review
lv_poisoned = lv_nlp[lv_nlp["text"].str.contains(("|".join(words)), case = False, na = False)]

#copy
lv_poisoned2 = lv_poisoned.copy() #for experimentation :)
lv_poisoned2.count()
lv_nlp2 = lv_nlp.copy()

# subset only bad reviews (nobody would give a good review to a restaurant in which they were poisoned)
lv_poisoned2["stars"] = pd.to_numeric(lv_poisoned2["stars"]) # REMOVE once dataset is cleaned
lv_poisoned2 = lv_poisoned2.loc[lv_poisoned2["stars"] < 3.0]

lv_poisoned2.count()
lv_poisoned2.head()


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


# convert data to list (fn does not accept pandas data types)
business_id = business_info["business_id"].values.tolist()
nlp_id = lv_nlp["business_id"].values.tolist()

# get unique values from poisoned_id, makes it substantially faster to compute
poisoned_id = lv_poisoned["business_id"].values.tolist()
poisoned_id = set(poisoned_id.copy())
poisoned_id = list(poisoned_id.copy())

# WORKS, BUT ONLY FOR BUSINESS_INFO
# apply fn to full datasets to create a variable that classifies restaurants depending on whether or not they have already caused food poisoning
# business_info["poisoned"] = is_poisoned(business_info["business_id"], lv_poisoned2["business_id"]) # DOES NOT WORK WITH PANDAS for some reason I don't understand :(
business_info["poisoned"] = is_poisoned(business_id, poisoned_id)
business_info.groupby("poisoned").size()

#PROBLEMARIC OUTPUT (more 1s than 0s...)
lv_nlp["poisoned"] = is_poisoned(nlp_id, poisoned_id)
lv_nlp.groupby("poisoned").size()


# debugging leftovers (keep for now)
poisoned_id[0:3]
full_id[0:3]
full_id

z = ["sfu68", "sdfz98"]
for i in enumerate(z):
    print(z)

type(z[1])

type(business_info)
type(lv_nlp["business_id"])
type(full_id)
type(one)
type(poisoned_id)
type(full_id[1:100])