from rest_framework.exceptions import ValidationError

from user.serialisers.userserialiser import UserSerialiser

from user.states.userstateinterface import UserStateInterface
# from user.user_context import UserContext


class SignedOutState(UserStateInterface):

    def __init__(self, user):
        self.user = user

    def sign_in(self, user_data):
        from user.states.signedinstate import SignedInState
        user_serialiser = UserSerialiser(data=user_data)
        if user_serialiser.is_valid():
            self.user.change_state(SignedInState(self.user))
            saved_user = user_serialiser.save()
            return saved_user
        else:
            # self.user.sign_in_failed()
            raise ValidationError(user_serialiser.errors)

    # def sign_in_processing(self):
    #     pass
    # def sign_in_successful(self):
    #     pass
    # def sign_in_failed(self):
    #     pass
    def sign_out(self):
        raise ValidationError("You are already signed out in this state")
    # def sign_out_processing(self):
    #     pass
    # def sign_out_successful(self):
    #     pass
    # def sign_out_failed(self):
    #     pass