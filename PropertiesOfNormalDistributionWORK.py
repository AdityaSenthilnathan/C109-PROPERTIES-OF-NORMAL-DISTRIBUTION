import statistics
from turtle import st
import plotly.figure_factory as ff
import pandas as pd
DataFrame = pd.read_csv('StudentsPerformance.csv')
dflist = DataFrame["reading score"].tolist()
stdev = statistics.stdev(dflist)
mean = statistics.mean(dflist)
mode = statistics.mode(dflist)
median = statistics.median(dflist)
startpnt = mean + stdev
endpnt = mean - stdev

num1 = 0

for a in dflist:
    if a < startpnt:
        if a > endpnt:
            num1 = num1 + 1

percent1 = (num1/(len(dflist) - 1)) * 100


startpnt2 = mean + stdev * 2
endpnt2 = mean - stdev * 2

num2 = 0

for a in dflist:
    if a < startpnt2:
        if a > endpnt2:
            num2 = num2 + 1

percent2 = (num2/(len(dflist) - 1)) * 100


startpnt3 = mean + stdev*3
endpnt3 = mean - stdev*3

num3 = 0


for a in dflist:
    if a < startpnt3:
        if a > endpnt3:
            num3 = num3 + 1

percent3 = (num3/(len(dflist) - 1)) * 100

print(percent1)
print(percent2)
print(percent3)


