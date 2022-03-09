#!/usr/bin/python3
import toml

config_abspath = '/root/massa/massa-node/base_config/config.toml'

bootstrap_list = [
    ["209.126.83.178:31245", "8CU8qkvKSrAQfhcUdMvStE4EqAkcgEW6QnjsyMaoMLdMuEpF3c"],
    ["195.201.141.203:31245", "5kEcQS9SSjh3CpVp8M4jGqWjrBdYu2eQjcgpgyRRW192XC3jKZ"],
    ["144.91.123.104:31245", "7hnqeZQ211KoY1DsYHx4Rp5VkaVSnT76acASkG4itrE6yhv2nq"],
    ["62.171.143.40:31245", "6vogoMZMDAceHVvrZEMFMwmVrqnNMRG54GWScU6HVrjGBNNGfr"],
    ["185.255.133.128:31245", "6MjKoPXbeaPwzjpxiA25RetjgvLgRHs1keR62z5bnR37nMM1ev"],
    ["167.99.217.85:31245", "8iHqyQwCLkL4zdsHQA6H4A74HqSm1Xyv1ZXvQWxJUrt8DmiF1K"],
    ["95.217.182.63:31245", "8WrG6g8jnaWHzpzCcUdrWp8AwUbiHC9gX3gxXfQ83VH9VEcTnf"],
    ["89.163.218.4:31245", "5nk5BGknhN1fnd4dHKeYoBcR4a7zArqfW9NgysCmsmVyG8JG48"],
    ["135.181.204.42:31245", "7kKRFLxgKCmCiYfZk51rj8Ba5DtFcyXUXaMYo9L4odgNN2KriF"],
    ["31.42.191.135:31245", "5k78cKSkLmMzWw8gBpV5P99GB2kPQGf1LsEZ5N8LViLfBwQERV"],
    ["157.90.173.148:31245", "6kiZuwezsBuonuQHMYczTtFaXHF1ob4N8TBsTva4ED5fuALAMK"],
    ["167.99.147.101:31245", "5S7GDJ6oQdPLnHAqWgdCvhCVH2951Fo5awqYNsQmU97Cb8dKTA"],
    ["158.51.121.238:31245", "6HSJ5riS2xM4Ui4GBqu5ttPVv3A69mWNS35VrSiSfdiQNJf7SU"],
    ["5.161.46.135:31245", "5W4D4kZQ5bHhZBeovE22EyTjrPdUXWNvqHFEUT5pccmGzTGX1T"],
    ["144.91.104.8:31245", "7cNKaRcJvozsZAzf2XckUvh9r8R78RLZ4WexqpJfPsPGsXwGe5"],
    ["194.233.87.33:31245", "6UKgfMkGu5TQk6Mxjffi8bbTqh7bT8Fp8hoYq7Hz9QCq1L11oi"],
    ["157.90.174.26:31245", "8NkMpapRfJdhCMnsUEazbNWC9s9PKX7NZDE1SyLbk1NGrCywL3"],
    ["213.246.39.63:31245", "5sfWiHoR57JAnrDzm3XkCHjuMwhoisVBhA1534Bs8QRZfLZyZq"],
    ["34.140.104.239:31245", "5H7RQLNFqbuuosVaGuUN56G7QHTuY1WpDBgumaRAySkSySET7d"],
    ["206.189.32.210:31245", "6dSDfXHqKSAVN1bdL6tiix2zg1iyqF35RZqfSume1xv8z2NrtH"],
    ["91.230.111.131:31245", "4tdj2zZidRcAFDpfDkC2DtKg1GfBHkh4ahuB44JnyeKYPtRQdz"],
    ["89.163.215.206:31245", "8L8SPiMjsCT8oQhzfDjDkpeFpzDzDq2RTx7fEzjmKEfQ8FrZpJ"],
    ["46.151.159.3:31245", "51e1Az1PycqHS57w4R28XSVF2tmr3Uu4EU8KUUdXJijjvrX5JW"],
    ["23.88.50.18:31245", "5SXBQWvXib8mjJdAZfQbbraAncCsfoYB9SWmXtGcFxwPxriix2"],
    ["144.91.89.106:31245", "5PZUL9bPHdPD4ib8VC8kG1GzLWWLUjF64yxsPGrHCQ2bXa8mMk"]
]

with open(config_abspath, 'r') as fh:
    config = toml.load(fh)

config['bootstrap']['bootstrap_list'] = bootstrap_list

with open(config_abspath, 'w') as fh:
    toml.dump(config, fh)
