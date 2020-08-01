import datetime
import os
import pkg_resources
import tornado.ioloop
import tornado.web
from tornado.options import options, define

from app.ui.web.handler import MainHandler, ClockWebSocket

define("host", default="localhost", help="app host", type=str)
define("port", default=8080, help="app port", type=int)
define("debug", default=False, help="debug mode", type=bool)

def resource_path(resource):
    return pkg_resources.resource_filename("app.ui.web", resource)

def make_app():
    settings = {'template_path': resource_path('templates/'),
                'static_path': resource_path('static/')}

    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", ClockWebSocket),
    ],
    debug=options.debug,
    **settings)

def main():
    options.parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
