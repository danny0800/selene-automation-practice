
#Успешный вход с валидными данными

from selene import browser, be, have

url = 'http://127.0.0.1:5500/pages/login.html' 

browser.open(url)
browser.element('#username').should(be.blank).type('testuser')
browser.element('#password').should(be.blank).type('password123')
browser.element('[name=remember]').click()
browser.element('[class=submit-btn]').click()

try: 
    browser.element('html').should(have.text('Успешный вход! Добро пожаловать, testuser!'))
    print('PASSED')

except:
    print('FAILED')


