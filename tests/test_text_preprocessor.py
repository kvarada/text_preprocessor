import pytest
from text_preprocessor import text_preprocessor

def test_preprocess_corpus():
    """
    :return:
    """    
    corpus = ["It was a great day. I loved the movie and spending time with you.",
              "The sky is always blue underneath. Remember that."]
    expected_answer = [['great', 'day'], ['loved', 'movie', 'spending', 'time'], ['sky', 'always', 'blue', 'underneath'], ['remember']]
    
    pp = text_preprocessor.MyPreprocessor()
    assert(pp.preprocess_corpus(corpus) == expected_answer)

