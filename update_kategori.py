import discord
import asyncio
import os
from datetime import datetime, time, timedelta, timezone

TOKEN = os.getenv("DISCORD_TOKEN")
CATEGORY_ID = int(os.getenv("CATEGORY_ID"))

# Misal zona waktu Indonesia (WIB = UTC+7)
WIB = timezone(timedelta(hours=7))

def get_waktu_teks(now):
    jam = now.hour + now.minute/60

    # Malam: 22:00–05:00
    if jam >= 22 or jam < 5:
        return "MALAM"
    # Pagi: 05:00–10:00
    elif 5 <= jam < 10:
        return "PAGI"
    # Siang: 10:00–16:00
    elif 10 <= jam < 16:
        return "SIANG"
    # Sore: 16:00–22:00
    else:
        return "SORE"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot login sebagai {client.user}")

    category = client.get_channel(CATEGORY_ID)
    if category and isinstance(category, discord.CategoryChannel):
        now = datetime.now(WIB)
        waktu_teks = get_waktu_teks(now)
        new_name = f"❖━━━━━『 PAKET {waktu_teks} 』━━━━━❖"
        await category.edit(name=new_name)
        print(f"✅ Kategori diubah jadi: {new_name}")
    else:
        print("❌ Kategori tidak ditemukan atau ID salah.")

    await client.close()

asyncio.run(client.start(TOKEN))
