#name = "samy"
#if name == "sam":
 #  print('hello sam')

#else:
 #   print('how are you')
#statement2 = ('''how is your "mother " is she fine 
# ''')
#print (statement2)
name = 'i am robert thuo '
name2 = 'i am Robert Thuo'
print (f"{name}{name2}")
print ((name.split(' ', maxsplit=5)) + (name2.split(' ' , maxsplit=10)) )
print((f'{name}') == (f'{name2}'))
print(('{0}') == ('{1}').format(name, name2))
print (('%s'%(name))<('%s'%(name2)))

if (('%s'%(name))<('%s'%(name2))):
    print("hello")
else:
    print('ooh no')
print(name.replace('thuo','kung\'u'))
print("{}".format(name2).count('o') )
print(f'{name}'.islower())
