from ast import While


sandwich_orders = ['pastrami', 'veggie', 'grilled cheese', 'pastrami',
                   'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

# 任务：
# 1. 把所有 pastrami 从 sandwich_orders 里删掉，并打印一句 "pastrami is sold out"
# 2. 再把剩下的三明治逐个做出来，放进 finished_sandwiches
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")
print("pastrami is sold out")
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)