#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import os
import webapp2
import jinja2
import csv

JINJA_ENVIRONMENT = jinja2.Environment(
  loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	title = "QuasiCon 2018 - Home"
    	template_vars={'title':title}
    	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    	self.response.out.write(template.render(template_vars))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
    	title = "QuasiCon 2018 - About"
    	template_vars={'title':title}
        template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    	self.response.out.write(template.render(template_vars))

class ScheduleHandler(webapp2.RequestHandler):
    def get(self):
    	title = "QuasiCon 2018 - Schedule"
    	template_vars={'title':title}
        template = JINJA_ENVIRONMENT.get_template('templates/schedule.html')
    	self.response.out.write(template.render(template_vars))

class LocationHandler(webapp2.RequestHandler):
    def get(self):
    	title = "QuasiCon 2018 - Location"
    	template_vars={'title':title}
        template = JINJA_ENVIRONMENT.get_template('templates/location.html')
    	self.response.out.write(template.render(template_vars))

class SpeakerHandler(webapp2.RequestHandler):
    def get(self):
    	title = "QuasiCon 2018 - Speakers"
    	template_vars={'title':title}
        template = JINJA_ENVIRONMENT.get_template('templates/speakers.html')
    	self.response.out.write(template.render(template_vars))

class SessionHandler(webapp2.RequestHandler):
    def get(self):
    	title = "QuasiCon 2018 - Propose a Session"
    	template_vars={'title':title}
        template = JINJA_ENVIRONMENT.get_template('templates/session.html')
    	self.response.out.write(template.render(template_vars))
    def post(self):
    	fname = self.request.get('fname')
    	lname = self.request.get('lname')
    	sname = self.request.get('sname')
    	dname = self.request.get('dname')
    	email = self.request.get('email')
    	sess = self.request.get('sess')
    	titles = self.request.get('titles')
    	sessd = self.request.get('sessd')
    	posi = self.request.get('posi')
#     	writehome = open("Sessions.csv","a")
#     	writehome.write(fname +"," + lname +"," + sname +"," +dname +"," +email +"," +sess +"," +titles +"," +sessd +"," +posi)
#     	writehome.close()
    	title = "QuasiCon 2018 - Home"
    	template_vars={'title':title}
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    	self.response.out.write(template.render(template_vars))


class VolunteerHandler(webapp2.RequestHandler):
    def get(self):
    	title = "Volunteer"
    	template_vars={'title':title}
        template = JINJA_ENVIRONMENT.get_template('templates/volunteer.html')
    	self.response.out.write(template.render(template_vars))
   

class ContactHandler(webapp2.RequestHandler):
    def get(self):
    	title = "Contact Us"
    	template_vars={'title':title}
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
    	self.response.out.write(template.render(template_vars))

class RegisterHandler(webapp2.RequestHandler):
    def get(self):
    	title = "QuasiCon 2018 - Register"
    	template_vars={'title':title}
        template = JINJA_ENVIRONMENT.get_template('templates/register.html')
    	self.response.out.write(template.render(template_vars))
    

app = webapp2.WSGIApplication([
    ('/index.html', MainHandler),
    ('/about.html', AboutHandler),
    ('/schedule.html', ScheduleHandler),
    ('/location.html', LocationHandler),
    ('/speakers.html', SpeakerHandler),
    ('/session.html', SessionHandler),
    ('/volunteer.html', VolunteerHandler),
    ('/contact.html', ContactHandler),
    ('/register.html', RegisterHandler),
    ('/', MainHandler)
], debug=True)
