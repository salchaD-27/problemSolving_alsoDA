# class Solution:
#     def invalidTransactions(self, transactions):    
#         r = {}
#         inv = []        
#         for i in transactions:
#             split = i.decode("utf-8").split(",")
#             name = str(split[0])
#             time = int(split[1])
#             amount = int(split[2])
#             city = str(split[3])
#             if time not in r: r[time] = {name: [city]}
#             else:
#                 if name not in r[time]: r[time][name]=[city]
#                 else: r[time][name].append(city)
                    
#         for i in transactions:
#             split = i.decode("utf-8").split(",")
#             name = str(split[0])
#             time = int(split[1])
#             amount = int(split[2])
#             city = str(split[3])
#             if amount > 1000:
#                 inv.append(i)
#                 continue
#             for j in range(time-60, time+61):
#                 if j not in r: continue
#                 if name not in r[j]: continue
#                 if len(r[j][name]) > 1 or (r[j][name][0] != city):
#                     inv.append(i)
#                     break               
#         return inv       

from collections import defaultdict
class Solution(object):
    def invalidTransactions(self, transactions):
        invalid = []
        # Record all transactions done at a particular time
        #   including the person and the location.
        transaction_time = defaultdict(dict)
        for transaction in transactions:
            name, str_time, amount, city = transaction.split(",")
            time = int(str_time)
            if name not in transaction_time[time]: transaction_time[time][name] = {city, }
            else: transaction_time[time][name].add(city)

        for transaction in transactions:
            name, str_time, amount, city = transaction.split(",")
            time = int(str_time)
            # # check amount
            if int(amount) > 1000:
                invalid.append(transaction)
                continue
            # # check if person did transaction within 60 minutes in a different city
            for inv_time in range(time-60, time+61):
                if inv_time not in transaction_time: continue
                if name not in transaction_time[inv_time]: continue
                trans_by_name_at_time = transaction_time[inv_time][name]
                if city not in trans_by_name_at_time or len(trans_by_name_at_time) > 1:
                    invalid.append(transaction)
                    break
        return invalid