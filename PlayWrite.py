# Selenium is a pain, Im switching to PlayWright
from playwright.sync_api import sync_playwright

dnsLookup = input("")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://viewdns.info/')
    page.fill('input[type="text"]', input)
    page.click('button[type=submit]')
