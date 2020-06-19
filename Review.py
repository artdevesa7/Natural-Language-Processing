from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from Part_of_Speech import get_part_of_speech
import re

lemmatizer = WordNetLemmatizer()

oprah_wiki = '<p>Working in local media, she was both the youngest news anchor and the first black female news anchor at Nashville\'s WLAC-TV. </p>'

result = re.sub(r'</?p>|([A-Z].[A-Z.]*)\.|,', '',oprah_wiki)
#this is better result = re.sub(r'</?p>|\.|,', '',oprah_wiki)
#use | for each Or

lower_result = result.lower()

tokenized = word_tokenize(lower_result)

lemmatizer = WordNetLemmatizer()

lemmatized = [lemmatizer.lemmatize(token,get_part_of_speech(token)) for token in tokenized]

print(lemmatized)