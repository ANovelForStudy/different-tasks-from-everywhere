
def increment_string(s):
    # separate the string into two parts - one without trailing digits and one with
    head, tail = s.rstrip('0123456789'), s[len(s.rstrip('0123456789')):]

    # check if tail contains any digits
    if tail:
        # get the length of tail and increment it by 1
        new_tail = str(int(tail) + 1)

        # check if the original tail had leading zeros
        if tail.startswith('0'):
            # prepend the required number of leading zeros to the new tail
            new_tail = new_tail.zfill(len(tail))
    else:
        # if tail is empty, initialize new_tail as '1'
        new_tail = '1'

    # return the concatenated string
    return head + new_tail
