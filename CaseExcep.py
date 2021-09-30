hours=int(input())
class LessThanFourty(Exception):
    pass
try:
    if hours<40:
        raise LessThanFourty("Hours is less than 40")
    else:
        print(hours)
except LessThanFourty as e:
    print(e)