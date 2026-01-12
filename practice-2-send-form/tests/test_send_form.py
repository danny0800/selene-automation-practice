from selene import browser, have, be 

def test_fill_form():
    browser.open('/') #Открыть браузер по умолчанию
    browser.element('#step1-name').should(be.blank).type('Daniil')
    browser.element('#step1-email').should(be.blank).type('simple@gmail.com')
    browser.element('#step1-phone').should(be.blank).type('+7 900 000 00 00')
    browser.element('#form-next-btn').hover().click()
    browser.element('#form-next-btn').click()
    browser.element('#step3-terms').click()
    browser.element('#form-submit-btn').click()
    browser.element('html').should(have.text('Форма успешно отправлена!'))