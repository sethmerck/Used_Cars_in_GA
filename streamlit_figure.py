### creates chart, using streamlit library, with the most recent csv file in working_dataset folder
import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

st.header('Breakdown of Listing Data from cars.com', divider='red')
st.write("")

f = open('log.txt', 'r')
num = int(f.read())
# st.set_page_config(layout="wide")
with open('status.log', 'r') as logs:
    lines = logs.readlines()[(-1 * num):]
    lines = [datetime.strptime(i[:10], '%Y-%m-%d').date() for i in lines]

start_t = lines[0]
end_t = lines[-1]
w, z = st.select_slider('Date Collected',options=lines, value=[start_t,end_t])

prev_file = f"test_actions{lines.index(w)+1}.csv"
recent_file = f"test_actions{lines.index(z) + 1}.csv"

prev_data = pd.read_csv(f'working_dataset/{prev_file}')
data = pd.read_csv(f'working_dataset/{recent_file}') #path folder of the data file

prev_data = prev_data.drop(prev_data[prev_data["Mileage"]<100].index)
data = data.drop(data[data["Mileage"]<100].index)

prev_data = prev_data.drop(prev_data[prev_data["Price"]<100].index)
data = data.drop(data[data["Price"]<100].index)


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots(1, 2)
fig.suptitle("Price vs. Mileage Regression Among All Listings")
prev_plot = sns.regplot(x=prev_data['Mileage'],y=prev_data['Price'], data=prev_data, line_kws={"color": "red"}, fit_reg=True, logx=True, truncate=True, ax=ax[0])
plot = sns.regplot(x=data['Mileage'],y=data['Price'], data=data, line_kws={"color": "red"}, fit_reg=True, logx=True, truncate=True, ax=ax[1])

count = 0
for k in ax:
    if count == 0:
        counts = prev_data["Price"].count().tolist()
        k.set_title(f"{w}\n\nn = {counts}")
    else:
        counts = data["Price"].count().tolist()
        k.set_title(f"{z}\n\nn = {counts}")
    k.set_xlabel('Mileage', fontsize = 18, labelpad=18)
    
    k.set_ylabel('Price', fontsize = 18, labelpad=18)
    
    k.set_ylim(0, 250000)
    
    k.set_xlim(0, 350000)
    count+=1


# st.write(prev_file)
st.pyplot(fig)
st.write("")

## sorts by make data ##

f = open('brands.txt')
brands = []
for i in f.readlines():
    brands.append(i.strip())

prev_data['Car'] = prev_data['Car'].str.split(' ')
data['Car'] = data['Car'].str.split(' ')

prev_data = prev_data.explode('Car')
data = data.explode('Car')

prev_data = prev_data.query(f"Car in {brands}")
data = data.query(f"Car in {brands}")

## price box plot #
a, b = plt.subplots(1,2, figsize=(10,5))

sorted_prev_data = prev_data[prev_data['Car'].str.contains("Honda|Chevrolet|Nissan|Ford|Toyota")]
sorted_data = data[data['Car'].str.contains("Honda|Chevrolet|Nissan|Ford|Toyota")]
sorted_box = sorted_prev_data.boxplot(column='Price', by="Car", rot=15, ax=b[0])
box = sorted_data.boxplot(column='Price', by="Car", rot=15, ax=b[1])

count = 0
for k in b:
    if count == 0:
        k.set_title(w)
        counts = sorted_prev_data.groupby(by="Car")["Price"].count().tolist()
    else:
        k.set_title(z)
        counts = sorted_data.groupby(by="Car")["Price"].count().tolist()
    k.set_xlabel('Car Make', fontsize = 14, labelpad=14)
    
    k.set_ylabel('Price', fontsize = 14, labelpad=14)
    labels = k.get_xticklabels(which='major')
    k.set_xticks(ticks=[1,2,3,4,5], labels=[f"{str(v)[12:-2]}\n n = {counts[i]}" for i, v in enumerate(labels)])
    count+=1
a.suptitle("Price Distribution Model of Five Most Common Car Makes\n", fontsize=16)
# labels = box.get_xticklabels(which='major')

# counts = sorted_data.groupby(by="Car")["Price"].count().tolist()
# box.set_xticks(ticks=[1,2,3,4,5], labels=[f"{str(v)[12:-2]}\n n = {counts[i]}" for i, v in enumerate(labels)])

st.pyplot(a)

## mileage box plot ##
a, b = plt.subplots(1,2, figsize=(10,5))

sorted_box = sorted_prev_data.boxplot(column='Mileage', by="Car", rot=15, ax=b[0])
box = sorted_data.boxplot(column='Mileage', by="Car", rot=15, ax=b[1])

count = 0
for k in b:
    if count == 0:
        k.set_title(w)
        counts = sorted_prev_data.groupby(by="Car")["Mileage"].count().tolist()
    else:
        k.set_title(z)
        counts = sorted_data.groupby(by="Car")["Mileage"].count().tolist()
    k.set_xlabel('Car Make', fontsize = 14, labelpad=14)
    
    k.set_ylabel('Mileage', fontsize = 14, labelpad=14)
    labels = k.get_xticklabels(which='major')
    k.set_xticks(ticks=[1,2,3,4,5], labels=[f"{str(v)[12:-2]}\n n = {counts[i]}" for i, v in enumerate(labels)])
    count+=1
a.suptitle("Mileage Distribution Model of Five Most Common Car Makes\n", fontsize=16)
# labels = box.get_xticklabels(which='major')

# counts = sorted_data.groupby(by="Car")["Price"].count().tolist()
# box.set_xticks(ticks=[1,2,3,4,5], labels=[f"{str(v)[12:-2]}\n n = {counts[i]}" for i, v in enumerate(labels)])

st.pyplot(a)

## stat_table ## 

# prev_data_grouped = prev_data.groupby(by="Car")["Price"].agg([np.mean, np.std, 'min', 'max', 'count'])
# data_grouped = data.groupby(by="Car")["Price"].agg([np.mean, np.std, 'min', 'max', 'count'])

# data_grouped['prev_count'] = prev_data_grouped['count']
# data_grouped['diff'] = data_grouped['count'] - prev_data_grouped['count']
# data_grouped.rename(columns={"mean": f"{z} Mean", "std": f"{z} STD Dev", "min": f"{z} Min", "max": f"{z} Max", "count": f"{z} Count", "prev_count": f"{w} Count", "diff": "Count_Difference"}, inplace=True)
# st.write(" ")
# st.title("Breakdown of Make Data")
# st.dataframe(data_grouped,use_container_width=True)
