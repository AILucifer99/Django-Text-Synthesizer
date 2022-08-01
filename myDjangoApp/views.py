# Created by Snehan Biswas
from django.http import HttpResponse
from django.shortcuts import render
from utils import punctuationSynthesizer as puncSyn 
from utils import keyphraseExtractor as keyPhGen
from utils import paraphraser as paraGen
import re
import nltk
nltk.download('punkt')


def index(request):
    return render(request, 'index.html')


def capitalization(seed_text, capitalize):
    if capitalize:
        seed = ""
        for items in seed_text:
            seed = seed + items.upper()
        return seed


def removePunctuationFunction(text_input, parse=False):
    if parse:
        text = text_input
        new_words = []
        for word in text:
            w = re.sub(r'[^\w\s]','',word) #remove everything except words and space
            w = re.sub(r'_','',w) #how to remove underscore as well
            new_words.append(w)
        return ''.join(new_words)
    else:
        return text_input


def synthesize(request):
    djangoText = request.GET.get('text', 'deafult')
    removePunc = request.GET.get('removePunctuation', "off")
    keyphraseExt = request.GET.get('keyphraseExtractor', "off")
    upperCaseText = request.GET.get('UpperCaseSynthesizer', "off")
    applyUpperCasePunc = request.GET.get('UpperCasePunctuationSynthesizer', "off")
    uppercaseKey = request.GET.get('UpperCaseKeywordSynthesizer', "off")
    paraphrasedKey = request.GET.get('textParaphraser', 'off')

    print(removePunc)
    print(djangoText)
    print(keyphraseExt)
    print(applyUpperCasePunc)
    print(uppercaseKey)
    print(paraphrasedKey)

    if uppercaseKey == "on":
        synthesized_text_1 = keyPhGen.Synthesize(
            puncSyn.Synthesize(djangoText, True), True
            )
        synthesized_text = capitalization(synthesized_text_1, True)
        params = {
            'purpose': "Capitalized Keyword Synthesizer",
            'synthesized_text': synthesized_text
        }
        return render(request, 'synthesize.html', params)

    elif applyUpperCasePunc == "on":
        synthesized_text_1 = puncSyn.Synthesize(djangoText, True)
        synthesized_text = capitalization(synthesized_text_1, True)
        params = {
            'purpose': "Punctuation and Capitalization Synthesizer",
            'synthesized_text': synthesized_text
        }
        return render(request, 'synthesize.html', params)

    elif removePunc == "on":
        synthesized_text = puncSyn.Synthesize(djangoText, True)
        params = {
            'purpose': 'Removed Punctuations', 
            'synthesized_text': synthesized_text
        }
        return render(request, 'synthesize.html', params)

    elif keyphraseExt == "on":
        synthesized_text = keyPhGen.Synthesize(
            puncSyn.Synthesize(djangoText, True), True
            )
        params = {
            'purpose': 'Kephrase Synthesizer', 
            'synthesized_text': synthesized_text
        }
        return render(request, 'synthesize.html', params)

    elif upperCaseText == "on":
        synthesized_text = capitalization(djangoText, True)
        params = {
            'purpose': 'Text Capitalization', 
            'synthesized_text': synthesized_text
        }
        return render(request, 'synthesize.html', params)
    elif paraphrasedKey == "on" :
        synthesized_text = paraGen.ParaphraserFunction(prompt_text=djangoText, tonality='')
        params = {
            'purpose': 'Text Paraphrasing', 
            'synthesized_text': synthesized_text
        }
        return render(request, 'synthesize.html', params)
        
    else:
        synthesized_text = removePunctuationFunction(djangoText, False)
        params = {
            'purpose': 'Removed Punctuations', 
            'synthesized_text': synthesized_text
        }
        return render(request, 'synthesize.html', params)



