from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

websites = [
    ("Google", "https://www.google.com", (By.NAME,"q")),
    ("DuckDuckGo","https://duckduckgo.com",(By.NAME,"q")),
    ("Bing","https://www.bing.com",(By.NAME,"q")),
    ("Yahoo","https://search.yahoo.com",(By.NAME,"p")),
    ("Yandex","https://yandex.com",(By.NAME,"text"))
]

queries = [
    "Python Tutorial",
    "Web Scraping",
    "Web Design",
    "Python OOP"
]