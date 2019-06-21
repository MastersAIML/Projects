from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-465745290291-467243504518-466251329397-368ea06dfc2183543f950aa3091c2eeb', #app verification token
							'xoxb-465745290291-465446699153-hHjl45L7ZjVoyNV3hldPVXko', # bot verification token
							'WvYa0IF55u4LlXbJWTDsrZFw', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))