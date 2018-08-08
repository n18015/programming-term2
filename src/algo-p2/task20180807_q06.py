fruits = {'apple': 'りんご', 'banana': 'バナナ', 'grape': 'ぶどう'}

for name in fruits.keys():
    i = fruits[name]
    s = "{0}は{1}という意味です".format(name, i)
    print(s)
