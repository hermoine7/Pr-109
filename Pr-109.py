import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()

mean=statistics.mean(data)
sd=statistics.stdev(data)
median=statistics.median(data)
mode=statistics.mode(data)

sd1Start=mean-sd
sd1End=mean+sd
sd2Start=mean-(2*sd)
sd2End=mean+(2*sd)
sd3Start=mean-(3*sd)
sd3End=mean+(3*sd)

sd1Data=[result for result in data if result>sd1Start and result<sd1End]
sd2Data=[result for result in data if result>sd2Start and result<sd2End]
sd3Data=[result for result in data if result>sd3Start and result<sd3End]

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
print("Standard Deviation: ", sd)
print("{} % of data lies in the 1 standard deviation".format(len(sd1Data)*100.0/len(data)))
print("{} % of data lies in the 2 standard deviations".format(len(sd2Data)*100.0/len(data)))
print("{} % of data lies in the 3 standard deviations".format(len(sd3Data)*100.0/len(data)))