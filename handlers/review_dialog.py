from aiogram import Router, types
from aiogram.types import CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

review_router = Router()


class RestourantReview(StatesGroup):
    waiting_for_name = State()
    waiting_for_contact = State()
    waiting_for_rate = State()
    waiting_for_extra_comments = State()


@review_router.callback_query(lambda call: call.data == "review:start")
async def start_review(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Как вас зовут?")
    await state.set_state(RestourantReview.waiting_for_name)
    await callback.answer()


@review_router.message(RestourantReview.waiting_for_name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваш номер телефона или инстаграм:")
    await state.set_state(RestourantReview.waiting_for_contact)


@review_router.message(RestourantReview.waiting_for_contact)
async def get_contact(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await message.answer("Поставьте нам оценку от 1 до 5:")
    await state.set_state(RestourantReview.waiting_for_rate)


@review_router.message(RestourantReview.waiting_for_rate)
async def get_rate(message: types.Message, state: FSMContext):
    if message.text.isdigit() and 1 <= int(message.text) <= 5:
        await state.update_data(rate=message.text)
        await message.answer("Оставьте дополнительные комментарии:")
        await state.set_state(RestourantReview.waiting_for_extra_comments)
    else:
        await message.answer("Пожалуйста, введите число от 1 до 5.")

    await state.clear()