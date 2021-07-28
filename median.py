import csv 
with open('height-weight.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
#sorting data to get the height of people
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))
#getting the mean
n= len(new_data)
new_data.sort()
#using float division to get the nearest whole number
#float division is shown by //
if n % 2== 0:
    #getting the first number
    median1=float(new_data[n//2])
    #getting the second number
    median2=float(new_data[n//2-1])
    #getting mean of those number
    median=(median1+median2)/2
else:
    median=new_data[n//2] 
    print(n)
print("median is :"+str(median))
       
