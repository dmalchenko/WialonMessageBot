# -*- coding: utf8 -*-
import telebot
import config

bot = telebot.AsyncTeleBot(config.token)
bot.remove_webhook()
bot.set_webhook(url=config.telegram_webhook_url, certificate=open(config.cert_file, 'r'))