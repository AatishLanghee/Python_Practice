########################################################################################################
# Question: One Time Password

# A company wishes to devise an order confirmation procedure.
# They plan to require an extra confirmation instead of simply auto-confirming the order at the time it is placed.
# for this purpose, the system will generate one time password to be shared with the customer.
# The customer who is placing the order has to enter the OTP to confirm the order.
# The OTP generated for the requested order ID, is the product of the digits in orderID.

# Write an algorithm to find the OTP for the OrderID.

# input -----> an integer representing order id
# output ----> an integer representing OTP
########################################################################################################
def generate_otp(d: int) -> int:
    otp: int = 1
    while d != 0:
        digit: int = d % 10
        otp = otp * digit
        d = d // 10

    return otp


if __name__ == "__main__":
    data: int = int(input("Enter the order ID :"))
    print(generate_otp(data))
