principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Please enter your principle: "))
    if principle <= 0:
        print("principle cant be negetive or zero")
while rate <= 0:
    rate = float(input("Please enter bank intrest rate: %"))
    if rate <= 0:
        print("rate cant be negetive or zero")
while time <= 0:
    time = int(input("Please enter your period of time: "))
    if time <= 0:
        print("time cant be negetive or zero")

total = principle * pow((1 + rate / 100),time)


print(f"balance after {time} years with {rate}% rate will be {total}")


