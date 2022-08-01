def Synthesize(text_input, parse=False):
    if parse:
        import re
        text = text_input
        new_words = []
        for word in text:
            w = re.sub(r'[^\w\s]','',word) #remove everything except words and space
            w = re.sub(r'_','',w) #how to remove underscore as well
            new_words.append(w)
        return ''.join(new_words)
    else:
        return text_input

