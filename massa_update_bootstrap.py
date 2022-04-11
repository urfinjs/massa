#!/usr/bin/python3
import toml

config_abspath = '/root/massa/massa-node/base_config/config.toml'

bootstrap_list = [
    ["65.108.14.245:31245", "8KKWHVJd2LKeVBNmYVEnX2mcwm7aQ3onsaR9fyETjgCB4uiQTs"],
    ["94.156.93.150:31245", "6FK8yGC1uQiTYdq4GfK8aNdC8MbLjfLzc5SaAwJ4snxsSDJsSU"],
    ["5.188.88.251:31245", "6Pwd4zQ3MMHp8vDRdwJhBRShD9dB6DTSHbJx1sHK2yLBorV7fC"],
    ["147.182.139.198:31245", "4zDLAs5zSfnS5VkBRUpwggNzVzkKT1eRH1gFdsHuYEh2GP9PZA"],
    ["89.108.71.233:31245", "5rDHwG5hnaneMc1j3mWitzf7bXTwDThFkKeHbLJchQnaCmN5yS"],
    ["49.12.44.71:31245", "6WQsWWF4D5rATBMtnUhuRLPxRkjoZNqqV2vwScDuvyBxCcm1mf"],
    ["94.140.249.153:31245", "71NRk5K5qk77LsgZcQ69PGQaWwT8AH8xwSitz2usZBvwDmVo8S"],
    ["109.205.181.58:31245", "7F5WDunitHr7Qcvj1QAiqg9WeNvpwe8X4475TgPhqd59jy1Zak"],
    ["5.161.97.72:31245", "5u15ahYe7AWBYbFdLzGt8wm9UCtTVS4SX8EMKQfY9hGQYXkihQ"],
    ["5.9.124.24:31245", "71aU88XGPfMYwqNasQD2g8v1gwG1rxfLxCu4LAq3WsEV3PLXjS"],
    ["185.245.182.243:31245", "7vBgwLE8TFmtpr4XLi7fDS2i272DYF6YQCqFHvQBUotaJ2SQf2"],
    ["45.85.147.46:31245", "5VGgcbPQVoq78Ss2SB69NZzXQwStbk1XkTMa2UbFUas4NVJYS4"],
    ["65.108.161.101:31245", "5cbfPqXKvBDfiLPAidwjBQr8WEB4ewnYjVCtT5ZY9mJSCR4KoS"],
    ["95.216.161.206:31245", "8C2k4nXnyvwxWBjaepmvQyKGytZN62BNTBjn1xBzeZcvga4Lqz"],
    ["213.202.238.195:31245", "8GZMyvjqHNLjjxGTN6rewYbNQqvWxFJ2ro8pkXdUQru4pawVPK"],
    ["95.179.215.97:31245", "6htuM82QYPJBqpMafscvwv23tombzvMWPBXGj5GgzQRYatQt6r"],
    ["78.31.66.108:31245", "88tCL5YNbkn22gWzreRpKkThCJFbe4QiPT5KPnekvbcTBGd5YF"],
    ["135.181.152.87:31245", "73z8huUL4KXkprtxrsYkSFyEycg64eoMf72JzX565ZL9EviSh2"],
    ["162.55.175.11:31245", "5RqmXKEeBUtU2dRNvhKGcoTcrjynaz5ZRYYpdfiKEdKMH4Fn8P"],
    ["82.64.138.122:31245", "8fUpgx86NWRdrUEn96pBWet515S3J5bSm1FtdhnJ4T71bWgdDD"],
    ["194.233.87.52:31245", "8ZzcuJvfAmqXsA22kNV7TbeysASAvCzjPGG6kQZJQuvJeL7miL"],
    ["45.150.67.107:31245", "8dq8YNHqUaSLZPasVWQj6QjSotrsDrygxYvphWE1FnKtVi8vDB"],
    ["94.124.78.102:31245", "88gDnfVSyevm4byHHK5Ec2XZqsgomzt412Pscr7Ea1TmY8oQT7"],
    ["194.163.171.44:31245", "8btkw4aVuj3HYVeg1AwPpD1wYFRPVp3Y5aEdcfEESFTjfhEVLB"],
    ["62.141.44.130:31245", "7FFSm1whXfTr46qVy3oTr1u1VPhCGVNa2yzJ7zwD16mqgoe2aR"],
]

with open(config_abspath, 'r') as fh:
    config = toml.load(fh)

config['bootstrap']['bootstrap_list'] = bootstrap_list

with open(config_abspath, 'w') as fh:
    toml.dump(config, fh)
