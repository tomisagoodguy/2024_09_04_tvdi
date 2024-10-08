
# code

```
import csv

students = []

with open('student.csv', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    #讀取行標題
    headers = next(csv_reader)
    #逐行讀取數據
    for row in csv_reader:
    # print(row)
        # student.append(row)
        # 使用zip函數將headers和row配對，轉換成字典
        student_dict = dict(zip(headers,row))
        students.append(student_dict)
 
for student in students:
     print(student)       
```

```
up_25 = [student for student in students if int(student['age'])>25]
print("年齡大於25歲的人:")

for student in up_25:
    print(student)
print(f"\n共有{len(up_25)}人年齡大於25歲")

```

```
with open('up_25.csv',mode='w',encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file,fieldnames=['name','age','city'])
    writer.writeheader()
    for student in up_25:
        writer.writerow(student)
        
    ```