import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurer le WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Accéder à la page web
url = 'https://www.manomano.fr/recherche/produit+jardin?referer_id=688173&msclkid=e425ba3d961f14207b59dd24a2142cdb&utm_source=bing&utm_medium=cpc&utm_campaign=SEM%20Bing_CPC_FR_B2C_Search_DSA%20-%20Search%20Pages&utm_term=2904&utm_content=2904%20-%20Hivernage%20de%20piscine'
driver.get(url)

try:
    # Attendre que les éléments contenant les prix soient chargés
    prices = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[itemprop="price"]'))
    )

    # Créer ou ouvrir un fichier CSV pour écrire
    with open('manomano_prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['OuterHTML'])  # Écrire l'en-tête du fichier CSV

        # Parcourir les prix récupérés et les écrire dans le fichier
        for price in prices:
            outer_html = price.get_attribute('outerHTML')  # Récupérer l'outerHTML
            writer.writerow([outer_html])  # Écrire l'outerHTML dans une nouvelle ligne

    print("Les outerHTML des prix ont été enregistrés dans manomano_prices.csv")

except Exception as e:
    print(f"Une erreur est survenue : {e}")

finally:
    # Fermer le navigateur
    driver.quit()
