#!/usr/bin/sh
echo 10c4 2022 | sudo tee /sys/bus/usb-serial/drivers/cp210x/new_id
echo 10c4 2021 | sudo tee /sys/bus/usb-serial/drivers/cp210x/new_id
