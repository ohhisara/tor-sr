#script para analisar o ficheiro stats.tor.json (resulta da aplicacao do parser tor ctl aos hosts)
# host:
#   send_bytes: 
#       {0...1646}
#   written_bytes: 
#       {0...1646}
import pandas as pd 
import matplotlib.pyplot as plt

main_dict = eval(open("/home/sara/Desktop/Meh/SR/shadow/shadow-plugin-tor/tools/stats.tor.json").read())

d = {}
names = []
i=0
for x,item in main_dict.items():
    for y, values in item.items():
        names.insert(i,str(y))
        d[y] = pd.DataFrame(values)

result = pd.concat(d,keys=names)
print result
result.to_csv('out_tor_stats.csv')
    