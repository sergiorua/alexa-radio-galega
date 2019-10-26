#!/bin/bash

# pybabel compile -i locales/en-GB/LC_MESSAGES/skill.po -o locales/en-GB/LC_MESSAGES/skill.mo

langs="pt-BR en-GB ja-JP gl-ES es-ES"
for l in $langs; do
  pybabel compile -i $l/LC_MESSAGES/data.po -o $l/LC_MESSAGES/data.mo
done
