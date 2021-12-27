import bs4
import requests
from selenium import webdriver
import random, string, time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


while True:
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    em_f_n = "".join(random.choices(string.ascii_letters, k=15))
    pw_f_n = "".join(random.choices(string.ascii_letters + string.digits, k=15))
    driver.get("https://proxy.webshare.io/register/")

    driver.find_element_by_name("email").send_keys(f"{em_f_n}@gmail.com")
    driver.find_element_by_name("password1").send_keys(pw_f_n)
    driver.find_element_by_class_name("btn").click()
    input("Complete captcha and then press enter.")
    driver.get("https://proxy.webshare.io/proxy/list?")
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="page-wrapper"]/div[2]/div/div[5]/div/div[1]/div[1]/div/button'
    ).click()
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for link in soup.find_all("a", class_="btn btn-primary"):
        link = link.get("href")
        if "proxy.webshare.io" in link:
            r = requests.get(link)
            prox = r.text.replace("\n", "")
            prox = prox.strip()
            with open("proxys.txt", "a") as f:
                f.write(prox + "\n")
    driver.close()
