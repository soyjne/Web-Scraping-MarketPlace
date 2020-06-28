from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(r"C:\Users\soyjne\Downloads\chromedriver_win32\chromedriver.exe", chrome_options=options)


products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product



for x in range(1, 10):
    driver.set_page_load_timeout(20)
    driver.get("https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&marketplace=FLIPKART&page=" + str(x))

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
        name=a.find('div', attrs={'class':'_3wU53n'})
        price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
        products.append(name.text)
        prices.append(price.text) 



print(products)

df = pd.DataFrame({'Product Name':products,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')


driver.quit()

