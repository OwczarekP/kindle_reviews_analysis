# Kindle Reviews Analysis
This project focus on analysis of reviews of the different versions of Kindle products:
* Kindle classic ads version
* Kindle classic non-ads version
* Kindle paperwhite ads version
* Kindle paperwhite non-ads version
* Kindle paperwhite signature edition

The reviews are scraped directly from Amazon site, focusing on only english sites: US, UK, Canada and Australia.
The reviews are divided into 3 categories based on the score of the product:
* 0-2 stars: Bad review
* 3 stars: Neutral review
* 4-5 stars: Good review

In this project we focus to answer the following questions:
* Is there differences between countries?
* Which version of Kindle is the best?
* Is there any differences in score between ads and non-ads version?
* What are the best and worse trait of each Kindle?

Additionaly the Sentiment Classification of reviews will be provided.

## Requirements
* beautifulsoup4==4.11.1
* datefinder==0.7.1
* mysql_connector_repackaged==0.3.1
* requests==2.28.1

## PowerBI Visualization

![PowerBI-Vis]('./powerBI/powerBI_v00.png')

Check this online: TO-DO

## TO-DO
- [x] Scrap Amazon Reviews & store in SQL database
- [ ] PowerBI Visualization
- [x] Data cleaning
- [ ] Exploratory Data Analysis
- [ ] Review Processing for Classification
- [ ] Sentiment Classification
## Running scripts

## Results 

## License

[MIT](https://choosealicense.com/licenses/mit/)
