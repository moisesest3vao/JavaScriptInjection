from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

#Here you can put the Url for target page
pageUrl = "https://www.google.com"
#Here you can put your JS Code
myscript = "console.log('working fine')"


def main():
  while(True):
    injectJSCode()

def injectJSCode():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1024x1400")
    chrome_driver = os.path.join(os.getcwd(), "C:\\phantomjs-2.1.1-windows\\bin\\chromedriver.exe")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

    driver.get(pageUrl)
    driver.execute_script(myscript);

    driver.get_screenshot_as_file("screenshot.png")
    driver.close()

if __name__ == '__main__' : main()