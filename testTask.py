# Нашей компании нужно сгруппировать клиентов для АБ-тестов. Алгоритм группировки очень простой - взять ID клиента
# (состоит из 5-7 цифр, например 7412567) и найти сумму всех его цифр. Получившееся число и является номером группы,
# в которую входит данный клиент.
#
# Для того чтобы понять, насколько хорош такой простой алгоритм, тебе нужно написать следующие диагностические функции:
#
# Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если нумерация ID сквозная и
# начинается с 0. На вход функция получает целое число n_customers (количество клиентов).
#
# Функция, аналогичная
# первой, если ID начинается с произвольного числа. На вход функция получает целые числа: n_customers (количество
# клиентов) и n_first_id (первый ID в последовательности).


# function that gets group number by customer id
def group_number_by_id(customer_id: int):
    group_num = 0
    while customer_id:
        group_num, customer_id = group_num + customer_id % 10, customer_id // 10
    return group_num


def sort_and_count_customers(all_customers: list[int]):
    # dict of all groups as a key and count of their customers as values'
    groups_with_count_of_their_members = {}

    for c in all_customers:
        # let's get key of the dict by customer id according to group number
        g = f'group number {group_number_by_id(c)}'

        # case of new group of customers
        if g not in groups_with_count_of_their_members:
            groups_with_count_of_their_members.update({g: 1})
        # case when group for this customer already exists
        else:
            groups_with_count_of_their_members[g] += 1

    return groups_with_count_of_their_members


# actually it's just special case of second function
def number_of_each_group_members_1(n_customers: int):
    # list of all customers we are operating with
    all_customers = range(0, n_customers)

    return sort_and_count_customers(all_customers)


# we can give it overall functionality with default value of the second argument equal to zero
def number_of_each_group_members_2(n_customers: int, n_first_id: int = 0):
    # list of all customers we are operating with
    all_customers = range(n_first_id, (n_first_id + n_customers))

    return sort_and_count_customers(all_customers)


assert group_number_by_id(1) == 1
assert group_number_by_id(7642) == 19
assert number_of_each_group_members_1(5) == {'group number 0': 1,
                                             'group number 1': 1,
                                             'group number 2': 1,
                                             'group number 3': 1,
                                             'group number 4': 1}

assert number_of_each_group_members_2(19, 1) == {'group number 1': 2,
                                                 'group number 2': 2,
                                                 'group number 3': 2,
                                                 'group number 4': 2,
                                                 'group number 5': 2,
                                                 'group number 6': 2,
                                                 'group number 7': 2,
                                                 'group number 8': 2,
                                                 'group number 9': 2,
                                                 'group number 10': 1}

assert number_of_each_group_members_2(5, 654321) == {'group number 21': 1,
                                                     'group number 22': 1,
                                                     'group number 23': 1,
                                                     'group number 24': 1,
                                                     'group number 25': 1}

assert number_of_each_group_members_2(0, 7412567) == {}
