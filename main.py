import requests
import os

# --- CONFIGURATION ---
# Colombo/Ja-Ela Coordinates
LAT = 7.08  
LON = 79.89
# Telegram Creds (We will load these from Environment Variables for security)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def check_weather():
    print("Fetching weather data...")
    # Using OpenMeteo API (Free)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current=rain,showers&timezone=Asia%2FColombo"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Get current rain amount (mm)
        current_rain = data['current']['rain']
        current_showers = data['current']['showers']
        total_precip = current_rain + current_showers
        
        print(f"Current Precipitation: {total_precip} mm")
        
        # LOGIC: If rain is greater than 0.5mm, send alert
        # if total_precip > 0.5:
        #     msg = f"⚠️ WEATHER ALERT: Rain detected in Ja-Ela/Colombo area! ({total_precip}mm). Check construction sites and campus updates."
        #     send_telegram_alert(msg)
        #     print("Alert sent!")
        # else:
        #     print("Weather looks clear. No alert needed.")

        # --- MODIFIED FOR TESTING ---
        # We removed the 'if total_precip > 0.5' check
        msg = f"🔔 TEST ALERT: The bot is working! Rain in Ja-Ela: {total_precip}mm."
        send_telegram_alert(msg)
        print("Test alert sent!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Bot Token or Chat ID missing.")
    else:
        check_weather()