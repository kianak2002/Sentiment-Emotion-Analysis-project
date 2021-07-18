import string
result = string.punctuation
print(result)

class dictionary:
    def __init__(self):
        f_pos = open('rt-polarity.pos', "r")
        txt_pos = f_pos.read().split()
        # print(txt_pos)
        self.pos = txt_pos

        f_neg = open('rt-polarity.neg', "r")
        txt_neg = f_neg.read().split()
        # print(txt_neg)
        self.neg = txt_neg
        self.dic_pos = {}
        self.dic_neg = {}

    def count(self):
        for i in range (len(self.pos)):
            if self.pos[i] in self.dic_pos:
                self.dic_pos[self.pos[i]] += 1
            else:
                self.dic_pos[self.pos[i]] = 1
        # print(self.dic_pos)
        for i in range (len(self.neg)):
            if self.neg[i] in self.dic_neg:
                self.dic_neg[self.neg[i]] += 1
            else:
                self.dic_neg[self.neg[i]] = 1
        # print(self.dic_neg)

    def decrease(self):
        delete, list_delete = [], []
        counter = 0
        for i in reversed(sorted(self.dic_pos.values())):
            if counter < 10:
                list_delete.append(i)
            counter += 1
        for i in self.dic_pos.keys():
            if self.dic_pos[i] == 1 or i in string.punctuation:
                delete.append(i)
            if self.dic_pos[i] in list_delete:
                delete.append(i)
        for x in delete:
            self.dic_pos.pop(x, None)

        print(self.dic_pos)


        delete, list_delete = [], []
        counter = 0
        for i in reversed(sorted(self.dic_neg.values())):
            if counter < 10:
                list_delete.append(i)
            counter += 1
        for i in self.dic_neg.keys():
            if self.dic_neg[i] == 1 or i in string.punctuation:
                delete.append(i)
            if self.dic_neg[i] in list_delete:
                delete.append(i)
        for x in delete:
            self.dic_neg.pop(x, None)

        print(self.dic_neg)



if __name__ == '__main__':
    dic = dictionary()
    dic.count()
    dic.decrease()




