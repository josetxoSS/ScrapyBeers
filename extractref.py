from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def extract_links():
    try:
        driver = webdriver.Chrome()
        # Navigate to the Goodreads website
        driver.get("https://www.goodreads.com/search?q=art&qid=nEDCIrTHUI")
        time.sleep(1)
        unique_links = set()
        try:
            for i in range(1, 10):
                # Find link elements
                link_xpath = f'//*[@id="bodycontainer"]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[{i}]/td[2]/a'
                link_elements = driver.find_elements(By.XPATH, link_xpath)
                
                # Iterate over each link element and extract href attribute
                for link_element in link_elements:
                    link = link_element.get_attribute('href')
                    yield link
            
        except NoSuchElementException:
            print("Link elements not found.")
        
        finally:
            time.sleep(3)  # Waiting for a while before closing the browser

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Quit the browser
        driver.quit()

links = extract_links()
for link in links:
    print(link)
