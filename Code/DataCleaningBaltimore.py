import csv

"""
This is to open a writer file to skip the unwanted data rows
and copy the rest to the file.
"""
ofile  = open('D:\RIT\SEM3\Big Data\project\dataset\\baltimoreFilter.csv', "w")
# file writer handle
writer = csv.writer(ofile, delimiter=',', lineterminator='\n')

"""
this code opens the file as a read only mode and reads it row by row.
The processing of the data is done on these rows.
"""
with open('D:\RIT\SEM3\Big Data\project\dataset\\baltimore.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    count = 0
    flag  =1
    rcount=0

    #for all the rows in the dataset "2.8" Million
    for row in spamreader:
        rcount = rcount+1
        flag = 1

        #select the elements which do not have data fields
        for elem in row:
            if (len(elem) < 1):
                #print(row)
                count = count + 1
                #set the flag as zero to skip the addition of the row
                flag =0

        if(flag== 1):

            #write it to the file if the row is not marked for deletion
            writer.writerow(row)

    # printing the deleted row to confirm
    print(count)
    print(rcount)