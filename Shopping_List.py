#assign prices to items
instant_noodles = 0.80
tuna_cans = 1.20
cereal_bars = 0.50

#count quantites purchased 
instant_noodle_qty = 5
tuna_can_qty = 3
cereal_bar_qty = 8

#calculate the amount of items purchased 
total_instant_noodles = (instant_noodles * instant_noodle_qty)
total_tuna_cans = (tuna_cans * tuna_can_qty)
total_cereal_bars = (cereal_bars * cereal_bar_qty)

#calculate the total money spent 
shopping_total = (total_instant_noodles + total_tuna_cans + total_cereal_bars)

#print a receipt showing the items purchased, the amount for each item, and overall total
print ("Camping Shop Receipt")
print ("-----------------------------")
print ("Instant Noodles:","£",total_instant_noodles)
print ("Canned Tuna:","£",total_tuna_cans)
print ("Cereal Bars:","£",total_cereal_bars)
print ("-----------------------------")
print ("Total:","£",shopping_total)