import datetime
import logging
from tornado.options import options

import tornado.web
import tornado.websocket


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("clock.html", host=options.host, port=options.port)

class ClockWebSocket(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
        
    def open(self):
        self.clock = tornado.ioloop.PeriodicCallback(self.send_time, 500, jitter=0.05)
        self.clock.start()
    
    def on_close(self):
        self.clock.stop()

    def on_message(self, message):
        logging.info(f"Message received: {message}")

    def send_time(self):
        self.write_message(str(datetime.datetime.utcnow()))