#import Dependencies
from bs4 import BeautifulSoup
import requests

url = 'https://www.etsy.com/search?q=knitted+Toe&explicit=1&order=price_desc'
response = requests.get(url) #request http Data at URL
soup=BeautifulSoup(response.content,'lxml') #parse the data with lxml data parser
#Find all containers in divs with classes named item-container that hold item objects and store them into a list
containers = soup.findAll("div", {"class":"js-merch-stash-check-listing"})

print("-----------------------------------------------------------------------------------------------------------")
print("Search Term:\n"+'"'+soup.h1.text+'"\n') #print <h1> tag contents text
print("Items: ",len(containers)) #print length of container
print("-----------------------------------------------------------------------------------------------------------")

#print(containers[0].a)
container=containers[0]

#CSV data input methods
filename = "EtsyProducts.csv"
f = open(filename,"w")
headers = "Brand, Product Name, Cost, Product Page\n"
f.write(headers)

for container in containers:
	brand_container = container.findAll("div", {"class":"v2-listing-card__shop"})
	brand = brand_container[0].p.text  #Call subclasses of container object 
	cost_container= container.findAll("span", {"class":"currency-value"})
	cost= cost_container[0].text
	product_name = container.a.h3.text.strip()
		
	urlContainer = container.find('a', href=True)
	productPage = urlContainer['href']
		
	print('===========================================================================================================')
	print("Brand: "+brand)
	print("Name: "+product_name)
	print("Price: "+cost+"\n")
	print("URL: "+productPage.strip());
	#sleep(randint(3,10))
	
	f.write(brand + "," + product_name.replace(",","|") + "," + cost + "," + productPage + "\n")
		
f.close() #Close CSV
	