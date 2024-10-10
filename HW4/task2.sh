#!/usr/bin/env bash

grep -c "sample" dataset1/file* | cut -d: -f1 | xargs grep -o "CSC510" | uniq -c | grep -v '^\s*1' | grep -v '^\s*2' | cut -d: -f1 | gawk '{ printf $1; system("ls -l " $2) }' | gawk '{ sub("-", " ", $0); print $1, $6, $10 }' | sort -k1,1nr -k2,2nr | gawk '{ print $3 }' | sed 's/file_/filtered_/'
