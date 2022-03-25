#This file will include a class with instance methods.
#That will be responsible to interact with our website.
#After we have some results, to apply filtrations.
from selenium.webdriver.remote.webdriver import WebDriver


class BookFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self):
        star_filtration_box = self.driver.find_element_by_css_selector(
            'div[data-filters-group="class"]'
        )
        star_child_elements = star_filtration_box.find_elements_by_ccs_selector('*')
        print(len(star_child_elements))
