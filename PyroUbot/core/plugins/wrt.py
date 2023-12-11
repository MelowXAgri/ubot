import os

from PIL import Image, ImageDraw, ImageFont


def text_set(text, max_line_length=55, max_lines=25):
    lines = []
    all_lines = text.split("\n")

    for line in all_lines:
        while len(line) > max_line_length and len(lines) < max_lines:
            lines.append(line[:max_line_length])
            line = line[max_line_length:]
        lines.append(line)

    return lines[:max_lines]


async def nulis_cmd(client, message):
    reply = message.reply_to_message

    if reply and (reply.text or reply.caption):
        text = reply.text or reply.caption
    elif len(message.command) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        return await message.reply(
            "Harap reply ke teks atau gunakan format /nulis [teks]"
        )

    try:
        img = Image.open("storage/template.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("storage/assfont.ttf", 30)
        x, y = 150, 135
        lines = text_set(text)
        line_height = font.getsize("hg")[1]

        for line in lines:
            draw.text((x, y), line, fill=(1, 22, 55), font=font)
            y += line_height - 5

        file = "ult.jpg"
        img.save(file)
        await message.reply_photo(photo=file)
        os.remove(file)
    except Exception as error:
        return await message.reply(str(error))
