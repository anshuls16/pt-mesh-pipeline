import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape data from the World Bank Evaluation and Ratings website
def scrape_world_bank_data():
    url = "https://ieg.worldbankgroup.org/data"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    tender_table = soup.find('table', {'class': 'views-table'})
    if tender_table:
        tbody = tender_table.find('tbody')
        rows = tbody.find_all('tr')
        
        data = []
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 3:
                tender_number = columns[0].text.strip()
                tender_title = columns[1].text.strip()
                tender_status = columns[2].text.strip()
                
                
                # Store the scraped data in a dictionary
                tender_data = {
                    'Tender Number': tender_number,
                    'Tender Title': tender_title,
                    'Tender Status': tender_status
                }
                
                data.append(tender_data)

        # Save the scraped data to a CSV file
        csv_filename = 'world_bank_tenders.csv'
        with open(csv_filename, 'w', newline='') as csv_file:
            fieldnames = ['Tender Number', 'Tender Title', 'Tender Status']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"Scraped World Bank data successfully. Saved to {csv_filename}")
    else:
        print("Unable to find tender data on the World Bank website.")


# Function to scrape data from the China Procurement Sources
def scrape_china_procurement_data():
    urls = [
        "https://www.chinabidding.com/en",
        "http://www.ggzy.gov.cn/",
        "http://en.chinabidding.mofcom.gov.cn/",
        "https://www.cpppc.org/en/PPPyd.jhtml",
        "https://www.cpppc.org:8082/inforpublic/homepage.html#/searchresult"
    ]
    
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Scraping logic for https://www.chinabidding.com/en
    if url == "https://www.chinabidding.com/en":
    tender_items = soup.find_all('div', {'class': 'chakan'})
    
    data = []
    for tender_item in tender_items:
        tender_title = tender_item.find('h1').text.strip()
        tender_details = tender_item.find('div', {'class': 'info'}).text.strip()
        
        # Store the scraped data in a dictionary
        tender_data = {
            'Tender Title': tender_title,
            'Tender Details': tender_details
        }
        
        data.append(tender_data)

    # Save the scraped data to a CSV file
    csv_filename = 'chinabidding_tenders.csv'
    with open(csv_filename, 'w', newline='') as csv_file:
        fieldnames = ['Tender Title', 'Tender Details']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Scraped chinabidding.com data successfully. Saved to {csv_filename}")


# Function to scrape data from the E-procurement Government of India website
def scrape_indian_govt_data():
    url = "https://etenders.gov.in/eprocure/app"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Function to scrape data from the E-procurement Government of India website
def scrape_indian_govt_data():
    url = "https://etenders.gov.in/eprocure/app"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    tender_table = soup.find('table', {'id': 'dataTable'})
    if tender_table:
        tbody = tender_table.find('tbody')
        rows = tbody.find_all('tr')

        data = []
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 3:
                tender_number = columns[0].text.strip()
                tender_title = columns[1].text.strip()
                tender_organization = columns[2].text.strip()

                # Store the scraped data in a dictionary
                tender_data = {
                    'Tender Number': tender_number,
                    'Tender Title': tender_title,
                    'Tender Organization': tender_organization
                }

                data.append(tender_data)

        # Save the scraped data to a CSV file
        csv_filename = 'indian_govt_tenders.csv'
        with open(csv_filename, 'w', newline='') as csv_file:
            fieldnames = ['Tender Number', 'Tender Title', 'Tender Organization']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"Scraped Indian government data successfully. Saved to {csv_filename}")
    else:
        print("Unable to find tender data on the Indian government website.")


# Main function to run the scraping process
def main():
    # Scrape data from the World Bank Evaluation and Ratings website
    scrape_world_bank_data()
    
    # Scrape data from the China Procurement Sources
    scrape_china_procurement_data()
    
    # Scrape data from the E-procurement Government of India website
    scrape_indian_govt_data()

if __name__ == '__main__':
    main()
