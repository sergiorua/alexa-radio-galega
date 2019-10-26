#!/bin/bash

langs="pt-BR en-GB ja-JP gl-ES es-ES"
for l in $langs; do
  pybabel init -i data.pot -l $(echo $l | gsed 's/-/_/g') -o $l/LC_MESSAGES/data.po
done
