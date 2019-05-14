import time
from selenium import webdriver
from datetime import datetime

name = "shokumosuke9th@gmail.com"
passe = ""
options = webdriver.ChromeOptions()


#options.add_argument('--headless')
def main_function():
    import time
    from selenium import webdriver
    from datetime import datetime
    print("open")
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com/')
    print("now opening")
    time.sleep(5)
    print("started login")
    #ログイン
    driver.find_element_by_xpath("//*[@id='gbwa']/div[1]/a").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='gb192']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div/a").click()
    time.sleep(5)
    loginput = driver.find_element_by_id("identifierId")
    loginput.send_keys(name)
    driver.find_element_by_id("identifierNext").click()
    #loginput.submit()
    time.sleep(5)
    loginput2 = driver.find_element_by_name("password")
    loginput2.send_keys(passer)
    time.sleep(5)
    driver.find_element_by_id("passwordNext").click()
    #loginput2.submit()
    time.sleep(10)
    print("login end...")
    print("show googlemap")
    #Googlemapの表示
    driver.get('https://www.google.com/')
    time.sleep(5)
    search_box = driver.find_element_by_name("q")
    search_box.send_keys('googlemap')
    search_box.submit()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div/div[1]/a").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='omnibox-singlebox']/div[1]/div[1]/button").click()
    #driver.find_element_by_class_name("searchbox_hamburger").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='settings']/div/div[2]/div/ul[3]/li[2]/button").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[4]/div[1]/button[1]").click()
    time.sleep(10)
    driver.maximize_window()
    time.sleep(3)
    file_name =datetime.now().strftime("imaage/%Y%m%d_%H%M%S_google.png") 
    driver.save_screenshot(file_name)
    #"images/"+datetime.now().strftime("%Y/%m/%d_%H:%M:%S_google.png"))
    print("shoted!!")
    driver.quit()
    #time.sleep(5)
    #driver.save_screenshot('search_results.png')
    #driver.quit()

#before = 0
while True:
    #time_str = datetime.now().strftime("%Y %m %d %H %M").split(" ")
    #time_int = [int(n) for n in time_str]
    #times = (time_int[2]*24+time_int[3])*60+time_int[4]
    #if (times - before) > 10:
    #before = times
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    main_function()
    time.sleep(600)
