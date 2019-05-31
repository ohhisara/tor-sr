#script para analisar o ficheiro stats.tor.json (resulta da aplicacao do parser tor ctl aos hosts)
# host:
#   send_bytes: 
#       {0...1646}
#   written_bytes: 
#       {0...1646}
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

main_dict = eval(open("/home/sara/Desktop/Meh/SR/shadow/shadow-plugin-tor/resource/tor-sr/final-results/stats.tor.json").read())

d = {}
names = []
i=0
for x,item in main_dict.items():
    for y, values in item.items():
        names.insert(i,str(y))
        i=i+1
        d[y] = pd.DataFrame(values)
        d[y].to_csv(str(y)+'.csv')

#conn = []
#j=0
#for y in d:
#    for x in d['torclient1'].bytes_written.values:
#        for z in d[y].bytes_read.values:
#            if x == z & not (y in conn):
#                conn.insert(j,y)
#                j=j+1
#print conn

#plt.plot(d['torclient1'].bytes_written)
#plt.show()
#plt.plot(d['middle1'].bytes_read)
#plt.show()


#print result




    