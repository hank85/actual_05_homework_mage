# _*_ coding: utf-8 _*_
import sys
import os
if len(sys.argv) == 2:
    log_file = sys.argv[1]
else:
    log_file = input("pls input the log file path:")
if not os.path.isfile(log_file):
    print("日志文件不存在")
    sys.exit(1)

require_data = {}

with open(log_file, 'rt') as f:
    for line in f:
        line = line.strip().split()
        if line:
            data = (line[0], line[6], line[8])
            if data in require_data:
                require_data[data] += 1
            else:
                require_data[data] = 1

sort_data = sorted(require_data.items(), key=lambda asd: asd[1], reverse=True)
top_ten = sort_data[0:10]
for value in top_ten:
    print("{}: {}次".format(value[0], value[1]))
