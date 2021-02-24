# clean your data in here

# make dataframe easily viewable
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

business_info.head()

# select only restaurants
business_info = business_info[business_info["categories"].str.contains("Restaurants", na = False)]
