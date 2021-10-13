# NLP Preprocessing steps
A preprocessing guide for a task using nlp.

## NLTK
The Natural Language Toolkit (NLTK), is a set of libraries and programs for symbolic and statistical processing from natural language to English, written in the Python programming language.

### Installing NLTK
    pip install nltk
    
## Removing unknown characters
Removing unknown words or characters, which may interfere with classification

## Lower casing
Putting all words to lowercase to be standardized

## Removing Punctuations
Removing punctuation to leave text only

## Removing stopwords
These are words that may be considered irrelevant to the set of results to be displayed in a search performed.

## Removing unknown words
Sometimes, depending on the font that the text came from, some unidentifiable characters may appear, and you need to remove them.

## Removing Frequent words
Frequent words are almost always devoid of meaning. These frequent words have high counts and so most scoring functions are rewarded for predicting their counts more than they are rewarded for predicting other words. Effectively every other word looks less common as a result.

## Removing rare words
Some of the words that are very unique in nature like names, brands, product names, and some of the noise characters. For example, it would be really bad to use names as a predictor for a text classification problem, even if they come out as a significant predictor.

## Steamming
For grammatical reasons, the words in a text use different forms of a word. In addition, there are derivationally related word families with similar meanings, such as democracy, democratic, and democratization. Thus, this processing has the function of reducing the word to its root.

## Removing URLs
Removes all url types contained in the text

## Removing tags
Removes all types of css tags contained in the text
