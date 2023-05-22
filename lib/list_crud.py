def create_an_empty_list():
    return []

create_an_empty_list()


def create_a_list():
    my_list = []
    for i in range(4):
        element = input("Enter element {} for the list: ".format(i + 1))
        my_list.append(element)
    return my_list

my_list = create_a_list()
print(my_list)


def add_element_to_end_of_list(my_list, element):
    my_list.append(element)
    return my_list

new_element = int(input("Enter your last element: "))
updated_list = add_element_to_end_of_list(my_list, new_element)
print(updated_list)


def add_element_to_start_of_list(my_list, element):
    my_list.insert(0, element)
    return my_list

new_element = int(input("Enter your first element: "))
updated_list = add_element_to_start_of_list(my_list, new_element)
print(updated_list)


def remove_element_from_end_of_list(my_list):
    if len(my_list) > 0:
        my_list.pop()
    return my_list

updated_list = remove_element_from_end_of_list(my_list)
print(updated_list)


def remove_element_from_start_of_list(my_list):
    if len(my_list) > 0:
        del my_list[0]
    return my_list

updated_list = remove_element_from_start_of_list(my_list)
print(updated_list)


def retrieve_first_element_from_list(my_list):
    if len(my_list) > 0:
        return my_list[0]
    else:
        return None

first_element = retrieve_first_element_from_list(my_list)
print(first_element)


def retrieve_element_from_index(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return None

index = 2
element = retrieve_element_from_index(my_list, index)
print(element)


def retrieve_last_element_from_list(my_list):
    if len(my_list) > 0:
        return my_list[-1]
    else:
        return None

last_element = retrieve_last_element_from_list(my_list)
print(last_element)