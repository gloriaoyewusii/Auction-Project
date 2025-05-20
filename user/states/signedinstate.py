from user.states.signedoutstate import SignedOutState
from user.states.userstateinterface import UserStateInterface
from user.user_context import UserContext


class SignedInState(UserStateInterface):
    def __init__(self, user : UserContext):
        self.user = user

    def sign_in(self):
        self.user.change_state(SignedOutState(self.user))

    def sign_in_processing(self):
        self.user.state = SignedOutState(self.user)

    def sign_in_successful(self):
        self.user.state = SignedInState(self.user)

    def sign_in_failed(self):
        self.user.state = SignedOutState(self.user)

    def sign_out(self):
        self.user.state = SignedInState(self.user)

    def sign_out_processing(self):
        self.user.state = SignedInState(self.user)

    def sign_out_successful(self):
        self.user.state = SignedOutState(self.user)

    def sign_out_failed(self):
        self.user.state = SignedInState(self.user)