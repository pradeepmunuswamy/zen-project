from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl


class GuviZenAutomation:
    def __init__(self, username, password):
        self.username = prdeemunuswamy@gmail.com
        self.password = Nopassword@26
        self.driver = webdriver.Firefox()

    def login(self):
        """
        This method logs into the https://www.zenclass.in website using the provided username and password
        """
        self.driver.get("https://www.zenclass.in/")
        self.driver.find_element_by_xpath("//a[@href='/users/sign_in']").click()
        self.driver.find_element_by_id("user_email").send_keys(self.username)
        self.driver.find_element_by_id("user_password").send_keys(self.password)
        self.driver.find_element_by_name("commit").click()

    def get_left_side_ribbon_info(self):
        """
        This method returns a list of all the information present on the left side ribbon of the Guvi Zen portal
        """
        # code to get information from the left side ribbon of the Guvi Zen portal
        # and store it in a list
        return info

    def raise_queries(self):
        """
        This method raises 5 queries in the query section of the Guvi Zen portal
        """
        # code to navigate to the query section and raise 5 queries with the specified heading and body

    def write_to_excel(self, info):
        """
        This method writes the given information to an Excel file
        """
        # code to create an Excel file and write the information to it

    def close(self):
        """
        This method closes the webdriver instance
        """
        self.driver.close()

    def run(self):
        self.login()
        info = self.get_left_side_ribbon_info()
        self.raise_queries()
        self.write_to_excel(info)
        self.close()


if __name__ == "__main__":
    automation = GuviZenAutomation("your_username", "your_password")
    automation.run()
