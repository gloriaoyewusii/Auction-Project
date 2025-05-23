

class UserContext:

    def __init__(self):
        from user.states.signedoutstate import SignedOutState
        self.state = SignedOutState(self)


    def change_state(self, new_state):
        self.state = new_state

    def sign_in(self, user_data):
        return self.state.sign_in(user_data)
    def sign_in_processing(self):
        self.state.sign_in_processing()
    def sign_in_successful(self):
        self.state.sign_in_successful()
    def sign_in_failed(self):
        self.state.sign_in_failed()

    def sign_out(self):
        self.state.sign_out()
    def sign_out_processing(self):
        self.state.sign_out_processing()
    def sign_out_successful(self):
        self.state.sign_out_successful()
    def sign_out_failed(self):
        self.state.sign_out_failed()


