import pkg_resources

import tornado.ioloop
import tornado.web

from tornado.options import options, define

from app.handler import MainHandler, ClockWebSocket

define("host", default="localhost", help="app host", type=str)
define("port", default=8080, help="app port", type=int)
define("debug", default=False, help="debug mode", type=bool)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", ClockWebSocket),
    ],
    debug=options.debug,
    template_path=pkg_resources.resource_filename("app", 'templates/'),
    static_path=pkg_resources.resource_filename("app", 'static/'))


def main():
    options.parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
