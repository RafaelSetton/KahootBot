from selenium import webdriver
from time import sleep
from random import choice, randint
from threading import Thread

game_pin = "721729"


class KahootBot:
    def __init__(self, pin, name, bot_id):
        self.driver = webdriver.Chrome()

        self.driver.get('https://kahoot.it/')
        sleep(0.5)

        self.driver.find_element_by_tag_name("input").send_keys(pin)
        self.driver.find_element_by_tag_name("button").click()

        sleep(3)

        self.driver.find_element_by_tag_name("input").send_keys(name+str(bot_id))
        self.driver.find_element_by_tag_name("button").click()

    def answer(self):
        while True:
            buttons = []
            while len(buttons) < 2:
                buttons = self.driver.find_elements_by_tag_name('button')

            sleep(0.2)
            choice(buttons).click()


def multi_task(bot_list):
        for bot in bot_list:
            Thread(target=bot.answer).start()


bots = []
for i in range(3):
    bots.append(KahootBot(game_pin, "Bot", i))

multi_task(bots)
