from trigrams import find_words, make_trigrams


text = "I wish I may I wish I might"


def test_find_words():
    words = find_words(text)

    assert words == ['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might']


def test_make_trigrams():
    result = make_trigrams(find_words(text))

    # expected = {"I wish": ["I", "I"],
    #             "wish I": ["may", "might"],
    #             "may I": ["wish"],
    #             "I may": ["I"],
    #             }
    print("result:", result)

    expected  = {("I", "wish"): ["I", "I"],
                 ("wish", "I"): ["may", "might"],
                 ("may", "I"): ["wish"],
                 ("I", "may"): ["I"],
                 }

    assert expected.keys() == result.keys()

    assert result == expected

    # assert False
