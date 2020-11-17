import os
base_list = os.listdir('music')
transition = 0
first_list = []
second_list = []
first_two_elements_list = []
second_two_elements_list = []
old_name = []
new_name = []
for i in base_list:
    first_list = i.split(' - ')
    transition = first_list[0]
    first_two_elements_list.append(transition)
    transition = first_list[1]
    first_two_elements_list.append(transition)
for i in range(1, len(first_two_elements_list), 2):
    second_list = first_two_elements_list[i].split('.')
    transition = second_list[0]
    second_two_elements_list.append(transition)
    transition = second_list[1]
    second_two_elements_list.append(transition)
for i in range(len(base_list)):
    old_name.append(base_list[i])
for i in range(0, len(first_two_elements_list), 2):
    new_name.append(second_two_elements_list[i] + ' - ' + first_two_elements_list[i] + '.mp3')
for i in range(len(new_name)):
    os.rename('music/' + old_name[i], 'music/' + new_name[i])
