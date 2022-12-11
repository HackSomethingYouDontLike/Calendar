#Find a day which matches with the date that you input
days = ['Saturday','Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31
months = [january,february,march,april,may,june,july,august,september,october,november,december]
month_names = ['january','february','march','april','may','june','july','august','september','october','november','december']

# January 1 in 2023 is Sunday according to calendar
sign = True
while sign:

    note = "WARNING! Write months' names fully\n"
    month = input(note + "Enter month: >>>")
    date = int(input("Enter a day: >>>"))
    if month in month_names:
        for i in range(0, 12):
            if month_names[i] == month:
                new_date = months[:i]
                summa = date + sum(new_date)
                remain = summa % 7
                print(days[remain])

    else:
        print('you did wrong while writing')

    x = input('enter "q" to quit or tap any key to continue\n>>>')
    if x.lower() == 'q':
        sign = False
    else:
        continue
