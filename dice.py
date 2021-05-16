import random
import statistics
import plotly.figure_factory as ff

dice_result=[]
count=[]

for i in range(0,1000):
  dice1=random.randint(1,6)
  dice2=random.randint(1,6)
  dice_result.append(dice1+dice2)

print(dice_result)

mean=sum(dice_result)/len(dice_result)
print("The mean of dice dataset is ",mean)

median=statistics.median(dice_result)
print("the median of dice dataset is",median)

mode=statistics.mode(dice_result)
print("Mode of dice dataset is",mode)

std_deviation=statistics.stdev(dice_result)
print("standard deviation",std_deviation)

fig=ff.create_distplot([dice_result],["result" ],show_hist=False)
fig.show()
