"""
Написать функцию count_words, которая будет считать количество слов в тексте,
с учетом, что в начале могут быть пробелы, в конце могут быть пробелы, между слов
может встречаться больше одного пробела подряд.
"""
import re


def count_words(text):
    pattern = re.compile(r'\w+(-\w+)*')
    count = 0
    text1 = text.split()
    for i in text1:
        if pattern.match(i):
            count += 1
    return count
