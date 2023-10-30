import os
import socket


class PrefixMiddleware(object):
    def __init__(self, app, voc=True):
        self.app = app
        if voc:
            # myip = self.get_myip()
            # mytoken = os.getenv("VOC_PROXY_TOKEN")
            # self.prefix = f'/hostip/{myip}:5000/vocproxy/{mytoken}'
            self.prefix = f"/proxy/5000/"
        else:
            self.prefix = ""

    def clear_prefix(self, s, prefix):
        if len(prefix) > 0 and s.startswith(prefix):
            return self.clear_prefix(s[len(prefix) :], prefix)
        else:
            return s

    def __call__(self, environ, start_response):
        environ["PATH_INFO"] = self.clear_prefix(
            environ["PATH_INFO"], self.prefix
        )
        environ["SCRIPT_NAME"] = self.prefix
        return self.app(environ, start_response)

    def get_myip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 53))
        return s.getsockname()[0]
