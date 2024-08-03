import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

# Define the URL
URL = "https://portals.au.edu.pk/aumeritlist/ETS_View.aspx"

def get_form_fields():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    form_data = {
        '__VIEWSTATE': soup.find('input', {'id': '__VIEWSTATE'})['value'],
        '__VIEWSTATEGENERATOR': soup.find('input', {'id': '__VIEWSTATEGENERATOR'})['value'],
        '__EVENTVALIDATION': soup.find('input', {'id': '__EVENTVALIDATION'})['value']
    }
    return form_data

def fetch_student_results(admit_card_number, form_data):
    headers = {
        "Host": "portals.au.edu.pk",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
    }

    payload = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": form_data['__VIEWSTATE'],
        "__VIEWSTATEGENERATOR": form_data['__VIEWSTATEGENERATOR'],
        "__EVENTVALIDATION": form_data['__EVENTVALIDATION'],
        "ctl00$AUContent$txt_regid": str(admit_card_number),
        "__ASYNCPOST": "true",
        "ctl00$AUContent$btnShow": "Search Result"
    }

    response = requests.post(URL, headers=headers, data=payload)

    soup = BeautifulSoup(response.text, 'lxml')

    merit_info_div = soup.find('div', {'id': 'AUContent_div_meritinfo'})
    if merit_info_div:
        admit_card_no = merit_info_div.find('span', {'id': 'AUContent_lbl_admitcardno'}).text.strip()
        full_name = merit_info_div.find('span', {'id': 'AUContent_lbl_fullname'}).text.strip()
        program_name = merit_info_div.find('span', {'id': 'AUContent_lbl_programname'}).text.strip()
        aggregate_merit_score = merit_info_div.find('span', {'id': 'AUContent_lbl_meritscore'}).text.strip()

        return {
            'Admit Card Number': admit_card_no,
            'Full Name': full_name,
            '1st Preference': program_name,
            'Aggregate Merit Score': aggregate_merit_score
        }
    else:
        return None

def collect_merit_data(start, end):
    merit_list = []
    form_data = get_form_fields()

    with ThreadPoolExecutor(max_workers=32) as executor:
        future_to_admit_card = {executor.submit(fetch_student_results, admit_card_number, form_data): admit_card_number for admit_card_number in range(start, end + 1)}

        for future in as_completed(future_to_admit_card):
            admit_card_number = future_to_admit_card[future]
            try:
                result = future.result()
                if result:
                    merit_list.append(result)
                    print(f"Successfully found data for Admit Card Number: {admit_card_number}")
                else:
                    print(f"No data found for Admit Card Number: {admit_card_number}")
            except Exception as e:
                print(f"Error 404 fetching data for Admit Card Number: {admit_card_number} - {e}")

    return merit_list

merit_data = collect_merit_data(2400015, 2420300) #Admit cards range defined
df = pd.DataFrame(merit_data)
df.to_csv('merit_list.csv', index=False)

# group by 1st preference
grouped_df = df.groupby('1st Preference').apply(lambda x: x.reset_index(drop=True))
grouped_df.to_csv('grouped_merit_list.csv', index=False)

print("Saved Successfully.")
