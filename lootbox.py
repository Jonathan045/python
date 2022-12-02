while True:

 import random

 rarity=("common","common","common","common","common","common","common","common","common","common","uncommon","uncommon","uncommon","uncommon","uncommon","rare","rare","rare","epic","epic","legendary")

 begin= input("Welkom bij de beste lootbox ooit, zou je willen proberen voor €5? ja/nee")

 if begin == "ja":

    print(random.choice(rarity))

 if begin == "nee":

    print("helaas")

    break