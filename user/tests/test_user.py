from django.test import TestCase

from user.states.signedinstate import SignedInState
from user.user_context import UserContext


class TestUserStates(TestCase):
    def test_that_user_can_signin(self):
        user_context = UserContext()
        user_data1 = {
            "email": "jdoe@gmail.com",
            "password": "password"
        }
        user = user_context.sign_in(user_data1)
        self.assertEqual(user.email, "jdoe@gmail.com")
        self.assertTrue(user.check_password("password"))

        self.assertIsInstance(user_context.state, SignedInState)