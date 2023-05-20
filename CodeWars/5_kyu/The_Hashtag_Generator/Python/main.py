
def generate_hashtag(s):
    return f"#{''.join(list(map(lambda x: x.capitalize(), s.split())))}" if s and len(s) < 140 else False
