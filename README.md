# ZooDAO 
## StakingPool

Forked from 
[https://github.com/Synthetixio/synthetix/tree/v2.27.2/](https://github.com/Synthetixio/synthetix/tree/v2.27.2/)

#### This repository contains the staking pool contract of the Zoo DAO project.

##### StakingPool contract is designed to stake sushi LP (Zoo-Dai) tokens with provided rewards in Zoo tokens.

Contract were designed to allocate rewards among stakers proportionally to their staked value and their staked time.
Reward amount were decided to remain the same during all staking time.

* Amount of reward allocated among all stakers for is predefined and stored in contract balance.

* Total reward per second in pool calculates as Zoo balance divided at **duration()**


##### Individual rewards for staking is basically based on totalRewardPerSecond divided by amount of stakers and multiplied by staked value.

| mainnet | address |
| --- | --- |
| Zoo Token | 0x09F098B155D561Fc9F7BcCc97038b7e3d20bAF74 |
| Zoo Token sushi LP (ZOO-DAI) | 0x8496E5f9bFb467841427e4f3183181C2E8DC162b |
| StakingPool | 0xF43De6A8b74dA89231F5aa91900E5d07b1d57046 |

| kovan | address |
| --- | --- |
| Zoo Token | 0x74a99f340108a8e9Ffe1a646829d20a9499E9687 |
| Zoo Reward Token(for kovan only) | 0x5816ceCaA2d0ACe3528090C61Dd19D1cA6F3a4e5 |
| Zoo-eth uniswap LP | 0xa6a1326Ac1a7F9C29443e45aD63fA659AfD01d4d |
| StakingPool | 0xb77B1E414d7eA884f5FeF1b7F34f526dc3E850dE |

> brownie  v1.16.1 - v1.18.1

> OpenZeppelin  v2.3.0

For running tests, clone the repository, and use ***brownie test*** command from the project root directory
