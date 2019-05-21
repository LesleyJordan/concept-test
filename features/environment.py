from behave import *
from splinter import Browser
import logging

# Configure things to be used later
# For user data, URLs, etc
def set_context(context):
  context.userdata = {
    'preferred_language': 'en'
  }
  context.basicurl = 'https://www.concept7.nl'

# Runs before any steps
def before_all(context):
  context.browser = Browser(driver_name='chrome')
  logformat = '%(levelname)s:%(asctime)s:%(relativeCreated)d:%(message)s'
  logfilename = './mylogging.log'
  loglevel = logging.INFO
  logging.basicConfig(filename=logfilename,level=loglevel,format=logformat)
  logging.info("Things have started")
  set_context(context)