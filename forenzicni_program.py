#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Pozdravljeni v forenzičnem programu"

DNA_osumljenca = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACA \
                 GCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCT \
                 CATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGG \
                 AAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

# splošne podatki - značilnosti, DNA
DNA_zapis_lasje = ["CCAGCAATCGC", "GCCAGTGCCG", "TTAGCTATCGC"]
DNA_zapis_obraz = ["GCCACGG", "ACCACAA", "AGGCCTCA"]
DNA_zapis_oci = ["TTGTGGTGGC", "GGGAGGTGGC", "AAGTAGTGAC"]
DNA_zapis_spol = ["TGAAGGACCTTC", "TGCAGGAACTTC"]
DNA_zapis_rasa = ["AAAACCTCA", "CGACTACAG", "CGCGGGCCG"]

opis_DNA_zapis_lasje = {"CCAGCAATCGC": "črni", "GCCAGTGCCG": "rjavi", "TTAGCTATCGC": "blond"}
opis_DNA_zapis_obraz = {"GCCACGG": "kvadrat", "ACCACAA": "okrogel", "AGGCCTCA": "ovalen"}
opis_DNA_zapis_oci = {"TTGTGGTGGC": "modre", "GGGAGGTGGC": "zelene", "AAGTAGTGAC": "rjave"}
opis_DNA_zapis_spol = {"TGCAGGAACTTC": "moški", "TGAAGGACCTTC": "ženski"}
opis_DNA_zapis_rasa = {"AAAACCTCA": "bela", "CGACTACAG": "črna", "CGCGGGCCG": "azijska"}

# iskanje ujemanja DNA osumljencev
DNA_ujemanja = []

for item in DNA_zapis_lasje:
    if item in DNA_osumljenca:
        DNA_ujemanja.append(opis_DNA_zapis_lasje[item])
for item in DNA_zapis_obraz:
    if item in DNA_osumljenca:
        DNA_ujemanja.append(opis_DNA_zapis_obraz[item])
for item in DNA_zapis_oci:
    if item in DNA_osumljenca:
        DNA_ujemanja.append(opis_DNA_zapis_oci[item])
for item in DNA_zapis_spol:
    if item in DNA_osumljenca:
        DNA_ujemanja.append(opis_DNA_zapis_spol[item])
for item in DNA_zapis_rasa:
    if item in DNA_osumljenca:
        DNA_ujemanja.append(opis_DNA_zapis_rasa[item])

print DNA_ujemanja

# opisni podatki osumljencev
Eva = ["ženski", "bela", "blond", "modre", "ovalen"]
Larisa = ["ženski", "bela", "rjavi", "rjave", "ovalen"]
Matej = ["moški", "bela", "črni", "modre", "ovalen"]
Miha = ["moški", "bela", "rjavi", "zelene", "kvadrat"]

# najdba osumljenca
while True:
    if set(DNA_ujemanja) == set(Eva):
        print "DNA ustreza Evi"
        break
    elif set(DNA_ujemanja) == set(Larisa):
        print "DNA ustreza Larisi"
        break
    elif set(DNA_ujemanja) == set(Matej):
        print "DNA ustreza Mateju"
        break
    elif set(DNA_ujemanja) == set(Miha):
        print "DNA ustreza Mihi"
        break
    else:
        print "DNA se ne ujema z nobenim osumljencem"
        break

print "Adijo"

