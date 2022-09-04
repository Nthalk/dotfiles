Create keyszer user:

    sudo useradd keyszer

Add udev rules:

    # file: /etc/udev/rules.d/90-keymapper-acl.rules
    KERNEL=="event*", SUBSYSTEM=="input", RUN+="/usr/bin/setfacl -m user:keymapper:rw /dev/input/%k"
    KERNEL=="uinput", SUBSYSTEM=="misc", RUN+="/usr/bin/setfacl -m user:keymapper:rw /dev/uinput"

Reload udev rules:

    sudo udevadm control --reload-rules && udevadm trigger

Add to .xsessionrc

    # file: .xsessionrc
    xhost +si:localuser:keymapper

Install and start service
    
    sudo cp config.py /home/keymapper/.config/keyszer/
    sudo cp keyszer.service /etc/systemd/system
    systemctl enable keyszer.service
    systemctl daemon-reload; systemctl restart keyszer.service; journalctl -f -u keyszer.service





