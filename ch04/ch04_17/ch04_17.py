def ispangram(s):
    letters = [chr(i) for i in range(97, 122+1)]
    s = list(s.lower())
    for letter in letters:
        if not letter in s:
            return False
    return True

if __name__ == '__main__':
    li = ['The quick brown fox jumps over the lazy dog.',
         'Does the quick brown fox jump over the lazy dog?',
         'Do big jackdaws love my sphinx of quartz?',
         'Yeah, I am your long-lost brother.']
    for s in li:
        print('"' + str(s) + '" a pangram?')
        print(str(ispangram(s)) + '\n')


'''
"The quick brown fox jumps over the lazy dog." a pangram?
True

"Does the quick brown fox jump over the lazy dog?" a pangram?
True

"Do big jackdaws love my sphinx of quartz?" a pangram?
True

"Yeah, I am your long-lost brother." a pangram?
False

'''
