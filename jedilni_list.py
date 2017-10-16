#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Program za kreiranje jedilnika"
jedilnik = {}

while True:
    meni = raw_input("Vnesi meni:")   # vnos menijev s cenami na jedilni list
    cena = raw_input("Vnesi ceno (brez znaka €):")
    jedilnik[meni] = cena

    nadaljuj = raw_input("Želite nadaljevati z vnosom menijev [d/n]?")
    if nadaljuj == "n":
        print "Zaključili ste z vnosom"
        break

print jedilnik

with open("menu.txt", "w+") as dnevni_meni:  # zapis menijev v datoteko menu.txt - prepisovalni način
    dnevni_meni.write("Danes nudimo:\n")
    for meni in jedilnik:
        dnevni_meni.write("%s, %s €\n" % (meni, jedilnik[meni]))

print "Lahko natisnete pripravljen jedilnik v menu.txt"
