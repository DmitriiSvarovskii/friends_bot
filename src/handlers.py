from aiogram import Router, types


router = Router(name=__name__)


@router.message()
async def send_echo(message: types.Message):
    try:
        if message.text or message.voice or message.photo:
            await message.delete()
    except TypeError:
        pass
