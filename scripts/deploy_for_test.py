import brownie
from brownie import TestERC20, StakingRewards, accounts

def main():
	staked_token = TestERC20.deploy(1e21, {"from": accounts[0]})
	reward_token = TestERC20.deploy(2 * 1e24, {"from": accounts[0]})

	staking = StakingRewards.deploy(accounts[0], reward_token.address,staked_token.address, {"from": accounts[0]})

	for account in accounts[1:]:
		staked_token.transfer(account, 1e18, {"from": accounts[0]})
		staked_token.approve(staking.address, 1e18, {"from":account})
	
	reward = 2000000 * 1e18
	reward_token.transfer(staking, reward)
	staking.notifyRewardAmount(reward)

	return (staked_token, reward_token, staking)