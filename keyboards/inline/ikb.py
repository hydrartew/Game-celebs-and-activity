from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=1,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(text='Игра в шляпу', callback_data='Игра в шляпу'),
                                    InlineKeyboardButton(text='Активити', callback_data='Активити'),
                                ],
                            ])

menu_admin = InlineKeyboardMarkup(row_width=1,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Игра в шляпу', callback_data='Admin hat'),
                                          InlineKeyboardButton(text='Активити', callback_data='Admin activity'),
                                      ],
                                  ])

generate_celebs = InlineKeyboardMarkup(row_width=1,
                                       inline_keyboard=[
                                           [
                                               InlineKeyboardButton(text='Киноиндустрия', callback_data='Киноиндустрия')
                                           ],
                                           [
                                               InlineKeyboardButton(text='Музыка', callback_data='Музыка')
                                           ],
                                           [
                                               InlineKeyboardButton(text='YouTube', callback_data='YouTube')
                                           ],
                                           [
                                               InlineKeyboardButton(text='Спорт', callback_data='Спорт')
                                           ],
                                           [
                                               InlineKeyboardButton(text='Политика', callback_data='Политика')
                                           ],
                                           [
                                               InlineKeyboardButton(text='Бизнес', callback_data='Бизнес')
                                           ],
                                           [
                                               InlineKeyboardButton(text='Учёные/Писатели',
                                                                    callback_data='Учёные/Писатели')
                                           ],
                                           [
                                               InlineKeyboardButton(text='Рандом', callback_data='Рандом')
                                           ],
                                       ])

# generation_estimation = InlineKeyboardMarkup(row_width=1,
#                                              inline_keyboard=[
#                                                  [
#                                                      InlineKeyboardButton(text='⭐️',
#                                                                           callback_data='⭐️'),
#                                                  ],
#                                                  [
#                                                      InlineKeyboardButton(text='⭐️⭐️',
#                                                                           callback_data='⭐️⭐️'),
#                                                  ],
#                                                  [
#                                                      InlineKeyboardButton(text='⭐️⭐️⭐️',
#                                                                           callback_data='⭐️⭐️⭐️'),
#                                                  ],
#                                                  [
#                                                      InlineKeyboardButton(text='⭐️⭐️⭐️⭐️',
#                                                                           callback_data='⭐️⭐️⭐️⭐️'),
#                                                  ],
#                                                  [
#                                                      InlineKeyboardButton(text='⭐️⭐️⭐️⭐️⭐️',
#                                                                           callback_data='⭐️⭐️⭐️⭐️⭐️'),
#                                                  ],
#                                              ])


generation_estimation = InlineKeyboardMarkup(row_width=1,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(text='1⭐️',
                                                                          callback_data='1⭐️'),
                                                     InlineKeyboardButton(text='2⭐️',
                                                                          callback_data='2⭐️'),
                                                     InlineKeyboardButton(text='3⭐️',
                                                                          callback_data='3⭐️'),
                                                     InlineKeyboardButton(text='4⭐️',
                                                                          callback_data='4⭐️'),
                                                 ],
                                                 [
                                                     InlineKeyboardButton(text='⭐️⭐️⭐️⭐️⭐️',
                                                                          callback_data='⭐️⭐️⭐️⭐️⭐️'),
                                                 ],
                                             ])

generating_more = InlineKeyboardMarkup(row_width=1,
                                       inline_keyboard=[
                                           [
                                               InlineKeyboardButton(text='Сгенерировать ещё',
                                                                    callback_data='Сгенерировать ещё'),
                                               InlineKeyboardButton(text='Выбор категорий',
                                                                    callback_data='Игра в шляпу'),
                                           ],
                                       ])

generating_words = InlineKeyboardMarkup(row_width=1,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(text='Сгенерировать',
                                                                     callback_data='Сгенерировать'),
                                            ],
                                        ])
