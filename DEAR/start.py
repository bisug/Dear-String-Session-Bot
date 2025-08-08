from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import OWNER_ID, F_SUB
from DEAR.db import db

@Client.on_message(filters.private & filters.command("start"))
async def start(bot: Client, msg: Message):
    # Save new users to DB
    if not await db.is_user_exist(msg.from_user.id):
        await db.add_user(msg.from_user.id, msg.from_user.first_name)

    # Force subscribe check
    if F_SUB:
        try:
            await bot.get_chat_member(int(F_SUB), msg.from_user.id)
        except:
            try:
                invite_link = await bot.create_chat_invite_link(int(F_SUB))
            except:
                await msg.reply("**❌ Make sure I am an admin in your channel with invite link permissions.**")
                return

            key = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("📢 Join Update Channel", url=invite_link.invite_link)],
                    [InlineKeyboardButton("✅ Check Again", callback_data="chk")]
                ]
            )

            await msg.reply_text(
                "**⚠️ Access Denied! ⚠️\n\nPlease join my update channel to use me. Once joined, click 'Check Again' to confirm.**",
                reply_markup=key
            )
            return  

    # If no F_SUB or already subscribed
    me = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""<b>𝐇𝐞𝐲 {msg.from_user.mention}🍷,\n\nɪ ᴀᴍ {me},\nᴛʀᴜsᴛᴇᴅ 𝗦𝗧𝗥𝗜𝗡𝗚 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 ʙᴏᴛ — ғᴜʟʟʏ sᴀғᴇ & sᴇᴄᴜʀᴇ.\nɴᴏ ᴀɴʏ ᴇʀʀᴏʀ!</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="⚡ Generate String Session ⚡", callback_data="generate")],
                [
                    InlineKeyboardButton("💬 Support Group", url="https://t.me/SuMelodyVibes"),
                    InlineKeyboardButton("📢 Update Channel", url="https://t.me/dear_sumi")
                ]
            ]
        )
    )

@Client.on_callback_query(filters.regex("chk"))
async def chk(bot: Client, cb: CallbackQuery):
    try:
        await bot.get_chat_member(int(F_SUB), cb.from_user.id)
    except:
        await cb.answer("🙅‍♂️ You are not joined my channel. Please join first, then try again.", show_alert=True)
        return

    me = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=cb.from_user.id,
        text=f"""<b>𝐇𝐞𝐲 {cb.from_user.mention}🍷,\n\nɪ ᴀᴍ {me},\nᴛʀᴜsᴛᴇᴅ 𝗦𝗧𝗥𝗜𝗡𝗚 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 ʙᴏᴛ — ғᴜʟʟʏ sᴀғᴇ & sᴇᴄᴜʀᴇ.\nɴᴏ ᴀɴʏ ᴇʀʀᴏʀ!</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="⚡ Generate String Session ⚡", callback_data="generate")],
                [
                    InlineKeyboardButton("💬 Support Group", url="https://t.me/SuMelodyVibes"),
                    InlineKeyboardButton("📢 Update Channel", url="https://t.me/dear_sumi")
                ]
            ]
        )
    )
