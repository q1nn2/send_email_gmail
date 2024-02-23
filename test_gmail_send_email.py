import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestGmailSendEmail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.gmail.com")

    def test_send_email(self):
        # Enter your email and password
        email = "your_email@gmail.com"
        password = "your_password"

        # Log in to your mailbox
        self.driver.find_element_by_id("identifierId").send_keys(email)
        self.driver.find_element_by_id("identifierId").send_keys(Keys.ENTER)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("password").send_keys(Keys.ENTER)

        # Click on the "Write" button
        self.driver.find_element_by_css_selector(".T-I-KE").click()

        # Enter the recipient's address, subject and text of the letter
        to_field = self.driver.find_element_by_name("to")
        to_field.send_keys("recipient@example.com")

        subject_field = self.driver.find_element_by_name("subjectbox")
        subject_field.send_keys("Тестовое письмо")

        body_field = self.driver.find_element_by_css_selector(".Am.Al.editable.LW-avf")
        body_field.send_keys("Привет, это тестовое письмо.")

        # Click on the "Send" button
        self.driver.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.v7.T-I-atl.L3").click()

        # Check that the email was sent successfully (you can add other checks)
        self.assertTrue("Message sent" in self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
