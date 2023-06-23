from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "simo",
    api_id=26022994,
    api_hash="2e84a6b68bd6b5a79f46e8192668e0ea",
    bot_token="6013874411:AAF95252Q7i6sqOTpDEkBKAca949CxIvIJU",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    S_E_M_O_E_L_K_B_E_R = "r_n_b1"
    await bot.send_message(r_n_b1, "** فشغيل الصانع عزيزي فينوم. **")
    print("[INFO]: فينوم قلبايي")
    await idle()
