#!/usr/bin/env sh
set -e

if command -v flatpak >/dev/null 2>&1; then
    if flatpak list --app | grep -q 'org\.inkscape\.Inkscape'; then
        EXE='flatpak run org.inkscape.Inkscape'
    else
        EXE='inkscape'
    fi
else
    EXE='inkscape'
fi

#find out -type f -name '*.png' -delete
.venv/bin/python generate.py
mkdir -p prev
cd svg
UPDATED=0
for i in *.svg; do
    o=../out/$(basename $i svg)png
    if [ ! -e $o ]; then
        echo $i
        echo '  no previous render exists'
        $EXE $i -TCo $o 2>/dev/null
        optipng -quiet $o
        UPDATED=$(($UPDATED + 1))
        cp -f $i ../prev/$i
    else
        if [ -e ../prev/$i ] && [ "$(diff $i ../prev/$i)" ]; then
            echo $i
            echo '  previous source exists but is different'
            $EXE $i -TCo $o 2>/dev/null
            optipng -quiet $o
            UPDATED=$(($UPDATED + 1))
            cp -f $i ../prev/$i
        else
            if [ ! -e ../prev/$i ]; then
                echo $i
                echo '  previous source does not exist'
                $EXE $i -TCo $o 2>/dev/null
                optipng -quiet $o
                UPDATED=$(($UPDATED + 1))
                cp -f $i ../prev/$i
            # else do nothing
            fi
        fi
    fi
done
if [ $UPDATED -ne 0 ]; then
    curl -m 3 -s "https://ntfy.hostingforyou.nl/sander-reveal" \
    -u ":tk_p7wsrbqi0zrhj69tj7yybx1ia3bq0" \
    -H "p:high" -H "ta:warning" \
    -d $UPDATED" artwork images have been updated, see https://otomeza.nsupdate.info/artwork/overview.html or https://otomesa.nsupdate.info/artwork/overview.html" > /dev/null
fi
cd ../out
if [ $(hostname) = kozan ] || [ $(hostname) = kosan ]; then
    cp -f * /var/www/html/artwork/
    cd ../photos
    cp -f *.jpg /var/www/html/artwork/
fi
cd ..
