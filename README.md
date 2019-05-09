# re-nfa-dfa-mindfa
正则文法
post类：
contacts函数：将正则表达式的 几种状态进行封装，再整体压回栈中，最终形成了一个整个的nfa关系栈，利用了dataframe的结构代替了图栈结构，比较节约时间和精力
postread函数：
根据开头规定的优先级入栈出栈传送给contacts函数，并将结果导出到表格nfa.csv（表格形式更清晰）
nfa_todfa类：
stac函数：
进行遍历前预处理，将dataframe三列（起点，权，终点）提取并传入函数
search函数：
寻找空可以到达的集合，遍历列表遇到空则传入函数build处理，并将返回的集合存入新的dfa表中
build——e函数：
 遍历并合并集合，返回从一个节点可以到达的所有包括空的顶点
search -end函数：
去掉多于状态
analyse:分析程序

（运行过程中生成的nfa,dfa，mindfa均输出为表格形式，方便查看步骤）
