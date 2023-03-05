from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/100_Greatest_African_Americans"


def main() -> None:
    driver = webdriver.Chrome()
    driver.get(URL)
    page = driver.page_source

    soup = BeautifulSoup(page, "html.parser")
    div_tag = soup.find("div", class_="div-col")

    for item in div_tag.contents:
        print(item)

    driver.close()


if __name__ == '__main__':
    main()