from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "simo",
    api_id=24209135,
    api_hash="9ad05c7abeb3fd58effd1328bb2af596",
    bot_token="6544840789:AAGhSIt-KF3EePHp2GJqk0bzP8k5mIi7JY4",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    S_E_M_O_E_L_K_B_E_R = "r_n_b1"
    await bot.send_message(r_n_b1, "** فشغيل الصانع عزيزي فينوم. **")
    print("[INFO]: فينوم قلبايي")
    await idle()
