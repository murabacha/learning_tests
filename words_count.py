phrase=input('enter your phrase please\n ')
words=phrase.split()
words_count = len(words)
sub = input('enter the word you need to search \n')
count = phrase.count(sub)

if words_count == 0:
    print('no phrase')
else:
    print(f'there are {words_count} words')

if count == 0:
    print(f'{sub} does not exist on this phrase')

else:
    print(f'there are {count} {sub} words out of {words_count} words ') 

