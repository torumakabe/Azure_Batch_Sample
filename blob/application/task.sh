#!/usr/bin/env bash

set -e
set -o pipefail

docker -H 0.0.0.0:2375 run torumakabe/azure-batch-sample python wordcount.py 'yourstorageaccount' 'yourinputcontainersas' 'inputcontainer' 'the_star_spangled_banner.txt' 'yourstorageaccount' 'outputcontainer' 'youroutputcontainersas'