# weather Script 
import requests

# موقعیت شهر (مثلاً کابل)
latitude = 34.5553
longitude = 69.2075

# آدرس API از Open-Meteo
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

# ارسال درخواست
response = requests.get(url)

# بررسی موفق بودن پاسخ
if response.status_code == 200:
    data = response.json()  # داده را به JSON تبدیل می‌کنیم
    current = data.get("current_weather", {})
    temperature = current.get("temperature")
    windspeed = current.get("windspeed")

    print("🌤 گزارش هوا برای کابل:")
    print(f"دمای فعلی: {temperature}°C")
    print(f"سرعت باد: {windspeed} km/h")

else:
    print("❌ خطا در دریافت داده از سرور:", response.status_code)