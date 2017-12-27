

WORDS_DICT = {'direction': ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
              'verb': ['go', 'stop', 'kill', 'eat'],
              'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
              'noun': ['door', 'bear', 'princess', 'cabinet']}


def scan(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if word.isdigit():
            result.append(('number', int(word)))
        elif word in WORDS_DICT['direction']:
            result.append(('direction', word))
        elif word in WORDS_DICT['verb']:
            result.append(('verb', word))
        elif word in WORDS_DICT['stop']:
            result.append(('stop', word))
        elif word in WORDS_DICT['noun']:
            result.append(('noun', word))
        else:
            result.append(('error', word))
    return result

print(scan("north south east"))
