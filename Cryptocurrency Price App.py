

###########################################################################

#                       Cryptocurrency Price App

###########################################################################




from gtts import gTTS                   # Google Text-to-Speech Library
import cryptocompare as cry             # Library that allows us to learn Cryptocurrency prices
from playsound import playsound



def cryptocurrency_price(crypto_short_name):            # Cryptocurrency's name parameter

    usdt_price = cry.get_price(crypto_short_name,currency="USDT")       # Getting Price
    btc_price = cry.get_price(crypto_short_name,currency="BTC")

    USDT = usdt_price[crypto_short_name]["USDT"]
    BTC = btc_price[crypto_short_name]["BTC"]

    print(f"""
{crypto_short_name} price is ${USDT}

The value of {crypto_short_name} in BTC is {BTC}""")



    text_for_gtts = f"{crypto_short_name} price is ${USDT}"

    sound_for_price = gTTS(text=text_for_gtts, lang="en", slow=False)       # Converting text to audio

    sound_for_price.save("price.mp3")

    playsound("price.mp3")          # Performing text audio


cryptocurrency_price("ETH")         # Enter the code that represents the Cryptocurrency.
                                    # Example: Bitcoin = BTC