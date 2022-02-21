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

def extract_percentage(text):
    output = float(text.split(" ")[0])

def send_email(price):
    sender = os.getenv('EMAIL_SENDER')
    receiver = os.getenv('EMAIL_RECEIVER')

    subject = "The stock price is lower than -0.10%"


    contents = f"""
    The stock price is now {price}%
    """

    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")



def main():
  driver = get_driver()
  time.sleep(2)
  element = driver.find_element(by="xpath", value ="/html/body/div[2]/div/section[1]/div/div/div[2]/span[2]")
  time.sleep(2)
  #print (element.text())
  #driver.current_url()

  if (float(text) < -0.10):
      send_email(str(text))

  return extract_percentage(element.text)

print(main())



