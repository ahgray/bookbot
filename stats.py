def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for char in list(text):
        lc = char.lower()
        if (lc) in chars:
            chars[lc] +=1
        else:
            chars[lc] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list