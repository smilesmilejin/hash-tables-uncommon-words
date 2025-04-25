# # Method 1 : Self
# # Time Complexity: O (n+m), n is length of s1, m is the length of s2
# # Space Complexity: O (n + m)
# def uncommon_from_sentences(s1, s2):
#     s1_map = {}
#     for word in s1.split():
#         s1_map[word] = 1
    
#     s2_map = {}
#     for word in s2.split():
#         s2_map[word] = 1

#     uncommon_words = []
#     # disallow_repeat_in_same_sentence: if three is no repetitive words in the sentence
#     if len(s1_map) == len(s1.split()):
#         for word in s1.split():
#             if not s2_map.get(word):
#                 uncommon_words.append(word)
    
#     if len(s2_map) == len(s2.split()):
#         for word in s2.split():
#             if not s1_map.get(word):
#                 uncommon_words.append(word)

#     return uncommon_words


## Method 2: 
def uncommon_from_sentences(s1, s2):
    # Create a dictionariies that maps the word to count
    word_counts = {}
    for word in s1.split() + s2.split():
        if not word_counts.get(word):
            word_counts[word] = 1
            continue
        word_counts[word] += 1

    uncommon_words = []
    for word, count in word_counts.items():
        if count == 1:
            uncommon_words.append(word)
    
    return uncommon_words
        