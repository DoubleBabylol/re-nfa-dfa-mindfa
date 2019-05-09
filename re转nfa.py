#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
operator_precedence ={
    '(':0,
    ')':0,
    '|':1,
    '.':2,
    '*':3
}
class post:
    def contacts(self,q,df,stack2):
        if q=='.':
            o=stack2.pop()
            p=stack2.pop()
            newstar={'start': p['end'], 'delta': ['-'], 'end': o['start']}
            df = df.append(pd.DataFrame(newstar))    #存入表格
            newop={'start': p['start'], 'delta': ['&'], 'end': o['end']}
            stack2.append(newop)   #运算结果压入中间栈
        elif q=='*':
            o=stack2.pop()
            newstar = {'start': o['end'], 'delta': ['-'], 'end': o['start']}
            df = df.append(pd.DataFrame(newstar))  # 循环情况存入表格
            newop = {'start': [self.k+1], 'delta': ['-'], 'end': o['start']}
            df = df.append(pd.DataFrame(newop))    #存  开头
            newos={'start':o['end'], 'delta': ['-'], 'end': [self.k+2]}
            df = df.append(pd.DataFrame(newos))   #村结尾
            newps = {'start': [self.k+1], 'delta': ['-'], 'end': [self.k+2]}
            df = df.append(pd.DataFrame(newps))   # 存入0个情况
            newsp={'start': [self.k+1], 'delta': ['&'], 'end': [self.k+2]}
            self.k = self.k + 2
            stack2.append(newsp)    #记录开头结尾押回中间栈
        else:
            o=stack2.pop()
            p=stack2.pop()
            newstar = {'start': [self.k+1], 'delta': ['-'], 'end': o['start']}
            df = df.append(pd.DataFrame(newstar))  # 存入表格
            newop1 = {'start': [self.k+1], 'delta': ['-'], 'end': p['start']}
            df = df.append(pd.DataFrame(newop1))  # 存入表格
            newop2 = {'start': o['end'], 'delta': ['-'], 'end': [self.k+2]}
            df = df.append(pd.DataFrame(newop2))  # 存入表格
            newop3 = {'start': p['end'], 'delta': ['-'], 'end': [self.k+2]}
            df = df.append(pd.DataFrame(newop3))  # 存入表格
            newstars = {'start': [self.k + 1], 'delta': ['&'], 'end': [self.k+2]}
            stack2.append(newstars)  #压入栈
            self.k=self.k+2
        return df
    def postread(self,s):
        stack1 =[]   #操作符栈
        stack2=[]     #字母中间站
          #结果栈
        skr = {'start': [0], 'delta': ['0'], 'end': [0]}
        df = pd.DataFrame(skr)
        self.k=0
        for i in s:
            if i not in operator_precedence:       #字母直接入栈
                star={'start': [self.k+1],
                      'delta':[i],
                      'end': [self.k+2]}
                stack2.append(star)
                df = df.append(pd.DataFrame(star))
                self.k=self.k+2
            else:
                if len(stack1) == 0:             #栈空直接入栈
                    stack1.append(i)
                else:
                    if i == '(':                     #左括号入栈
                        stack1.append(i)
                    elif i == ')':                 #右括号则回溯到左括号并合并左右括号，整体入栈
                        while stack1[-1] != '(':
                            q=stack1.pop()
                            df=self.contacts(q,df,stack2)    #k是记录序号 q为出栈的操作符，df为结果，stack2中间站
                        stack1.pop()
                    elif operator_precedence[i]>operator_precedence[stack1[-1]]:
                        stack1.append(i)
                    else:
                        while len(stack1)!=0 and operator_precedence[i]<operator_precedence[stack1[-1]]:
                            q=stack1.pop()
                            df=self.contacts(q, df, stack2)
                        stack1.append(i)
        while len(stack1)!=0:
            q = stack1.pop()
            df=self.contacts(q, df, stack2)
        df=df[['start','delta','end']]
        #df.index = range(df.shape[0])
        print(df)
        df.to_csv('datas.csv', sep=',', index=False)
if __name__ == "__main__":
    s='a.b*|c'
    op = post()
    p = op.postread(s)