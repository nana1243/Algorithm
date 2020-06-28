import datetime
from datetime import timedelta


def caltime(time: list):
    dt = time[0] + " " + time[1]
    end = datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')
    deltatime = (float(time[2][:-1]))
    start = end - timedelta(seconds=deltatime)
    start = start.hour*3600 + start.minute*60 + start.second
    end = end.hour*3600 + end.minute*60 + end.second
    return start, end


def parsing(line):
    line = line.split(" ")
    return line


def solution(lines):
    tmp = []
    s=set()
    for elm in lines:
        elm = parsing(elm)
        start, end = caltime(elm)
        s.add(start)
        s.add(end)
        tmp.append((start, end))

    minstarttime = min(s)
    maxendtime= max(s)


    d={t:0 for t in range(minstarttime,maxendtime+1)}

    for elm in tmp:
        for i in range(elm[0],elm[1]+1):
            d[i]=d[i]+1
            print(d)


    return d





lines=[
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
solution(lines)
