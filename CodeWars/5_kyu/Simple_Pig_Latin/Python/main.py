
def pig_it(text):
    result = text.split(" ")
    for i in range(len(result)):
        if result[i].isalpha():
            result[i] += result[i][0]
            result[i] = result[i][1:] + 'ay'

    return " ".join(result)
