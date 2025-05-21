
from user.states.userstateinterface import UserStateInterface
from user.user_context import UserContext

from rest_framework.exceptions import ValidationError

from user.serialisers.userserialiser import UserSerialiser


class SignedInState(UserStateInterface):
    def __init__(self, user : UserContext):
        self.user = user

    def sign_in(self, user_data):
        if isinstance(self.user.state, SignedInState):
            raise ValidationError('You are already signed in with this account.')
    def sign_out(self):
        from user.states.signedoutstate import SignedOutState
        self.user.change_state(SignedOutState(self.user))

    # def sign_in_processing(self):
    #     self.user.state = SignedOutState(self.user)
    #
    # def sign_in_successful(self):
    #     self.user.state = SignedInState(self.user)
    #
    # def sign_in_failed(self):
    #     self.user.state = SignedOutState(self.user)



    # def sign_out_processing(self):
    #     self.user.state = SignedInState(self.user)
    #
    # def sign_out_successful(self):
    #     self.user.state = SignedOutState(self.user)
    #
    # def sign_out_failed(self):
    #     self.user.change_state(SignedInState(self.user))