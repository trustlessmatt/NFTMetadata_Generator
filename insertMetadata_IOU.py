import os
import json

if not os.path.exists('./metadata'):
    os.makedirs('./metadata')

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }

for i in range(0, 39):
    token_id = i
    token = {
        "name": "IOU",
        "symbol": "IOU",
        "image": str(token_id) + '.png',
        "description": "This is a placeholder for your special fries.  Fox is cooking em! Chill!!! This is meant for staking only and not for resale - or transfer.  When your special fries are ready we will exchange this NFT for your custom piece. This NFT will de-activate within 30 days and be completely useless.",
        "tokenId": token_id,
        "external_url": "http://www.mickeydegods.com/",
        "seller_fee_basis_points": 10000,
        "properties": {
          "files": [
            {
              "uri": str(token_id) + '.png',
              "type": "image/png"
            }
          ],
          "category": "image",
          "creators": [
            {
              "address": "J7T25FgKxrHqL7CpX8r6kSMcSRgST21mgkf5jCtw1z6j", # DAO addy
              "share": 100
            }
          ]
        },
        "collection": {"name": "IOU", "family": "IOU"},
        "attributes": []
    }
    token["attributes"].append(getAttribute("What are you looking at?", "Nothing to see here"))

    with open('./metadata/' + str(token_id) + ".json", 'w', newline='') as outfile:
        json.dump(token, outfile, indent=4)
