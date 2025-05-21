from rest_framework.exceptions import ValidationError

from user.serialisers.userserialiser import UserSerialiser
# from user.user_context import UserContext
#
#
# class UserService:
#
#     def __init__(self, user:UserContext):
#         self.user = user
#
#
#     def register(self, user_data):
        # self.user.sign_in(user_data)
        # user_serialiser = UserSerialiser(data=user_data)
        # self.user.sign_in_processing()
        # if user_serialiser.is_valid():
        #     self.user.sign_in_successful()
        #     saved_user = user_serialiser.save()
        #
        #     return saved_user
        # else:
        #     self.user.sign_in_failed()
        #     raise ValidationError(user_serialiser.errors)



