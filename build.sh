for D in ./* ;do
  if [ -d "$D" ]; then
    cd "$D" || continue
    ./render.sh
    cp -r
    cd ..
  fi
done
