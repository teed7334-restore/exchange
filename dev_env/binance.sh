#!/bin/bash
docker rm -f binance;
docker run \
--name binance \
-v `pwd`/../:/app \
-it binance bash;
