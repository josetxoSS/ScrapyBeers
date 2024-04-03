# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 18:28:21 2024

@author: miriam
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# URL de la página
url = 'https://www.goodreads.com/genres/biography'

# Realizar la solicitud GET
response = requests.get(url)

# Analizar el HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar los contenedores de los libros
book_containers = soup.find_all('div', class_='coverWrapper')
urls = []

# Iterar sobre los contenedores de libros
for container in book_containers:
    link = container.find('a')['href']
    urls.append('https://www.goodreads.com/' + str(link))

# Configurar el servicio de ChromeDriver
service = Service(r"C:\Users\miria\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# Iniciar el navegador Chrome
driver = webdriver.Chrome(service=service)

titulo = []
autor = []
fecha_pub = []
num_pag = []
precio = []
rating = []
num_ratings = []
num_reviews = []


for url in urls:    
    # Cargar la página
    driver.get(url)
    
    # Encontrar el elemento utilizando Selenium
    wait = WebDriverWait(driver, 10)
    
    # Título del libro
    titulo.append(driver.find_element(By.CSS_SELECTOR, 'h1.Text.Text__title1[data-testid="bookTitle"]').text.strip())
    
    # Autor
    autor.append(driver.find_element(By.CSS_SELECTOR, 'span[data-testid="name"]').text.strip())    

    # Año de publicación
    fecha_pub.append(driver.find_element(By.CSS_SELECTOR, 'p[data-testid="publicationInfo"]').text.strip()) 
    
    # Número de páginas
    num_pag.append(driver.find_element(By.CSS_SELECTOR, 'p[data-testid="pagesFormat"]').text.strip()) 
    
    # Precio
    try:
        element = driver.find_element(By.XPATH, '(//span[@class="Button__labelItem" and contains(text(), "Kindle")])[1]')
        texto = element.text.strip()
        precio.append(texto)
    except NoSuchElementException:
        # Si no se encuentra el elemento, asignar un valor vacío
        precio.append("Precio no disponible")
    
    # Rating
    rating.append(driver.find_element(By.CSS_SELECTOR, 'div.RatingStatistics__rating[aria-hidden="true"]').text.strip()) 
    
    # Número de ratings
    num_ratings.append(driver.find_element(By.CSS_SELECTOR, 'span[data-testid="ratingsCount"]').text.strip())
    
    # Número de reviews
    num_reviews.append(driver.find_element(By.CSS_SELECTOR, 'span[data-testid="reviewsCount"]').text.strip())
   

# Crear un diccionario con las listas
datos = {'Titulo': titulo, 'Autor': autor, 'Año de publicación': fecha_pub, 'Número de páginas': num_pag, 'Precio': precio, 'Rating': rating, 'Número Ratings': num_ratings, 'Número Reviews': num_reviews}

# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(datos)