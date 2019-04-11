change = {}
while True:
    try:
        cost = float(input("Cost: "))
    except:
        print('Invalid input')
        continue
    else:
        break

while True:
    try:
        paid = float(input("Paid: "))
    except:
        print('Invalid input')
        continue
    else:
        break

change_to_return = paid - cost

def convert_to_50k(amount,change):
    if int(amount/50000) > 0:
        change['50.000'] = int(amount/50000)
        return ((amount%50000),change)
def convert_to_10k(amount,change):
    if int(amount/10000) > 0:
        change['10.000'] = int(amount/10000)
        return ((amount%10000), change)
def convert_to_5k(amount, change):
    if int(amount/5000) > 0:
        change['5000'] = int(amount/5000)
        return ((amount%5000), change)
def convert_to_1k(amount, change):
    if int(amount/1000) > 0:
        change['1000'] = int(amount/1000)
        return ((amount%1000), change)
def convert_to_500(amount, change):
    if int(amount/500) > 0:
        change['500'] = int(amount/500)
        return ((amount%500), change)
def convert_to_200(amount, change):
    if int(amount/200) > 0:
        change['200'] = int(amount/200)
        return ((amount%200), change)
def convert_to_100(amount, change):
    if int(amount/100) > 0:
        change['100'] = int(amount/100)
        return ((amount%100), change)

if isinstance(convert_to_50k(change_to_return, change), tuple):
    change_to_return, change = convert_to_50k(change_to_return, change)
if isinstance(convert_to_10k(change_to_return, change), tuple):
    change_to_return, change = convert_to_10k(change_to_return, change)
if isinstance(convert_to_5k(change_to_return, change), tuple):
    change_to_return, change = convert_to_5k(change_to_return, change)
if isinstance(convert_to_1k(change_to_return, change), tuple):
    change_to_return, change = convert_to_1k(change_to_return, change)
if isinstance(convert_to_500(change_to_return, change), tuple):
    change_to_return, change = convert_to_500(change_to_return, change)
if isinstance(convert_to_200(change_to_return, change), tuple):
    change_to_return, change = convert_to_200(change_to_return, change)
if isinstance(convert_to_100(change_to_return, change), tuple):
    change_to_return, change = convert_to_100(change_to_return, change)
print(change, change_to_return)
