#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd


class search:
	def search_end(self, index, columns, pk,pf):
		if len(index) == 1:
			return pk
		for j in columns:  # 找出不等价的
			for i in index:
				# print(i,j,pk.ix[i, j])
				if pk.ix[i, j] not in index and pk.ix[i, j] != 'none':
					index.remove(i)
		if len(index) >= 2:
			t = index.pop()
			ks = index.copy()
			if index:
				for i in index:
					pf.replace(i, t, inplace=True)  # 将等价状态用一个表示\
			if len(ks) >= 1:
				for i in columns:
					for j in ks:
						if pk.ix[t, i] == 'none' and pk.ix[j, i] != 'none':
							x = pk.ix[t, i]
							y = pk.ix[j, i]
							pk.ix[t, i] = y
		pk.drop_duplicates(columns, inplace=True)  # 删除重复项'''
		return pk
	def ifilter(self,pf):
		columns = list(pf.columns)  # 获取列名
		k = list(pf[columns[0]])  # 获取第一列的所有元素
		pf.index = k
		pf.drop(columns[0], axis=1, inplace=True)
		return pf
		
		

if __name__ == "__main__":
	pf = pd.read_csv('dfa.csv')
	op = search()
	print(pf)
	columns = list(pf.columns)  # 获取列名
	k = list(pf[columns[0]])  # 获取第一列的所有元素
	pf.index = k
	pn = pf.filter(like='_', axis=0)  # 过滤出末态的行
	pj = pf.append(pn)
	pn=op.ifilter(pn)
	#print(pj.index.is_unique)  判断是否重复行
	pj = pj.drop_duplicates(subset=columns, keep=False)    #keep 是否保留第一次出现的重复行
	pj = op.ifilter(pj)
	pf.drop(columns[0], axis=1, inplace=True)
	stack1 = []  # 终态
	stack2 = []  # 非终态
	while k:
		s = k.pop()
		l = len(s)
		if s[l - 1] == '_':
			stack1.append(s)
		else:
			stack2.append(s)
	columns = list(pf.columns)
	pn = op.search_end(stack1, columns,pn,pf)
	print(pn)
	pj = op.search_end(stack2, columns, pj,pf)
	print(pj)
	pf.to_csv('mindfa.csv')
