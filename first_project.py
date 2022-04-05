# First

flatten_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_list = list()

def flatten(x):
    for i in x:
        if isinstance(i,list):
            flatten(i)
        else:
            new_list.append(i)

flatten(flatten_list)
print(new_list)

# Second

reverse_flatten_list = [[1, 2], [3, 4], [5, 6, 7]]
new_list = list()

def reverse_flatten(x):
    for i in x[::-1]:
        if isinstance(i,list):
            new_list.append(i[::-1])
       
reverse_flatten(reverse_flatten_list)
print(new_list)
