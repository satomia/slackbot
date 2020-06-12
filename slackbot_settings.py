#coding: utf-8
import os
# print(os.environ["USERNAME"])
API_TOKEN = os.environ["SLACK_API_TOKEN"]
DEFAULT_REPLY = "Hey, I'm on Heroku!"

PLUGINS = [
    "slackbot.plugins",
    "plugins"
]