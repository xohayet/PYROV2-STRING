import os
import asyncio

from pyrogram import Client

name = "Rekha"
api_id = 24906331
api_hash = "866e8e4637fb269388b50202fb0f169c"


async def init():
    print("🌺 Please Wait 🌿...")
    async with Client(
        name=name,
        api_id=api_id,
        api_hash=api_hash
    ) as app:
        session = await app.export_session_string()
        caption = f"**🥀 Your Pyrogram V2 String Session Is Here ✨...**\n\n`{session}`\n\n**©️ @NikkiAssociation**"
        try:
            await app.join_chat("NikkiAssociation")
            await app.join_chat("NikkiSupportChat")
            await app.send_message("NikkiSupportChat", "**Thank You For Your String\nGenerator Repository.**")
        except:
            pass
        try:
            await app.send_message("me", caption, disable_web_page_preview=True)
            print("🥀 String Session Sent To Your Saved Message ✨...")
        except Exception as e:
            print(f"🚫 Error: {e}")
        
    

if __name__ == "__main__":
    asyncio.run(init())
    for file in os.listdir():
        if file.endswith(".session"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".session-journal"):
            os.remove(file)
