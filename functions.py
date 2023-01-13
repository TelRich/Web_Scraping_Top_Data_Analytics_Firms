# Import necessary library
import pandas as pd

"""
The blow function can extract the following firm details from the html tags:
Position, Names (pass in the list starting from the 4th item), Motors, Reviews,
Prices, Employess, Year founded, and Location 
"""
def extract_detail(name, tag_lst):
    lst = [tag.text for tag in tag_lst]
    print(f"The number of firm {name} extracted is {len(lst)}")
    return pd.Series(lst)

""" The below are individual functions to extract each firm details"""

def extract_position(tag_lst):
    pos_lst = [pos.text for pos in tag_lst]
    print(f"The number of firm pos extracted is {len(pos_lst)}")
    return pd.Series(pos_lst)

def extract_names(tag_lst):
    names_lst = [name.text for name in tag_lst[3:]]
    print(f"The number of firm name extracted is {len(names_lst)}")
    return pd.Series(names_lst)

def extract_motors(tag_lst):
    motor_lst = [motor.text for motor in tag_lst]
    print(f"The number of firm motor extracted is {len(motor_lst)}")
    return pd.Series(motor_lst)

def extract_reviews(tag_list):
    review_lst = [review.text for review in tag_list]
    print(f"The number of review extracted is {len(review_lst)}")
    return pd.Series(review_lst)

def extract_progress_values(tag_lst):    
    service_pct = [percent[1].text for percent in enumerate(tag_lst) if percent[0]%2 ==0]
    platform_pct = [percent[1].text for percent in enumerate(tag_lst) if percent[0]%2 ==1]       
    print(f"The number of service percent is {len(service_pct)}")
    print(f"The number of platform percent is {len(platform_pct)}")
    return pd.Series(service_pct), pd.Series(platform_pct) 

def exttract_prices(tag_lst):    
    price_lst = [price.text for price in tag_lst]
    print(f"The number of price extracted is {len(price_lst)}")
    return pd.Series(price_lst)

def extract_employees(tag_lst):
    emps_lst = [emp.text for emp in tag_lst]
    print(f"The number of employees extracted is {len(emps_lst)}")
    return pd.Series(emps_lst)

def extract_founded_year(tag_lst):    
    year_lst = [year.text for year in tag_lst]
    print(f"The number of year extracted is {len(year_lst)}")
    return pd.Series(year_lst)

def extract_locations(tag_lst):
    firm_lst = [firm.text for firm in tag_lst]
    print(f"The number of locations extracted is {len(firm_lst)}")
    return pd.Series(firm_lst)