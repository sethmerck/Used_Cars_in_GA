import requests
import csv
from bs4 import BeautifulSoup as bs


with open("zips.txt") as f:
    zip_dict = []
    for line in f.readlines():
        page_counter = 1

        url = f"https://www.cars.com/shopping/results/?list_price_max=&makes[]=&maximum_distance=1&models[]=&page={page_counter}&page_size=100&stock_type=all&zip={line.strip()}"
        req = requests.get(url)
        soup = bs(req.text)

        pages = soup.find_all('li', attrs={'class': 'sds-pagination__item'})

        if len(pages) > 1:
            for i in range(1, len(pages) + 1):
                
                req = requests.get(f"https://www.cars.com/shopping/results/?list_price_max=&makes[]=&maximum_distance=1&models[]=&page={page_counter}&page_size=100&stock_type=all&zip={line.strip()}")
                soup = bs(req.text)
                page_counter+=1
                miles = soup.find_all('div', attrs={"class": "mileage"})
                prices = soup.find_all('span', attrs={"class": "primary-price"})

                count = 0
                miles_count = 1
                price_count = 0

                
                vehicles = soup.find_all('a', attrs={"class": "vehicle-card-link js-gallery-click-link"})
                new_used = soup.find_all('p', attrs={'class': 'stock-type'})

                

                for a in vehicles:
                    soup_dict = {}
                    
                    if a['href'].endswith("?attribution_type=se_rp"):
                        break
                    else:
                        if new_used[count].get_text().strip().endswith('Certified'):
                            continue
                        elif new_used[count].get_text().strip() == 'Used':
                            try:
                                soup_dict['Zip'] = line.strip()
                                soup_dict['Car'] = a.get_text().strip()
                                soup_dict['Price'] = prices[price_count].get_text().strip()
                                soup_dict['Mileage'] = miles[miles_count].get_text().strip()
                                soup_dict['Link'] = "https://www.cars.com" + a['href']
                                # soup_dict[a.get_text().strip()] = [prices[price_count].get_text().strip(), miles[miles_count].get_text().strip()]
                                miles_count += 1
                                price_count += 1
                                count+=1
                            except IndexError:
                                print('REEEEEEEEEEEEEEEEe')
                                print("")
                        else:
                            price_count += 1
                            count+=1
                            
                    if len(soup_dict) == 0:
                        zip_dict.append({'Zip': line.strip(), 'Car': '', 'Price': '', 'Mileage': '', 'Link': ''})
                    else:
                        zip_dict.append(soup_dict)
        else:

            miles = soup.find_all('div', attrs={"class": "mileage"})
            prices = soup.find_all('span', attrs={"class": "primary-price"})

            count = 0
            miles_count = 1
            price_count = 0

            
            vehicles = soup.find_all('a', attrs={"class": "vehicle-card-link js-gallery-click-link"})
            new_used = soup.find_all('p', attrs={'class': 'stock-type'})

            

            for a in vehicles:
                soup_dict = {}
                if a['href'].endswith("?attribution_type=se_rp"):
                    break
                else:
                    if new_used[count].get_text().strip() == 'Used':
                        try:
                            soup_dict['Zip'] = line.strip()
                            soup_dict['Car'] = a.get_text().strip()
                            soup_dict['Price'] = prices[price_count].get_text().strip()
                            soup_dict['Mileage'] = miles[miles_count].get_text().strip()
                            soup_dict['Link'] = "https://www.cars.com" + a['href']
                            # soup_dict[a.get_text().strip()] = [prices[price_count].get_text().strip(), miles[miles_count].get_text().strip()]
                            miles_count += 1
                            price_count += 1
                            count+=1
                        except IndexError:
                            print('REEEEEEEEEEEEEEEEe')
                            print("")
                    else:
                        price_count += 1
                        count+=1
                if len(soup_dict) == 0:
                    zip_dict.append({'Zip': line.strip(), 'Car': '', 'Price': '', 'Mileage': '', 'Link': ''})
                else:
                    zip_dict.append(soup_dict)
        # print(zip_dict)


fields = ['Zip', 'Car', 'Price', 'Mileage', 'Link']
with open("test_links.csv", "w") as f:
    w = csv.DictWriter(f, fields)
    w.writeheader()
    w.writerows(zip_dict)
