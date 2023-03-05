from bs4 import BeautifulSoup
from selenium import webdriver
import random

URL = "https://en.wikipedia.org/wiki/100_Greatest_African_Americans"


def scrape() -> list:
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

    # print(person_soup)
    # print('\n')

    text = ''
    for p in paragraphs:
        text = text + p.text.strip()
        text = text.replace("negro", "")

    text = text[:2048]

    # just to initialize img_address
    img_address = (person_soup.find_all('img')[4]).get('alt')
    images = (person_soup.find_all('img'))[:8]

    count = 0
    for i in images:
        # find first img of person
        if random_name in i.get('alt'):
            img_address = (i.get('src'))
            break
        count += 1

    img_address = img_address.replace(" ", "_")

    # print(img_address)
    # print('https:' + img_address)

    driver.close()

    # person_arr = [text, 'https://en.wikipedia.org/wiki/File:' + img_address,
    #               'https://en.wikipedia.org' + people[random_name]]
    person_arr = [text, 'https:' + img_address,
                  'https://en.wikipedia.org' + people[random_name]]

    # person_arr: [text, img address, link to wiki page]
    print(person_arr)
    return person_arr


if __name__ == '__main__':
    scrape()
