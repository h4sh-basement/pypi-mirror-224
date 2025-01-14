
// autogenerated by brownie
// do not modify the existing settings
module.exports = {
    initialBaseFeePerGas: 0,
    networks: {
        hardhat: {
            gasPrice: 0,
            // hardfork: "londqon",
            // base fee of 0 allows use of 0 gas price when testing
            initialBaseFeePerGas: 0,
            // brownie expects calls and transactions to throw on revert
            throwOnTransactionFailures: true,
            throwOnCallFailures: true,
            accounts: {
                mnemonic: "test test test test test test test test test test test junk",
                count: 1,
                accountsBalance: "80000000000000000000000000000" // 100M ETH
            }
       }
    }
}