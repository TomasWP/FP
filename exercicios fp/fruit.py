def isInBasket(b1,b2,b3):
   lst = []
   for element in b1:
      if element in b3:
         continue
      else:
         if element in lst:
            continue
         else:
            lst.append(element)
   for element in b2:
      if element in b3:
         continue
      else:
         if element in lst:
            continue
         else:
            lst.append(element)
   return lst

fruit = isInBasket(basket1, basket2, basket3)