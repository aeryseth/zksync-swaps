from web3 import Web3, HTTPProvider, Account
from zksync_sdk import ZkSyncProviderV01, HttpJsonRPCTransport, network, ZkSync, EthereumProvider, Wallet, ZkSyncSigner, EthereumSignerWeb3, ZkSyncLibrary
# Load crypto library
library = ZkSyncLibrary()
# Create Zksync Provider
provider = ZkSyncProviderV01(provider=HttpJsonRPCTransport(network=network.goerli))
# Setup web3 account
account = Account.from_key("PRIVATE_KEY")
# Create EthereumSigner
ethereum_signer = EthereumSignerWeb3(account=account)
# Load contract addresses from server
contracts = await provider.get_contract_address()
# Setup web3
# NOTE: Please ensure that the web3 provider and zksync provider match.
# A mainnet web3 provider paired with a testnet zksync provider will transact on mainnet!!
w3 = Web3(HTTPProvider(endpoint_uri="GETH_ENDPOINT" ))
# Setup zksync contract interactor
zksync = ZkSync(account=account, web3=w3,
                zksync_contract_address=contracts.main_contract)
# Create ethereum provider for interacting with ethereum node
ethereum_provider = EthereumProvider(w3, zksync)

# Initialize zksync signer, all creating options were described earlier
signer = ZkSyncSigner.from_account(account, library, network.goerli.chain_id)
# Initialize Wallet
wallet = Wallet(ethereum_provider=ethereum_provider, zk_signer=signer,
                eth_signer=ethereum_signer, provider=provider)
