'spam eggs' # 'spam eggs' single quotes
'doesn\'t' # "doesn't" escape single quotes

a = "baris1\n baris2" #new line
print(a)
# baris1
# baris2
print(r"C:\\files\name") # print row dan ga jadi new line


#string beda" indent
print("""\
bebas
	sdgasjdf
	 asdf
	 		afsdf
""")

#glued + repeat with * !behaviorjavascriptrepeat
3*'jaka'+'prima'
#jakajakajakaprima

#gabung tanpa operator !behaviorjavascript
'jaka' 'prima'
#jakaprima

#output string array data !behaviorjavascript
a = 'jako'
a[3] #k
a[-1] #o
a[1:3] #ak string ambil dari index 1 dan ambil 3-1 data setelahnya
a[:1] + a[3:] #jo


# length
len(a);


#tranverse
a[1::2] #ao
a[::-1] #okaj
