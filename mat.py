import csv


w=5
h=32

matrix=[[0 for x in range(w)] for y in range(h)]



matrix[:][0] = 1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2


with open('some.csv', 'wb') as f:
    writer = csv.writer(f)
    for row in matrix:
        writer.writerow(row)



f.close()

