# You have to run this file in the terminal to get the results in the excel file

import requests
import pandas as pd
from bs4 import BeautifulSoup 



# Specify the URL
url = 'https://www.ewrc-results.com/final/80236-rally-guanajuato-mexico-2023/'
html = requests.get(url)


# Parse the HTML
s = BeautifulSoup(html.content, 'html.parser')  

# Find the main element on the webpage
results = s.find(class_='final-results')


# Find all the elements for finishing place, driver number, driver-co-driver names, and car model
finishingPlace = results.find_all('td', class_='font-weight-bold text-left')
driverNumber = results.find_all('td', class_='final-results-number text-left text-primary font-weight-bold')
driver_codriver_names = results.find_all('a')
rc_type = results.find_all('td', class_ = 'final-results-cat fs-091')
finish_time = results.find_all('td', class_ = 'font-weight-bold text-right final-results-times')
times_diff = results.find_all('td', class_ = 'font-weight-bold text-right final-results-int')


data = []

# Iterate over all the lists simultaneously using zip()
for place, number, names, rc_info, timing, time_difference in zip(finishingPlace, driverNumber, driver_codriver_names, rc_type, finish_time, times_diff):
    # Strip the text and format it
    place_text = place.text.strip()
    number_text = number.text.strip()
    names_text = ' - '.join([name.strip() for name in names.text.strip().split(' - ')])
    rc_text = rc_info.text.strip()
    time_text = timing.text.strip()
    time_difference_text = time_difference.text.strip() 

    data.append([place_text, number_text, names_text, rc_text, time_text, time_difference_text])
    # Print the formatted output
    #print(f"{place_text}    {number_text}    {names_text}    {time_text}     {time_difference_text}")

# Create a pandas DataFrame
df = pd.DataFrame(data, columns=['Finishing Place', 'Driver Number', 'Driver-Co-Driver Names', 'RC Type', 'Finish Time', 'Time Difference'])

# Save the DataFrame to an Excel/CSV file
#df.to_excel('rally_results.xlsx', index=False)
df.to_csv('rally_results.csv', index=False)