
# Exercise 1:

f = open('cigs.csv', 'rb')
reader = csv.reader(f)
index = 0
for row in reader:
    if index != 0:
        print row
    index += 1
f.close()

#  Exercise 2


import csv
f = open('cigs.csv', 'rb')
reader = csv.reader(f)
rownum = 0
weight = []
vol = []
for row in reader:
    if rownum == 0:
        header = row
    else:
        print "row = ", row
        r = map(str, row[0].split())
        print "formated row = ", r
    rownum += 1
f.close()



import csv
f = open('cigs.csv', 'rb')
reader = csv.reader(f)
rownum = 0
tar = []
nicotine = []
for row in reader:
    if rownum == 0:
        header = row
    else:
        r = map(str, row[0].split())
        tar.append(r[1])
        nicotine.append(r[2])
    rownum += 1
 
print "Tar = ", tar
print "Nicotine = ", nicotine
f.close()

# Exercise 3: matplotlib: an easy plot/ Exercise 4: axes labels


from pylab import*
fig = plt.figure()
scatter (tar, nicotine)
fig.savefig("cig_scatter.png")



fig = plt.figure()
plot (tar, nicotine)
fig.savefig("cig_scatter_plot.png")


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('')
ax.set_xlabel('Tar (mg)')
ax.set_ylabel('Nicotine (mg)')
ax.scatter(tar, nicotine)
fig.savefig("cig_scatter_label.png")



fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('')
ax.set_xlabel('Tar (mg)')
ax.set_ylabel('Nicotine (mg)')
ax.plot(tar, nicotine)
fig.savefig("cig_scatter_label_plot.png")



