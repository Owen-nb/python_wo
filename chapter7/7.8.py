from joblib import PrintTime


sandwiches_orders=['1','2','3','4','5']
sandwiches_finished=[]
i=0
while i<5:
    sandwiches_finished.append(sandwiches_orders[i])
    print(f"i made your {sandwiches_orders[i]}")
    i+=1

print ("all finished,there are")
for num in sandwiches_finished:
    print(num)

