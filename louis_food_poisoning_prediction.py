#Louis' Food Poisoning Prediction

# subset reviews that experienced food poisoning, by matching words to their reviews
words = ["poison", "diarrhea", "diarrhoea", "vomit", "puking", "puked", "threw up", "throw up", "sick"] # don't use "sick", as only 1/2 correlated with negative review
lv_poisoned = lv_nlp[lv_nlp["text"].str.contains(("|".join(words)), case = False, na = False)]

#copy
lv_poisoned2 = lv_poisoned.copy() #for experimentation :)
lv_poisoned2.count()

# subset only bad reviews (nobody would give a good review to a restaurant in which they were poisoned)
lv_poisoned2["stars"] = pd.to_numeric(lv_poisoned2["stars"]) # REMOVE once dataset is cleaned
lv_poisoned2 = lv_poisoned2.loc[lv_poisoned2["stars"] < 3.0]
lv_poisoned2.count()

lv_poisoned.head()

lv_poisoned2["poisoned"] = np.where(lv_poisoned2["text"] =)


print(lv_poisoned2["text"])


