from nose.tools import *
from ex49.sentence import *


def test_sentence():
    assert(parse_sentence(scan("kill the bear")), Sentence('player', 'kill', 'bear'))
    assert(parse_sentence(scan("hit the bear on the nose")), Sentence('player', 'hit', 'bear'))


def test_error():
    assert_raises(PharseError, parse_object, scan("the to dd"))

