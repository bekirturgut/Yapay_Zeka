from logic import *

#yagmur = Symbol('yağmur yağıyor') # ! burda bir sembol ataması var yani mantıksal önerme tanımlaması yapılır
#bekir = Symbol('bekir eve gitti') # ? burda da üstteki gibi bekir adında değişkene bekir eve gitti mantıksal atama yapıldı 
#okul = Symbol('okul kapalı') # ? okul değişkenine okul kapalı önermesi atandı.
#cumle = And(bekir , okul)
#print(cumle.formula())
#knowledeg = Implication(And(yagmur, bekir) , okul)
#print(knowledeg.formula())

# def check_knowledge(knowledge):
#     for symbol in semboller:
#         if model_check(knowledge, symbol):
#             print(f"{symbol}: YES", "green")
#         elif not model_check(knowledge, Not(symbol)):
#             print(f"{symbol}: MAYBE")


# mutfak = Symbol("mutfak")
# banyo = Symbol("banyo")
# salon = Symbol("salon")
# odalar = [mutfak, banyo, salon]

# bicak = Symbol("bicak")
# silah = Symbol("silah")
# sopa = Symbol("sopa")
# silahlar = [bicak, silah, sopa]

# bekir = Symbol("bekir")
# sude = Symbol("sude")
# emine = Symbol("emine")
# insanlar = [bekir, sude, emine]

# semboller = odalar + silahlar + insanlar


# bilgi = And(
#     Or(bicak, silah, sopa),
#     Or(mutfak, banyo, salon),
#     Or(bekir, sude, emine)
# )

# bilgi.add(And(Not(bekir),Not(mutfak),Not(silah)))
# bilgi.add(Or(Not(emine), Not(banyo), Not(bicak)))
# bilgi.add(Not(sude))
# bilgi.add(Not(salon))
# check_knowledge(bilgi)

insanlar = ["bekir","sude","emine","ali"]
evler = ["villa","apartman","daire","müstakil"]
semboller = []
bilgi = And()
for insan in insanlar:
    for ev in evler:
        semboller.append(Symbol(f"{insan} {ev}"))
    
for insan in insanlar:
    bilgi.add(Or(
        Symbol(f"{insan} villa"),
        Symbol(f"{insan} apartman"),
        Symbol(f"{insan} daire"),
        Symbol(f"{insan} müstakil"),
    ))

for ev in evler:
    for insan1 in insanlar:
        for insan2 in insanlar:
            if insan1 != insan2:
                bilgi.add(Implication(
                    Symbol(f"{insan1} {ev}"),
                    Not(Symbol(f"{insan2} {ev}"))
                ))

print("Bilgi:", bilgi.formula())

# bilgi.add(Or(Symbol("bekir villa"), Symbol("bekir apartman")))
# bilgi.add(Not(Symbol("sude daire")))
# bilgi.add(Not(Symbol("emine villa")))

# for sembol in semboller:
#     if model_check(bilgi,sembol):
#         print(sembol)