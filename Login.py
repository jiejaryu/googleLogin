import requests
import http.cookiejar, urllib.request
from bs4 import BeautifulSoup

class Google:
    """docstring for Google"""
    def __init__(self, login, pwd):
        url_login = "https://accounts.google.com/ServiceLogin"
        url_auth = "https://accounts.google.com/ServiceLoginAuth"
        self.cookie = http.cookiejar.MozillaCookieJar()
        self.ses = requests.session()
        self.ses.cookies = self.cookie
        login_html = self.ses.get(url_login)
        soup_login = BeautifulSoup(login_html.content, "lxml").find('form').find_all('input')

        my_dict = {}
        for u in soup_login:
            if u.has_attr('value'):
                my_dict[u['name']] = u['value']

        my_dict['Email'] = login
        my_dict['Passwd'] = pwd
        self.ses.post(url_auth, data = my_dict)


    def get(self, URL, header = {}):
        return self.ses.get(URL, headers = header)


    def post(self, URL, payload, header = {}):
        return self.ses.post(URL, data = payload, headers = header)
    
Google ('', '') # your email and password



