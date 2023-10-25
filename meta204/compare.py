import os
import json

seen_unis = [
            "4FEF",
            "53E4",
            "55DF",
            "5929",
            "5BDF",
            "5E74",
            "609F",
            "6216",
            "65BC",
            "66AB",
            "6975",
            "6BCF",
            "6FC0",
            "7576",
            "7AF9",
            "80FD",
            "82E5",
            "89D2",
            "8DA3",
            "9577",
            "98A8",
            "5167",
            "53EF",
            "5617",
            "592B",
            "5C07",
            "5E7D",
            "60B2",
            "6240",
            "65E2",
            "66AE",
            "6A02",
            "6C23",
            "70BA",
            "7678",
            "7BA1",
            "8129",
            "8302",
            "89F4",
            "8DB3",
            "9593",
            "9A01",
            "5176",
            "53F3",
            "56E0",
            "5951",
            "5C11",
            "5E9C",
            "60BC",
            "62B1",
            "65E5",
            "66F2",
            "6B21",
            "6C34",
            "7121",
            "76DB",
            "7D42",
            "81E8",
            "842C",
            "8A00",
            "8DE1",
            "9670",
            "9AB8",
            "5217",
            "5408",
            "56FA",
            "5984",
            "5C71",
            "5F15",
            "60C5",
            "652C",
            "6614",
            "6703",
            "6B23",
            "6C38",
            "7136",
            "76E1",
            "7D43",
            "81EA",
            "862D",
            "8A17",
            "8E81",
            "9673",
            "9F4A",
            "521D",
            "548C",
            "5728",
            "5A1B",
            "5CFB",
            "5F62",
            "653E",
            "6620",
            "6709",
            "6B64",
            "6CC1",
            "7336",
            "76F8",
            "7D72",
            "81F3",
            "865B",
            "8A60",
            "8FF0",
            "96A8",
            "5316",
            "54B8",
            "5730",
            "5B87",
            "5DBA",
            "5F6D",
            "60E0",
            "6545",
            "6625",
            "6717",
            "6B72",
            "6D41",
            "751F",
            "77E3",
            "7FA4",
            "81F4",
            "8A95",
            "9047",
            "96C6",
            "53C8",
            "54C1",
            "5750",
            "5B99",
            "5DE6",
            "5F8C",
            "611F",
            "6558",
            "662F",
            "671F",
            "6B7B",
            "6D6A",
            "7531",
            "77E5",
            "8001",
            "8207",
            "8996",
            "8AF8",
            "904A",
            "96D6",
            "53CA",
            "54C9",
            "5916",
            "5BA4",
            "5DF1",
            "5F97",
            "6168",
            "6587",
            "6642",
            "672A",
            "6B8A",
            "6E05",
            "7562",
            "77ED",
            "8005",
            "8208",
            "89BD",
            "8C48",
            "9077",
            "975C",
            "53D6",
            "55BB",
            "5927",
            "5BC4",
            "5E36",
            "5FEB",
            "61F7",
            "65AF",
            "66A2",
            "6797",
            "6BA4",
            "6E4D",
            "7570",
            "7A3D",
            "807D",
            "820D",
            "89C0",
            "8CE2",
            "9304",
            "985E",
            "60D3",
            "8909"
        ]
unseen_unis = [
            "4E8B",
            "4ECA",
            "4FC2",
            "4E8E",
            "4F5C",
            "4E11",
            "4FE1",
            "4E00",
            "4EAD",
            "4EBA",
            "4E16",
            "4E0D",
            "4E4B",
            "4EA6",
            "4EF0",
            "4E5D",
            "4E5F",
            "4EE5",
            "4FDB",
            "4E91"
        ]


seen_unis = [chr(int(x, 16)) for x in seen_unis]
unseen_unis = [chr(int(x, 16)) for x in unseen_unis]

cm = "/research/dept8/fyp22/fyy2203/FYP2/meta204/val"

meta = os.listdir(cm)

for font in meta:
    print(font)
    j = 0
    ff = os.path.join(cm,font)
    file = os.listdir(ff)
    file = [x.split(".png")[0] for x in file]
    
    font_seen = [x for x in seen_unis if x not in file]
    font_un = [x for x in unseen_unis if x not in file]
    print(font_seen)
    print(font_un)