import sys
from collections import Counter

def max_occurrences_words(word_dict,i):
    sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    result_list = []

    if sorted_words:
        max_word, max_count = sorted_words[i]
        result_list.extend([max_word, max_count])

    return result_list
#step 1

text_loc = input("Enter text location in your pc: ").strip()


try:
    with open(text_loc, 'r') as file:
        
        text_content = file.read()
        text_with_spaces = text_content.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ')

        words_list = text_with_spaces.split()  
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"Unexpected error: {e}")


#step 2
words_dist = dict(Counter(words_list))

#step 3
for i in range(int(sys.argv[1])):
    result_list = max_occurrences_words(words_dist,i)
    print("word - " , result_list[0] , " " , result_list[1] , "times")
