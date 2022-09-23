search = 'd2b'

while search == "d2b":
    dec2bin = input("\nDecimal Value: ")
    try:
        dec2bin = int(dec2bin)
    except ValueError:
        pass
    else:
        print("Binary Value: " + "{0:b}".format(dec2bin))
        continue

    try:
        dec2bin = float(dec2bin)
    except ValueError:
        pass
    else:
        #code for float to binary goes here
        continue

    if dec2bin == "back":
        search = 0