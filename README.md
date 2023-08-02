# READ ME

Python scripts I used to collect and clean used car data are located in this repository.

CSV files in "outputs" folder were then used to create Tableau dashboard located <a href="https://public.tableau.com/app/profile/sethmerck/viz/GeorgiaUsedCarData/Dashboard1">here.</a>

Text files in "assets" folder were used as lists to iterate over after being read into Python.

This is a personal project to help in my search of buying another used car. 

## How It's Made: 

**Tech used:** BeautifulSoup and Pandas libraries in Python; Tableau

I used the BeautifulSoup library in Python to scrape used car listing data in Georgia from cars.com. Then cleaned up the data collected and saved it as a CSV file using Pandas.

"get_listing_data.py" file gets zip code, mileage, price, car make and model, and associated link for every listing on cars.com with a Georgia zip code. All listings were saved in a CSV file. Data was then cleaned using pandas to create cleaned tables to be used in Tableau for data visualizations.
