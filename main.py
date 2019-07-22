import webapp2
import os
import jinja2
#import logging

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template  = jinja_env.get_template("template/start.html")
        self.response.write(template.render())

class enterHandler(webapp2.RequestHandler):
    def get(self):
        template  = jinja_env.get_template("template/enter.html")
        self.response.write(template.render())
class selfieHandler(webapp2.RequestHandler):
    def get(self):
        template  = jinja_env.get_template("template/selfie.html")
        self.response.write(template.render())
class callHandler(webapp2.RequestHandler):
    def get(self):
        template  = jinja_env.get_template("template/call.html")
        self.response.write(template.render())
class summonHandler(webapp2.RequestHandler):
    def get(self):
        template  = jinja_env.get_template("template/summon.html")
        self.response.write(template.render())

class hideHandler(webapp2.RequestHandler):
    def get(self):
        template  = jinja_env.get_template("template/hide.html")
        self.response.write(template.render())
class runHandler(webapp2.RequestHandler):
    def get(self):
        template  = jinja_env.get_template("template/run.html")
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/',MainHandler),
    ('/',enterHandler),
    ('/selfie',selfieHandler),
    ('/call',callHandler),
    ('/summon',summonHandler),
    ('/hide',hideHandler),
    ('/enter',enterHandler),
    ('/enter',enterHandler),
], debug=True)
