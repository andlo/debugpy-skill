from mycroft import MycroftSkill, intent_file_handler


class Debugpy(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('debugpy.intent')
    def handle_debugpy(self, message):
        self.speak_dialog('debugpy')


def create_skill():
    return Debugpy()

