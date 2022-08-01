def Synthesize(text_input, generateKeywords):
    import nltk
    from rake_nltk import Rake
    nltk.download('stopwords')
    if generateKeywords:
        text = text_input
        rake_nltk_var = Rake()
        rake_nltk_var.extract_keywords_from_text(text)
        keyword_extracted = rake_nltk_var.get_ranked_phrases()
        print(keyword_extracted)
        seed = ""
        counter = 0
        for items in keyword_extracted:
            seed = seed + items + ", "
            counter += 1
            if counter == 20:
                break
        return seed
    else:
        return 