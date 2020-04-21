from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import sys

class scrapper:

    def __os_detect(self):
        os = None
        if sys.platform.startswith('linux'):
            os = "linux"

        elif sys.platform.startswith('win32'):
            os = "win32"

        elif sys.platform.startswith('darwin'):
            os = "darwin"

        return os


    def __browser(self):
        os_detected = self.__os_detect()
        if os_detected:
            options = Options()
            options.headless = True
            profile = webdriver.FirefoxProfile()
            profile.set_preference('intl.accept_languages', 'en-US, en')
            path = "./geckodriver/" + os_detected
            browser = webdriver.Firefox(firefox_profile=profile, options=options, executable_path= path)
            return browser

        else:
            print("ERROR: type of operating system not detected")
	
    def __browser_quit(self, browser):
        browser.quit()
	
    def find_elements_by_tag_name(self, url, tag):
        ''' Get all headings in url page '''

        browser = self.__browser()
        browser.get(url)
        elements = browser.find_elements_by_tag_name(tag)

        self.__browser_quit(browser)
        for ele in elements:
            print("element " + str(ele))

        #return elements

if __name__ == "__main__":
    pass
	
