from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class HomepageTestCase(StaticLiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Safari()
        self.selenium.maxmize_window()
        self.user = User.objects.creat_user(username='bryant', email='w@bryant.com',
                                            password='heyulong')
        super(HomepageTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(HomepageTestCase, self).tearDown()

    def test_visit_homepage(self):
        self.selenium.get('%s%s' % (self.live_server_url, "/"))

        self.assertIn("Bryant Studio - Enjoy Create & Share",
                      self.selenium.title)
