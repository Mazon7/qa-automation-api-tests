
class AuthUser:
    @staticmethod
    def get_body(user, pass_w):
        email = user
        password = pass_w
        print(email, password)
        return {"email": email, "password": password}


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
