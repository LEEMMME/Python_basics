# with open('D:/PC--Python/python入门基础/listoo.txt', encoding='utf-8') as _object:
#     contents = _object.readlines()
# for content in contents:
#     print(content.rstrip())
# with open('dig.txt', 'w', encoding='utf-8') as message:
#     messages = '诗仙李白'
#     message.write(messages)
# with open('dig.txt', 'a', encoding='utf-8') as message:
#     messages = '诗仙李白\n'
#     message.write(messages)
import json
message = ['I love you girl ii']
with open('dig.txt', 'a', encoding='utf-8') as messages:
    json.dump(message, messages)

