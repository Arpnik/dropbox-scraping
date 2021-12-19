import time
from selenium import webdriver
from com.scrappy.PropertyConfig import getDriverPath


def login(driver, password):
    password_box = driver.find_elements_by_xpath("//input[@name='shared-link-password']")[0]
    password_box.send_keys(password)
    continue_span = driver.find_elements_by_xpath("//span[text()='Continue']")[0]
    continue_btn = continue_span.find_elements_by_xpath("..")[0]
    continue_btn.click()


def accept_cookies(driver):
    ##TODO change iframe to this and than accept accept cookie
    time.sleep(20)
    print("sleep over")
    iframe = driver.find_elements_by_xpath('//*[@id="consent-iframe"]');
    driver.switch_to.frame(iframe)
    accept_btn = driver.find_elements_by_xpath("//button[@id='_evidon-accept-button']")
    accept_btn.click()


def scroll_and_capture_images(driver):
    ##TODO scroll and capture screen shot for all pages
    return


def login_and_download(url, password):
    url = "https://www.dropbox.com/s/ip7i88vhiiy5wjo/Perio%202.pdf?dl=0"
    password = "furcation"
    driver = webdriver.Chrome(executable_path=getDriverPath())
    driver.maximize_window();
    driver.get(url)
    # accept_cookies(driver)
    login(driver, password)
    print("Scrolling 1")
    div = driver.find_element_by_xpath('//*[@id="fvsdk-mount-point"]/div/div/div[1]/div/article/div[2]');
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
