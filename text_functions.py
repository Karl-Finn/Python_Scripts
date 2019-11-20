def format_txt_file_as_list(file):
    """Takes a text file as input and returns a list
            of each word from the file (Duplicates are allowed)
        Note: hyphened words will NOT be treated as distinct words.
            The hyphen will be removed and the words will be taken seperately.
        """
    file_formatted = file.lower() \
        .replace(",", "") \
        .replace("-", " ") \
        .replace(".", "") \
        .replace("\n\n", " ")
    word_list = file_formatted.split()
    return word_list


def get_text_file_from_net(text_url):
    """Takes a URL of a text file that is on the web as
        a string and returns the text file as a string
        using the Request Library."""
    try:
        import requests
        retrieve = requests.get(text_url)
        text_file_str = retrieve.text
        return text_file_str
    except Exception as err:
        print(f"Error occurred: {err}")


def unique_words_list(checklist, exclude_list):
    """Takes two lists of words as input.
        Param 1: a list of words which will be checked against Param 2
        Param 2: a second list of words
        Output: A list of words from Param 1 that do NOT appear in Param 2
    """
    unique = [word for word in checklist if word not in exclude_list]
    return unique


def word_hist(word_list):
    """
    :param word_list: a list of words
    :return: a dictionary histogram of each word and how many times it appears in wordList
    """
    hist = dict()
    for word in word_list:
        if word not in hist:
            hist[word] = 1
        else:
            hist[word] += 1
    return hist
