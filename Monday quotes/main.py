import datetime as dt
import smtplib
import random
MY_EMAIL = "goolor.love.isthebest@gmail.com"
MY_PASSWORD = "xpup otrj smmu ujtx"

now = dt.datetime.now()
day = now.weekday()
if day == 6:
    with open("quotes.txt", "r") as quotes:
        quotes_str = quotes.read()
        quotes_list = quotes_str.splitlines()
    quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="24AyaanDube@lgs.slough.sch.uk",
                            msg="subject:Good morning"
                                "\n\nHello,"
                                "\n I know this is probably the day you hate the most so here's some motivation:"
                                f"\n{quote}")
