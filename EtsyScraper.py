#import Dependencies
from bs4 import BeautifulSoup
import requests

url = 'https://www.kinga.sk/product/hercules-chess-set-drevena-sachovnica-28x28cm/'
response = requests.get(url) #request http Data at URL
soup=BeautifulSoup(response.content,'lxml') #parse the data with lxml data parser
#Find all containers in divs with classes named item-container that hold item objects and store them into a list
containers = soup.findAll("span", {"class":"woocommerce-Price-amount amount"})

print(soup)
print("-----------------------------------------------------------------------------------------------------------")
print("Search Term:\n"+'"'+soup.h1.text+'"\n') #print <h1> tag contents text
print("Items: ",len(containers)) #print length of container
print("-----------------------------------------------------------------------------------------------------------")


for container in containers:
	print(container.text)
	
