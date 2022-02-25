import time
import yagmail
import os
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
import os

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blank-features = AutomationControlled")

    #driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver = webdriver.Chrome(executable_path="/Users/ericowusujunior/PycharmProjects/BrowserAutomation/chromedriver")

    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")

    return driver

#This function extracts the stock value from a website
def extract_percentage(text):
    output = float(text.split(" ")[0])
    return output

#This function is to send the email
def send_mail(price):
    sender = "e.owusu89@gmail.com"
    receiver = "e.owusu@dal.ca"
    my_password = os.getenv("password")
    subject = "This is to notify you about a change in stock price"

    yag = yagmail.SMTP(user=sender, password=my_password)

    yag.send(to=receiver, subject=subject, contents= f"""The stock price is now {price}""")
    my_secret = os.environ['password']
    print("Email Sent!")

#This is the main function to call all other functions
def main():
  driver = get_driver()
  time.sleep(2)
  element = driver.find_element(by="xpath", value ="/html/body/div[2]/div/section[1]/div/div/div[2]/span[2]")
  time.sleep(2)


  #print (element.text())
  #driver.current_url()
  final = extract_percentage(element.text)
  if (final == -6.48):
    send_mail(final)





print(main())



