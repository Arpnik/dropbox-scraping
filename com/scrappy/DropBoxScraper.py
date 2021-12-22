import time
from selenium import webdriver


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


def capture(driver, name):
    driver.maximize_window()
    driver.save_screenshot("C:\\Users\\USER\\Pictures\\Screenshots\\" + name + ".jpg")


def scroll_and_capture_images(driver):
    ##TODO add wait for loading elements
    # WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[starts-with(@class, 'pdfViewport_')]//ol//li[@data-index=0]")))
    current = 0
    prev = -1
    maxLi = int(driver.find_elements_by_xpath("//div[starts-with(@class, 'pdfViewport_')]//ol//li")[-1].get_attribute(
        "data-index"))
    while (current <= maxLi) or (prev > current):
        liElement = driver.find_element_by_xpath(
            "//div[starts-with(@class, 'pdfViewport_')]//ol//li[@data-index=" + str(current) + "]")
        driver.execute_script("arguments[0].scrollIntoView(true);", liElement)
        print(liElement.get_attribute("data-index"))
        capture(driver, liElement.get_attribute("data-index"))
        prev = current
        current += 1
        maxLi = int(driver.find_elements_by_xpath("//div[starts-with(@class, 'pdfViewport_')]//ol//li")[-1]
                    .get_attribute("data-index"))


def loginAndDownload(url, password):
    driver = initialise(url)
    acceptCookies(driver)
    login(driver, password)
    time.sleep(30)
    scroll_and_capture_images(driver)
    driver.quit()