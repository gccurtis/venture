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

app = webapp2.WSGIApplication([
    ('/',MainHandler),
    ('/',enterHandler),
    ('/selfie',selfieHandler),
    ('/call',callnHandler),
    ('/summon',summonHandler),
], debug=True)
