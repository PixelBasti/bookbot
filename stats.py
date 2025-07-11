def words_count(string):
    return len(string.split()) 

def char_count (string):
    char_amount = {
        "a":0
    }
    for i in string.lower():
        if i in char_amount:
            char_amount[i] += 1
        else:
            char_amount[i] = 1
    return char_amount

def sort(items):
    return items["num"]

def char_sort(d):
    l = []
    for i in d:
        l.append({"char": i, "num": d[i]})
    l.sort(reverse=True, key=sort)
    return l