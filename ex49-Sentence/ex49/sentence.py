
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


class PharseError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, object):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, skip_type):
    while peek(word_list) == skip_type:
        match(word_list, skip_type)


def parse_verb(word_list):
    skip(word_list, 'stop')
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        PharseError("Expecting a verb next!")


def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)
    if next == 'direction':
        return match(word_list, 'direction')
    elif next == 'noun':
        return match(word_list, 'noun')
    else:
        PharseError("Expecting a noun or direction next!")


def parse_subject(word_list, subj):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    return Sentence(subj, verb, obj)


def parse_sentence(word_list):
    skip(word_list, 'stop')
    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        return parse_subject(word_list, ('noun', 'player'))
    else:
        PharseError("Must start with subject, object,or verb not: %s" % start)





