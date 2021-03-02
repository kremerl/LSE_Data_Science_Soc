# clean your data in here

# make dataframe easily viewable
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 300)


business_info.head()
lv_nlp.head()

# select only restaurants
business_info = business_info[business_info["categories"].str.contains("Restaurants", na = False)]
lv_nlp = lv_nlp.merge(business_info["business_id"], on='business_id', how='inner')