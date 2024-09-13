from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Inicializar Faker para generar datos aleatorios
fake = Faker()

# Configuración del WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar en modo headless (sin GUI)

def submit_form(url):
    # Usar webdriver-manager para configurar ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Configura WebDriverWait
    wait = WebDriverWait(driver, 10)

    try:
        # Navegar al dominio
        driver.get(url)

        # Rellenar el formulario con datos aleatorios
        full_name = fake.name()
        email = f"{fake.user_name()}@stopfuckkingspamming.com.net"  # Establecer dominio fijo
        domain = "com.net"  # Establecer dominio fijo

        # Mostrar los valores generados
        print(f"Generated Full Name: {full_name}")
        print(f"Generated Email: {email}")
        print(f"Generated Domain: {domain}")

        # Esperar a que los campos sean visibles
        print("Waiting for full name field...")
        full_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "full_name")))
        print("Full name field found!")

        print("Waiting for email field...")
        email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        print("Email field found!")

        print("Waiting for domain field...")
        domain_field = wait.until(EC.visibility_of_element_located((By.NAME, "domain")))
        print("Domain field found!")

        # Encuentra y rellena los campos del formulario
        full_name_field.send_keys(full_name)
        email_field.send_keys(email)
        domain_field.send_keys(domain)

        # Envía el formulario
        print("Waiting for submit button...")
        submit_button = wait.until(EC.element_to_be_clickable((By.NAME, "submit")))
        submit_button.click()

        # Esperar la redirección a /submit.php
        wait.until(EC.url_contains('/submit.php'))

        print("Sent")

    finally:
        # Cierra el navegador al final
        driver.quit()

def main():
    url = 'https://x.com'  # Reemplaza con la URL de tu formulario
    num_threads = 5  # Número de hilos a usar
    interval = 10  # Intervalo en segundos entre cada ejecución del bucle

    while True:
        # Crear un ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(submit_form, url) for _ in range(num_threads)]
            
            # Esperar a que todos los hilos terminen
            for future in as_completed(futures):
                future.result()

        # Esperar un intervalo antes de reiniciar el proceso
        print(f"Waiting for {interval} seconds before restarting...")
        time.sleep(interval)

if __name__ == "__main__":
    main()
