from aiogram.filters.command import Command
from aiogram import Router, F
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message, FSInputFile
from .kandinsky import generate_image

history_context = []
router = Router()


def main_menu_markup() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="Generate picture")],
        [KeyboardButton(text="Back")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="What do you want?",
    )


@router.message(Command("start"))
async def start(message: Message) -> None:
    await message.reply(
        "Hello!\nWould you like a picture?", reply_markup=main_menu_markup()
    )


@router.message(F.text)
async def text_handler(message: Message) -> None:
    history_context.append(message.text)

    if message.text == "Generate picture":
        await message.reply("Write </> and discribe a picture")

    elif message.text == "Back":
        await message.reply("Bye")

    elif message.text is not None:
        previous_message = get_previous_message(history_context)

        if previous_message == "Generate picture":
            await message.reply("Generating a picture :)\nMay take a couple of minutes")

            result = generate_image(message.text)
            if not result:
                await message.reply("Couldn't get the picture :(")
                return

            photo_file = FSInputFile(path="Picture.png")

            await message.reply_photo(photo_file, caption="Picture :)")


def get_previous_message(context: list) -> str:
    if len(context) == 1:
        return ""

    return context[len(context) - 2]
