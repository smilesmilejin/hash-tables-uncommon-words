# # Method 1
# def uncommon_from_sentences(sentences):
    
#     # Create a sentence_map that maps the index to a dictionary (each word is the key, and the value is 1)
#     sentence_map = {}
#     for index, sentence in enumerate(sentences):
#         sentence_map[index] = {}
#         sentence_words = sentence.split() # ['this', 'apple', 'is', 'sweet']

#         for word in sentence_words:
#             sentence_map[index][word] = 1

#     uncommon_words = []
#     for i in range(len(sentences)):
#         # disallow_repeat_in_same_sentence
#         # if there are repetitive in the same sentence skip the sentence
#         if len(sentences[i].split())!= len(sentence_map[i]):
#             continue

#         for word in sentences[i].split():
#             found = False
#             for j in range(len(sentence_map)):
#                 if word in sentence_map[j] and (i != j):
#                     found = True
#                     break

#             if (not found) and (word not in uncommon_words):
#                 uncommon_words.append(word)

#     return uncommon_words


## Method 2: 
def uncommon_from_sentences(sentences):
    # Create a dictionariies that maps the word to count
    word_counts = {}
    for sentence in sentences:
        for word in sentence.split():
            current_count = word_counts.get(word, 0)
            word_counts[word] = current_count + 1

    uncommon_words = []
    for word, count in word_counts.items():
        if count == 1:
            uncommon_words.append(word)
    
    return uncommon_words
        