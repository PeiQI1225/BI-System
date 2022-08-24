
class Response:

    def __init__(self, data, msg='success', code=0):
        response = {}
        self.response = response
        self.data = data
        self.msg = msg
        self.code = code
        self.response['data'] = self.data
        self.response['msg'] = self.msg
        self.response['code'] = self.code

    def return_response(self):
        return self.response
