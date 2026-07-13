#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


list1 = pd.read_csv('csv/CRMLSListing202401.csv')
len(list1)
#27454 rows in January 2024


# In[4]:


list2 = pd.read_csv('csv/CRMLSListing202402.csv')
len(list2)
#22428 rows in February 2024


# In[5]:


list3 = pd.read_csv('csv/CRMLSListing202403.csv')
len(list3)
#32282 rows in March 2024


# In[6]:


list4 = pd.read_csv('csv/CRMLSListing202404.csv')
len(list4)
#36503 rows in April 2024


# In[7]:


list5 = pd.read_csv('csv/CRMLSListing202405.csv')
len(list5)
#38796 rows in May 2024


# In[8]:


list6 = pd.read_csv('csv/CRMLSListing202406.csv')
len(list6)
#35893 rows in June 2024


# In[9]:


list7 = pd.read_csv('csv/CRMLSListing202407.csv')
len(list7)
#36340 rows in July 2024


# In[10]:


list8 = pd.read_csv('csv/CRMLSListing202408.csv')
len(list8)
#35305 rows in August 2024


# In[11]:


list9 = pd.read_csv('csv/CRMLSListing202409.csv')
len(list9)
#34625 rows in September 2024


# In[12]:


list10 = pd.read_csv('csv/CRMLSListing202410.csv')
len(list10)
#34730 rows in October 2024


# In[13]:


list11 = pd.read_csv('csv/CRMLSListing202411.csv')
len(list11)
#25128 rows in November 2024


# In[14]:


list12 = pd.read_csv('csv/CRMLSListing202412.csv')
len(list12)
#19417 rows in December 2024


# In[15]:


list13 = pd.read_csv('csv/CRMLSListing202501.csv')
len(list13)
#37469 rows in January 2025


# In[16]:


list14 = pd.read_csv('csv/CRMLSListing202502.csv')
len(list14)
#33983 rows in February 2025


# In[17]:


list15 = pd.read_csv('csv/CRMLSListing202503.csv')
len(list15)
#38492 rows in March 2025


# In[18]:


list16 = pd.read_csv('csv/CRMLSListing202504.csv')
len(list16)
#40187 rows in April 2025


# In[19]:


list17 = pd.read_csv('csv/CRMLSListing202505.csv')
len(list17)
#40271 rows in May 2025


# In[20]:


list18 = pd.read_csv('csv/CRMLSListing202506.csv')
len(list18)
#26399 rows in June 2025


# In[21]:


list19 = pd.read_csv('csv/CRMLSListing202507.csv')
len(list19)
#27345 rows in July 2025


# In[22]:


list20 = pd.read_csv('csv/CRMLSListing202508.csv')
len(list20)
#25210 rows in August 2025


# In[23]:


list21 = pd.read_csv('csv/CRMLSListing202509.csv')
len(list21)
#26923 rows in September 2025


# In[24]:


list22 = pd.read_csv('csv/CRMLSListing202510.csv')
len(list22)
#27586 rows in October 2025


# In[25]:


list23 = pd.read_csv('csv/CRMLSListing202511.csv')
len(list23)
#20677 rows in November 2025


# In[26]:


list24 = pd.read_csv('csv/CRMLSListing202512.csv')
len(list24)
#18773 rows in December 2025


# In[27]:


list25 = pd.read_csv('csv/CRMLSListing202601.csv')
len(list25)
#35302 rows in January 2026


# In[28]:


list26 = pd.read_csv('csv/CRMLSListing202602.csv')
len(list26)
#32884 rows in February 2026


# In[29]:


list27 = pd.read_csv('csv/CRMLSListing202603.csv')
len(list27)
#39153 rows in March 2026


# In[30]:


list28 = pd.read_csv('csv/CRMLSListing202604.csv')
len(list28)
#39020 rows in April 2026


# In[31]:


list29 = pd.read_csv('csv/CRMLSListing202605.csv')
len(list29)
#36115 rows in May 2026


# In[32]:


listing = pd.concat([list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,
    list11, list12, list13, list14, list15, list16, list17, list18, list19, list20,
    list21, list22, list23, list24, list25, list26, list27, list28, list29])
len(listing)
listing.to_csv('listing.csv', index=False)
#924690 rows after concatenation


# In[33]:


listing_residential = listing[listing["PropertyType"] == "Residential"]
len(listing_residential)
listing_residential.to_csv('listing_residential.csv', index=False)
#589353 rows after residential filter


# In[34]:


sold1 = pd.read_csv('csv/CRMLSSold202401_filled.csv')
len(sold1)
#17958 rows in January 2024


# In[35]:


sold2 = pd.read_csv('csv/CRMLSSold202402.csv')
len(sold2)
#19925 rows in February 2024


# In[36]:


sold3 = pd.read_csv('csv/CRMLSSold202403_filled.csv')
len(sold3)
#23276 rows in March 2024


# In[37]:


sold4 = pd.read_csv('csv/CRMLSSold202404_filled.csv')
len(sold4)
#24640 rows in April 2024


# In[38]:


sold5 = pd.read_csv('csv/CRMLSSold202405_filled.csv')
len(sold5)
#26487 rows in May 2024


# In[39]:


sold6 = pd.read_csv('csv/CRMLSSold202406_filled.csv')
len(sold6)
#24328 rows in June 2024


# In[40]:


sold7 = pd.read_csv('csv/CRMLSSold202407_filled.csv')
len(sold7)
#26240 rows in July 2024


# In[41]:


sold8 = pd.read_csv('csv/CRMLSSold202408.csv')
len(sold8)
#24558 rows in August 2024


# In[42]:


sold9 = pd.read_csv('csv/CRMLSSold202409.csv')
len(sold9)
#21267 rows in September 2024


# In[43]:


sold10 = pd.read_csv('csv/CRMLSSold202410.csv')
len(sold10)
#23274 rows in October 2024


# In[44]:


sold11 = pd.read_csv('csv/CRMLSSold202411.csv')
len(sold11)
#20279 rows in November 2024


# In[45]:


sold12 = pd.read_csv('csv/CRMLSSold202412.csv')
len(sold12)
#20241 rows in December 2024


# In[46]:


sold13 = pd.read_csv('csv/CRMLSSold202501_filled.csv')
len(sold13)
#18738 rows in January 2025


# In[47]:


sold14 = pd.read_csv('csv/CRMLSSold202502.csv')
len(sold14)
#18702 rows in February 2025


# In[48]:


sold15 = pd.read_csv('csv/CRMLSSold202503.csv')
len(sold15)
#21445 rows in March 2025


# In[49]:


sold16 = pd.read_csv('csv/CRMLSSold202504.csv')
len(sold16)
#23262 rows in April 2025


# In[50]:


sold17 = pd.read_csv('csv/CRMLSSold202505.csv')
len(sold17)
#23154 rows in May 2025


# In[51]:


sold18 = pd.read_csv('csv/CRMLSSold202506.csv')
len(sold18)
#22883 rows in June 2025


# In[52]:


sold19 = pd.read_csv('csv/CRMLSSold202507.csv')
len(sold19)
#23646 rows in July 2025


# In[53]:


sold20 = pd.read_csv('csv/CRMLSSold202508.csv')
len(sold20)
#22972 rows in August 2025


# In[54]:


sold21 = pd.read_csv('csv/CRMLSSold202509.csv')
len(sold21)
#22443 rows in September 2025


# In[55]:


sold22 = pd.read_csv('csv/CRMLSSold202510.csv')
len(sold22)
#23233 rows in October 2025


# In[56]:


sold23 = pd.read_csv('csv/CRMLSSold202511.csv')
len(sold23)
#19088 rows in November 2025


# In[57]:


sold24 = pd.read_csv('csv/CRMLSSold202512.csv')
len(sold24)
#20538 rows in December 2025


# In[58]:


sold25 = pd.read_csv('csv/CRMLSSold202601.csv')
len(sold25)
#16487 rows in January 2026


# In[59]:


sold26 = pd.read_csv('csv/CRMLSSold202602.csv')
len(sold26)
#19010 rows in February 2026


# In[60]:


sold27 = pd.read_csv('csv/CRMLSSold202603.csv')
len(sold27)
#23372 rows in March 2026


# In[61]:


sold28 = pd.read_csv('csv/CRMLSSold202604.csv')
len(sold28)
#24261 rows in April 2026


# In[62]:


sold29 = pd.read_csv('csv/CRMLSSold202605.csv')
len(sold29)
#24194 rows in May 2026


# In[63]:


sold = pd.concat([sold1, sold2, sold3, sold4, sold5, sold6, sold7, sold8, sold9, sold10,
                  sold11, sold12, sold13, sold14, sold15, sold16, sold17, sold18, sold19, sold20,
                  sold21, sold22, sold23, sold24, sold25, sold26, sold27, sold28, sold29])
len(sold)
sold.to_csv('sold.csv', index = False)
#639901 rows after concatenation


# In[64]:


sold_residential = sold[sold["PropertyType"] == "Residential"]
len(sold_residential)
sold_residential.to_csv('sold_residential.csv', index=False)
#430437 rows after Residential filter


# In[65]:


# Unique property types found
print(sold['PropertyType'].unique())


# In[66]:


# Filtering logic applied
print(f"Total rows before filter: {len(sold)}")
sold_residential = sold[sold['PropertyType'] == 'Residential']
print(f"Total rows after Residential filter: {len(sold_residential)}")


# In[67]:


# Null-count summary table
null_counts = sold_residential.isnull().sum()
null_pct = (null_counts / len(sold_residential)) * 100
null_summary = pd.DataFrame({'null_count': null_counts, 'null_pct': null_pct})
print(null_summary)


# In[68]:


# Missing value report columns above 90% null
high_null = null_summary[null_summary['null_pct'] > 90]
print("Columns above 90% null:")
print(high_null)


# In[69]:


# Numeric distribution summary for ClosePrice, LivingArea, DaysOnMarket
cols = ['ClosePrice', 'LivingArea', 'DaysOnMarket']
print(sold_residential[cols].describe(percentiles=[.25, .5, .75]))


# In[70]:


# Save filtered dataset as new CSV
sold_residential.to_csv('sold_residential_week2.csv', index=False)


# In[71]:


listings = pd.read_csv('listing_residential.csv', low_memory=False)


# In[72]:


# Step 1 - Fetch the mortgage rate data from FRED
url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US"
mortgage = pd.read_csv(url, parse_dates=['observation_date'])
mortgage.columns = ['date', 'rate_30yr_fixed']
print(mortgage.head())


# In[73]:


# Step 2 - Resample weekly rates to monthly averages
mortgage['year_month'] = mortgage['date'].dt.to_period('M')
mortgage_monthly = (
    mortgage.groupby('year_month')['rate_30yr_fixed']
    .mean()
    .reset_index()
)
print(mortgage_monthly.head())


# In[74]:


sold['year_month'] = pd.to_datetime(sold['CloseDate'], format='mixed').dt.to_period('M')

listings['year_month'] = pd.to_datetime(
    listings['ListingContractDate'], format='mixed'
).dt.to_period('M')


# In[75]:


# Step 4 - Merge
sold_with_rates = sold.merge(mortgage_monthly, on='year_month', how='left')
listings_with_rates = listings.merge(mortgage_monthly, on='year_month', how='left')


# In[76]:


# Step 5 - Validate the merge
print(f"Null rates in sold: {sold_with_rates['rate_30yr_fixed'].isnull().sum()}")
print(f"Null rates in listings: {listings_with_rates['rate_30yr_fixed'].isnull().sum()}")


# In[ ]:


# Save enriched datasets
sold_with_rates.to_csv('sold_with_rates.csv', index=False)
listings_with_rates.to_csv('listings_with_rates.csv', index=False)
print("Saved sold_with_rates.csv and listings_with_rates.csv")


# In[ ]:


# Preview
print(
    sold_with_rates[
        ['CloseDate', 'year_month', 'ClosePrice', 'rate_30yr_fixed']
    ].head()
)


# In[ ]:




