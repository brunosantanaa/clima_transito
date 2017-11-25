from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class data:
    def __init__(self):
        pass
    def wazeScraping(self, latitude, longitude):
        ''' Recupera o nível de congestionamento próximo ao local selecionado.

            Argumentos
            ---------

            latitude: Latitude do local a ser analizado 
            longitude: Latitude do local a ser analizado

            Retorna
            -------
            severity: Número de pontos congestionados por nível de congestionamento [1..4]

        '''
        driver = webdriver.Chrome()
        ac = ActionChains(driver)
        url = 'https://www.waze.com/pt-BR/livemap?zoom=17&lat={0:.6f}&lon={1:.6f}'.format(latitude, longitude)
        print(url)
        try:
            driver.get(url)
            severity = []
            for itens in range(1, 5):
                sev = "div.leaflet-overlay-pane g path.jam.severity-{0}.leaflet-clickable.jam.severity-{0}".format(itens)
                severity.append(len(driver.find_elements_by_css_selector(sev)))
            return severity
        finally:
            driver.quit()