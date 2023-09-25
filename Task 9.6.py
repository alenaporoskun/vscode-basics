def generator_numbers(string=""):
    print(string)
    string = string.replace(":", "").replace(",", "").replace("$", "").replace(".", "").split()
    print(string)
    for i in string:
        try:
            yield int(i)
        except Exception:
            pass
        
def sum_profit(string):
    res = generator_numbers(string)
    sum = 0
    for i in res:
        sum += i
        print(i)
    print('sum ', sum)
    return sum
        
    
sum_profit(string="The resulting profit was: from the southern possessions $ 10, from the northern colonies $50, and the king gave $100")