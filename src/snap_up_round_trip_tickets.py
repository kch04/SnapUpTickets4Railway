from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'

url = 'http://railway.hinet.net/Foreign/TW/etkind_roundtrip.html'

def book_tickets(browser):
    try:
        browser.get(url)

        elem_person_id = browser.find_element_by_id('person_id')
        elem_person_id.send_keys('Your ID Number')

        # 抓取下拉選單元件
        select = Select(browser.find_element_by_name('from_station'))
        select.select_by_value('100') # 台北

        select = Select(browser.find_element_by_name('to_station'))
        select.select_by_value('004') # 台東

        # 去程
        select = Select(browser.find_element_by_name('getin_date'))
        select.select_by_visible_text('2019/03/19【二】') # 去程 乘車日期

        select = Select(browser.find_element_by_name('train_type'))
        select.select_by_value('*4') # 車種 全部車種

        select = Select(browser.find_element_by_name('getin_start_dtime'))
        select.select_by_visible_text('08:00') # 起始時間

        select = Select(browser.find_element_by_name('getin_end_dtime'))
        select.select_by_visible_text('14:00') # 截止時間

        select = Select(browser.find_element_by_name('order_qty_str'))
        select.select_by_visible_text('1') # 訂票張數

        # 回程
        select = Select(browser.find_element_by_name('getin_date2'))
        select.select_by_visible_text('2019/03/19【二】') # 回程 乘車日期

        select = Select(browser.find_element_by_name('train_type2'))
        select.select_by_value('*4') # 車種 全部車種

        select = Select(browser.find_element_by_name('getin_start_dtime2'))
        select.select_by_visible_text('16:00') # 起始時間

        select = Select(browser.find_element_by_name('getin_end_dtime2'))
        select.select_by_visible_text('22:00') # 截止時間

        select = Select(browser.find_element_by_name('order_qty_str2'))
        select.select_by_visible_text('1') # 訂票張數

        # 點擊 開始訂票
        browser.find_element_by_css_selector('.btn.btn-primary').click()

        element = browser.find_element_by_id('idRandomPic')
        left = element.location['x']
        right = element.location['x'] + element.size['width']
        top = element.location['y']
        bottom = element.location['y'] + element.size['height']

        """
        # Save captcha
        from PIL import Image
        browser.save_screenshot('screenshot.jpg')
        img = Image.open('screenshot.jpg')
        img = img.crop((left, top, right, bottom))
        img = img.convert('RGBA')

        r, g, b, a = img.split()
        img = Image.merge("RGB", (r, g, b))
        img.save('captcha.jpg')
        
        # break the captcha
        # [TODO]
        """

        return 0 # success
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
        return -1 # fail

if __name__ == '__main__':
    res = -1
    count = 0

    browser = webdriver.Chrome(chrome_path)

    # 最大化顯示
    browser.maximize_window()

    while res != 0 and count < 30:
        res = book_tickets(browser)
        count = count + 1
        time.sleep(2)

    #browser.quit()
