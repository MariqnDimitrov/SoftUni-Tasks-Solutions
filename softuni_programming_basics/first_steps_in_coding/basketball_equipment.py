year_price=int(input())
basketball_shoes=year_price - year_price*0.40
basketball_clothes=basketball_shoes - basketball_shoes*0.20
basketball_ball=basketball_clothes*0.25
basketball_accessories=basketball_ball*0.20
full_price=basketball_accessories + basketball_ball + basketball_clothes + basketball_shoes + year_price
print(full_price)