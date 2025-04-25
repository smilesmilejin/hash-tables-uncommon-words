def uncommon_from_sentences(s1, s2):
    s1_map = {}
    for word in s1.split():
        s1_map[word] = 1
    
    s2_map = {}
    for word in s2.split():
        s2_map[word] = 1

    uncommon_words = []
    # disallow_repeat_in_same_sentence: if three is no repetitive words in the sentence
    if len(s1_map) == len(s1.split()):
        for word in s1.split():
            if not s2_map.get(word):
                uncommon_words.append(word)
    
    if len(s2_map) == len(s2.split()):
        for word in s2.split():
            if not s1_map.get(word):
                uncommon_words.append(word)

    return uncommon_words




# - A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# - A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# - Given two sentences s1 and s2, return a list of all the uncommon words. The words may be returned in any order.