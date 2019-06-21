from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-465745290291-467243504518-465764399875-aaa34669852b1a47abfdc476c7cf14bc', #app verification token
							'xoxb-465745290291-465764400867-9tfCxFZQi3SXHFNZzaI1ZsVe', # bot verification token
							'l37zjmQs09lwfye1Uag6tv7i', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))