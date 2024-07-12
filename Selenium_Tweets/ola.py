#Codigo funcional hasta la parte de buscar tweets

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

# Ruta al chromedriver (ajusta la ruta según tu configuración)
chromedriver_path = r"C:\Users\Erick Carreño\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Abrir Twitter
driver.get("https://x.com/i/flow/login")

# Esperar a que la página cargue y el campo de nombre de usuario esté presente
wait = WebDriverWait(driver, 30)
username = wait.until(EC.presence_of_element_located((By.NAME, "text")))
username.send_keys("erickcarre8@gmail.com")
username.send_keys(Keys.RETURN)

# Esperar manualmente para resolver CAPTCHA u otras verificaciones
print("Por favor, resuelve el CAPTCHA o cualquier verificación adicional manualmente.")
time.sleep(40)  # Tiempo suficiente para resolver manualmente (ajustar según sea necesario)

# Esperar a que la página de la contraseña cargue
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys("SMITEeslalei1")
password.send_keys(Keys.RETURN)

# Esperar a que el inicio de sesión complete
time.sleep(5)

# Buscar un término
search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Search query"]')))
search_box.send_keys("Python")
search_box.send_keys(Keys.RETURN)

# Aumentar el tiempo de espera para la carga de tweets
try:
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweet"]')))
    # Recuperar los tweets
    tweets = driver.find_elements(By.XPATH, '//div[@data-testid="tweet"]')
    
    if not tweets:
        print("No se encontraron elementos de tweets después de la búsqueda.")
    else:
        # Imprimir el texto de los primeros 5 tweets
        for tweet in tweets[:5]:
            print(tweet.text)
        
except TimeoutException:
    print("Tiempo de espera agotado. No se encontraron elementos de tweets después de la búsqueda.")

# Cerrar el navegador
driver.quit()