# third task
def thesaurus(*names):
    output_dict = {}
    for name in names:
        value = output_dict.get(name[0])
        if value is None:
            output_dict[name[0]] = [name]
        else:
            output_dict[name[0]].append(name)
    return output_dict


