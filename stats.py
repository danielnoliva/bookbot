def get_word_count(book_text):
    return len(book_text.split())

def count_characters(book_text):
    character_count = {}
    for char in book_text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_by_num(character_count):
    return character_count["num"]

def make_sorted_list(character_count):
    as_list = []
    for char, count in character_count.items():
        as_list.append({"char": char, "num": count})
    as_list.sort(key=sort_by_num, reverse=True)
    return as_list