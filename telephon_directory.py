def find_num(name):
    print(name, ":", d[name])


def replace_num(name, num):
    d[name] = num
    print("Directory is updated\n", name, ":", d[name])


def replace_name(name, num):
    for key, value in d.items():
        if num == value:
            d[name] = d[key]
            del d[key]
            break
    print("Directory is updated\n", name, ":", d[name])


d = {'Rahul':  4536752067,
     'Tushar': 6956542475,
     'Rajiv':  5439627979,
     'Pratik': 4857952545,
     'Sriti':  6890392545,
     }

find_num('Pratik')
replace_num('Rahul', 9546776254)
replace_name('Ishani', 5439627979)