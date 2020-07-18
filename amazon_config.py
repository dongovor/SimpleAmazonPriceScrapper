from selenium import webdriver
import platform

DIRECTORY = 'reports'
NAME = 'PS4'
CURRENCY = '€'
MIN_PRICE = '275'
MAX_PRICE = '650'
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = 'http://www.amazon.de/'

def get_chrome_webdriver(options):
    if 'Windows' in platform.system():
        return webdriver.Chrome('./chromedriver_83win', chrome_options=options)
    elif 'Linux' in platform.system():
        return webdriver.Chrome('./chromedriver_83linux', chrome_options=options)
    elif 'Darwin' in platform.system():
        return webdriver.Chrome('./chromedriver_83mac', chrome_options=options)

def get_chrome_webdriver_options():
    return webdriver.ChromeOptions()

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')

def set_browser_headless(options):
    options.add_argument('--headless')

