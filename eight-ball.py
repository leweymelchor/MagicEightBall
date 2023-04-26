is_workday = True
is_sunny = False

def gear_for_day(is_workday, is_sunny):
    needs = []

    if is_workday:
        needs.append("laptop")
    elif is_workday is False and is_sunny is False:
        needs.append("umbrella")
    elif is_workday is False and is_sunny:
        needs.append("surfboard")
    else:
        pass

    return needs

print(gear_for_day(is_workday, is_sunny))