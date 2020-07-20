#!/usr/bin/env bash

apt install -y -V apt-transport-https 
wget -O /usr/share/keyrings/apache-arrow-keyring.gpg https://dl.bintray.com/apache/arrow/debian/apache-arrow-keyring.gpg
tee /etc/apt/sources.list.d/apache-arrow.list <<APT_LINE
deb [arch=amd64 signed-by=/usr/share/keyrings/apache-arrow-keyring.gpg] https://dl.bintray.com/apache/arrow/debian/ buster main
deb-src [signed-by=/usr/share/keyrings/apache-arrow-keyring.gpg] https://dl.bintray.com/apache/arrow/debian/ buster main
APT_LINE
apt update --allow-insecure-repositories
apt install -y -V --allow-unauthenticated libarrow-dev libparquet-dev
