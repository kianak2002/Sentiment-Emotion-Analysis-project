# AL_Pro4import string

'''
    to make 4 dictionary and count the repetition 
    1- single word of positive (dic_pos_unigram)
    2- dual word of positive (dic_pos_bigram)
    3- single word of negative (dic_neg_unigram)
    4- dual word of negative (dic_neg_bigram)
'''


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

    '''
        count the repetition of each single word
    '''

    def count_unigram(self):
        for i in range(len(self.pos)):
            if self.pos[i] in self.dic_pos_unigram:
                self.dic_pos_unigram[self.pos[i]] += 1
            else:
                self.dic_pos_unigram[self.pos[i]] = 1
        # print(self.dic_pos_unigram)
        for i in range(len(self.neg)):
            if self.neg[i] in self.dic_neg_unigram:
                self.dic_neg_unigram[self.neg[i]] += 1
            else:
                self.dic_neg_unigram[self.neg[i]] = 1
        # print(self.dic_neg)
        # for i in self.dic_pos_unigram.keys():
        #     if i == 'why':
        #         print('why pos', self.dic_pos_unigram[i])
        # for i in self.dic_neg_unigram.keys():
        #     if i == 'why':
        #         print('why neg', self.dic_neg_unigram[i])
        # for i in self.dic_pos_unigram.keys():
        #     if i == 'did':
        #         print('did pos', self.dic_pos_unigram[i])
        # for i in self.dic_neg_unigram.keys():
        #     if i == 'did':
        #         print('did neg', self.dic_neg_unigram[i])

    '''
        decrease dictionary by removing the top 10 repetition and
        the words only were repeated one time and punctuations 
        in unigram dictionary
    '''

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

    '''
        count the repetition of each dual words
    '''

    def count_bigram(self):
        for i in range(len(self.pos) - 1):
            if str(self.pos[i] + ' ' + self.pos[i + 1]) in self.dic_pos_bigram:
                self.dic_pos_bigram[self.pos[i] + ' ' + self.pos[i + 1]] += 1
            else:
                self.dic_pos_bigram[self.pos[i] + ' ' + self.pos[i + 1]] = 1
        # print(self.dic_pos_bigram)
        for i in range(len(self.neg) - 1):
            if self.neg[i] + ' ' + self.neg[i + 1] in self.dic_neg_bigram:
                self.dic_neg_bigram[self.neg[i] + ' ' + self.neg[i + 1]] += 1
            else:
                self.dic_neg_bigram[self.neg[i] + ' ' + self.neg[i + 1]] = 1
        # print()
        # for i in self.dic_pos_bigram.keys():
        #     if i == 'why did':
        #         print('why did pos', self.dic_pos_bigram[i])
        # for i in self.dic_neg_bigram.keys():
        #     if i == 'why did':
        #         print('why did neg', self.dic_neg_bigram[i])

    '''
        decrease dictionary by removing the top 10 repetition and
        the words only were repeated one time and punctuations 
        in bigram dictionary
    '''

    def decrease_bigram(self):
        delete, list_delete = [], []
        counter = 0
        # print(len(self.dic_pos_bigram))
        for i in self.dic_pos_bigram.keys():
            if self.dic_pos_bigram[i] == 961 or self.dic_pos_bigram[i] == 720 or self.dic_pos_bigram[i] == 696 or \
                    self.dic_pos_bigram[i] == 615 or self.dic_pos_bigram[i] == 514 or self.dic_pos_bigram[i] == 477 \
                    or self.dic_pos_bigram[i] == 332 or self.dic_pos_bigram[i] == 296 or self.dic_pos_bigram[i] == 282 \
                    or self.dic_pos_bigram[i] == 262:
                print(i, self.dic_pos_bigram[i])
            # if i == 'why did':
            #     print('hiiiiiii')
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


'''
    to find out the comment is positive or negative 
'''


class calculator:
    def __init__(self, dic_pos_unigram, dic_neg_unigram, dic_pos_bigram, dic_neg_bigram, words):
        self.dic_pos_unigram = dic_pos_unigram
        self.dic_neg_unigram = dic_neg_unigram
        self.dic_pos_bigram = dic_pos_bigram
        self.dic_neg_bigram = dic_neg_bigram
        self.words = words

    '''
        to find the repetition of each single word and 
        dual word in positive dictionaries
    '''

    def count_w_pos(self):
        con_pos_bigram, pos_unigram = [], []
        M = 0
        for i in self.dic_pos_unigram:
            M += self.dic_pos_unigram[i]

        for i in range(1, len(words)):
            check = False
            for j in self.dic_pos_bigram:
                if words[i - 1] + ' ' + words[i] == j:
                    print(words[i - 1] + ' ' + words[i], self.dic_pos_bigram[j])
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

    '''
        to find the repetition of each single word and 
        dual word in negative dictionaries
    '''

    def count_w_neg(self):
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

    '''
        find the possibility of sentence being positive or 
        negative in bigram formula and chose the landas so 
        that landa1 + landa2+ landa3 = 1 and 0 < teta < 1  
    '''

    def possibility_bigram(self):
        landa3 = 0.6
        landa2 = 0.35
        landa1 = 0.05
        teta = 0.15
        multi_pos, multi_neg = 1, 1
        pos_unigram, con_pos_bigram, M_pos = self.count_w_pos()
        print('M pos', M_pos)
        for i in range(len(self.words) - 1):
            if pos_unigram[i] != 0:
                print(words[i])
                sub = landa3 * (con_pos_bigram[i] / pos_unigram[i]) + landa2 * (pos_unigram[i + 1] / M_pos) + (
                        landa1 * teta)
            else:
                sub = landa2 * (pos_unigram[i + 1] / M_pos) + (landa1 * teta)
            multi_pos *= sub
        if pos_unigram[0] != 0:
            multi_pos *= pos_unigram[0] / M_pos
        print('pos', multi_pos * 1000000)

        neg_unigram, con_neg_bigram, M_neg = self.count_w_neg()
        print('M neg', M_neg)
        for i in range(len(self.words) - 1):
            if neg_unigram[i] != 0:
                print(words[i])
                sub = landa3 * (con_neg_bigram[i] / neg_unigram[i]) + landa2 * (neg_unigram[i + 1] / M_neg) + (
                        landa1 * teta)
            else:
                print('jjjjj')
                sub = landa2 * (neg_unigram[i + 1] / M_neg) + (landa1 * teta)
            print(sub)
            multi_neg *= sub
        if neg_unigram[0] != 0:
            multi_neg *= neg_unigram[0] / M_neg
        print('neg', multi_neg * 1000000)

        return multi_pos, multi_neg

    '''
        find the possibility of sentence being positive or 
        negative in unigram formula
    '''

    def possibility_unigram(self):
        multi_pos, multi_neg = 1, 1
        pos_unigram, con_pos_bigram, M_pos = self.count_w_pos()
        for i in range(len(self.words)):
            multi_pos *= (pos_unigram[i] / M_pos)

        neg_unigram, con_neg_bigram, M_neg = self.count_w_neg()
        for i in range(len(self.words)):
            multi_neg *= (neg_unigram[i] / M_neg)

        return multi_pos, multi_neg


'''
    find all 4 dictionaries using other class 
    get input sentence and calculate unigram or bigram
    that the sentence is positive or negative.
'''
if __name__ == '__main__':
    dic = dictionary()
    dic.count_unigram()
    dic_pos_unigram, dic_neg_unigram = dic.decrease_unigram()
    print('\n\n')
    dic.count_bigram()
    dic_pos_bigram, dic_neg_bigram = dic.decrease_bigram()
    print('\n\n')
    while True:
        words = input().split()
        if words[0] != '!q':
            cal = calculator(dic_pos_unigram, dic_neg_unigram, dic_pos_bigram, dic_neg_bigram, words)
            print('1- unigram       2- bigram')
            choose = input()
            if choose == '1':
                multi_pos, multi_neg = cal.possibility_unigram()
                if multi_pos < multi_neg:
                    print('filter this')
                else:
                    print('not filter this')
            elif choose == '2':
                multi_pos, multi_neg = cal.possibility_bigram()
                if multi_pos < multi_neg:
                    print('filter this')
                else:
                    print('not filter this')
            else:
                print('wrong input')
                break
        else:
            break

