# coding=utf-8
import random
import signal

class Game(object):
    """docstring for Game"""

    def __init__(self, times):
        super(Game, self).__init__()
        self.answer = 0
        self.count = 1
        self.times = times

    def randomanswer(self):
        self.answer = random.randrange(1, 10)
        lis = range(0, 10)
        lis.remove(self.answer)
        remain = random.sample(lis, 3)
        for i in remain:
            self.answer = self.answer * 10 + i

    def userinput(self):

        if self.count <= self.times:
            try:
                self.user_input = int(raw_input('请输入四位数:'))
            except Exception as e:
                print '输入格式不正确，请输入数字'
            else:
                if len(str(self.user_input)) == len(set(str(self.user_input))) and len(str(self.user_input)) == 4:
                    return self.ruler()
                else:
                    print '数值不能含有重复数字,或者数值长度不正确'
                # return True

    def ruler(self):
        self.fprint = ''
        i = 0
        self.count += 1
        while i < len(str(self.answer)):
            if str(self.answer).find(str(self.user_input)[i]) >= 0:

                if str(self.answer)[i] == str(self.user_input)[i]:
                    self.fprint = self.fprint + 'A'
                else:
                    self.fprint = self.fprint + 'B'
            i += 1
        self.fprint = ''.join(sorted(self.fprint))
        if self.fprint == '':
            self.fprint = '0000'
        if self.fprint == 'AAAA':
            print '恭喜过关'
            return True
        print self.fprint

    def showanswer(self):
        print 'answer:', self.answer
        # return self.answer

    def giveup(self, signum, frame):
        self.showanswer()
        exit()

    def rungame(self):
        '''
        调用rungame运行游戏,绑定giveup函数到ctr+z 信号上，当信号发生时跳出主程序，直接执行该函数
        '''
        signal.signal(signal.SIGTSTP, self.giveup)

        self.randomanswer()
        while True:
            if self.userinput() == True:
                self.showanswer()
                break

a = Game(15)
a.rungame()
