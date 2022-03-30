from booking.booking import Booking

try:
    with Booking() as bot:
        # a = 2 / 0
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go('Salvador')
        bot.select_dates(check_in_date='2022-03-30',
                         check_out_date='2022-03-31')
        bot.select_adults(1)
        bot.click_search()
        bot.apply_filtrations()
        print(len(bot.report_results()))

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '   set PATH=%PATH;C:path-to-your-folder \n \n'
            'Linux: \n'
            'PATH=$PATH:"/home/tiago/Documents/Projects/bot/run.py \n'
        )
    else:
        raise