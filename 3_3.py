user_list ={}


def thesaurus(*names):
    for name in names:
        if name[0] in user_list:
            user_list[name[0]].append(name)
        else:
            user_list [name[0]] = [name]

    return user_list

print(thesaurus("Иван", "Мария", "Петр", "Илья"))
