import time


days_month = [['01', '31'],['02','30']]

#days_month = [['01', '31'], ['02', '29'], ['03', '31'], ['04', '30'], 
#            ['05', '31'], ['06', '30'], ['07', '31'], ['08', '31'], 
#            ['09', '30'], ['10', '31'], ['11', '30'], ['12', '31']]

for i in range(len(days_month)):
    month = str(days_month[i][0])
    max_days = int(days_month[i][1])
    for j in range(1, (max_days + 1)):
        print('Month: ' + month + ' Day: ' + str(j))
    time.sleep(1)

