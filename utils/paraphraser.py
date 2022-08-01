import random
import math
import openai
import textwrap


def outputPreprocessing(seed_text, preprocess=True) :
    if preprocess :
        # Wrap this text.
        wrapper = textwrap.TextWrapper(width=20)
        word_list = wrapper.wrap(text=seed_text)
        return ' '.join(word_list)


def parseInputFunction(input_text, parse_text) :
    if parse_text :
        seed_text = "Rewrite the following paragraph:\nParagraph: {}".format(input_text)
        return seed_text
    else:
        return input_text


def parseHyperparameters(hyperParamName, range_1, range_2, controller, parseHyperParam=True) :
    if hyperParamName == "temperature" :
        return random.choice([round(random.uniform(range_1, range_2), 3) for _ in range(controller)])
    elif hyperParamName == "max_tokens" :
        return math.ceil(random.choice([round(random.uniform(range_1, range_2), 3) for _ in range(controller)]))
    elif hyperParamName == "frequency_penalty" :
        return random.choice([round(random.uniform(range_1, range_2), 3) for _ in range(controller)])
    else:
        return None


def ParaphraserFunction(prompt_text, tonality) :

    openai.api_key = "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"

    if tonality == "Professional" :
        response = openai.Completion.create(
        model="text-davinci-001",
        prompt=parseInputFunction(prompt_text, True),
        temperature=parseHyperparameters("temperature", 0.7, 0.75, 2, True),
        max_tokens=parseHyperparameters("max_tokens", 225, 265, 2, True),
        top_p=1,
        frequency_penalty=parseHyperparameters("frequency_penalty", 0.1, 0.15, 2),
        presence_penalty=0,)
        return response.choices[0].text

    elif tonality == "Formal" :
        response = openai.Completion.create(
        model="text-davinci-001",
        prompt=parseInputFunction(prompt_text, True),
        temperature=parseHyperparameters("temperature", 0.6, 0.7, 2, True),
        max_tokens=parseHyperparameters("max_tokens", 225, 265, 2, True),
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,)
        return response.choices[0].text

    elif tonality == "Childish" :
        response = openai.Completion.create(
        model="text-davinci-001",
        prompt=parseInputFunction(prompt_text, True),
        temperature=parseHyperparameters("temperature", 0.5, 0.65, 2, True),
        max_tokens=parseHyperparameters("max_tokens", 200, 225, 2, True),
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,)
        return response.choices[0].text

    elif tonality == "Luxurious" :
        response = openai.Completion.create(
        model="text-davinci-001",
        prompt=parseInputFunction(prompt_text, True),
        temperature=parseHyperparameters("temperature", 0.7, 0.75, 2, True),
        max_tokens=parseHyperparameters("max_tokens", 225, 265, 2, True),
        top_p=1,
        frequency_penalty=parseHyperparameters("frequency_penalty", 0.15, 0.25, 2),
        presence_penalty=0,)
        return response.choices[0].text

    else :
        response = openai.Completion.create(
        model="text-davinci-001",
        prompt=parseInputFunction(prompt_text, True),
        temperature=0.75,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,)
        return response.choices[0].text

