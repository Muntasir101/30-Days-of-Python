import random
import string


# function to generate a coupon code
def generate_coupon_code(length):
    coupon_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    coupon_codes = ''.join(random.choice(coupon_chars) for i in range(length))
    return coupon_codes


# generate a coupon code of length 8
coupon_code = generate_coupon_code(8)

# print the coupon code
print("Coupon code:", coupon_code)
