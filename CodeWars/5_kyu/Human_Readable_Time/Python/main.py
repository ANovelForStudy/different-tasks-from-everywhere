
def make_readable(seconds):
    hours = seconds // (60 * 60)
    minutes = (seconds - (hours * 60 * 60)) // 60
    seconds = seconds - (hours * 60 * 60) - (minutes * 60)

    return "{:0>2}:{:0>2}:{:0>2}".format(hours, minutes, seconds)
