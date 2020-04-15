import requests
import pandas as pd
from bs4 import BeautifulSoup

def access_XML_API(API_number = "07EWHs1EmV98ZN6NuZmMYo2KcS0nh5IPx"):


    URL = f'https://api.findmespot.com/spot-main-web/consumer/rest-api/2.0/public/feed/{API_number}/message.xml'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    messages = soup.find_all('message')

    MessengerName =[]
    latitude =[]
    longitude = []
    unixtime = []

    for i in messages:
        MessengerName.append(i.find('messengername').string.strip())
        latitude.append(i.find('latitude').string.strip())
        longitude.append(i.find('longitude').string.strip())
        unixtime.append(i.find('unixtime').string.strip())

    locationdf = pd.DataFrame({'MessengerName':pd.Series(MessengerName),
                               'Latitude':pd.Series(latitude),
                               'Longitude':pd.Series(longitude),
                               'Unixtime':pd.Series(unixtime)
    })

    return locationdf


#TODO make a visual representation of this data that may or may not be interactive

if __name__ == "__main__":

    access_XML_API()




















    # login_url = 'https://login.findmespot.com/spot-main-web/auth/login.html'
    # URL = f'https://api.findmespot.com/spot-main-web/consumer/rest-api/2.0/{API_number}/message.xml'
    # data = {
    #     'uiFrmLogin: uiFrmLogin'
    #     'j_username': 'JAYBARLOW33',
    #     'j_password': '3Spot99-1'
    # }
    #
    # with requests.Session() as s:
    #     site = s.get('https://login.findmespot.com/spot-main-web/auth/login.html')
    #     content = BeautifulSoup(site.content, "html.parser")
    #     token_1 = content.find("input", {"name":"j_idt111"})["value"]
    #     token_2 = content.find("input", {"name": "javax.faces.ViewState"})["value"]
    #     print(content)
    #     data = {
    #         'uiFrmLogin': 'uiFrmLogin',
    #         'j_idt111': token_1,
    #         'j_username': 'JAYBARLOW33',
    #         'j_password': '3Spot99-1',
    #         'login':'Login',
    #         'javax.faces.ViewState':token_2
    #     }
    #     s.post(login_url, data)
    #     index_page = s.get(URL)
    #     soup = BeautifulSoup(index_page.text, 'html.parser')
    #     print(soup.title)