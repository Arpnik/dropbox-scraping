import time
from selenium import webdriver

# from com.scrappy.PropertyConfig import getDriverPath


def initialise(url):
    # driverPath = getDriverPath()
    driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\Documents\\dropbox-scraping\\chromedriver.exe")
    driver.maximize_window()
    driver.get(url)
    return driver


def login(driver, password):
    passwordBox = driver.find_elements_by_xpath("//input[@name='shared-link-password']")[0]
    passwordBox.send_keys(password)
    continueSpan = driver.find_elements_by_xpath("//span[text()='Continue']")[0]
    continueBtn = continueSpan.find_elements_by_xpath("..")[0]
    continueBtn.click()


def acceptCookies(driver):
    iframe = driver.find_element_by_xpath('//*[@id="consent-iframe"]')
    driver.switch_to.frame(iframe)
    acceptBtn = driver.find_element_by_xpath("//button[@id='_evidon-accept-button']")
    acceptBtn.click()
    driver.switch_to.default_content()


def scroll_and_capture_images(driver):
    ##TODO scroll and capture screen shot for all pages
    return


def loginAndDownload(url, password):
    url = "https://www.dropbox.com/s/ip7i88vhiiy5wjo/Perio%202.pdf?dl=0"
    password = "furcation"
    driver = initialise(url)
    acceptCookies(driver)
    login(driver, password)
    div = driver.find_element_by_xpath('//*[@id="fvsdk-mount-point"]/div/div/div[1]/div/article/div[2]')
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', div)
    # print("Scrolling 2")
    # div = driver.find_element_by_tag_name("ol").find_element_by_xpath("..")
    # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", div)
    # print("Scrolling 3")
    # div = driver.find_element_by_tag_name("ol").find_element_by_xpath("..").find_element_by_xpath("..")
    # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", div)
    # print("done")
    time.sleep(105)
    driver.close()
