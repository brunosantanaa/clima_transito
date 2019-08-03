# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlopen
import json

class ClimaTransito:
    def __init__(self, latitude, longitude):
        '''
            Argumentos
            ---------

            latitude: Latitude do local a ser analizado 
            longitude: Latitude do local a ser analizado
        '''
        self.latitude = latitude
        self.longitude = longitude
    def wazeScraping(self):
        ''' Recupera o nivel de congestionamento próximo ao local selecionado.

            Retorna
            -------
            severity: Numero de pontos congestionados por nível de congestionamento [1..4]

        '''
        driver = webdriver.Chrome()
        ac = ActionChains(driver)
        url = 'https://www.waze.com/pt-BR/livemap?zoom=17&lat={0:.6f}&lon={1:.6f}'.format(self.latitude, self.longitude)
        print(url)
        try:
            driver.get(url)
            severity = []
            for itens in range(1, 6):
                #sev = "//*[@class='wm-jam-layer__bg' and @class='wm-jam-layer__bg--level-{0}' and @class='leaflet-interactive']".format(itens)
                sev = ".wm-jam-layer__bg--level-{0}".format(itens)
                #sev = "div.leaflet-overlay-pane g path.jam.severity-{0}.leaflet-clickable.jam.severity-{0}".format(itens)
                severity.append(len(driver.find_elements_by_css_selector(sev)))
                #severity.append(len(driver.find_elements_by_class_name(sev)))
                #severity.append(len(driver.find_elements_by_xpath(sev)))
            return severity
        finally:
            driver.quit()
            
    def clima(self):
        api = '0376c266715d4bdcc96f19c6bd407f8a'
        la = self.latitude
        lo = self.longitude
        url = 'http://api.openweathermap.org/data/2.5/weather?lat={0:.6f}&lon={1:.6f}&APPID={2}&units=metric'.format(la, lo, api)
        with urlopen(url) as conn:
            clima = json.loads(conn.read().decode('utf-8'))
            return clima