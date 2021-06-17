# Introduction
My journey with Data Science started about 3 months ago when I undertook the Data Science Immersive program at General Assembly in Singapore. The following is my journey for my final capstone project for graduation. The programming language used here is Python.

# Background
Since the founding of the first commercial airlines in 1909, humanity have come a long way in mass air transportation. With the emergence of multiple carriers serving similar routes, there has been an increasing need to differentiate and market each airline from its competitors. The paramount aspect of customer satisfaction is one such way. Social media has a growing influence on our purchase decision and should be taken into account by airlines management.

The analysis of Tweets is one such way to measure customer sentiment.

# Problem Statement
To provide recommendations on specified areas of improvement for United Airlines based on passenger comments.

# Methodology

## Getting Data Points
Tweets have been identified as the source for passenger comments and both Kaggle and the Twitter API have been used to collect about 6,000 tweets about #unitedairlines.

Kaggle Data : https://www.kaggle.com/crowdflower/twitter-airline-sentiment

Twython was used together with the Twitter API to collect more United Airlines related tweets. You can sign up for the the API access at https://developer.twitter.com/

## Data Cleaning
Unnecessary text such as repeated tweets, '@' and '#' tags, urls, punctuation were removed. 

## Sentiment Analysis

### VADER
VADER was first used to evaluate the tweets prior to removing punctuation and changing them to lower case. Vader returns postitive, neutral, negative and compound scores. 

### TextBlob
TextBlob was used to evaluate the sentiments as a second base for comparison. Further pre-processing is done for tweets including changing them to lower case, removing numerical characters, removing stopwwords and removing punctuation. TextBlob returns polarity and subjectivity scores. 

## Topic Modelling
The first two approaches that I undertook for topic modelling are LDA and Doc2Vec, the results, read by human eye were not convincing thus manual keyword labelling was applied. 

### Latent Dirichlet Allocation
After plotting an Intertopic Distance Map, the spaces between the topics seems significant. However, the tweets categorized bu the models were not indicative of their topic distinctively. 

### Doc2Vec
This model returned rather high simliarity scores for a large number of tweets thus, also did not provide a conclusive categorization result. 

### Keywords Labelling
11 topics were identified, namely compliment, staff, delay, ticketing/billing, baggage, refund, cancellation, online, loyalty program, flight connections and children. The number of keywords used for each topic range from 2 to 13. 

# Deployment
Flask and Heroku were used for deployment into a webapp. The link for the site is: https://airlines-sentiment-analysis.herokuapp.com/#background
