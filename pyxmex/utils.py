def range_from_list(list_obj, range_start, range_end):
    result_string = ''

    for idx, val in enumerate(list_obj):
        if idx >= range_start and idx <= range_end:
            result_string += val

    return result_string
