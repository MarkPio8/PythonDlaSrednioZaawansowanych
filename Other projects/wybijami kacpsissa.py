from time import sleep
from selenium import webdriver


driver1  = webdriver.Chrome(executable_path=r"C:\Users\marek\OneDrive\Pulpit\chrome\chromedriver.exe")

driver1.get("https://www.youtube.com/watch?v=Pz345z0Bg3A")

while True:
    sleep(60)
    driver1.refresh()