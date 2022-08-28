
def get_pattern_time_query(time_start: int, time_end: int) -> str:
    str_time1 = str(time_start)
    str_time2 = str(time_end)
    pattern = ''
    for i in range(len(str_time1)):
        if str_time1[i] == str_time2[i]:
            pattern += str_time1[i]
        else:
            break

    return pattern


def get_host(host):
    if 'http' in host[:4]:
        return host
    else:
        return 'http://' + host


if __name__ == '__main__':

    print(get_pattern_time_query(166151437, 166150000)) #166151