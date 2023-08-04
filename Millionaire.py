import random
from time import sleep
from colorama import Fore
import os

def use_call_friend_after_joker1(question):# joker 1 istifade edildikden sonra call friend jokeri.dost sehv dese 50 50 jokerindeki sehv cavab cixmasi ucun
    global joker1den
    global sehv
    global yoxlama
    global joker1_count
    global joker2_count
    global joker3_count
    if joker2_count == 1:
        dogrucavab = joker1den[0]
        randomeded = random.randint(1, 100)

        if randomeded < 70:
            print("Dostunuz bunu dedi:", dogrucavab)
        else:
            print("Dostunuz bunu dedi:", sehv[0])

        select = input("Seçdiyiniz variant")
        joker2_count -= 1

        if select == dogrucavab:
            print("Doğrudur")
            pul()
        elif select == "0":
            yoxlama = "s"
        elif select == "1":

            use_50_50(question)
            joker1_count -= 1
        elif select == "2":
            while True:
                print("istifadə edilib")
                select2 = input("Seçdiyiniz variant")

                if select2 == "1":
                    use_50_50(question)
                    joker1_count -= 1
                    break
                elif select2 == "2":
                    continue
                elif select2 == "0":
                    yoxlama = "s"
                    break
                elif select2 == "3":
                    use_auditoria(question)
                    joker3_count -= 1
                    break
                elif select2 == question[2]:
                    print("Doğrudur")
                    pul()
                    break
                else:
                    yoxlama = False
                    print("Yanlışdır")
                    break

        elif select == "3":
            use_auditoria(question)
            joker3_count -= 1

        else:
            yoxlama = False
            print("Yanlışdır")
    else:
        while True:
            print("İstifadə edilib")
            select2 = input("Seçdiyiniz variant")

            if select2 == "1":
                use_50_50(question)
                joker1_count -= 1
                break
            elif select2 == "2":
                continue
            elif select2 == "3":
                use_auditoria(question)
                joker3_count -= 1
                break
            elif select2 == question[2]:
                print("Doğrudur")
                pul()
                break
            elif select2 == "0":
                yoxlama = "s"
                break
            else:
                yoxlama = False
                print("Yanlışdır")
                break#

def use_auditoria_after_joker1(question):   # joker 1 istifade edildikden sonra auditoriya jokeri auditoria sehv dese 50-50 jokerindeki sehv cavab olur
    global yoxlama
    global joker1den
    global sehv
    global joker1_count
    global joker2_count
    global joker3_count
    if joker3_count == 1:
        dogrucavab = joker1den[0]
        randomeded = random.randint(1, 100)

        if randomeded < 70:
            print("Auditoriyanın çox hissəsi bunu dedi:", dogrucavab)
        else:

            print("Auditoriyanın çox hissəsi bunu dedi:", sehv[0])

        select = input("Seçdiyiniz variant")
        joker3_count -= 1
        if select == dogrucavab:
            pul()
            print("Doğrudur")
        elif select == "0":
            yoxlama = "s"

        elif select == "1":

            use_50_50(question)
            joker1_count -= 1
        elif select == "3":
            while True:
                print("İstifadə edilib")
                select2 = input("Seçdiyiniz variant")

                if select2 == "2":

                    use_callfriend(question)
                    joker2_count -= 1
                    break
                elif select2 == "3":

                    continue
                elif select2 == "1":

                    use_50_50(question)
                    joker1_count -= 1
                    break
                elif select2 == question[2]:
                    print("Doğrudur")
                    pul()
                    break
                elif select2 == "0":
                    yoxlama = "s"
                    break
                else:
                    yoxlama = False
                    print("Yanlışdır")
                    break

        elif select == "2":

            use_callfriend(question)
            joker2_count -= 1

        else:
            yoxlama = False
            print("Yanlışdır")
    else:
        while True:
            print("İstifadə edilib")
            select2 = input("Seçdiyiniz variant")

            if select2 == "2":

                use_callfriend(question)
                joker2_count -= 1
                break
            elif select2 == "3":

                continue
            elif select2 == "1":

                use_50_50(question)
                joker1_count -= 1
                break
            elif select2 == question[2]:
                print("Doğrudur")
                pul()
                break
            elif select2 == "0":
                yoxlama = "s"
                break
            else:
                yoxlama = False
                print("Yanlışdır")
                break

def variant(question):  #variantlarin ekrana cixarilmasi
    liste = question[1]
    print(f'''
    {liste[0]}     {liste[1]}
    {liste[2]}     {liste[3]}
''')
def print_joker():#jokerler ve qazancin ekranda gosterilmesi
    global money
    print(Fore.GREEN)
    print("Jokers")
    print('[1] 50-50')
    print('[2] Call Friend')
    print('[3] Auditoria')
    print("[0] Çıxış")
    print(Fore.RESET)

    print(f"Qazanc:{money}")   #qazanc
joker1den = 0  #50 50 istifade edikden sonra ekrana cixan iki variantdan dogru olan variant
sehv = 0       #50 50 istifade edikden sonra ekrana cixan iki variantdan yanlis olan variant
def use_50_50(question):# 50-50 joker
    global joker1den
    global yoxlama
    global money
    global count
    global joker1_count
    global joker2_count
    global joker3_count
    global sehv
    if joker1_count == 1:

        for i in question[1]:
            if i.startswith(question[2]):
                question[1].remove(i)
                sehv = random.choice(question[1])
                joker1den = i
                print(f"""
        {i}         {sehv}
""")

        select = input("Seçdiyiniz variant")
        joker1_count -= 1

        if select == question[2]:
            pul()
            print("Doğrudur")
        elif select == "1":
            while True:
                print("İstifadə edilib")
                select2 = input("Seçdiyiniz variant")

                if select2 == "2":
                    use_callfriend(question)
                    joker2_count -= 1
                    break
                elif select2 == "1":
                    continue
                elif select2 == "3":
                    use_auditoria(question)
                    joker3_count -= 1
                    break
                elif select2 == question[2]:
                    print("Doğrudur")
                    pul()
                    break
                elif select2 == "0":
                    yoxlama = "s"
                    break
                else:
                    yoxlama = False
                    print("Yanlışdır")
                    break

        elif select == "2":
            use_call_friend_after_joker1(question)
            joker2_count -= 1

        elif select == "3":
            use_auditoria_after_joker1(question)
            joker3_count -= 1
        elif select == "0":
            yoxlama = "s"


        else:
            yoxlama = False
            print("Yanlışdır")
    else:
        while True:
            print("İstifadə edilib")
            select2 = input("Seçdiyiniz variant")

            if select2 == "2":

                use_callfriend(question)
                joker2_count -= 1
                break
            elif select2 == "1":
                continue
            elif select2 == "3":
                use_auditoria(question)
                joker3_count -= 1
                break
            elif select2 == question[2]:
                print("Doğrudur")
                pul()
                break
            elif select2 == "0":
                yoxlama = "s"
                break
            else:
                yoxlama = False
                print("Yanlışdır")
                break


def use_callfriend(question): #call friend joker
    global yoxlama
    global joker1_count
    global joker2_count
    global joker3_count
    if joker2_count == 1:
        dogrucavab = question[2]
        randomeded = random.randint(1, 100)
        sehvcavab = ["a", "b", "c", "d"]
        randomsehv = random.choice(sehvcavab)

        if randomeded < 70:
            print("Dostunuz bunu dedi:", dogrucavab)
        else:
            sehvcavab.remove(dogrucavab)
            print("Dostunuz bunu dedi:", randomsehv)

        select = input("Seçdiyiniz variant")
        joker2_count -= 1
        if select == dogrucavab:
            print("Doğrudur")
            pul()
        elif select == "0":
            yoxlama = "s"
        elif select == "2":
            while True:
                print("İstifadə edilib")
                select2 = input("Seçdiyiniz variant")
                if select2 == "1":
                    use_50_50(question)
                    joker1_count -= 1
                    break
                elif select2 == "0":
                    yoxlama = "s"
                    break
                elif select2 == "2":
                    continue
                elif select2 == "3":
                    use_auditoria(question)
                    joker3_count -= 1
                    break
                elif select2 == question[2]:
                    print("Doğrudur")
                    pul()
                    break
                else:
                    yoxlama = False
                    print("Yanlışdır")
                    break
        elif select == "1":
            use_50_50(question)
            joker1_count -= 1
        elif select == "3":
            use_auditoria(question)
            joker3_count -= 1
        else:
            yoxlama = False
            print("Yanlışdır")
    else:
        while True:
            print("İstifadə edilib")
            select2 = input("Seçdiyiniz variant")
            if select2 == "1":
                use_50_50(question)
                joker1_count -= 1
                break
            elif select2 == "2":
                continue
            elif select2 == "3":
                use_auditoria(question)
                joker3_count -= 1
                break
            elif select2 == question[2]:
                print("Doğrudur")
                pul()
                break
            elif select2 == "0":
                yoxlama = "s"
                break
            else:
                yoxlama = False
                print("Yanlışdır")
                break

def use_auditoria(question):   # auditoriya jokeri
    global yoxlama
    global joker1_count
    global joker2_count
    global joker3_count
    if joker3_count == 1:
        dogrucavab = question[2]
        randomeded = random.randint(1, 100)
        sehvcavab = ["a", "b", "c", "d"]
        randomsehv = random.choice(sehvcavab)

        if randomeded < 70:
            print("Auditoriyanin çox hissəsi bunu dedi:", dogrucavab)
        else:
            sehvcavab.remove(dogrucavab)
            print("Auditoriyanin çox hissəsi bunu dedi:", randomsehv)

        select = input("Seçdiyiniz variant")
        joker3_count -= 1
        if select == dogrucavab:
            pul()
            print("Doğrudur")
        elif select == "0":
            yoxlama = "s"

        elif select == "1":
            use_50_50(question)
            joker1_count -= 1
        elif select == "2":
            use_callfriend(question)
            joker2_count -= 1
        elif select == "3":
            while True:
                print("İstifadə edilib")
                select2 = input("Seçdiyiniz variant")
                if select2 == "2":
                    use_callfriend(question)
                    joker2_count -= 1
                    break
                elif select2 == "3":
                    continue
                elif select2 == "1":
                    use_50_50(question)
                    joker1_count -= 1
                    break
                elif select2 == "0":
                    yoxlama = "s"
                    break

                elif select2 == question[2]:
                    print("Doğrudur")
                    pul()
                    break
                else:
                    yoxlama = False
                    print("Yanlışdır")
                    break
        else:
            yoxlama = False
            print("Yanlışdır")

    else:
        while True:
            print("İstifadə edilib")
            select2 = input("Seçdiyiniz variant")
            if select2 == "2":
                use_callfriend(question)
                joker2_count -= 1
                break
            elif select2 == "3":
                continue
            elif select2 == "1":
                use_50_50(question)
                joker1_count -= 1
                break
            elif select2 == question[2]:
                print("Doğrudur")
                pul()
                break
            elif select2 == "0":
                yoxlama = "s"
                break
            else:
                yoxlama = False
                print("Yanlışdır")
                break

def pul():         #pulun sualin sirasina gore hesablanmasi
    global count
    global money
    if count == 15:
        money = 100
    elif count == 14:
        money = 200
    elif count == 13:
        money = 300
    elif count == 12:
        money = 500
    elif count == 11:
        money = 1000
    elif count == 10:
        money = 2000
    elif count == 9:
        money = 4000
    elif count == 8:
        money = 8000
    elif count == 7:
        money = 16000
    elif count == 6:
        money = 32000
    elif count == 5:
        money = 64000
    elif count == 4:
        money = 125000
    elif count == 3:
        money = 250000
    elif count == 2:
        money = 500000
    elif count == 1:
        money = 1000000

def baraj():#baraja gore pulun hesablanmasi
    global count
    global money
    if count == 15 or count == 14 or count == 13 or count == 12 or count == 11:
        money = 0
    elif count == 10 or count == 9 or count == 8 or count == 7 or count == 6:
        money = 1000
    elif count == 5 or count == 4 or count == 3 or count == 2 or count == 1:
        money = 32000

    print("Qazanc:", money)
def begin():#intro
    print(Fore.YELLOW + "Oyun başlayır...")
    sleep(2)

    print(Fore.RESET)
    print('''Seçimlər:
1.Tapdığınız variantı variantla qeyd edin!
2.50 % jokerini istifadə etmek üçün  (1)-ə basın!
3.Call friend jokerini istifadə etmək üçün (2)-yə basın!
4.Auditoria jokerini istifadə etmək üçün (3)-ə basın!
5.Oyundan çəkilmək üçün (0)-a basın!  
            ''')

def out():
    global count
    if count != 0:
        sleep(2)
        print(Fore.RED, "Oyun bitdi...")
        print(Fore.RESET)
def win():
    global count
    if count == 0:
        sleep(2)
        print("Qazanc:", money)
        sleep(2)
        print(Fore.CYAN, "Təbriklər qazandınız...")
        print(Fore.RESET)

question1 = ["Azerbaycanin paytaxti haradir?", ["a.Baki", "b.Ankara", "c.Gence", "d.Naxcivan"], "a"]
question2 = ["Turkiyenin paytaxti haradir?", ["a.Istanbul", "b.Ankara", "c.Izmir", "d.Adana"], "b"]
question3 = ["Dordbucaqlinin daxili bucaqlarinin cemi?", ["a.180", "b.90", "c.360", "d.732"], "c"]
question4 = ["Ucbucagin daxili bucaqlarinin cemi", ["a.222", "b.333", "c.323", "d.180"], "d"]
question5 = ["9 ustu 2 nece edir", ["a.23", "b.45", "c.81", "d.100"], "c"]
question6 = ["Ikinci dunya muharibesi necenci illerdedir", ["a.1941-45", "b.1956-78", "c.1967-90", "d.1845-47"], "a"]
question7 = ["Istanbulun fethi necemci ildedir", ["a.1234", "b.1453", "c.1345", "d.1456"], "b"]
question8 = ["Mis elementinin yazilisi", ["a.Li", "b.Mi", "c.Fe", "d.Cu"], "d"]
question9 = ["Pythonda dovru qirmaq ucun neden istifade olunur", ["a.print", "b.append", "c.break", "d.return"], "c"]
question10 = ["1 hefte nece gundur?", ["a.3", "b.7", "c.1", "d.2"], "b"]
question11 = ["1 gun nece saatdir ?", ["a.23", "b.3", "c.11", "d.24"], "d"]
question12 = ["1 saat nece deqiqedir", ["a.33", "b.44", "c.60", "d.28"], "c"]
question13 = ["1 deq nece saniyedir?", ["a.60", "b.22", "c.11", "d.44"], "a"]
question14 = ["2+2 nece edir?", ["a.5", "b.3", "c.4", "d.2"], "c"]
question15 = ["7 * 8 nece edir?", ["a.23", "b.59", "c.56", "d.15"], "c"]

questions = [question1[0], question2[0], question3[0], question4[0], question5[0], question6[0], question7[0], question8[0],
             question9[0], question10[0], question11[0], question12[0], question13[0], question14[0], question15[0]]

count = 15 #sual ve dovr sayi
money = 0 # qazanc
yoxlama = True #jokerden cixan cavabin yoxlanilmasi
joker1_count = 1
joker2_count = 1         #jokerlerin sayi
joker3_count = 1
begin()
while count > 0:
    random_question = random.choice(questions)#random sual
    questions.remove(random_question)#bir daha cixmamasi ucun sualin silinmesi
    print(random_question)

    if random_question == question1[0]:
        variant(question1)
        print_joker()
        select_variant = input("Seçdiyiniz variant")
        if select_variant == question1[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question1)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":

                print("Qazanc:", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "2":
            use_callfriend(question1)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":

                print("Qazanc:", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question1)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":

                print("Qazanc:", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question2[0]:
        variant(question2)
        print_joker()
        select_variant = input("Seçdiyiniz variant")
        if select_variant == question2[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question2)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1

                continue
        elif select_variant == "2":
            use_callfriend(question2)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question2)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question3[0]:
        variant(question3)
        print_joker()
        select_variant = input("Seçdiyiniz variant")
        if select_variant == question3[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question3)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "2":
            use_callfriend(question3)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question3)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question4[0]:
        variant(question4)
        print_joker()
        select_variant = input("Seçdiyiniz variant")
        if select_variant == question4[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question4)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "2":
            use_callfriend(question4)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question4)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question5[0]:
        variant(question5)
        print_joker()
        select_variant = input("Seçdiyiniz variant")
        if select_variant == question5[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question5)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1

                continue
        elif select_variant == "2":
            use_callfriend(question5)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question5)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question6[0]:
        variant(question6)
        print_joker()
        select_variant = input("Seçdiyiniz variant")
        if select_variant == question6[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question6)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "2":
            use_callfriend(question6)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question6)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question7[0]:
        variant(question7)
        print_joker()
        select_variant = input("Seçdiyiniz variant")
        if select_variant == question7[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question7)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "2":
            use_callfriend(question7)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question7)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question8[0]:
        variant(question8)
        print_joker()
        select_variant = input("Seçdiyiniz variant")
        if select_variant == question8[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question8)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "2":
            use_callfriend(question8)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question8)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question9[0]:
        variant(question9)
        print_joker()
        select_variant = input("Seçdiyiniz variant:")
        if select_variant == question9[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question9)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "2":
            use_callfriend(question9)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question9)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question10[0]:
        variant(question10)
        print_joker()
        select_variant = input("Seçdiyiniz variant:")
        if select_variant == question10[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question10)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "2":
            use_callfriend(question10)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question10)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question11[0]:
        variant(question11)
        print_joker()
        select_variant = input("Seçdiyiniz variant:")
        if select_variant == question11[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question11)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "2":
            use_callfriend(question11)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question11)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question12[0]:
        variant(question12)
        print_joker()
        select_variant = input("Seçdiyiniz variant:")
        if select_variant == question12[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question12)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "2":
            use_callfriend(question12)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question12)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question13[0]:
        variant(question13)
        print_joker()
        select_variant = input("Seçdiyiniz variant:")
        if select_variant == question13[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question13)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "2":
            use_callfriend(question13)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question13)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question14[0]:
        variant(question14)
        print_joker()
        select_variant = input("Seçdiyiniz variant:")
        if select_variant == question14[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question14)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "2":
            use_callfriend(question14)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question14)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break
    elif random_question == question15[0]:
        variant(question15)
        print_joker()
        select_variant = input("Seçdiyiniz variant:")
        if select_variant == question15[2]:
            print("Doğrudur")
            pul()
        elif select_variant == "0":
            print("Qazanc", money)
            break
        elif select_variant == "1":
            use_50_50(question15)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "2":
            use_callfriend(question15)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        elif select_variant == "3":
            use_auditoria(question15)
            if yoxlama == False:
                baraj()
                break
            elif yoxlama == "s":
                print("Qazanc", money)
                break
            else:
                count -= 1
                continue
        else:
            print("Yanlışdır")
            baraj()
            break


    count -= 1
    os.system("cls")
win()
out()