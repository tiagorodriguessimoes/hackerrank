"""
We define a word as a non-empty maximum sequence of characters that can contain only lowercase letters, uppercase letters, digits and underscores '_' (ASCII value 95). Maximum sequence means that the word has to be immediately preceeded by a character not allowed to occur in a word or by the left boundary of the sentence, and it has to be immediately followed by a character not allowed to occur in a word or by the right boundary of the sentence.

Given sentences and words, for each of these words, find the number of its occurences in all the sentences.

Input Format

In the first line there is a single integer . Each of the next lines contains a single sentence. After that, in the next line, there is a single integer denoting the number of words. In the -th of the next lines, there is a single word denoting the -th word for which, you have to find the number of its occurences in the sentences.

Constraints


Output format

For every word, print the number of occurrences of the word in all the N sentences listed.

Sample Input

1
foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo.
1
foo

Sample Output

6

Explanation

    foo is the first word
    (foo) is preceeded by '(' and followed by ')', so it's the second word.
    foo-bar is considered as two words and 'foo' is the first of them. It is preceeded by a space and followed by a hyphen '-'
    bar-foo also contains foo for the same reason mentioned above
    foo_bar is a single single word and hence foo in it is not counted
    foo'bar is considered as two words and 'foo' is the first of them. It is preceeded by a space and followed by a apostrophe "'"
    foo. as it is preceeded by a space and followed by a dot'.'

"""

import re
from collections import Counter

def main():
    # Validate input
    N = raw_input()
    N = int (N)
    assert (N >= 1 and N <= 100), "Input must be between 1 and 100."
    sentences = ""
    for i in xrange(N):
        sentence = raw_input()
        sentences += ' ' + sentence

    T = raw_input()
    T = int (T)
    assert ( T >= 1 and T <= 10), "Input must be between 1 and 10."
    words_to_find = []
    for i in xrange(T):
        word = raw_input()
        words_to_find.append(word)

    words_list = sentence_split(sentences)
    cnt = Counter(words_list)

    for i in words_to_find:
        print(cnt[i])

def sentence_split(s):
    regex = r'[A-Za-z0-9\_]*'
    words_list = re.findall(regex, s)
    return words_list

if __name__ == '__main__':
    main()
