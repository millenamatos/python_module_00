def ft_recursive_util(current_day, harvest_day):
    if current_day <= harvest_day:
        print("Day", current_day)
        current_day += 1
        ft_recursive_util(current_day, harvest_day)


def ft_count_harvest_recursive():
    harvest_day = int(input("Days until harvest: "))
    current_day = 1
    ft_recursive_util(current_day, harvest_day)
    print("Harvest time!")
