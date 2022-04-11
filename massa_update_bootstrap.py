#!/usr/bin/python3
import toml

config_abspath = '/root/massa/massa-node/base_config/config.toml'

bootstrap_list = [
  ["207.244.231.182:31245", "85vnmoZAA1pB9U55nc3rjo2acoG93YnRgjZAjQXaWNgsgd1cm1"],
  ["45.87.0.248:31245", "71N7FjSbhh9sR5Lbci7zuXd4uHCB3ynMdZRAcc2GFSaJPWdB1r"],
  ["95.216.162.190:31245", "7MbFbMhzWGygTHfL6PVHHP3xPuvUBqgkTyYWd5WrBstdnufM7Z"],
  ["136.244.110.125:31245", "71P16DQUM7gqmCVZtpNs8FKUpGa5pZTecKr14d2u7KZWfDY44i"],
  ["5.161.76.10:31245", "5PKSBV4fb51mbSpnVZS83VVHTn9c4mN3evkXrDrbge5XPULu7W"],
  ["116.203.211.140:31245", "7MP9espYx5iYKLr9fPb9zR9DrcD4DSmXBaYtrrJtcqRjqP456p"],
  ["65.108.49.230:31245", "5uUgcsUd6nmTL88k8YYhFmjBKMeMh5qMRZ7gbuVyXAmuWsuVTf"],
  ["147.182.139.198:31245", "4zDLAs5zSfnS5VkBRUpwggNzVzkKT1eRH1gFdsHuYEh2GP9PZA"],
  ["135.181.194.236:31245", "7MyEeXZBD5mHMC5VmuLcVwpKZxsPeoGv9xb1LmPg7MadHyoiDx"],
  ["89.163.213.19:31245", "8QVANZrwn9m725oQVPSE11dNxxMweEn7CG43st9RsQXHupRWH9"],
  ["84.52.99.180:31245", "8SWoTLzBQjsHFJ56SSjzdPcN8q8ATkW4wVvWYLsKH5vRrPuQq2"],
  ["144.76.186.36:31245", "5zRyerpUbWaSxj8b1e2xtdCSwbGiGCYyTycdaHPEo1bfZNH9yR"],
  ["167.179.79.174:31245", "5it6jen7D9nDkCj6hdmNDfKdMAphowpzazWSP4LPVFp2AkTcQR"],
  ["194.163.182.21:31245", "8J1LKF3jGvW5oCC62Jt88a65pPziQsYMjRE1UAdHRVztqkcShJ"],
  ["217.79.180.243:31245", "8EU1DXur3rDZxNztccFy1caaWk8wz5K6CqKes6am71PLuHf3f8"],
  ["185.197.195.13:31245", "5A2n8naajRVGN6R3HtKNSEGNn25dgcMQaBXLqmAf9HLankjojF"],
  ["78.46.148.56:31245", "5yFboU7QBPY5XPVXvRWaSk71TQV3BjUounWR88kcbrkXdXozDn"],
  ["209.145.53.208:31245", "8N4F33MyFqRxwxAbTogbvQuLZ5bXNeRqaBezGzdPeLsCj9L4Ay"],
  ["75.119.151.244:31245", "8BvM2VhHT1Xpv4HhuoCC1duAJoZA5rapSMPgPfVMSpntqD1TbS"],
  ["194.163.165.246:31245", "7RQz9w4gkXUCDtmhWhwekczrjiSEAMn24HswVs36StQqUjfjwS"],
  ["79.143.181.220:31245", "6GHNwdqDpHPusUYXNNKUnKrQfEyW47YyPjaMCXKB7gzdpYHfJt"],
  ["188.40.106.218:31245", "6iwHSRFjBAFkXBP8P1fYRiXAWUX15xyhZGwuXh5jrQtLnyz1An"],
  ["207.148.15.99:31245", "8fb46obmNJinZByTZzHbsP9MjNPJeZNgYB1DPj8LBrSZsBnDMh"],
  ["135.181.250.24:31245", "6KQk27HC22dzqzoTH7GsU4PGLcFSTb6UJp4fhgarL9qUqrUWMF"],
  ["143.198.141.7:31245", "6pVSAJHuK68RK4R1aD6Wm8HtFh8XCjHyR8adhm7PDmJw2Gad21"],
]

with open(config_abspath, 'r') as fh:
    config = toml.load(fh)

config['bootstrap']['bootstrap_list'] = bootstrap_list

with open(config_abspath, 'w') as fh:
    toml.dump(config, fh)
