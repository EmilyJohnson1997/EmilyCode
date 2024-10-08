# func_py_sort_words_by_length.py
def func_py_sort_words_by_length(sentence):
    words = sentence.split()
    words.sort(key=len)
    return words
