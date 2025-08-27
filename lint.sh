#!/usr/bin/env sh
set -e

echo '* CHECKBASHISMS'
checkbashisms *.sh

echo '* GREP CJK'
grep -n '[ ,\.:()a-zA-Z0-9]' hiragana/*.txt
grep -n '。。' hiragana/*.txt
grep -n '：。' hiragana/*.txt
grep -n '、。' hiragana/*.txt
grep -n '　　' hiragana/*.txt

