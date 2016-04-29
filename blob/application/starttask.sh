#!/usr/bin/env bash

set -e
set -o pipefail

apt-get update
apt-get -y install wget unzip jq apparmor apt-transport-https ca-certificates
apt-get -y install linux-image-extra-$(uname -r)
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo deb https://apt.dockerproject.org/repo ubuntu-trusty main > /etc/apt/sources.list.d/docker.list
apt-get update
apt-get -y purge lxc-docker
apt-get -y install docker-engine
service docker stop
echo DOCKER_OPTS=\"-H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock\" >> /etc/default/docker
rm -f /var/lib/docker/network/files/local-kv.db
service docker start