with open(f"FILES/poem.txt","r") as a:
    a=a.read()
if 'twinkle' in a:
    print("twinkle is present")
else:
    print("twinkle is not present")