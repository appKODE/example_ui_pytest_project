from appium import webdriver
from time import sleep
from .page import MainPage
from .utils import get_recent_file, get_bundle, PATH
from .config import FULL_PATH, DESIRED_CAPS, APPIUM_HOST, DEFAULT_APP


class TestUM:
    def setup_class(self):
        recent_file = get_recent_file(FULL_PATH) or DEFAULT_APP  # получить имя самого нового файла в папке на
        # МАШИНЕ, откуда тесты запускаются: если не найден файл, то взять дефолтное имя apk (этот файл должен лежать
        # на СЕРВЕРЕ)
        path_with_file = FULL_PATH + recent_file
        desired_caps = DESIRED_CAPS
        desired_caps["app"] = PATH(path_with_file)
        self.bundle = get_bundle(recent_file)
        self.driver = webdriver.Remote(APPIUM_HOST, desired_caps)

    def teardown_class(self):
        self.driver.quit()

    def test_onboarding(self):
        main_page = MainPage(self.driver, self.bundle)
        sleep(6)
        main_page.click_onboarding()
        main_page.do_swipe_jesture()
