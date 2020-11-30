import mechanize;

browser = mechanize.Browser()

browser.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0')]



browser.open("http://192.168.0.1/login.html")

browser.select_form(FORM_NAME)
browser.form['USERNAME_FIELD'] = 'abc'
browser.form['PASSWORD_FIELD'] = 'password'
browser.submit()
print browser.response().read()
print browser.geturl()
