import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Ruta al chromedriver (ajusta la ruta según tu configuración)
chromedriver_path = r"C:\Users\PCarreño\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Abrir Twitter
driver.get("https://x.com/i/flow/login")

# Esperar a que la página cargue y el campo de nombre de usuario esté presente
wait = WebDriverWait(driver, 60)
username = wait.until(EC.presence_of_element_located((By.NAME, "text")))
username.send_keys("erickcarre8@gmail.com")  # COLOCA TU USUARIO AQUI
username.send_keys(Keys.RETURN)

# Esperar manualmente para resolver CAPTCHA u otras verificaciones
print("Por favor, resuelve el CAPTCHA o cualquier verificación adicional manualmente.")
time.sleep(40)  # Tiempo suficiente para resolver manualmente (ajustar según sea necesario)

# Esperar a que la página de la contraseña cargue
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys("SMITEeslalei1")  # TU CONTRASEÑA AQUI
password.send_keys(Keys.RETURN)

# Esperar a que el inicio de sesión complete
time.sleep(5)

# Esperar a que la barra de búsqueda esté presente
try:
    search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')))
    search_box.send_keys("Verdi Cevallos")  # MODIFICA EL TERMINO AQUI
    search_box.send_keys(Keys.RETURN)
except TimeoutException:
    print("No se encontró la barra de búsqueda.")
    driver.quit()
    exit()
except NoSuchElementException as e:
    print(f"Error al encontrar el elemento de búsqueda: {e}")
    driver.quit()
    exit()

# Esperar a que los resultados de la búsqueda carguen
try:
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="primaryColumn"]')))

    # Intentar imprimir el HTML de la página actual para depurar
    page_html = driver.page_source
    with open("page_source.html", "w", encoding="utf-8") as file:
        file.write(page_html)
    print("HTML de la página guardado en 'page_source.html'")

    # Hacer clic en "Latest" para obtener los tweets más recientes
    try:
        latest_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Latest" or text()="Más reciente"]')))
        latest_tab.click()
    except TimeoutException:
        print("No se encontró la pestaña 'Latest'.")
        driver.quit()
        exit()

    # Aumentar el tiempo de espera para la carga de tweets
    tweet_data = []
    scroll_pause_time = 2  # Tiempo de pausa entre desplazamientos
    tweets_collected = 0
    max_scroll_attempts = 50  # Limitar el número de intentos de desplazamiento
    scroll_attempts = 0
    last_height = driver.execute_script("return document.body.scrollHeight")

    while tweets_collected < 200 and scroll_attempts < max_scroll_attempts:
        try:
            # Recuperar los tweets
            tweets = driver.find_elements(By.XPATH, '//article[@role="article"]')
            for tweet in tweets[tweets_collected:]:
                try:
                    content = tweet.find_element(By.XPATH, './/div[@lang]').text.replace("\n", " ")
                    timestamp = tweet.find_element(By.XPATH, './/time').get_attribute("datetime")
                    username = tweet.find_element(By.XPATH, './/span[contains(text(), "@")]').text
                    tweet_data.append([username, timestamp, content])
                    tweets_collected += 1
                    if tweets_collected >= 200:
                        break
                except NoSuchElementException:
                    continue
            # Verificar si hay un mensaje de error en la página
            try:
                error_message = driver.find_element(By.XPATH, '//*[contains(text(), "ha ocurrido un error")]')
                if error_message:
                    print("Se detectó un error en la página de Twitter. Terminando la ejecución.")
                    break
            except NoSuchElementException:
                pass
            # Desplazarse hacia abajo para cargar más tweets
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)  # Esperar a que se carguen más tweets

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            scroll_attempts += 1
        except Exception as e:
            print(f"Error durante la carga de tweets: {e}")
            break

    # Guardar en un archivo CSV
    with open("tweets.csv", mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Timestamp", "Content"])
        writer.writerows(tweet_data)
    print("Información de tweets guardada en tweets.csv")

except TimeoutException:
    print("Tiempo de espera agotado. No se encontraron elementos de tweets después de la búsqueda.")

# Cerrar el navegador
driver.quit()
