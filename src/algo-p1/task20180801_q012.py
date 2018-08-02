# 購入するりんごの個数を、プログラム実行時に入力しよう。
apple_price = 200


input_count = input()


count = float(input_count)
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')
