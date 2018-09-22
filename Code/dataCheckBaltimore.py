import csv

"""
opening the file to read. these functions are used to get the details and of the data
"""
def function2():
    with open('D:\RIT\SEM3\Big Data\project\dataset\\baltimore.csv', 'r') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=',')
         count = 0
         hashSet = {}
         rcount = 0

         # for all the rows in the dataset "2.8" Million
         for row in spamreader:
             rcount = rcount + 1
             if row[4] in hashSet:
                 print("not primary")
             hashSet[row[4]] = 0


"""
opening the file to read. This is then used to populate all the details required
"""
def function1():
     with open('D:\RIT\SEM3\Big Data\project\dataset\\baltimore.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        count = 0
        hashSet = {}
        rcount = 0

        # for all the rows in the dataset "2.8" Million
        for row in spamreader:
            rcount = rcount + 1
            if row[2] in hashSet:
                pass
            hashSet[row[2]] = 0

        print(hashSet)



