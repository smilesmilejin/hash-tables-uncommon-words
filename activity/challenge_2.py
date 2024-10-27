def uncommon_from_sentences(sentences):
    counts = {}
    for sentence in sentences:
        count_words(sentence, counts)

    return find_uncommon(counts)

def count_words(sentence, counts):
    for word in set(sentence.split()):
        count = counts.get(word, 0)
        counts[word] = count + 1
        
def find_uncommon(counts):
    return [word for word, count in counts.items() if count == 1]
