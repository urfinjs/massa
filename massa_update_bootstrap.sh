#!/bin/bash

apt update
apt --installed list 2>/dev/null | grep python3 || apt install python3 -y && python3 --version
apt --installed list 2>/dev/null | grep python3-pip || apt install python3-pip -y && pip3 --version
apt upgrade -y

pip3 install toml

python3 <(wget -qO- https://raw.githubusercontent.com/urfinjs/massa/main/massa_update_bootstrap.py)

echo "New bootstrap list:"
grep bootstrap_list /root/massa/massa-node/base_config/config.toml

systemctl restart massad && sleep 10 && journalctl -u massad -n 25
