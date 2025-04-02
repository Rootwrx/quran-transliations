#!/bin/bash

for i in $(seq 1 114);do
    cp ${i}/index.json  {$i}.json

done
