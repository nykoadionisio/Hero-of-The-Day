from bs4 import BeautifulSoup
from selenium import webdriver
import random

URL = "https://en.wikipedia.org/wiki/100_Greatest_African_Americans"


def main() -> None:
    driver = webdriver.Chrome()
    driver.get(URL)
    page = driver.page_source

    soup = BeautifulSoup(page, "html.parser")
    a = soup.select("div > ol > li > a")

    people = {}
    for link in a:
        name = link.get('title')
        href = link.get('href')

        if "(" in name:
            i = name.index('(')
            name = name[:i - 1]

        people[name] = href

    random_name = random.choice(list(people.keys()))

    driver.get('https://en.wikipedia.org' + people[random_name])
    person_page = driver.page_source
    person_soup = BeautifulSoup(person_page, "html.parser")
    paragraphs = person_soup.find_all('p')

    text = ''
    for p in paragraphs:
        text = text + p.text.strip()

    driver.close()

    return text


if __name__ == '__main__':
    main()
