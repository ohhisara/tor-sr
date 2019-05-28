#script para analisar o ficheiro stats.shadow.json (resulta da aplicacao do shadow parser a shadow.log)
# host:
#       recv:
#           bytes_*: 
#               {0...1799}
#        send:
#           bytes_*:
#               {0...1799}
import pandas as pd 
import matplotlib.pyplot as plt

main_dict = eval(open("/home/sara/Desktop/Meh/SR/shadow/src/tools/stats.shadow.json").read())
d = {}
names = []
i=0
for x,item in main_dict.items():
    for y, values in item.items():
        names.insert(i,str(y))
        for z,byte_info in values.items()
            d[y] = pd.DataFrame(byte_info)

result = pd.concat(d,keys=names)
print result
result.to_csv('out_shadow_stats.csv')