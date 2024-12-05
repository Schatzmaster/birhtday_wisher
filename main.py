# import smtplib
import datetime as dt
import random

import pandas as pd
import smtplib

##### Vars for smtplib
MY_EMAIL = "jasp.hanson@gmail.com"
PASSWORD = "wtup crew punp pxhi"

##### Vars for datetime
now = dt.datetime.now()
day = now.day
day_of_week = now.weekday()
month = now.month
year = now.year

#### Vars for Pandas
pd.set_option("display.max_colwidth", None)
data = pd.read_csv("quotes.txt", chunksize=1, header=None, encoding="utf-8")
lines = []

# ------------------------------SENDING EMAIL------------------------
for chunk in data:
    lines.append(chunk.iloc[0, 0])
if day_of_week == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        quote = random.choice(lines)
        print(quote)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="karolinehansenhh@gmail.com",
                            msg=f"Subject:Motivierender Spruch am {day}. {month}. {year}"
                                f"\n\n{quote}")
else:
    print("It's not thursday")
