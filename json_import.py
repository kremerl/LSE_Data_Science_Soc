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



# fn provided by Chris Chia, pres of DS soc, thanks Chris!
def df_from_json(filepath: str) -> pd.DataFrame:
    """
    Inputs: takes in the path to the .json file as str
    Returns: returns .json, normalised as dataframe
    Example usage: 
    business_df = df_from_json("yelp_academic_dataset_business.json")
    business_df.to_csv("business_df", index=False)
    Notes:
    this is small enough to fit into memory, 
    at least for the business json at ~ 100 MB
    The data may not be fully normalised, so a closer inspection
    at the .json file is required
    """
    temp = []
    with open(filepath) as f:
        for i, line in tqdm.tqdm(enumerate(f)):
            # try and parse the line as a JSON / dict
            try:
                temp += [json.loads(line)]
            # an error might occur, if so do nothing
            except:
                pass
    # close the file buffer
    f.close()
    # convert from array of jsons to DataFrame
    return pd.json_normalize(temp)


business_df = df_from_json("/Users/louiskremer/Desktop/GitHub_Projects/Yelp Data local/json_data/yelp_business_info.json")
business_df.to_csv("business_info.csv", index=False)