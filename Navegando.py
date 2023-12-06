from selenium import webdriver # Para manejar la web
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
import time

#Opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = "C://Users//madar//Downloads//chromedriver-win64//chromedriver-win64//chromedriver.exe"

driver = webdriver.Chrome()
# Iniciarla en la pantalla 2
driver.set_window_position(2000,0)
driver.maximize_window()
time.sleep(1)

# Inicializamos el navegador
driver.get('https://www.eltiempo.es')