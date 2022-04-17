import os
import io
import csv
import sys
import math
import json

# This tool takes Mickey Degods Combo NFT data and inserts it into
# JSON files corresponding to the NFT (name of file, file attributes)

# pseudo:
#1: Fox delivers a folder of numbered images 0 thru n
#2: The metadata on our spreadsheet has every piece of data needed as well as a matching ID to the image
#3: For each image number in the list...
  # Grab trait info for this image:
    # Combo name
    # Royalty address
    # Attributes: 
      # Items 1 thru 5 (none is valid entry)
      # Skin
      # Chain
      # Neck tat
      # Arm tat
      # Special
    # Calculated royalty (number out of 100, i.e. 5% = 5)
  # Insert into an array (list)
  # Dump into JSON named after this image number

#### Generate Metadata for each Image    

f = open('./combos_test.json',) 

if not os.path.exists('./metadata'):
    os.makedirs('./metadata')

data = json.load(f)

# Changes this IMAGES_BASE_URL to yours 
IMAGES_BASE_URL = "uploaded images URL"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }

for i in data:
    token_id = i['tokenId']
    share = i['share']
    addy = i['address']
    token = {
        "name": str(i['name']).strip(),
        "symbol": "COMBO",
        "image": str(token_id) + '.png', #IMAGES_BASE_URL + 
        "description": "You've picked up some tasty treats, and now you've minted them into a Mickey's combo. Get ready to stake that shiz!",
        "tokenId": token_id,
        "seller_fee_basis_points": 1000,
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
              "share": 100 - share
            },
            {
              "address": str(addy).strip(), #royalty addy
              "share": share
            }
          ]
        },
        "attributes": []
    }
    token["attributes"].append(getAttribute("Item 1", i["Item 1"]))
    token["attributes"].append(getAttribute("Item 2", i["Item 2"]))
    token["attributes"].append(getAttribute("Item 3", i["Item 3"]))
    token["attributes"].append(getAttribute("Item 4", i["Item 4"]))
    token["attributes"].append(getAttribute("Item 5", i["Item 5"]))
    token["attributes"].append(getAttribute("Skin", i["Skin"]))
    token["attributes"].append(getAttribute("Chain", i["Chain"]))
    token["attributes"].append(getAttribute("Neck Tat", i["Neck Tat"]))
    token["attributes"].append(getAttribute("Arm Tat", i["Arm Tat"]))
    token["attributes"].append(getAttribute("Special", i["Special"]))

    with open('./metadata/' + str(token_id) + ".json", 'w', newline='') as outfile:
        json.dump(token, outfile, indent=4)

f.close()


# # for each line in the list...
# for myFile in fileList:
#     # create the input file and prepare for writing
#     with open(inputFileLocation + myFile + '.csv', 'w', newline='') as inputFileCSV:
#         # create writer object
#         resultsFileWriter = csv.writer(inputFileCSV)
#         # file creation based on keywords in file name
#         if 'grades' in myFile:
#             if 'quiz' in myFile:
#                 resultsFileWriter(['name', 'question', 'result', 'comment']) # header row
#                 for row in inputMatrix_df.itertuples():
#                     # write to file
#                     if row.Result != "True":
#                         resultsFileWriter.writerow([row.name, row.question, row.result, row.comment])
#                     else:
#                         resultsFileWriter.writerow([row.name, row.question, row.result, "N/A"])
#             elif 'exam' in myFile:
#                 # do stuff