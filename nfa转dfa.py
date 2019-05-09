#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
class nfa_todfa:
	def build_e(self, k, pf, start, delta, end):
		a = set()
		while len(k) != 0:
			t = k.pop()
			a.add(int(t))
			for i in range(pf.shape[0]):  # 按nfa行数循环
				if int(start[i]) == int(t) and delta[i] == '-':
					if end[i] not in a:  # 如果不在集合中在加入集合
						k.append(end[i])  # 入栈   循环下来
						a.add(end[i])  # 符合条件的节点入集合
					else:
						pass
				else:
					pass
		return a  # 将循环完的整个列表的闭包
	
	def search_set(self, a, b, c, col, allstart, pf):
		# 用于存储一行数据并存入nepf
		stack2 = []  # 用于存储不重复的需要查找的集合
		stack2.append(allstart)
		self.stack3 = []
		pk = pd.DataFrame(columns=col)
		while len(stack2) != 0:
			stack1 = []
			h = stack2.pop()
			h = list(h)
			self.stack3.append(h)
			stack1.append(h)
			for i in range(len(col) - 1):  # abc
				g = []
				for j in range(len(h)):  # 917
					for k in range(len(a)):  # 1423554656  12
						if col[i + 1] == b[k] and a[k] == h[j]:
							g.append(c[k])
				m = self.build_e(g, pf, a, b, c)  # 返回闭
				m = list(m)
				# if 10 in m:
				# m.append(0)
				if len(m) == 0:
					u = [1000000]
					stack1.append(u)
				elif m in self.stack3:
					stack1.append(m)
				elif m not in self.stack3:
					stack2.append(m)
					stack1.append(m)
			pk = pk.append(pd.DataFrame([stack1], columns=col))
		#
		return pk
	
	def stac(self, pf):
		set_a = set(pf['start'])
		set_b = set(pf['end'])
		start = (format(max(set_a - set_b)))
		global end
		end = (format(max(set_b - set_a)))  # print(start,end)          # 此处求出起始节点和终止节点
		column = set(pf.loc[pf['delta'] >= 'a', 'delta'])  # 取出a-z的字母  ？？？？？？？不全
		global col
		col = list(column)  # print(pf['start']==9,'end') 输出布尔值
		col.insert(0, 'start')
		stack1 = []
		stack1.append(start)
		a = pf['start']
		b = pf['delta']
		c = pf['end']
		allstart = self.build_e(stack1, pf, a, b, c)
		pk = self.search_set(a, b, c, col, allstart, pf)
		return pk
	
	def replaces(self):
		self.dict1 = {}
		for i, m in enumerate(self.stack3):
			l = m
			l = [str(x) for x in l]
			l = ','.join(l)
			if end in l:
				self.dict1[l] = str(i)+'_'
			else:
				self.dict1[l] =str(i)
		self.dict1['1000000'] = 'NaN'
	
	def func(self, s):
		l = []
		for x in s:
			l.append(str(x))
		return self.dict1[','.join(l)]

if __name__ == "__main__":
	sp = nfa_todfa()
	pf = pd.read_csv('datas.csv')  # 读取表格
	pk = sp.stac(pf)
	print(pk)
	sp.replaces()
	for i in col:
		pk[i] = pk[i].apply(lambda s: sp.func(s))
	u=pk.columns.values
	pk.drop_duplicates(u,inplace=True)
	pk.to_csv('dfa.csv', index=False)
	print(pk)
