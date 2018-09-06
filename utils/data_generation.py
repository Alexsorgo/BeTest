"""
Provide fake test data for tests.
"""
import random
import string

from faker import Factory


class __Fake:

    def __init__(self, localization='en_US'):
        self.fake = Factory.create(localization)

    @property
    def get_email(self):
        return self.fake.email()

    @property
    def get_first_and_last_names(self):
        new_name = self.fake.name().split(" ")
        first_name = "ANT_" + new_name[0]
        last_name = "ANT_" + new_name[1]
        return first_name, last_name

    @property
    def get_username(self):
        return "ANT_" + self.fake.word()

    @property
    def get_phone_number(self):
        return "+38063" + str(self.fake.random_number(7))

    @staticmethod
    def get_string(str_length=100):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=str_length))

    @property
    def get_url(self):
        return self.fake.url()

    @property
    def get_text_message(self):
        return "ANT_" + self.fake.sentence()

    @property
    def get_word(self):
        return "ANT_" + self.fake.word()


magic = __Fake()
