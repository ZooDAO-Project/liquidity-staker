#!/usr/bin/python3

import brownie
from brownie import chain

def test_stake(accounts, staking_contracts):
	(staked_token, reward_token, staking) = staking_contracts

	time1 = chain.time()
	staking.stake(1e17, {'from': accounts[1]})

	chain.sleep(1000)

	tx1 = staking.getReward({"from": accounts[1]})
	reward1 = tx1.events["RewardPaid"]["reward"]
	staking.stake(1e17, {"from": accounts[2]})

	time2 = chain.time()
	chain.sleep(1000)

	tx2 = staking.getReward({"from": accounts[1]})
	reward2 = tx2.events["RewardPaid"]["reward"]
	staking.withdraw(1e17, {"from": accounts[2]})

	time3 = chain.time()
	chain.sleep(1000)

	tx3 = staking.getReward({"from": accounts[1]})
	reward3 = tx3.events["RewardPaid"]["reward"]

	print("rewards:")
	print(reward1)
	print(reward2)
	print(reward3)

	print("times:")
	print(time1)
	print(time2)
	print(time3)

	print(f"difference between reward1 and reward3 {reward3 - reward1}")

	assert reward2 < reward1
	assert reward2 < reward3
	assert reward3 - reward1 < 1e18 # 1e14 - eps
	assert abs(reward3 / reward2 - 2) < 0.002

def test_getReward_after_withdraw(accounts, staking_contracts):
	(staked_token, reward_token, staking) = staking_contracts

	time1 = chain.time()
	staking.stake(1e17, {'from': accounts[1]})

	chain.sleep(1000)

	tx1 = staking.getReward({"from": accounts[1]})
	reward1 = tx1.events["RewardPaid"]["reward"]
	staking.stake(1e17, {"from": accounts[2]})

	time2 = chain.time()
	chain.sleep(1000)

	tx2 = staking.getReward({"from": accounts[1]})
	reward2 = tx2.events["RewardPaid"]["reward"]
	staking.withdraw(1e17, {"from": accounts[2]})

	time3 = chain.time()
	chain.sleep(1000)

	tx3 = staking.getReward({"from": accounts[1]})
	reward3 = tx3.events["RewardPaid"]["reward"]
	
	tx4 = staking.getReward({"from": accounts[2]})
	reward4 = tx4.events["RewardPaid"]["reward"]

	assert reward4 - reward2 < 1e18