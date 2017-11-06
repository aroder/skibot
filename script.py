import sys
from wit import Wit

access_token = '7QOKJPX4ZANI6PNYUDIXEK2MFDBH3FP4'

# print(sys.argv)

# if len(sys.argv) != 1:
#     print('usage: python <query>')
#     exit(1)

# def send(request, response):
#     print(response['text'])

# actions = {
#     'send': send
# }

client = Wit(access_token=access_token)
client.message('What are snow conditions in Vail?')

