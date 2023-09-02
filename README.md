# READ ME

This is a personal project to aid in my search of buying another used car and to understand the trends in the used car market in my local area. 

The Python scripts I used to collect and clean used car data are located in this repository. I then compiled these scripts into one script "main.py" which automatically runs once every few days using GitHub Actions. The output of this python script is a cleaned CSV file of all relevant car listings in the state of Georgia from cars.com. CSV files are located in the "working_dataset" directory.

CSV files in this folder were can be used to create a Tableau a dashboard located <a href="https://public.tableau.com/app/profile/sethmerck/viz/GeorgiaUsedCarData/Dashboard1">here.</a> However, I'm using Streamlit to create data visualizations that update automatically as new data comes in, located <a href="https://carsga.streamlit.app/">here.</a> The code used for generating these visualizations is located in the "streamlit_figure.py" file in this repo.

## How It's Made: 

**Tech used:** BeautifulSoup and Pandas libraries in Python; Tableau; GitHub Actions

I used the BeautifulSoup library in Python to scrape used car listing data in Georgia from cars.com. Then cleaned up the data collected and saved it as a CSV file using Pandas.

I scraped zip code, mileage, price, car make and model, and associated link for every listing on cars.com with a Georgia zip code. Data was then cleaned using pandas before saving as a CSV file.

Workflow folder and main.py file use Github Actions to periodically scrape, clean, and save data in an updated csv file.

## Results:

I found quite a few reasonably valued cars in my area that I'm interested in. I also found which makes were most widely resold in the state (Honda, Chevrolet, Nissan, Ford, Toyota).


## Optimizations:

Currently working on using GitHub Actions to automate data pipeline. Will produce updated csv file at regular time intervals. Link Streamlit or Tableau dashboard to this repo to have the most updated data shown on dashboard. Eventually once enough time has passed, create visualizations showing the change in dataset over time and observe any trends if present.
