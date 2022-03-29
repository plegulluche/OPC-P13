from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class TestAuthentification(StaticLiveServerTestCase):
    def setUp(self):
        # Open browser with webdriver and create a user on register route
        self.browser = webdriver.Chrome("tests/functionnal test/chromedriver")
        self.browser.get(self.live_server_url + reverse("register"))

        femail = self.browser.find_element_by_name("email")
        femail.send_keys("testuser@gmail.com")
        fusername = self.browser.find_element_by_name("username")
        fusername.send_keys("testuser")
        password1 = self.browser.find_element_by_name("password1")
        password1.send_keys("UnMotDePasse12")
        password2 = self.browser.find_element_by_name("password2")
        password2.send_keys("UnMotDePasse12")
        validate = self.browser.find_element_by_id("register")
        validate.click()

    def tearDown(self):
        # Close the browser
        self.browser.close()

    def test_register(self):
        self.assertEqual(
            self.browser.find_element_by_tag_name("h5").text,
            "Gardenizer , l'organisateur simple et efficace",
        )
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("mainpage")
        )

    def test_logout(self):
        logout = self.browser.find_element_by_id("logout")
        logout.click()

        self.assertNotEqual(self.browser.page_source.find("Calendrier"), 1)
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("mainpage")
        )

    def test_login(self):
        logout = self.browser.find_element_by_id("logout")
        logout.click()
        selectlogin = self.browser.find_element_by_id("login")
        selectlogin.click()
        email = self.browser.find_element_by_name("email")
        email.send_keys("testuser@gmail.com")
        password = self.browser.find_element_by_name("password")
        password.send_keys("UnMotDePasse12")

        self.assertEqual(
            self.browser.find_element_by_tag_name("h1").text, "Se connecter"
        )
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("login")
        )
