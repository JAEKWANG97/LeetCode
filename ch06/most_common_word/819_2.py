
import re
paragraph = "a, a, a, a, b,b,b,c, c"
paragraph = paragraph.lower()
banned = ["a"]
cleaned_arr = re.sub('[^a-zA-Z\s]', ' ' , paragraph)
print(cleaned_arr.split())
from collections import defaultdict
word_dict = defaultdict(int)
max_word = ""
for x in cleaned_arr.split():
    if x not in banned:
        word_dict[x] += 1
        if word_dict[x] > word_dict[max_word]:
            max_word = x
        
print(max_word)