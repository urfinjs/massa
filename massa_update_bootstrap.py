#!/usr/bin/python3
import toml

config_abspath = '/root/massa/massa-node/base_config/config.toml'

bootstrap_list = [
    ["185.217.126.178:31245", "7bKVu43o1e6MZsj9xsKFcq14B75vNjirTSW2umaaTMngfbWsL3"],
    ["104.129.128.122:31245", "5EBePa834f8P3Ei6Vx7JFPzaq6JpsL4fDBRwePWfkiWM45yh6n"],
    ["65.21.242.5:31245",  "6gkR8BbtpKCSkSoXtdmj1722Gp1iH49D2F8kJhGD6k1VhJrChH"],
    ["51.250.18.248:31245",  "7tg9CfaM2xCiqyiZutpsagGrK5TtkU2paK7nLLoa21qdqjhZMR"],
    ["135.181.112.215:31245", "6jeAcQYVTjiJnw4eyr8SMWAsAaMtWLN6HutNfVvB9TfV8EZEep"],
    ["38.242.201.240:31245", "5yEwmraRY7wnEUZDzcWbnJ6sYqXaxcy8GfrDeJ6PTXx3HEKF92"],
    ["194.163.166.47:31245",   "74a6newcBkijYx6YSaQcyHX5j5oSjF2wFEAahGb7XNxQZSfboF"],
    ["194.163.182.239:31245", "6BDnKc5L7mpbW5K7c99TxZ5bQatpw2yiKPhTvPr49rNe9QnC7p"],
    ["178.170.41.160:31245", "8mVVr2pyNgDqxBS9LCCmX8gBLAvc1R6wt5mwZgbZtj26oGmUWs"],
    ["195.201.91.249:31245", "8UzkUgUTtdfntGsuUfbvmLZREnYYBU2mi6ggebcJsBsDTBX7z2"]
]

with open(config_abspath, 'r') as fh:
    config = toml.load(fh)

config['bootstrap']['bootstrap_list'] = bootstrap_list

with open(config_abspath, 'w') as fh:
    toml.dump(config, fh)
