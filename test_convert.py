#!/usr/bin/env python3
"""Test romaji converters."""

from kanaconv import KanaConv
from romkan import to_hiragana, to_katakana, to_roma
from pykakasi import kakasi

hiragana = 'ほうじょうのかた、じゅうじがらみ、じゆうわざ'
katakana = 'ホウジョウノカタ、ジュウジガラミ、ジユウワザ'
hepburn_standard = 'hōjōnokata, jūjigarami, jiyūwaza'
hepburn_simplified = 'houjounokata, juujigarami, jiyuuwaza'
print('INPUT')
print(f'{hiragana=}')
print(f'{katakana=}')
print(f'{hepburn_standard=}')
print(f'{hepburn_simplified=}')

print('\nKANACONV')  # use | for word separation to prevent macron
print(f'hiragana to_romaji: {KanaConv().to_romaji(hiragana)}')
print(f'katakana to_romaji: {KanaConv().to_romaji(katakana)}')

print('\nPYKAKASI')
res = kakasi().convert(hiragana)
print('hiragana convert[hepburn]:',
      ''.join(item['hepburn'] for item in res).replace(',', ', '))
print('hiragana convert[kana]:',
      ''.join(item['kana'] for item in res).replace(',', ', '))
res = kakasi().convert(katakana)
print('katakana convert[hepburn]:',
      ''.join(item['hepburn'] for item in res).replace(',', ', '))
print('katakana convert[hira]:',
      ''.join(item['hira'] for item in res).replace(',', ', '))

print('\nROMKAN')
print(f'hiragana to_roma: {to_roma(hiragana).replace("、", ", ")}')
print(f'katakana to_roma: {to_roma(katakana).replace("、", ", ")}')
print(f'hepburn_simplified to_katakana: {to_katakana(hepburn_simplified)}')
print(f'hepburn_simplified to_hiragana: {to_hiragana(hepburn_simplified)}')
