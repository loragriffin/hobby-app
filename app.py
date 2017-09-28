import tornado.ioloop
import tornado.web
import tornado.log


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.set_header('Content-type', 'text/plain')
        self.write("Hello, world")


class YouHandler(tornado.web.RequestHandler):
    def get(self, name):
        # self.set_header('Content-type', 'text/plain')
        name = self.get_query_argument('name', 'Nobody')
        self.write("Hello, world")


class YouThreeHandler(tornado.web.RequestHandler):
    def get(self, name):
        # self.set_header('Content-type', 'text/plain')
        names = self.get_query_arguments('name')
        for name in names:
            self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/hello/(.*)", YouHandler),
        (r"/hello2", YouHandler),
        (r"/hello3", YouThreeHandler),
    ], autoreload=True)


if __name__ == "__main__":
    tornado.log.enable_pretty_logging()

    app = make_app()
    app.listen(8888, print('Server started on localhost:8888'))
    tornado.ioloop.IOLoop.current().start()
