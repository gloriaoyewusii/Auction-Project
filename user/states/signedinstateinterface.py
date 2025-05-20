from abc import ABC


class UserStateInterface(ABC):

    def __init__(self, user):
        self.user = user

    def sign_in(self):
        pass
    def sign_in_successful(self):
        pass
    def sign_in_processing(self):
        pass
    def sign_in_failed(self):
        pass
