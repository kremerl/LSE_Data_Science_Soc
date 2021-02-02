# in this file, json is transformed to csv

# extract business_id and stars variable from reviews file
data = {'business_id': [], 'stars': [], 'review_date': [], 'text': []}

with open('/Users/louiskremer/Desktop/GitHub_Projects/Yelp Data local/json_data/yelp_reviews.json') as reviews_file:
    for line in tqdm.tqdm(reviews_file):
        review = json.loads(line)
        data['business_id'].append(review['business_id'])
        data['stars'].append(review['stars'])
        data['review_date'].append(review['date'])
        data['text'].append(review['text'])


# convert the extracted variables to data frame
reviews_df = pd.DataFrame(data)
del data
reviews_df.head()


del review
del reviews_file
del line

# create subset only containing Las Vegas (largest city data)
data2 = {'business_id': [], 'city': []}

with open('/Users/louiskremer/Desktop/GitHub_Projects/Yelp Data local/json_data/yelp_business_info.json') as business_file:
    for line in tqdm.tqdm(business_file):
        business = json.loads(line)
        data2['business_id'].append(business['business_id'])
        data2['city'].append(business['city'])


city_df = pd.DataFrame(data2)
city_df.head()
lv_df = city_df[city_df['city'].str.contains('Las Vegas')]
lv_df.count()


del data2
del business
del business_file
del line
del city_df

# select only Las Vegas text data
lv_reviews_df = lv_df.merge(reviews_df, on='business_id', how='left')
lv_reviews_df.head()

# turn into csv for export
lv_reviews_df.to_csv('lv_nlp.csv', sep=',', index=False)


# now load the business info json
data2 = {'business_id': [], 'city': [], 'state': [], 'latitude': [], 'longitude': [], 'stars': [],
         'review_count': [], 'is_open': [], 'categories': []
         }

with open('/Users/louiskremer/Desktop/GitHub_Projects/Yelp Data local/json_data/yelp_business_info.json') as business_file:
    for line in tqdm.tqdm(business_file):
        business = json.loads(line)
        data2['business_id'].append(business['business_id'])
        data2['city'].append(business['city'])
        data2['state'].append(business['state'])
        data2['latitude'].append(business['latitude'])
        data2['longitude'].append(business['longitude'])
        data2['stars'].append(business['stars'])
        data2['review_count'].append(business['review_count'])
        data2['is_open'].append(business['is_open'])
        data2['categories'].append(business['categories'])

business_df = pd.DataFrame(data2)
business_df.head()

del data2
del line

business_df.to_csv('business_info.csv', sep=',', index=False)



#with open('/Users/louiskremer/Desktop/GitHub_Projects/Yelp Data local/json_data/yelp_business_info.json') as business_file:
#    data3 = json.load(business_file)
#    df =pd.json_normalize(data3, 'attributes', {'BusinessAcceptsCreditCards','BikeParking','GoodForKids'
#        ,'BusinessParking','ByAppointmentOnly','RestaurantsPriceRange2'})
