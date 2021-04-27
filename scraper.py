from urllib.request import urlopen
# the urllib.request library function urlopen allows us to open up urls

from bs4 import BeautifulSoup
# let's install beautifulsoup4 for its ability to parse and grab html content from a page

url_to_scrape = "https://planetdesert.com/collections/cactus"
#url that we want to get information from

request_page = urlopen(url_to_scrape)
#urlopen function opens the url, we pass the url as an arguement into this function

page_html = request_page.read()
#we use the read function to get the html data from the page

request_page.close()
#Close it as we got everything we need from it

# you can add headers to identify as a browser for some websites like amazon

html_soup = BeautifulSoup(page_html, 'html.parser')
#BS4 now will load all the html into it's parser, lets save it into a var called html_soup

cactus_items = html_soup.find_all('div', class_="grid-product__content")
#this example is using cactus, so let's save all the different html elements of each cactus product into a variable
#called cactus_items. We will use BS4's inbuilt find_all function as we are scraping multiple items

filename = 'products.csv'
#lets create a file using python

f = open(filename, 'w')
#open that file and give python write permissions

headers = 'Title, Price \n'
#Since we are capturing two data points, lets create 2 column names
#title and price

f.write(headers) #writes headers
#Get python to write these headers on the top of the columns we are about to populate


for cactus in cactus_items:
#using a for loop, lets go through each of the different elements collected from the page
    title = cactus.find('div', class_='grid-product__title').text
    #everytime we see a div with a class grid-product__title lets grab it's text and save it into a var called title
    
    price = cactus.find('div', class_='grid-product__price').text
    #everytime we see a div with a class grid-product__price lets grab it's text and save it into a var called price

    f.write(title + ',' + price)
    #our CSV is comma seperated, to lets add each of the title and prices comma seperated
    #title of the product + , + price

f.close()
#close the file
