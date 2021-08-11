import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(3)
    try:
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket")))
        button = True
    except Exception:
        button = False
    assert button, 'Button not finded.'