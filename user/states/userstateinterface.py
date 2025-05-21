from abc import ABC


class UserStateInterface(ABC):

    def sign_in(self, user_data):
        pass
    def sign_in_successful(self):
        pass
    def sign_in_processing(self):
        pass
    def sign_in_failed(self):
        pass
    def sign_out(self):
        pass
    def sign_out_processing(self):
        pass
    def sign_out_successful(self):
        pass
    def sign_out_failed(self):
        pass
