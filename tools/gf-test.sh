#!/bin/sh

fontbakery check-googlefonts ../../barlow/fonts/ttf/Barlow-*.ttf > ../../barlow/tests/barlow.fb.txt
fontbakery check-googlefonts ../../barlow/fonts/ttf/BarlowSemiCondensed-*.ttf > ../../barlow/tests/barlow.semicondensed.fb.txt
fontbakery check-googlefonts ../../barlow/fonts/ttf/BarlowCondensed-*.ttf > ../../barlow/tests/barlow.condensed.fb.txt
