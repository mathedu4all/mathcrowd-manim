#!/bin/bash

cd ./projects || exit
for D in ./* ;do
  if [ -d "$D" ]; then
    cd "$D" || continue
    ./render.sh
    mkdir -p ../../output/"$D"
    if [ -d "./videos" ]; then
      rsync -av --delete ./videos ../../output/"$D"
    fi

    if [ -d "./images" ]; then
      rsync -av --delete ./images ../../output/"$D"
    fi
    cd ..
  fi
done
