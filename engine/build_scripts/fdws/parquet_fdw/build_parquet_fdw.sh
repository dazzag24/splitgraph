#!/bin/bash -ex

cd /src/parquet_fdw

export DESTDIR=/output/root
make install

