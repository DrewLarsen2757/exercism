class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if len(self.card_num) > 1 and self.card_num.isdigit():
            reversed_card = self.card_num[::-1]
            doubled = [int(x) * 2 for x in reversed_card[1::2]]
            not_doubled = [int(x) for x in reversed_card[::2]]
            val_doubled = [x - 9 if x > 9 else x for x in doubled]
            print(val_doubled)
            print(not_doubled)
            total = sum(val_doubled) + sum(not_doubled)
            print(total)
            if total % 10 == 0:
                return True
            else:
                return False
        else:
            return False
             

