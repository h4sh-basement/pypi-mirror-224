from covalent import Client
import pytest
import os


class TestNftService:
    
    @pytest.fixture
    def client(self):
        return Client(os.environ.get('COVALENT_API_KEY'))

    
    def test_success(self, client: Client):
        res = client.nft_service.get_chain_collections("eth-mainnet")
        assert res.error == False
        assert res.data.chain_id == 1
        assert res.data.chain_name == "eth-mainnet"
        assert len(res.data.items) > 0
        
    
    def test_unsupported_chains(self, client: Client):
        res = client.nft_service.get_chain_collections("fantom-mainnet")
        assert res.error == True
        assert res.data == None
        assert res.error_message == "250/fantom-mainnet chain not supported, currently supports: 1/eth-mainnet 56/bsc-mainnet 137/matic-mainnet 10/optimism-mainnet 42161/arbitrum-mainnet "
        assert res.error_code == 400
        
    
    def test_success_for_nfts_address(self, client: Client):
        res = client.nft_service.get_nfts_for_address("eth-mainnet", "demo.eth")
        assert res.error == False
        assert res.data.address == "0xfc43f5f9dd45258b3aff31bdbe6561d97e8b71de"
        assert len(res.data.items) > 0
    
    
    def test_no_asset_metadata(self, client: Client):
        res = client.nft_service.get_nfts_for_address("eth-mainnet", "demo.eth", None, True)
        assert res.error == False
        assert res.data.address == "0xfc43f5f9dd45258b3aff31bdbe6561d97e8b71de"
        assert len(res.data.items) > 0
        assert res.data.items[0].nft_data[0].original_owner == None
        assert res.data.items[0].nft_data[0].external_data == None
        assert res.data.items[0].nft_data[0].asset_cached == None
        assert res.data.items[0].nft_data[0].image_cached == None
    
    
    def test_success_for_token_Ids_for_contract_metadata(self, client: Client):
        res = client.nft_service.get_token_ids_for_contract_with_metadata("eth-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b6")
        assert res.error == False
        assert len(res.data.items) > 0
        assert res.data.items[0].contract_name == "Potatoz"
    
    
    def test_no_metadata_for_token_Ids_for_contract_metadata(self, client: Client):
        res = client.nft_service.get_token_ids_for_contract_with_metadata("eth-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b6", True)
        assert res.error == False
        assert len(res.data.items) > 0
        assert res.data.items[0].nft_data.external_data == None
    
    
    def test_success_for_nft_metadata_token_Id_contract(self, client: Client):
        res = client.nft_service.get_nft_metadata_for_given_token_id_for_contract("eth-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b6", "7142")
        assert res.error == False
        assert len(res.data.items) > 0
        assert res.data.items[0].contract_name == "Potatoz"
        assert res.data.items[0].nft_data.token_id == 7142
        assert res.data.items[0].nft_data.external_data.name == "Potatoz #7142"
    
    
    def test_no_metadata_for_nft_metadata_token_Id_contract(self, client: Client):
        res = client.nft_service.get_nft_metadata_for_given_token_id_for_contract("eth-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b6", "7142", True)
        assert res.error == False
        assert res.data.items[0].nft_data.external_data == None
    
    
    def test_success_for_nft_transactions_contract_token_Id(self, client: Client):
        res = client.nft_service.get_nft_transactions_for_contract_token_id("eth-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b6", "7142")
        assert res.error == False
        assert len(res.data.items) > 0
        assert res.data.items[0].contract_name == "Potatoz"
        assert len(res.data.items[0].nft_transactions) > 0
    
    
    def test_malformed_addres_for_nft_transactions(self, client: Client):
        res = client.nft_service.get_nft_transactions_for_contract_token_id("eth-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b62123", "7142")
        assert res.error == True
        assert res.data == None
        assert res.error_code == 400
        assert res.error_message == "Malformed address provided: 0x39ee2c7b3cb80254225884ca001f57118c8f21b62123"
    
    
    def test_success_traits_collection(self, client: Client):
        res = client.nft_service.get_traits_for_collection("eth-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b6")
        assert res.error == False
        assert len(res.data.items) > 0
        assert res.data.items[0].name == "Type"
        assert res.data.items[1].name == "Stage"
        assert res.data.items[2].name == "Size"
        assert res.data.items[3].name == "Pose"
        assert res.data.items[4].name == "Mutation"
        assert res.data.items[5].name == "Element"

    
    def test_unsupported_address_traits_collection(self, client: Client):
        res = client.nft_service.get_traits_for_collection("fantom-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b6")
        assert res.error == True
        assert res.data == None
        assert res.error_message == "250/fantom-mainnet chain not supported, currently supports: 1/eth-mainnet 56/bsc-mainnet 137/matic-mainnet 10/optimism-mainnet 42161/arbitrum-mainnet "
        assert res.error_code == 400
    
    
    def test_success_for_attributes_trait_collection(self, client: Client):
        res = client.nft_service.get_attributes_for_trait_in_collection("eth-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b6", "Type")
        assert res.error == False
        assert len(res.data.items) > 0
        assert res.data.items[0].trait_type == "Type"
        assert len(res.data.items[0].values) > 0
    
    
    
    def test_invalid_trait_address_for_attributes_trait_collection(self, client: Client):
        res = client.nft_service.get_attributes_for_trait_in_collection("eth-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b6", "Color")
        assert res.error == False
        assert len(res.data.items[0].values) == 0

    
    
    def test_success_collection_traits_summary(self, client: Client):
        res = client.nft_service.get_collection_traits_summary("eth-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b6")
        assert res.error == False
        assert len(res.data.items) > 0
        assert res.data.items[0].name == "Type"
        assert res.data.items[1].name == "Stage"
        assert res.data.items[2].name == "Size"
        assert res.data.items[3].name == "Pose"
        assert res.data.items[4].name == "Mutation"
        assert res.data.items[5].name == "Element"
        
    
    def test_invalid_contract_address_collection_traits_summary(self, client: Client):
        res = client.nft_service.get_collection_traits_summary("eth-mainnet", "0x23492")
        assert res.error == True
        assert res.data == None
        assert res.error_code == 400
        assert res.error_message == "Malformed address provided: 0x23492"
    
    
    
    def test_success_check_ownership_nft(self, client: Client):
        res = client.nft_service.check_ownership_in_nft("eth-mainnet", "0xe1da9e3ea9efc074ebffd4d2bed209b370705188", "0x510647c2064c4b1cc32bfb19d04b3919f0020559")
        assert res.error == False
        assert len(res.data.items) > 0
        assert res.data.collection == "0x510647c2064c4b1cc32bfb19d04b3919f0020559"
        assert res.data.address == "0xe1da9e3ea9efc074ebffd4d2bed209b370705188"
        assert res.data.items[0].contract_name == "Yamabushi's Horizons by Richard Nadler"
    
    
    
    def test_malformed_address_check_ownership_nft(self, client: Client):
        res = client.nft_service.check_ownership_in_nft("eth-mainnet", "0x123", "0x510647c2064c4b1cc32bfb19d04b3919f0020559")
        assert res.error == True
        assert res.data == None
        assert res.error_code == 400
        assert res.error_message == "Malformed address provided: 0x123"
    
    
    
    def test_success_check_ownership_nft_token_Ids(self, client: Client):
        res = client.nft_service.check_ownership_in_nft_for_specific_token_id("eth-mainnet", "0xe1da9e3ea9efc074ebffd4d2bed209b370705188", "0x510647c2064c4b1cc32bfb19d04b3919f0020559", "1801236275")
        assert res.error == False
        assert len(res.data.items) > 0
        assert res.data.collection == "0x510647c2064c4b1cc32bfb19d04b3919f0020559"
        assert res.data.address == "0xe1da9e3ea9efc074ebffd4d2bed209b370705188"
        assert res.data.items[0].token_id == 1801236275
    
    
    
    def test_wallet_not_own_nft(self, client: Client):
        res = client.nft_service.check_ownership_in_nft_for_specific_token_id("eth-mainnet", "0x1a002d5d3807adcd194c233c293105366419b54d", "0x510647c2064c4b1cc32bfb19d04b3919f0020559", "1801236275")
        assert res.error == False
        assert len(res.data.items) == 0
    
    
    
    def test_malformed_address_ownership_nft_tokens(self, client: Client):
        res = client.nft_service.check_ownership_in_nft_for_specific_token_id("eth-mainnet", "0x123", "0x510647c2064c4b1cc32bfb19d04b3919f0020559", "1801236275")
        assert res.error == True
        assert res.data == None
        assert res.error_code == 400
        assert res.error_message == "Malformed address provided: 0x123"
    
    
    
    def test_success_nft_external_metadata_contract(self, client: Client):
        res = client.nft_service.get_nft_external_metadata_for_contract("eth-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b6", "7142")
        assert res.error == False
        assert len(res.data.items) > 0
        assert res.data.items[0].contract_name == "Potatoz"
        assert res.data.items[0].contract_address == "0x39ee2c7b3cb80254225884ca001f57118c8f21b6"
        assert res.data.items[0].type == "nft"
    
    
    
    def test_invalid_address_external_metadata_contract(self, client: Client):
        res = client.nft_service.get_nft_external_metadata_for_contract("eth-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b", "7142")
        assert res.error == True
        assert res.error_code == 400
        assert res.error_message == "Malformed address provided: 0x39ee2c7b3cb80254225884ca001f57118c8f21b" 
    

    
    def test_invalid_token_Id_external_metadata_contract(self, client: Client):
        res = client.nft_service.get_nft_external_metadata_for_contract("eth-mainnet", "0x39ee2c7b3cb80254225884ca001f57118c8f21b6", "1asd")
        assert res.error == True
        assert res.error_code == 400
        assert res.error_message == "Invalid tokenID parameter" 
       
    
    
    
    
    
    
    
    
    
        
        
    
        

    
    
    
    
    
    
    
    
    
    
