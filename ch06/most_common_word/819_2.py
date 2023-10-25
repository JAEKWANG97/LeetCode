
import re
paragraph = "Bob hit a ball, the hit BALL flew far after"
banned = ["hit"]
cleaned_arr = re.sub('[^a-zA-Z\s] ', '' , paragraph.lower()).split()

from collections import defaultdict
word_dict = defaultdict(int)

max_word = ""
for x in cleaned_arr:
    word_dict[x] += 1
    if word_dict[x] > word_dict[max_word]:
        max_word = x
        
print(max_word)