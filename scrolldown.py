from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ScrapyBook:
    def __init__(self):
        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome()
        # Navigate to the Goodreads website
        self.driver.get("https://www.goodreads.com/")
        # Maximize the browser window
        self.driver.maximize_window()
        self.mail = "samisanchezlol@hotmail.com"
        self.password = "Password96"
        self.list_categories =  [
            "Art",
            "Biography",
            "Business",
            "Children's",
            "Christian",
            "Classics",
            "Comics",
            "Cookbooks",
            "Ebooks",
            "Fantasy",
            "Fiction",
            "Graphic Novels",
            "Historical Fiction",
            "History",
            "Horror",
            "Memoir",
            "Music",
            "Mystery",
            "Nonfiction",
            "Poetry",
            "Psychology",
            "Romance",
            "Science",
            "Science Fiction",
            "Self Help",
            "Sports",
            "Thriller",
            "Travel",
            "Young Adult"
        ]

    def fill_form(self, element, content, idStatus = True):
        if (idStatus):
            input = self.driver.find_element(By.ID,element )
        else :
            input = self.driver.find_element(By.CLASS_NAME,element )
        input.clear()
        input.send_keys(content)
        time.sleep(1)

    def click_element(self, element, idStatus = True):
        if (idStatus):
            input = self.driver.find_element(By.ID,element )
        else :
            input = self.driver.find_element(By.CLASS_NAME,element )
        input.click()
        time.sleep(2)

    def login(self):
        # Find the email input field and enter the email
        self.fill_form("ap_email",self.mail)
        # Find the password input field and enter the password
        self.fill_form("ap_password",self.password)
        # Click on the "Sign In" button
        self.click_element("signInSubmit")

    def click_sign_in_one(self):
        #----------------------------------------------------------- Special container , I can not use the method fill form
        # Find the "Already a member?" div element
        auth_switch_flow_div = self.driver.find_element(By.CLASS_NAME, "authSwitchFlow")
        # Find the "Sign In" link within the div
        sign_in_link = auth_switch_flow_div.find_element(By.CLASS_NAME, "gr-hyperlink")
        # Click on the "Sign In" link
        sign_in_link.click()
        time.sleep(2)
        #-----------------------------------------------------------
        # Find the "Sign in with email" button and click on it
        self.click_element("authPortalSignInButton",False)
    
    def search_books(self):
        # Fill the input with the category
        self.fill_form("searchBox__input","Art",False)
        # Find the search button by its class name and click it
        self.click_element("searchBox__icon--magnifyingGlass",False)
        # Extract url of the books
        link_elements = self.driver.find_element(By.XPATH,'//*[@id="bodycontainer"]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr//a')
        # Extract links from the elements
        print(link_elements)
        # Print the links
  
    
    def run(self):
        self.click_sign_in_one()
        self.login()
        time.sleep(2)
        self.search_books()

    def quit_driver(self):
        # Close the webdriver
        self.driver.quit()

# Create an instance of the ScrapyBook class
scrapy_book = ScrapyBook()

# Call the click_sign_in_one method
scrapy_book.run()

# Quit the webdriver
scrapy_book.quit_driver()


