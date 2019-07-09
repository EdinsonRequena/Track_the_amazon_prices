

import requests
from bs4 import BeautifulSoup
import smtplib
import time

#Link of the product you want to consult.
URL = 'https://www.amazon.es/Apple-MacBook-pulgadas-n%C3%BAcleos-generaci%C3%B3n/dp/B07S33G1WR/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=macbook+pro+15&qid=1562453325&s=gateway&sr=8-3'

#Place your user agent right after "User-Agent": you can know your user agent searching in google "my user agent"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

def check_price():
	"""this function checks the name, price of the product and activates the send_mail function if necessary"""
	
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	converted_price = float(price[0:5])

	#put the price with which you want to send an email just after converted_price <
	if converted_price < 2.500:
		send_mail()

	print(converted_price,"euros")
	print(title.strip())


def send_mail():
	"""make the process to send the mail."""
	
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	#Put the gmail account that will send you the email and your password. Gmail account that WILL SEND the mail, remember that
	server.login("user_will_send_the_mail@gmail.com", "password")

	subject = "Price fell down!!"
	body = "Check the amazon link right know!!\n https://www.amazon.es/Apple-MacBook-pulgadas-n%C3%BAcleos-generaci%C3%B3n/dp/B07S33G1WR/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=macbook+pro+15&qid=1562453325&s=gateway&sr=8-3"

	msg = f"Subject: {subject}\n\n{body}"

	#The first argument of server.sendmail () will be the gmail account that will send the mail, the second argument will be the email account that will receive the mail
	server.sendmail("user_will_send_the_mail@gmail.com","user_will_receive_the_mail@gmail.com",msg)
	print("THE EMAIL WAS SENT WITH SUCCESS!!")

	server.quit()

while(True):
	check_price()
	time.sleep(60*60)