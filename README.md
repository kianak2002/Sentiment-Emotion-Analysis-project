# AL_Pro4
import string

class dictionary:
    def __init__(self):
        f_pos = open('rt-polarity.pos', "r")
        print(type(f_pos.readline()))
        txt_pos = f_pos.read().split()
        # print(txt_pos)
        self.pos = txt_pos

        f_neg = open('rt-polarity.neg', "r")
        txt_neg = f_neg.read().split()
        # print(txt_neg)
        self.neg = txt_neg
        self.dic_pos_unigram = {}
        self.dic_neg_unigram = {}
        self.dic_pos_bigram = {}
        self.dic_neg_bigram = {}

    def count_unigram(self):
        for i in range (len(self.pos)):
            if self.pos[i] in self.dic_pos_unigram:
                self.dic_pos_unigram[self.pos[i]] += 1
            else:
                self.dic_pos_unigram[self.pos[i]] = 1
        # print(self.dic_pos)
        for i in range (len(self.neg)):
            if self.neg[i] in self.dic_neg_unigram:
                self.dic_neg_unigram[self.neg[i]] += 1
            else:
                self.dic_neg_unigram[self.neg[i]] = 1
        # print(self.dic_neg)

    def decrease_unigram(self):
        delete, list_delete = [], []
        counter = 0
        for i in reversed(sorted(self.dic_pos_unigram.values())):
            if counter < 10:
                list_delete.append(i)
            counter += 1
        for i in self.dic_pos_unigram.keys():
            if self.dic_pos_unigram[i] == 1 or i in string.punctuation:
                delete.append(i)
            if self.dic_pos_unigram[i] in list_delete:
                delete.append(i)
        for x in delete:
            self.dic_pos_unigram.pop(x, None)

        # print(self.dic_pos_unigram)


        delete, list_delete = [], []
        counter = 0
        for i in reversed(sorted(self.dic_neg_unigram.values())):
            if counter < 10:
                list_delete.append(i)
            counter += 1
        for i in self.dic_neg_unigram.keys():
            if self.dic_neg_unigram[i] == 1 or i in string.punctuation:
                delete.append(i)
            if self.dic_neg_unigram[i] in list_delete:
                delete.append(i)
        for x in delete:
            self.dic_neg_unigram.pop(x, None)

        # print(self.dic_neg_unigram)
        return self.dic_pos_unigram, self.dic_neg_unigram

    def count_bigram(self):
        for i in range (len(self.pos)-1):
            if str(self.pos[i] + ' ' + self.pos[i + 1]) in self.dic_pos_bigram:
                self.dic_pos_bigram[self.pos[i] + ' ' + self.pos[i + 1]] += 1
            else:
                self.dic_pos_bigram[self.pos[i] + ' ' + self.pos[i + 1]] = 1
        # print(self.dic_pos_bigram)
        for i in range (len(self.neg)-1):
            if self.neg[i]+ ' ' + self.neg[i + 1] in self.dic_neg_bigram:
                self.dic_neg_bigram[self.neg[i] + ' ' + self.neg[i + 1]] += 1
            else:
                self.dic_neg_bigram[self.neg[i] + ' ' + self.neg[i + 1]] = 1
        # print()

    def decrease_bigram(self):
        delete, list_delete = [], []
        counter = 0
        for i in reversed(sorted(self.dic_pos_bigram.values())):
            if counter < 10:
                list_delete.append(i)
            counter += 1
        for i in self.dic_pos_bigram.keys():
            temp = i.split()
            if self.dic_pos_bigram[i] == 1 or temp[0] in string.punctuation or temp[1] in string.punctuation:
                delete.append(i)
            if self.dic_pos_bigram[i] in list_delete:
                delete.append(i)
        for x in delete:
            self.dic_pos_bigram.pop(x, None)

        # print(self.dic_pos_bigram)


        delete, list_delete = [], []
        counter = 0
        for i in reversed(sorted(self.dic_neg_bigram.values())):
            if counter < 10:
                list_delete.append(i)
            counter += 1
        for i in self.dic_neg_bigram.keys():
            if self.dic_neg_bigram[i] == 1 or i in string.punctuation:
                delete.append(i)
            if self.dic_neg_bigram[i] in list_delete:
                delete.append(i)
        for x in delete:
            self.dic_neg_bigram.pop(x, None)

        # print(self.dic_neg_bigram)

        return self.dic_pos_bigram, self.dic_neg_bigram
class calculator:
    def __init__(self, dic_pos_unigram, dic_neg_unigram, dic_pos_bigram, dic_neg_bigram, words):
        self.dic_pos_unigram = dic_pos_unigram
        self.dic_neg_unigram = dic_neg_unigram
        self.dic_pos_bigram = dic_pos_bigram
        self.dic_neg_bigram = dic_neg_bigram
        self.words = words

    def wi_con_pos(self):
        con_pos_bigram, pos_unigram = [], []
        M = 0
        for i in self.dic_pos_unigram:
            M += self.dic_pos_unigram[i]

        for i in range (1, len(words)):
            check = False
            for j in self.dic_pos_bigram:
                if words[i-1] + ' ' + words[i] == j:
                    print(words[i-1] + ' ' + words[i], self.dic_pos_bigram[j])
                    con_pos_bigram.append(self.dic_pos_bigram[j])
                    check = True
            if not check:
                con_pos_bigram.append(0)

        for i in range(len(words)):
            check = False
            for j in self.dic_pos_unigram:
                if words[i] == j:
                    print(words[i], self.dic_pos_unigram[j])
                    pos_unigram.append(self.dic_pos_unigram[j])
                    check = True
            if not check:
                pos_unigram.append(0)
        print(pos_unigram)
        print(con_pos_bigram)
        return pos_unigram, con_pos_bigram, M


    def wi_con_neg(self):
        con_neg_bigram, neg_unigram = [], []
        M = 0
        for i in self.dic_neg_unigram:
            M += self.dic_neg_unigram[i]

        for i in range(1, len(words)):
            check = False
            for j in self.dic_neg_bigram:
                if words[i - 1] + ' ' + words[i] == j:
                    print(words[i - 1] + ' ' + words[i], self.dic_neg_bigram[j])
                    con_neg_bigram.append(self.dic_neg_bigram[j])
                    check = True
            if not check:
                con_neg_bigram.append(0)

        for i in range(len(words)):
            check = False
            for j in self.dic_neg_unigram:
                if words[i] == j:
                    print(words[i], self.dic_neg_unigram[j])
                    neg_unigram.append(self.dic_neg_unigram[j])
                    check = True
            if not check:
                neg_unigram.append(0)
        print(neg_unigram)
        print(con_neg_bigram)
        return neg_unigram, con_neg_bigram, M

    def possibility(self):
        landa1 = 0.6
        landa2 = 0.35
        landa3 = 0.05
        teta = 0.15
        multi_pos, multi_neg = 1, 1
        pos_unigram, con_pos_bigram, M_pos = self.wi_con_pos()
        print('M pos', M_pos)
        for i in range(len(self.words)-1):
            if pos_unigram[i] != 0:
                print(words[i])
                sub = landa3*(con_pos_bigram[i]/pos_unigram[i]) + landa2*(pos_unigram[i+1]/M_pos) +(landa1 * teta)
            else:
                sub = landa2 * (pos_unigram[i + 1] / M_pos) + (landa1 * teta)
            multi_pos *= sub
        multi_pos *= pos_unigram[0]
        print(multi_pos)

        neg_unigram, con_neg_bigram, M_neg = self.wi_con_neg()
        print('M neg', M_neg)
        for i in range(len(self.words)-1):
            if neg_unigram[i] != 0:
                print(words[i])
                sub = landa3*(con_neg_bigram[i]/neg_unigram[i]) + landa2*(neg_unigram[i+1]/M_neg) +(landa1 * teta)
            else:
                sub = landa2 * (neg_unigram[i + 1] / M_neg) + (landa1 * teta)
            multi_neg *= sub
        multi_neg *= neg_unigram[0]
        print(multi_neg)

        return multi_pos, multi_neg




if __name__ == '__main__':
    dic = dictionary()
    dic.count_unigram()
    dic_pos_unigram, dic_neg_unigram = dic.decrease_unigram()
    print()
    dic.count_bigram()
    dic_pos_bigram, dic_neg_bigram = dic.decrease_bigram()
    words = input().split()
    cal = calculator(dic_pos_unigram, dic_neg_unigram, dic_pos_bigram, dic_neg_bigram, words)
    multi_pos, multi_neg = cal.possibility()
    if multi_pos < multi_neg:
        print('filter this')
    else:
        print('not filter this')




