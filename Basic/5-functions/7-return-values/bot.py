def sum_weights(beep_weight, bop_weight):
    print("their sum weight is:",beep_weight + bop_weight)
    totalweight = beep_weight + bop_weight
    return totalweight
    
def calc_avg_weight(beep_weight, bop_weight):
    average = sum_weights(beep_weight, bop_weight)/2
    print("their ave weight is:",average)
    
def run():
    bot_one_weight = int(input("what is beep weight?\n"))
    bot_two_weight = int(input("what is bop weight?\n"))
    function = input("what function should i run? 'sum' or 'ave'\n")
    
    if function == "sum":
        sum_weights(bot_one_weight,bot_two_weight)
        
    elif function == "ave":
        calc_avg_weight(bot_one_weight,bot_two_weight)

run()