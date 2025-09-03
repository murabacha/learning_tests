#coffee shop ordering 
food_menu = [{'chapati':25},
             {'nyama choma1kg':200},
             {'matumbo 1kg':250},
             {'rice 1 plate':300},
             {'potatoes 1 plate':500},]
cart = {}

def menu():

    print('*******our menu*******')
    for i in range(len(food_menu)):
        for x,y in food_menu[i].items():
            print(i+1,x,'-',y)
    print('6 view cart')
    print('7 checkout')
    print('8 exit')
    selection = input('enter you choice\n')
    if selection in ['1', '2', '3', '4','5']:
        amount = int(input('how much do you want'))
        cart.update({amount : {food_menu[int(selection) - 1]}})
        print(cart)


menu()


    