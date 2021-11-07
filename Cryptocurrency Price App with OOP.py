from gtts import gTTS         # Google Text-to-Speech Library
import cryptocompare as cry   # Library that allows us to learn Cryptocurrency prices
from playsound import playsound




class cryptocurrency_app():


    def __init__(self,crypto_short_name):    # When the Class object is generated, the __init__ function starts to run.

        self.crypto_short_name = crypto_short_name



    def cryptocurrency_price(self):

        usdt_price = cry.get_price(self.crypto_short_name,currency="USDT")
        btc_price = cry.get_price(self.crypto_short_name,currency="BTC")

        self.USDT = usdt_price[self.crypto_short_name]["USDT"]
        self.BTC = btc_price[self.crypto_short_name]["BTC"]

        self.en_lang = f"""
    {self.crypto_short_name} price is ${self.USDT}
    
    The value of {self.crypto_short_name} in BTC is {self.BTC}"""   # English Text


        print(f"""
    {self.crypto_short_name} price is ${self.USDT}
    
    The value of {self.crypto_short_name} in BTC is {self.BTC}""")




    def converting_text_to_audio(self):

        text_for_gtts = f"{self.crypto_short_name} price is ${self.USDT}"

        sound_for_price = gTTS(text=text_for_gtts, lang="en", slow=False)

        sound_for_price.save("price.mp3")


        return  playsound("price.mp3")



    ##############  For German Language:


    def cryptocurrency_price_for_german(self):

        usdt_price = cry.get_price(self.crypto_short_name, currency="USDT")
        btc_price = cry.get_price(self.crypto_short_name, currency="BTC")

        self.USDT = usdt_price[self.crypto_short_name]["USDT"]
        self.BTC = btc_price[self.crypto_short_name]["BTC"]

        print(f"""
        Der {self.crypto_short_name}-Preis beträgt {self.USDT} US-Dollar

        Der Wert von {self.crypto_short_name} in BTC beträgt {self.BTC}.""")



    def converting_text_to_audio_for_german(self):

        text_for_gtts = f"Der {self.crypto_short_name}-Preis beträgt {self.USDT} US-Dollar"

        sound_for_price = gTTS(text=text_for_gtts, lang="de", slow=False)

        sound_for_price.save("price.mp3")


        return  playsound("price.mp3")





def run_app():

    choose_crypto = input("""
    Please Enter the Code of the Cryptocurrency you want: """)
    choose_lang = input("""
    For German Language: 1
        For English Language: 2""")

    perform_app = cryptocurrency_app(choose_crypto)      # Enter the code that represents the Cryptocurrency.
                                                                    # Example:  Solana = SOL

    if choose_lang == "1":

        perform_app.cryptocurrency_price_for_german()

        perform_app.converting_text_to_audio_for_german()

    else:

        perform_app.cryptocurrency_price()

        perform_app.converting_text_to_audio()



run_app()     # Perform App