#!/bin/bash
new_file_prefix=cleared
for file in $(ls)
do
  if [ -d "$file" ]; then
    continue
  fi
  new_file_name=$new_file_prefix'_'$file
  echo "$file"  "$new_file_name"
  python date_trip.py "$file" "$new_file_name"
done
