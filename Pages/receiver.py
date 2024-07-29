import os
import re
import imaplib
import email
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.test import WebsiteTester


class EmailReceiver:
    def __init__(self, initial_url, maildrop_url):
        self.initial_url = initial_url
        self.maildrop_url = maildrop_url
        self.driver = webdriver.Safari()
        self.website_tester = WebsiteTester(self.initial_url)
        time.sleep(10)

    def navigate_to_initial_url(self):
        try:
            print("Navigating to initial URL...")
            self.driver.get(self.initial_url)
            print("Successfully navigated to initial URL.")
        except Exception as e:
            print(f"Error navigating to initial URL: {str(e)}")

    def navigate_to_maildrop(self):
        try:
            print("Navigating to Maildrop URL...")
            self.driver.get(self.maildrop_url)
            email_field = self.driver.find_element(By.CSS_SELECTOR, ".flex.flex-auto.flex-wrap.lg\:max-w-\[50ch\].md\:flex-nowrap.md\:px-0.px-8  .bg-white.border-stone-400.dark\:bg-stone-800\/95.dark\:border-stone-500.dark\:text-stone-50.flex-auto.placeholder-stone-400.px-2.py-2.rounded-md.text-base")
            # email_field.send_keys(self.maildrop_address)
            email_field.send_keys(self.website_tester.generate_random_email())
            email_field.send_keys(Keys.RETURN)
            print("Navigated to Maildrop and entered email address.")
        except Exception as e:
            print(f"Error navigating to Maildrop URL: {str(e)}")

    def fetch_invitation_link(self):
        try:
            print("Fetching the invitation email...")
            time.sleep(15)  # Wait for email to arrive

            for _ in range(20):  # Check up to 20 times (e.g., up to 100 seconds)
                emails = self.driver.find_elements(By.CSS_SELECTOR, "a.message-list-item")
                if emails:
                    print(f"Emails found: {len(emails)}")
                    for email_item in emails:
                        email_item.click()
                        time.sleep(2)  # Wait for the email content to load
                        email_body = self.driver.find_element(By.CSS_SELECTOR, "div.message-body").text
                        invitation_link = self.extract_invitation_link(email_body)
                        if invitation_link:
                            return invitation_link
                        else:
                            print("No invitation link found in email.")
                print("No emails found, retrying...")
                time.sleep(5)
        except Exception as e:
            print("Error fetching invitation link:", e)
        return None

    def extract_invitation_link(self, email_body):
        link = re.search(r'(https?://\S+)', email_body)
        if link:
            print(f"Invitation link found: {link.group()}")
            return link.group()
        return None

    def open_invitation_link(self, link):
        try:
            self.driver.get(link)
            print("Successfully opened invitation link.")
        except Exception as e:
            print(f"Error opening invitation link: {str(e)}")

    def navigate_to_geonadir_and_login(self, email):
        try:
            print("Navigating to GeoNadir URL and logging in...")
            self.driver.get("https://staging.geonadir.com/myprojects?login=sign-in")
            time.sleep(2)  # Wait for page to load

            # Fill in the email field
            email_field = self.driver.find_element(By.NAME, "#email")
            email_field.send_keys(email)

            # Fill in other necessary login fields (assuming password field)
            password_field = self.driver.find_element(By.NAME, "password")
            password_field.send_keys("password")  # Use the appropriate password

            # Submit the form
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            print("Login form submitted.")
        except Exception as e:
            print(f"Error logging into GeoNadir: {str(e)}")

    def close_driver(self):
        print("Closing the browser...")
        self.driver.quit()


if __name__ == "__main__":
    email_receiver = EmailReceiver(
        "https://staging.geonadir.com/myprojects?login=sign-in",
        "https://maildrop.cc/inbox/"
    )
    email_receiver.navigate_to_initial_url()
    # Assuming share_project function is called here and sends the invitation
    time.sleep(10)  # Wait for the invitation email to be sent

    email_receiver.navigate_to_maildrop()

    invitation_link = email_receiver.fetch_invitation_link()
    if invitation_link:
        email_receiver.open_invitation_link(invitation_link)
    else:
        print("No invitation link found.")

    # Assuming the invitation link logs in the user automatically, or perform the login manually
    email_receiver.navigate_to_geonadir_and_login()

    time.sleep(10)
    email_receiver.close_driver()
