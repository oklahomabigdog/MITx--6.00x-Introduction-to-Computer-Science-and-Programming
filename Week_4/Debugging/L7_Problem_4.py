def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
   if len(set1) == 0:
       print "in first part"
       return set2
   elif set1[0] in set2:
       print "in second part"
       return union(set1[1:], set2)
   else:
       print "in third part"
       return set1[0] + union(set1[1:], set2)

print "\n============"
print "Test Suite D"
print "============"
union('','abc')
union('a','abc')
union('ab','abc')
union('d','abc')