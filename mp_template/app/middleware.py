import os
import socket

class PrefixMiddleware(object):

    def __init__(self, app, voc=True):
        self.app = app
        if voc:
            myip = self.get_myip()
            mytoken = os.getenv("VOC_PROXY_TOKEN")
            self.prefix = f'/hostip/{myip}:5000/vocproxy/{mytoken}'
        else:
            self.prefix = ''

    def __call__(self, environ, start_response):
        print(environ['PATH_INFO'], self.prefix)
        environ['SCRIPT_NAME'] = self.prefix
        return self.app(environ, start_response)

    def get_myip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 53))
        return s.getsockname()[0]