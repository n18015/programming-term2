# 所持金からりんごが買えるかどうか判断しよう(if,elif,elseステートメントを使ってみよう)
apple_price = 200

money = 1000

input_count = input('購入するりんごの個数を入力してください：')
count = int(input_count)
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')



if money > total_price :
    print('りんごを' + str(count) + '個買いました 残金は' + str(money - total_price) + '円です')
# おつりがなければ、買った個数を「りんごを(個数)個買いました」と表示し、「財布が空になりました」と表示してください。
# 所持金と支払い金額が「等しければ」りんごが買えて残金が残りません。
if money == total_price:
    print('りんごを' + str(count) + '個買いました')
    print('財布が空になりました')


else:
    print('お金が足りません りんごを買えませんでした')
