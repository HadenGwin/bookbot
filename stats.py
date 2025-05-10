def word_count(words):
    indWords = words.split()
    numCount = len(indWords)
    return numCount

def char_count(words):
    counts: dict[str, int] = {}
    for ch in words.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    newDict = [{"character" : char, "num" : count} for char, count in dict.items() if char.isalpha()]
    newDict.sort(reverse=True, key=sort_on)
    return newDict
    