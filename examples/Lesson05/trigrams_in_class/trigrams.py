

def find_words(text):
    return text.split()


def make_trigrams(words):
    """
    build trigram dict from a list words
    """
    tris = {}
    for i in range(len(words) - 2):
        first = words[i]
        second = words[i + 1]
        third = words[i + 2]

        pair = (first, second)
        print(pair, third)
        # if pair in tris:
        #     print("the value:", tris[pair])
        #     tris[pair].append(third)
        # else:
        #     tris[pair] = [third]
        # try:
        #     tris[pair].append(third)
        # except KeyError:
        #     tris[pair] = [third]
        tris.setdefault(pair, []).append(third)


    return tris

