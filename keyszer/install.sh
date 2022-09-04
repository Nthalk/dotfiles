#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

mkdir -p /home/keymapper/.config/keyszer
rm /home/keymapper/.config/keyszer/config.py
cp "$DIR/config.py" /home/keymapper/.config/keyszer/config.py
chown -R keymapper:keymapper /home/keymapper/.config/keyszer

rm /etc/systemd/system/keyszer.service
cp "$DIR/keyszer.service" /etc/systemd/system/keyszer.service
systemctl daemon-reload; systemctl restart keyszer.service; journalctl -f -u keyszer.service
