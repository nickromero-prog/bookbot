from collections import Counter

def get_word_count(file_contents):
    word_count = len(file_contents.split())
    return word_count

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def convert_to_sorted_list(char_count_dict):
    chars_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():  # Only use alphabetical characters
            # Create a new dictionary with two key-value pairs
            char_dict = {'char': char, 'count': count}
            # Add this dictionary to our list
            chars_list.append(char_dict)

    def sort_on(dict):
        return dict['count']
    
    chars_list.sort(reverse=True, key=sort_on)

    # Now you would sort this list...
    
    return chars_list

def format_sorted_list(sorted_list):
    # Loop through each character dictionary
    for char_dict in sorted_list:
        char = char_dict['char']
        count = char_dict['count']
        print(f"{char}: {count}")