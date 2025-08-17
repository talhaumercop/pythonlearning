# # new_list=[n+1 for n in range(1,5)]
# # print(new_list)
# #
# import random
#
# names=['talha','rehman','azeem','tarjumaan']
# #
# # new_list=[name.upper() for name in names if len(name)>5]
# # print(new_list)
#
# new_dict={name:random.randint(1,20) for name in names}
# # passed_doct={name:value for (name,value) in new_dict.items() if value > 15}
# print(new_dict)

import pandas as pd

data=pd.read_csv('nato_phonetic_alphabet.csv')

new_dict={row.letter:row.code for (index,row) in data.iterrows()}
print(new_dict)

user_value=input('enter your name: ')

new_list=[letters for (key,letters) in new_dict.items() for i in user_value.upper() if key == i if key == i]
print(new_list)