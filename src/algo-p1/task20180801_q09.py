# ifの条件に該当しなかった場合に、他の条件に該当するかをelifステートメントで判断してみよう
money = 100
apple_price = 100

if money > apple_price:
    print('りんごを買うことができます')

elif money == apple_price:
    print('りんごを買うことができますが所持金が0になります')

else:
    print('お金が足りません')
