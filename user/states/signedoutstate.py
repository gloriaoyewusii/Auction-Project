from user.states.userstateinterface import UserStateInterface
from user.user_context import UserContext


class SignedOutState(UserStateInterface):

    def __init__(self, user : UserContext):
        self.user = user

    def sign_in(self):
        pass
    def sign_in_processing(self):
        pass
    def sign_in_successful(self):
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