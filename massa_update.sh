#!/bin/bash

. $HOME/.bashrc && . $HOME/.bash_profile

apt update && apt upgrade -y
apt install wget jq git build-essential pkg-config libssl-dev -y

if [[ -n $(systemctl | grep massad) ]]; then
  systemctl stop massad
else
  printf "[Unit]
Description=Massa Node
After=network-online.target

[Service]
User=$USER
WorkingDirectory=$HOME/massa/massa-node
ExecStart=$HOME/massa/massa-node/massa-node
Restart=on-failure
RestartSec=3
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/massad.service
fi

local massa_version=`wget -qO- https://api.github.com/repos/massalabs/massa/releases/latest | jq -r ".tag_name"`
wget -qO $HOME/massa.tar.gz "https://github.com/massalabs/massa/releases/download/${massa_version}/massa_${massa_version}_release_linux.tar.gz"
tar -xvf $HOME/massa.tar.gz
rm -rf $HOME/massa.tar.gz

chmod +x $HOME/massa/massa-node/massa-node $HOME/massa/massa-client/massa-client

tee <<EOF >/dev/null $HOME/massa/massa-node/config/config.toml
[network]
routable_ip = "`wget -qO- eth0.me`"
EOF

systemctl daemon-reload && systemctl enable massad && systemctl restart massad

local massa_addr=$(cd $HOME/massa/massa-client/ && ./massa-client wallet_info | grep Address | awk '{print $2}')
echo "massa wallet address: $massa_addr"
