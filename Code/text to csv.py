fh = open("C:\\Users\\kolev\\Documents\\v3.txt", "r")
sql = open("C:\\Users\\kolev\\Documents\\v3_SQL.txt", "w")

col = []
col = fh.readline().strip() .split(",")
data = []
data2 = []
data2.append("CREATE TABLE IF NOT EXISTS TABLE_NAME(\
  key VARCHAR(100),\
  dno DECIMAL(10, 2),\
  pno DECIMAL(10, 2),\
  desc VARCHAR(100),\
  date DECIMAL(10, 2),\
  time VARCHAR(100),\
  loc VARCHAR(100),\
  lon DECIMAL(10, 2),\
  lat DECIMAL(10, 2)\
);")

sql.writelines(data2)

count=1

for line in fh:

    data = line.strip().split(",")
    data2=[]
    data2.append("INSERT INTO EMR(key, dno, pno, desc, date, time, loc, lon, lat) VALUES (")
    data2.append("'"+data[0]+"'")
    data2.append(",")
    data2.append(data[1])
    data2.append(",")
    data2.append(data[2])
    data2.append(",")
    data2.append("'"+data[3]+"'")
    data2.append(",")
    data2.append(data[4])
    data2.append(",")
    data2.append("'"+data[5]+"'")
    data2.append(",")
    data2.append("'"+data[6]+"'")
    data2.append(",")
    data2.append(data[7])
    data2.append(",")
    data2.append(data[8])
    data2.append(")\n")

    sql.writelines(data2)
    count = count+1
    if(count%100000==0):
        print(count)

print(count)

