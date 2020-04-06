from celery import shared_task
from selenium import webdriver


@shared_task
def ExecGoogleDirectionTask(departure, destination, mode):
    # 爬取頁面網址
    url = 'http://127.0.0.1:8080/googleMapAPI.html?Departure=' + departure + '&Destination=' + destination + '&Mode=' + mode
    # 目標元素的xpath
    # xpath = '//div[@id="imgid"]/ul/li/a/img'
    xpath = "//a[@id='id1']"
    # 啟動chrome瀏覽器
    chromeDriver = './chromedriver'  # chromedriver檔案放的位置
    driver = webdriver.Chrome(chromeDriver)
    result = None
    # 最大化窗口，因為每一次爬取只能看到視窗内的圖片
    driver.maximize_window()
    # 瀏覽器打開爬取頁面
    driver.get(url)
    for element in driver.find_elements_by_xpath(xpath):
        result = element.text
    # import time
    # time.sleep(1)
    driver.close()
    return result
