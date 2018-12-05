from .locators import MainPageLocators


class BasePage(object):

    def __init__(self, driver, bundle):
        self.driver = driver
        self.bundle = bundle

    def do_swipe_jesture(self):
        size = self.driver.get_window_size()
        startx, starty = int(size['width']) * 0.8, int(size['height']) * 0.5
        endx, endy = int(size['width']) * 0.2, int(size['height']) * 0.5
        self.driver.swipe(startx, starty, endx, endy, 300)


class MainPage(BasePage):

    def click_onboarding(self):
        MainPageLocators.ONBOARDING_PAGE[1].format(self.bundle)
        element = self.driver.find_element(
            *MainPageLocators.ONBOARDING_PAGE
        )
        element.click()


class CheckinPage(BasePage):
    pass
