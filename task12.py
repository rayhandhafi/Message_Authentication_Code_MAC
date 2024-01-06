import hashlib
key = "s1tt_kkd_2023"
msg = "bohemian rhapsody"
print("Demonstration of secret prefix MAC")
print("Style-1")
m1 = hashlib.sha1()
m1.update(key.encode())
m1.update(msg.encode())
sh1_hex = m1.hexdigest()
print("MAC in hex: ", sh1_hex)

print("Style-2")
m2 = hashlib.sha1()
in_msg = key+msg
m2.update(in_msg.encode())
sh2_hex = m2.hexdigest()
print("MAC in hex: ", sh2_hex)

print("MAC verification in the receiver")
m3 = hashlib.sha1()
keyr = "s1tt_kkd_2023"
#keyr = "s1tt_kkd_2024"
print("receiver key: ", keyr)
rec_msg = keyr+msg
m3.update(rec_msg.encode())
sh3_hex = m3.hexdigest()

#sh2_hex is the hash computed by the transmitter
#sh3_hex is the hash computed by the receiver

if sh3_hex == sh2_hex:
    print("Message is valid")
else:
    print("Message is invalid")