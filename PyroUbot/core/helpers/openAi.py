import asyncio

import g4f
import openai

from PyroUbot import OPENAI_KEY

openai.api_key = OPENAI_KEY


class OpenAi:
    @staticmethod
    async def ChatGPT(question):
        try:
            response = await g4f.ChatCompletion.create_async(
                model=g4f.models.default,
                provider=g4f.Provider.GeekGpt,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question},
                ],
                timeout=60,
            )
            return response if response else "lagi error coba lagi nanti"
        except Exception as error:
            return str(error)

    @staticmethod
    async def ImageDalle(question):
        response = await asyncio.to_thread(
            openai.Image.create,
            prompt=question,
            n=1,
        )
        return response["data"][0]["url"]

    @staticmethod
    async def SpeechToText(file):
        audio_file = open(file, "rb")
        response = await asyncio.to_thread(
            openai.Audio.transcribe, "whisper-1", audio_file
        )
        return response["text"]
