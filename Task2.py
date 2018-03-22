"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""
calls_time = {}
for row in calls:
    if row[0] in calls_time:
        calls_time[row[0]] += int(row[3])
    else:
        calls_time[row[0]] = int(row[3])
    if row[1] in calls_time:
        calls_time[row[1]] += int(row[3])
    else:
        calls_time[row[1]] = int(row[3])

max_calls_time=max(zip(calls_time.values(),calls_time.keys()))
print("{} spent the longest time, {} seconds, on th phone during September 2016".format(max_calls_time[1],max_calls_time[0]))
