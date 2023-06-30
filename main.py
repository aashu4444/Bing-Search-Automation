import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search_query(text_box_name, search_button_id, driver):
    query_url = "https://hipsum.co/api/?type=hipster-centric&sentences=1"
    query = requests.get(query_url).json()[0]

    # Find the search box and click on the search button to search
    text_box = driver.find_element(by=By.NAME, value=text_box_name)
    submit_button = driver.find_element(by=By.ID, value=search_button_id)

    text_box.clear()
    text_box.send_keys(query)
    driver.implicitly_wait(0.7)
    submit_button.click()



# Define how many times you want to search
lifecycle = 120

wait = 1

if __name__ == "__main__":
    print("Opening web browser...")
    # Select browser
    driver = webdriver.Edge()


    # Open the webpage of Bing
    driver.get("https://bing.com")
    driver.implicitly_wait(wait)


    print("browser opened. Waiting for correct time to run")
    while True:
        print("Automation started...")


        

        for i in range(1, lifecycle):
            time.sleep(5)
            if i == 1:
                # Find the search box and click on the search button to search
                search_query('q', 'search_icon', driver)

                driver.implicitly_wait(wait)

            else:
                time.sleep(15)
                # Again search another query from the results page
                search_query('q', "sb_form_go", driver)
                driver.implicitly_wait(wait)
