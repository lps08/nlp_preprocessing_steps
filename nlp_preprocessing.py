import re
import nltk
import string
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem import RSLPStemmer

# download list of stopwords
nltk.download('stopwords')
# RSLPStemmer
nltk.download('rslp')
# WordNetLemmatizer
nltk.download('wordnet')
# download machado files
nltk.download('machado')

class NLPreprocessing():
    """
        Some texte preprocessing to nlp task
    """

    @staticmethod
    def remove_unknown_char(text:str, unknown_char:str) -> str:
        """
            Remove all unknown character setted by parameter
        """
        return " ".join([word.replace(unknown_char, '') for word in text.split()])

    @staticmethod
    def remove_punctuations(text:str) -> str:
        """
            Remove all ponctuations in the text input
        """
        punct = string.punctuation

        return text.translate(str.maketrans('', '', punct))

    @staticmethod
    def remove_stopwords(text:str) -> str:
        """
            Revemo all stopwords of a text input
        """
        stopwd = stopwords.words('portuguese')

        return " ".join([word for word in text.split() if word not in stopwd])

    @staticmethod
    def frequent_words(text:str, num_top_frequency:int = 10) -> list:
        """
            Return a list of words frequency
        """
        freq = Counter()

        for word in text.split():
            # counting each word
            freq[word] += 1

        return freq.most_common(num_top_frequency)

    @staticmethod
    def remove_freq_words(text:str, top_frequency_word:int = 10) -> str:
        """
            Remove all stopwords in the input text
        """

        freq_words = [word for (word, _) in NLPreprocessing.frequent_words(text=text, num_top_frequency=top_frequency_word)]

        return " ".join([word for word in text.split() if word not in freq_words])

    @staticmethod
    def rare_words(text:str, top_rare_word:int = 10) -> str:
        """
            List of rare words
        """

        freq_words = [word for (word, _) in NLPreprocessing.frequent_words(text=text, num_top_frequency=None)]

        # reversing top freq words to get all the rare one.
        rare_words = freq_words[::-1]
        
        return " ".join([word for word in text.split() if word not in rare_words[:top_rare_word]])

    @staticmethod
    def steamming(text:str) -> str:
        """
            Reduces the eatch word to the root
        """
        steammer = RSLPStemmer()

        return " ".join([steammer.stem(word) for word in text.split()])

    @staticmethod
    def remove_urls(text:str) -> str:
        """
            Remove all url symbols from the input text
        """
        upattern = re.compile(r'https?://\S+|www\.\S+')
        return upattern.sub(r'', text)

    @staticmethod
    def remove_tags(text):
        """
            Remove all tags from the input text
        """
        pattern = re.compile('<.*?>')
        return pattern.sub(r'', text)

    