dict_manager = {}
while True:
    print('\navailable dictionaries:')
    if dict_manager:
        for name in dict_manager:
            print('-' ,name)
    else:
        print('no dictionaries yet')
    choice = input('\nenter the name of the dictionary or type {{new }} to create a new one or {{quit}} to exit').strip().lower()
    if choice == 'quit':
        print('exiting program')
        break
    elif choice == 'new':
        new_name = input('enter a name for the dictionary:').strip()
        if new_name in dict_manager:
            print('thers a dictionary with that name')
        else:
            dict_manager[new_name] = {}
            print(f'created a new dictionary\'{new_name}\'')
    elif choice in dict_manager:
        key = input('enter a key')
        value = input('enter a value')
        dict_manager[choice][key] = value
        print(f'added\'{key}:{value}\' to \'{choice}\'')
    else:
        print('dictionary not found ')

