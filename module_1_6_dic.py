my_dic = {'Denis': 1964, 'Max': 1998, 'Jane': 2001}
print(my_dic)
print('Existing date: ', my_dic['Denis'])
print('Not Existing date: ', my_dic.get('Kate'))
my_dic.update({'Kate': 2005, 'Petr': 1987})
a = my_dic.pop('Max')
print('Delited date: ', a)
print('Modified dictionry: ', my_dic)
print('')
my_set={1,3,5,8,3,2,5,77, 'Radio', (1,2,4,5,)}
print('Set: ', my_set)
my_set.add(13)
my_set.add('Home')
my_set.discard(2)
print('Modified set: ',my_set)
