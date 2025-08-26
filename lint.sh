#!/usr/bin/env sh
set -e

echo '* CHECKBASHISMS'
checkbashisms *.sh

echo '* NON-CJK'
grep '[ ,\.:()a-zA-Z0-9]' hiragana/*.txt

