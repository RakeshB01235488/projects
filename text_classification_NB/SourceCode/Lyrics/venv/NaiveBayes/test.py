'''strng="the quick brown fox jumps over the lazy dog."
test="Quick brown".lower()
words = strng.split()
for word in words:
    count = test.count(word.lower())
    print(count)'''
from stemming.porter2 import stem
tk = ['I', 'need', 'an', 'easy', 'friend', 'I', 'do,', 'with', 'an', 'ear', 'to', 'lend', 'I', "don't", 'think',
          'you', 'fit', 'this', 'shoe', 'I', 'do,', "won't", 'you', 'have', 'a', 'clue', "I'll", 'take', 'advantage',
          'while', 'You', 'hang', 'me', 'out', 'to', 'dry', 'But', 'I', "can't", 'see', 'you', 'every', 'night', 'Free',
          "I'm", 'standing', 'in', 'your', 'line', 'I', 'do', 'hope', 'you', 'have', 'the', 'time', 'I', 'do', 'pick',
          'a', 'number', 'too', 'I', 'do', 'keep', 'a', 'date', 'with', 'you', "I'll", 'take', 'advantage', 'while',
          'You', 'hang', 'me', 'out', 'to', 'dry', 'But', 'I', "can't", 'see']
for word in tk:
 print("wl="+word.lower())


content="my baby taught me how to be"
print(content.count(stem("baby".strip())))
print(stem(content))