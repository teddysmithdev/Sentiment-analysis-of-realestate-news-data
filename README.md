# Sentiment-analysis-of-financial-news-data
This was developed from interest in trading algorithms. I couldn't find anyone who had performed sentiment analysis on real-estate related news, so I decided to code one.

Demo: https://upbeat-neumann-e3f17d.netlify.com/

Currently it uses Scrapy (deployed from scraping hub) to crawl Bing search engine 
  * Each day at 9:00AM Scrapy crawls news for 'real-estate'
  * Article contents are run thru TextBlob (NLTK wrapper that makes sentiment analysis very simple in Python)
  * Contents are stored in a MongoDB database and sentiment is added incremently
  * Flask API is used as backend to communicate to front-end
  * Data is displayed in React App with ChartJS to display all results
  * Each crawl is presented along with a link to all articles scraped for that day



## File Description 

	USEFUL_FILES
      -> api - This is where Flask API is stored
      -> newscrawler - Scrapy framerwork and where all spiders are held. I currently have only one spider but plan to add more.
      -> client - React app that displays a nice UI to see data.
      
  

## Contribute

If you would like to contribute to this repo or have any ideas to make this better, feel free to submit a pull request or contact me at gyaneshmalhotra [at] gmail [dot] com.
For starters, there are some tasks available in the project tab of this repo on which you can start working on.