# Bayangkan kamu buat AI model yang bisa predict crypto price
# OOP bikin code lebih organized dan reusable

class CryptoPricePredictor:
    """Class untuk predict harga crypto"""
    
    def __init__(self, model_name, ticker):
        # __init__ = constructor, jalankan sekali saat object dibuat
        self.model_name = model_name
        self.ticker = ticker  # BTC, ETH, dll
        self.model = None
        self.accuracy = 0
        print(f"Predictor untuk {ticker} sudah siap!")
    
    def train(self, historical_data):
        """Method untuk training model"""
        print(f"Training {self.model_name} dengan {len(historical_data)} data points...")
        # Di sini nanti kita pake scikit-learn
        self.accuracy = 0.87  # dummy value, nanti beneran
        print(f"Akurasi model: {self.accuracy:.2%}")
    
    def predict(self, current_price):
        """Method untuk predict harga berikutnya"""
        if self.model is None:
            print("❌ Model belum di-train!")
            return None
        
        predicted_price = current_price * 1.05  # dummy logic
        return predicted_price

# Cara pakai:
btc_predictor = CryptoPricePredictor("Random Forest", "BTC")
# Output: Predictor untuk BTC sudah siap!

btc_predictor.train([100, 105, 102, 108, 110])
# Output: Training Random Forest dengan 5 data points...
#         Akurasi model: 87.00%

next_price = btc_predictor.predict(50000)
# Output: 52500