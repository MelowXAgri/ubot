import asyncio
import io
import os

import cv2
import requests
from pyrogram import raw

from PyroUbot import *


async def ReTrieveFile(input_file_name):
    headers = {"X-API-Key": RMBG_API}
    files = {"image_file": (input_file_name, open(input_file_name, "rb"))}
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True,
    )


async def process_image(client, message, process_func):
    if RMBG_API is None:
        return

    if message.reply_to_message:
        reply_message = message.reply_to_message
        processing_msg = await message.reply("<i>ᴘʀᴏᴄᴇssɪɴɢ...</i>")

        try:
            if (
                isinstance(reply_message.media, raw.types.MessageMediaPhoto)
                or reply_message.media
            ):
                downloaded_file_name = await client.download_media(
                    reply_message, "./downloads/"
                )
                await processing_msg.edit(
                    "<i>ᴍᴇɴɢʜᴀᴘᴜs ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ᴅᴀʀɪ ɢᴀᴍʙᴀʀ ɪɴɪ...</i>"
                )
                output_file_name = await ReTrieveFile(downloaded_file_name)
                os.remove(downloaded_file_name)
            else:
                await processing_msg.edit(
                    "<i>ʙᴀɢᴀɪᴍᴀɴᴀ ᴄᴀʀᴀ ᴍᴇɴɢʜᴀᴘᴜs ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ɪɴɪ?</i>"
                )
        except Exception as e:
            return await processing_msg.edit(f"{str(e)}")

        content_type = output_file_name.headers.get("content-type")

        if "image" in content_type:
            with io.BytesIO(output_file_name.content) as remove_bg_image:
                remove_bg_image.name = "rbg.png"
                await client.send_document(
                    message.chat.id,
                    document=remove_bg_image,
                    force_document=True,
                    reply_to_message_id=message.id,
                )
                await processing_msg.delete()
        else:
            await processing_msg.edit(
                "<b>Error:</b>\n<i>{}</i>".format(
                    output_file_name.content.decode("UTF-8")
                )
            )
    else:
        await message.reply("sɪʟᴀᴋᴀɴ ᴍᴇᴍʙᴀʟᴀs ɢᴀᴍʙᴀʀ")


async def process_image_command(client, message, process_func):
    ureply = message.reply_to_message
    processing_msg = await message.reply("<i>ᴘʀᴏᴄᴇssɪɴɢ...</i>")

    if not ureply:
        return await processing_msg.edit("sɪʟᴀᴋᴀɴ ᴍᴇᴍʙᴀʟᴀs ɢᴀᴍʙᴀʀ")

    downloaded_file_name = await client.download_media(ureply, "./downloads/")

    if downloaded_file_name.endswith(".tgs"):
        cmd = ["lottie_convert.py", downloaded_file_name, "yin.png"]
        file = "v1.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        img = cv2.VideoCapture(downloaded_file_name)
        heh, lol = img.read()
        cv2.imwrite("v1.png", lol)
        file = "v1.png"

    image = cv2.imread(file)

    if process_func == cv2.GaussianBlur:
        processed_image = cv2.GaussianBlur(image, (35, 35), 0)
    elif process_func == cv2.bitwise_not:
        processed_image = cv2.bitwise_not(image)
    elif process_func == cv2.flip:
        mirrored_image = cv2.flip(image, 1)
        processed_image = cv2.hconcat([image, mirrored_image])

    cv2.imwrite("v1.jpg", processed_image)

    await client.send_photo(
        message.chat.id,
        "v1.jpg",
        reply_to_message_id=message.id,
    )
    await processing_msg.delete()
    os.remove("v1.png")
    os.remove("v1.jpg")
    os.remove(downloaded_file_name)


async def rbg_cmd(client, message):
    await process_image(client, message, ReTrieveFile)


async def blur_cmd(client, message):
    await process_image_command(client, message, cv2.GaussianBlur)


async def negative_cmd(client, message):
    await process_image_command(client, message, cv2.bitwise_not)


async def miror_cmd(client, message):
    await process_image_command(client, message, cv2.flip)
