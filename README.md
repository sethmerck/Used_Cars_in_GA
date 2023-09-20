# READ ME

This is a project to aid in my search of buying another used car and to understand the trends in the used car market in my local area. 

The Python scripts I used to collect and clean used car data are located in this repository. I then compiled these scripts into one script "main.py" which automatically runs once every few days using GitHub Actions. The output of this python script is a cleaned CSV file containing all relevant car listings in the state of Georgia from cars.com. CSV files are located in the "working_dataset" directory.

CSV files in this folder can be used to create a Tableau dashboard, example located <a href="https://public.tableau.com/app/profile/sethmerck/viz/GeorgiaUsedCarData/Dashboard1">here.</a> However, I'm using Streamlit to create data visualizations that update automatically as new data comes in, located <a href="https://carsga.streamlit.app/">here.</a> The code used for generating these visualizations is located in the "streamlit_figure.py" file in this repo.

## How It's Made: 

**Tech used:** BeautifulSoup, Pandas, Seaborn, Matplotlib, and Streamlit libraries in Python; GitHub Actions; Tableau

I used the BeautifulSoup library in Python to scrape used car listing data in Georgia from cars.com. Then cleaned up the data collected and saved it as a CSV file using Pandas.

I scraped zip code, mileage, price, car make and model, and associated link for every listing on cars.com with a Georgia zip code. Data was then cleaned using pandas before saving as a CSV file.

Workflow folder and main.py file use Github Actions to periodically run this code that scrapes, cleans, and saves data in an updated csv file. "streamlit_figure.py" file is then linked to an app generated by Streamlit. This code can read in any of these csv files that represent snapshots in time of the data I collected, outputting visualizations for whichever dates are selected while using the Streamlit app.

## Results:

I found quite a few reasonably valued cars in my area that I'd consider purchasing. I also found which makes were most widely resold in the state (Honda, Chevrolet, Nissan, Ford, Toyota). 

Along with this, I found American made cars (Chevrolet and Ford) had more listings and their price distributions skewed higher compared to the other three most common car makes (Honda, Nissan, Toyota). However, I did not find much difference in the mileage distributions for listings of these five brands. 

The next few weeks will be spent discovering any new insights to be found in my datasets as more data comes in. As time progresses and my dataset grows, I'd like the ability to observe any broader trends (such as noticeable changes in price) that may be occurring within my local used car market.

## Optimizations:

Improve layout of data presentation within Streamlit. Generate more descriptive statistics based on regional (zip code or zip code clusters) within Georgia.
