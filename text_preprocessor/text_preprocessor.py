from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string


class MyPreprocessor:

    def __init__(self):
        self.stop_words = list(set(stopwords.words('english')))
        punctuation = string.punctuation
        self.stop_words += list(punctuation)

    def __preprocess(self, text):
        """
        Given a text, this function returns a preprocessed
        text which is tokenized and free from stopwords.

        Arguments:
        text -- (str)
            text to be preprocessed

        Returns:
            (list)
                a list containing tokens in the preprocessed text
        """
        text = text.replace(r'<br />', ' ')
        preprocessed = []
        tokenized = word_tokenize(text)
        for token in tokenized:
            token = token.lower()
            if token not in self.stop_words:
                preprocessed.append(token)
        return preprocessed

    def preprocess_corpus(self, doc_list):
        """
        Given a list of documents doc_list (e.g., reviews, news articles)
        this function carries out sentence tokenization and other preprocessing
        and returns a preprocessed corpus.

        Arguments:
        doc_list -- (list)
            a list of strings, each string representing a document.
        Returns:
        preprocessed_corpus -- (list)
            a list of lists of preprocessed (tokenized and stopword-removed)
            sentences in the documents with the following format.
        [[sent1_word1, sent1_word2, sent1_word3, ...],
        [sent2_word1, sent2_word2, sent2_word3, ...], ...]
        """
        preprocessed_corpus = []
        for doc in doc_list:
            # sentence tokenization
            sentences = sent_tokenize(doc)
            preprocessed_corpus.extend([self.__preprocess(sentence)
                                        for sentence in sentences])
        return preprocessed_corpus


if __name__ == "__main__":
    pp = MyPreprocessor()
    corpus = ["It was a great day. ",
              "I loved the movie and spending time with you.",
              "The sky is always blue underneath. Remember that."]

    print(pp.preprocess_corpus(corpus))
