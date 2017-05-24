#import Stack


from Stack.linkedstack import LinkedStack

class Palindrom():
    def __init__(self):
        self._words = []

    def read(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            for el in f.readlines():
                el = el.split()[0]
                if '/' in el:
                    el = el[:el.index('/') - 1]
                self._words.append(el)



    @staticmethod
    def is_word_Pal(word):
        stack = LinkedStack()
        l = len(word)

        for i in range(l // 2):
            stack.push(word[i])
            # print(let)
        for i in range((l+1)//2, l):
            if word[i] != stack.peek():
                return False
            else:
                stack.pop()
        #print(word)
        return True

    def find_palindrome_write(self, file):
        with open(file, 'w', encoding='utf-8') as f:
            for el in self._words:
                if Palindrom.is_word_Pal(el):
                    #print(el)
                    f.write(el+'\n')

                # print(el)

d = Palindrom()
d.read('words.txt')
#print(d._words)

d.find_palindrome_write('pol_en.txt')