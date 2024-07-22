safety_nylon=int(input())*1.50
paint=int(input())*14.50
paint_thinner=int(input())*5.00
hours=int(input())
extra_paint=paint*0.10
extra_nylon=3
final_safety_nylon= safety_nylon + 3
final_paint=paint + extra_paint
bags=0.40
materials=final_paint + final_safety_nylon + paint_thinner + bags
masters=(materials*0.30)*hours
final_sum=materials+masters
print(final_sum)