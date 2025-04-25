def uncommon_from_sentences(sentences):
    
    # Create a sentence_map that maps the index to a dictionary (each word is the key, and the value is 1)
    sentence_map = {}
    for index, sentence in enumerate(sentences):
        sentence_map[index] = {}
        sentence_words = sentence.split() # ['this', 'apple', 'is', 'sweet']

        for word in sentence_words:
            sentence_map[index][word] = 1

    uncommon_words = []
    for i in range(len(sentences)):
        # disallow_repeat_in_same_sentence
        # if there are repetitive in the same sentence skip the sentence
        if len(sentences[i].split())!= len(sentence_map[i]):
            continue

        for word in sentences[i].split():
            found = False
            for j in range(len(sentence_map)):
                if word in sentence_map[j] and (i != j):
                    found = True
                    break

            if (not found) and (word not in uncommon_words):
                uncommon_words.append(word)
                
    return uncommon_words





# sentences = [
#         "this apple is sweet",
#         "this apple is sour",
#     ]

# sentence_map = {}
# for index, sentence in enumerate(sentences):
#     sentence_map[index] = {}
#     sentence_words = sentence.split() # ['this', 'apple', 'is', 'sweet']
#     # sentence_words['this'] = 1

#     for word in sentence_words:
#         sentence_map[index][word] = 1


# print(sentence_map)

# {0: {'this': 1, 'apple': 1, 'is': 1, 'sweet': 1}, 1: {'this': 1, 'apple': 1, 'is': 1, 'sour': 1}}