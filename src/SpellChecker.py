# from spellchecker import SpellChecker
#
# spell = SpellChecker()
#
#
# def correct_sentence_spellchecker(line):
#     lines = line.strip().split(' ')
#     new_line = ""
#     similar_word = {}
#     for l in lines:
#         new_line += str(spell.unknown(l)) + " "
#     # similar_word[l]=spell.candidates(l)
#     return new_line


from autocorrect import spell

def correct_sentence(line):
    lines = line.strip().split(' ')
    new_line = ""
    similar_word = {}
    for l in lines:
        new_line += str(spell(l)) + " "
    # similar_word[l]=spell.candidates(l)
    return new_line


# from textblob import TextBlob
#
# def correct_sentence_textblob(line):
#     lines = line.strip().split(' ')
#     new_line = ""
#     similar_word = {}
#     for l in lines:
#         b = TextBlob(l)
#         new_line += str(b.correct()) + " "
#         #new_line += spell(l) + " "
#     # similar_word[l]=spell.candidates(l)
#     return new_line
