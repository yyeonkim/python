menu={'banana':2000,'strawberry':1500,'blueberry':3000,'apple':1000}
print(menu)

def fruits(kind,many,much):
    print('I want to buy them.')
    print('Check please.')
    print(much)
    if much>menu[kind]*many:
        print('Here you are.',much-menu[kind]*many)

    elif much==menu[kind]*many:
        print('Thanks. Have a nice day.')

    else:
        print('You have to pay more.',menu[kind]*many-much)
