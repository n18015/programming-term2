items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')

    input_count = input()

    a = "購入する{0}の個数は{1}個です".format(item_name, input_count)
    print(a)

    count = int(input_count)

    total_price = items[item_name] * count

    z = "支払い金額は{0}円です".format(total_price)
    print(z)

