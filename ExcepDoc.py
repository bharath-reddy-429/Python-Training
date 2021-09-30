#Doctor will be not available from 1 to 3 and 8 to 9
time=int(input())
class NotAvailError(Exception):
    pass
try:
    if time in [21,2,3,8,9]:
        raise NotAvailError("You can't make appointment")
    else:
        print("Appointment is fixed")
except Exception as e:
    print(e)