def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

def get_text_count(text):
    text_array = text.split()
    dictionary = {}
    for word in text_array:
        # print(len(word))
        if len(word) > 1:
            for char in word:
                # print(char)
                if char.lower() in dictionary:
                    dictionary[char.lower()] += 1
                else:
                    dictionary[char.lower()] = 1
        else:
            if word.lower() in dictionary:
                dictionary[word.lower()] += 1
            else:
                dictionary[word.lower()] = 1
    # print(dictionary)
    return dictionary, len(text_array)

def sort_and_prune(dictionary):
    # print(dictionary.items())
    # print(dictionary)
    list_of_dictionaries = []
    for key, value in dictionary.items():
        if key.isalpha():
            list_of_dictionaries.append({"letter" : key, "num": value})
    # print(list_of_dictionaries.sort(key = lambda x : x["num"], reverse=True))
    sorted_dict = sorted(list_of_dictionaries, reverse = True, key= lambda x: x["num"])
    # sorted_dict = list_of_dictionaries.sort(reverse = True, key=list_of_dictionaries["num"])
    return(sorted_dict)