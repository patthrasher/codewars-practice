def duty_free(price, discount, holiday_cost):
    # return int(holiday_cost / (price - (((100-discount)/100) * price)))

    # discount_percent = (100 - discount) / 100
    # discount_price = price * discount_percent
    # savings = price - discount_price
    # how_many_bottles = int(holiday_cost / savings)
    # return how_many_bottles

    # another way with less math haha
    saving = price * discount / 100.0
    print(saving)
    return int(holiday_cost / saving)

print(duty_free(10, 10, 500))
print(duty_free(12, 50, 1000))
