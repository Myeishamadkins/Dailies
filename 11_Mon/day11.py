# split the bill
def split_bill(bill, allergy, money_gave):
    # money_gave = 0
    # change = 0
    # total = 0
    shared_total = 0

    bill.remove(bill[0])
    shared_total += sum(bill)
    print(f"shared total: {shared_total}")
    money_due = shared_total / 2
    print(f"money due: {money_due}")
    change = money_gave - money_due
    print(f"change: {change}\n")

if __name__ == "__main__":
    print(split_bill([9.50, 11.75, 18.50, 3, 3], 0, 30), 11.875)
    print(split_bill([3, 4], 1, 4), 2.5)
    print(split_bill([1], 0, 0),0)
    print(split_bill([1], 0, 1), 1)
    print(split_bill([3, 4, 3], 0, 4), .5)
