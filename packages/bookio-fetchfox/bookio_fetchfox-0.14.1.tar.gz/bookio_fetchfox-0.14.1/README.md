# book.io / fetchfox

> Collection of API services to fetch information from several blockchains.

![](https://s2.coinmarketcap.com/static/img/coins/64x64/4030.png)
![](https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png)
![](https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png)
![](https://s2.coinmarketcap.com/static/img/coins/64x64/3890.png)


## Supported Blockchains

### Algorand

```python
import os
from fetchfox.blockchains import Algorand

algorand = Algorand(
    nftexplorerapp_api_key=os.getenv("NFTEXPLORER_API_KEY"),
)

# Brave New World
creator_address = "6WII6ES4H6UW7G7T7RJX63CUNPKJEPEGQ3PTYVVU3JHJ652W34GCJV5OVY"

for asset in algorand.get_assets(creator_address):
    print(asset)
```

#### Services

* get_asset ([algonode.cloud](https://algonode.cloud))
* get_assets ([algonode.cloud](https://algonode.cloud))
* get_holdings ([algonode.cloud](https://algonode.cloud))
* get_snapshot ([algonode.cloud](https://algonode.cloud))
* get_campaigns ([book.io](https://book.io))
* get_listings ([randgallery.com](https://randgallery.com) / [algoxnft.com](https://algoxnft.com))
* get_floor ([randgallery.com](https://randgallery.com) / [algoxnft.com](https://algoxnft.com))
* get_sales ([nftexplorer.app¹](https://nftexplorer.app))


### Cardano

```python
import os
from fetchfox.blockchains import Cardano

cardano = Cardano(
    blockfrostio_project_id=os.getenv("BLOCKFROST_PROJECT_ID"),
)

# Gutenberg Bible
policy_id = "477cec772adb1466b301fb8161f505aa66ed1ee8d69d3e7984256a43"

for asset in cardano.get_assets(policy_id):
    print(asset)
```

#### Services

* get_asset ([blockfrost.io²](https://blockfrost.io))
* get_assets ([blockfrost.io²](https://blockfrost.io))
* get_holdings ([blockfrost.io²](https://blockfrost.io))
* get_campaigns ([book.io](https://book.io))
* get_snapshot ([blockfrost.io²](https://blockfrost.io))
* get_listings ([jpg.store](https://jpg.store))
* get_floor ([jpg.store](https://jpg.store))
* get_sales ([jpg.store](https://jpg.store))
* get_ranks ([cnft.tools](https://cnft.tools))


### EVM (Ethereum and Polygon)

```python
import os
from fetchfox.blockchains import Ethereum, Polygon

ethereum = Ethereum(
    geckodriver_path=os.getenv("GECKODRIVER_PATH"),
    moralisio_api_key=os.getenv("MORALIS_API_KEY"),
    openseaio_api_key=os.getenv("OPENSEA_API_KEY"),
)

polygon = Polygon(
    geckodriver_path=os.getenv("GECKODRIVER_PATH"),
    moralisio_api_key=os.getenv("MORALIS_API_KEY"),
    openseaio_api_key=os.getenv("OPENSEA_API_KEY"),
)


# Alice in Wonderland
contract_address = "0x919da7fef646226f88f70305201de392ff365059"

for asset in ethereum.get_assets(contract_address):
    print(asset)

# Art of War
contract_address = "0xb56010e0500e4f163758881603b8083996ae47ec"

for asset in polygon.get_assets(contract_address):
    print(asset)
```

#### Services

* get_asset ([moralis.io³](https://moralis.io))
* get_assets ([moralis.io³](https://moralis.io))
* get_holdings ([moralis.io³](https://moralis.io))
* get_snapshot ([moralis.io³](https://moralis.io))
* get_campaigns ([book.io](https://book.io))
* get_listings ([opensea.io⁴](https://opensea.io))
* get_floor ([opensea.io⁴](https://opensea.io))
* get_sales ([opensea.io⁴](https://opensea.io))


> ¹ **nftexplorer.app** services require an [api key](https://www.nftexplorer.app/nftx-api).
> 
> ² **blockfrost.io** services require a [project id](https://blockfrost.dev/docs/overview/plans-and-billing).
> 
> ³ **moralis.io** services require an [api key](https://moralis.io/pricing).
> 
> ⁴ **opensea.io** some services also require an [api key](https://docs.opensea.io/reference/api-keys). 

---

![fetch, the fox](https://i.imgur.com/fm6mqzS.png)
> fetch, the fox

