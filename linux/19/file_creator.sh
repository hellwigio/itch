#!/bin/bash

WD="random_files"

mkdir -p "$WD"

for i in {1..100}; do
    touch "$WD/$RANDOM"
done
