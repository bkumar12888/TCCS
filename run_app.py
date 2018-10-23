from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-461998691799-460774806084-462348140966-013de96be4c56b0995ed7bf72ec58114', #app verification token
							'xoxb-461998691799-460776293044-q9UhNXsrHnfHEwQTdT9nGToY', # bot verification token
							'SG3gd8CAbJaYtqt9ZXuIhw9R', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))