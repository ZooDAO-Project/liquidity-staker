# Zoo DAO 
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
| Zoo Token sushi LP | tba |
| StakingPool | tba |

| kovan | address |
| --- | --- |
| Zoo Token | 0x74a99f340108a8e9Ffe1a646829d20a9499E9687 |
| Zoo Reward Token(for kovan only) | 0x61E6d7e7281bfcbD254Dc02F3b87e574f754826c |
| Zoo-eth uniswap LP | 0xa6a1326Ac1a7F9C29443e45aD63fA659AfD01d4d |
| StakingPool | 0xDB608dD7B180f1e1cfc2aaD86b34cBd674B0f3B7 |

> brownie  v1.16.1 - v1.18.1

> OpenZeppelin  v2.3.0

For running tests, clone the repository, and use ***brownie test*** command from the project root directory