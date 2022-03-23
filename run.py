from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.select_place_to_go('Salvador')
    bot.select_dates(check_in_date='2022-03-24',
                     check_out_date='2022-03-29')
    bot.select_adults()

    bot.descrease_adults_element()
