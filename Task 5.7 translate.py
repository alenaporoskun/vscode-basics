CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION): 
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
    
def translate(name):
    word = ""
    for ch in name:
        word += ch.translate(TRANS)

    #print(word)
    return word

print(translate('д Д в В'))
print(translate('Дмитро Короб'))
print(translate('Олекса Івасюк'))