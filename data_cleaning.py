# clean your data in here

# make dataframe easily viewable
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 300)


business_info.head()
lv_nlp.head()

# select only restaurants
business_info = business_info[business_info["categories"].str.contains("Restaurants", na = False)]
lv_nlp = lv_nlp.merge(business_info["business_id"], on='business_id', how='inner')

#categories into cuisines
new2 = business_info['categories'].str.split(', ')

#counting unique values
counts = []
for i in new2:
    for x in i:
        counts.append(x)
x= pd.Series(counts).value_counts()

#cuisine categories
Cuisine = []
for x in new2:
    for i in x[1:]:
        #others = False
        if i== 'Fast Food' or i=='Pizza' or i=="Burgers" or i=="Chicken Wings":
            Cuisine.append('Fast Food')
            break
        elif i=='Mexican':
            Cuisine.append('Mexican')
            break
        elif i=='American (Traditional)' or i=='American (New)':
            Cuisine.append('American')
            break
        elif i=='Chinese':
            Cuisine.append('Chinese')
            break
        elif i=='Italian':
            Cuisine.append('Italian')
            break
        elif i=='Coffee & Tea':
            Cuisine.append('Coffee & Tea')
            break
        elif i=='Japanese' or i=='Sushi Bars':
            Cuisine.append('Japanese')
            break
        elif i=='Seafood':
            Cuisine.append('Seafood')
            break
        elif i=='Asian Fusion':
            Cuisine.append('Asian Fusion')
            break
        elif i=='Indian':
            Cuisine.append('Indian')
            break
        elif i=='Thai':
            Cuisine.append('Thai')
            break
        elif i=='Mediterranean':
            Cuisine.append('Mediterranean')
            break
        elif i=='Vietnamese':
            Cuisine.append('Vietnamese')
            break
    else:
        Cuisine.append('Others')


#attach cuisine to the df
business_info = business_info.copy() #to avoid SettingWithCopyWarning
business_info['Cuisine'] = Cuisine

with open('data_pickled.pkl', 'wb') as f:
    pickle.dump(business_info, f)