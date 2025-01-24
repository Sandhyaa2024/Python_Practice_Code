main_str = input()
sub_str = input()


def count_substring(main_str, sub_str):
    c = 0
    for i in range(len(main_str)):
        if (main_str[i:len(sub_str)+i] == sub_str):
            c += 1
    return c

