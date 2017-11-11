from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web

#import tornado.log
import logging

app_log = logging.getLogger(__name__)
app_log.setLevel(logging.INFO)

class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '3.5.1',
                     'last_build':  date.today().isoformat() }
        self.write(response)

class ErrorHandler(tornado.web.RequestHandler):
    def get(self, error_code):
        app_log.warning('receive code %s',error_code)
        if error_code == "1":
            self.set_status(501)
        elif error_code == 2:
            self.send_error(502)
        else:
            raise tornado.web.HTTPError(500)

class TestHandler(tornado.web.RequestHandler):
    def initialize(self):
        app_log.info('Hello Test : %s', self.request)

    def get(self):
        self.write("request test")
        filters = self.request.arguments
        for k,v in filters.items():
            print "arg {0} : {1}".format(k, v)
        self.set_status(200)


application = tornado.web.Application([
    (r"/error/([0-9]+)", ErrorHandler),
    (r"/test", TestHandler),
    (r"/version", VersionHandler)
])

if __name__ == "__main__":

    logging.getLogger("tornado.access").setLevel(logging.INFO)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
