#!/usr/bin/env sh
set -e

echo '* CHECKBASHISMS'
checkbashisms *.sh

echo '* NON-CJK'
grep '[ ,\.:()]' *.txt

