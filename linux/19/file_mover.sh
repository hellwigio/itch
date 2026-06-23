#!/bin/bash

from="random_files"
to="even_files"

mkdir -p $to

count=0

for file in $from/*; do
	if [ ! -f $file ]; then
		continue
	fi

	name=$(basename $file)

	if (( $name % 2 )); then
		continue
	fi

	mv $file $to

	if [ $? -ne 0 ]; then
		echo "Error. $file is not moved."
		continue
	fi

	count=$((count + 1))
done

echo "$count files are moved."
