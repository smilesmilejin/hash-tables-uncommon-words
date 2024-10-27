def uncommon_from_sentences(s1, s2):
    counts = {}
    count_words(s1, counts)
    count_words(s2, counts) 
    return find_uncommon(counts)

def count_words(sentence, counts):
    for word in sentence.split():
        count = counts.get(word, 0)
        counts[word] = count + 1
        
def find_uncommon(counts):
    return [word for word, count in counts.items() if count == 1]