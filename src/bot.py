# Import Classes
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Bot(object):
    
    def __init__(self, **kwargs):
        super().__init__()
        
        self.bot = ChatBot('Buddy',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///database.sqlite3',
            logic_adapters=[
                'chatterbot.logic.BestMatch',
                'chatterbot.logic.TimeLogicAdapter'
            ],
            preprocessors=[
                'chatterbot.preprocessors.clean_whitespace'
            ]
        )
        
        environment_default = os.getenv('CHATTERBOT_SHOW_TRAINING_PROGRESS', True)
        self.show_training_progress = kwargs.get(
            'show_training_progress',
            environment_default
        )
        
    def train(self):
        trainer = ChatterBotCorpusTrainer(self.bot, show_training_progress=self.show_training_progress)
        trainer.train(
            "chatterbot.corpus.portuguese.conversations",
            "chatterbot.corpus.portuguese.greetings",
            "chatterbot.corpus.portuguese.compliment"
        )
        return self
        
    def process(self, request):
        try:
            return self.bot.get_response(request).text
        except:
            return "Eu não estou me sentindo muito bem... voltarei mais tarde."
