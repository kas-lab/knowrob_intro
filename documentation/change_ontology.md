# Examples on how to change properties on individuals
```
triple(pap:'milk_product_1', soma:hasMassAttribute, X)
```
X: http://www.airlab.org/tiago/pick-and-place#milk_weight_full.

```
?- kb_project(triple(pap:'milk_product_1', soma:hasMassAttribute, pap:'milk_weight_half'))
```
true.

```
?- triple(pap:'milk_product_1', soma:hasMassAttribute, X)
```
X: http://www.airlab.org/tiago/pick-and-place#milk_weight_full ;

X: http://www.airlab.org/tiago/pick-and-place#milk_weight_half.

?-  kb_unproject(triple(pap:'milk_product_1', soma:hasMassAttribute, pap:'milk_weight_full'))
true.
?- triple(pap:'milk_product_1', soma:hasMassAttribute, X)
X: http://www.airlab.org/tiago/pick-and-place#milk_weight_half.



# print("------changing values----")
# query = pq.prolog_query("triple(pap:'milk_product_1', soma:hasMassAttribute, X)")
# print("Mass attribute of milk product 1:")
# pq.print_all_solutions(query)

# query = pq.prolog_query("kb_project(triple(pap:'milk_product_1', soma:hasMassAttribute, pap:'milk_weight_half'))")
# print("Changed:")
# pq.print_all_solutions(query)

# query = pq.prolog_query("triple(pap:'milk_product_1', soma:hasMassAttribute, X)")
# print("Mass attribute of milk product 1:")
# pq.print_all_solutions(query)

# query = pq.prolog_query("kb_unproject(triple(pap:'milk_product_1', soma:hasMassAttribute, pap:'milk_weight_full'))")
# print("Removed old values:")
# pq.print_all_solutions(query)

# query = pq.prolog_query("triple(pap:'milk_product_1', soma:hasMassAttribute, X)")
# print("Mass attribute of milk product 1:")
# pq.print_all_solutions(query)


# print("------ Changing values in time----")

# print("----------------- Instant 1 ----------------")

# # SINCE 1
# query = pq.prolog_query("kb_call(holds(pap:'milk_product_1', soma:'hasMassAttribute', X) during [0, 1])")
# print("Mass attribute of milk product 1 at instant [0, 1]:")
# rv = pq.print_all_solutions(query)

# string_query = "kb_project(holds(pap:'milk_product_1', soma:'hasMassAttribute', " + rv[0] + ":'" + rv[1] + "') until 1)"
# query = pq.prolog_query(string_query)
# print("Remove previous value: {}".format(rv[1]))
# pq.print_all_solutions(query)

# query = pq.prolog_query("kb_project(holds(pap:'milk_product_1', soma:'hasMassAttribute', pap:'milk_weight_half') since 1)")
# print("Assert that weight is half since instant 1:")
# pq.print_all_solutions(query)

# query = pq.prolog_query("kb_call(holds(pap:'milk_product_1', soma:'hasMassAttribute', X) since 1)")
# print("Checking weight at instant 1:")
# pq.print_all_solutions(query)

# print("----------------- Instant 2 ----------------")

# # SINCE 2
# query = pq.prolog_query("kb_call(holds(pap:'milk_product_1', soma:'hasMassAttribute', X) during [1, 2])")
# print("Mass attribute of milk product 1 at instant [1, 2]:")
# rv = pq.print_all_solutions(query)

# string_query = "kb_project(holds(pap:'milk_product_1', soma:'hasMassAttribute', " + rv[0] + ":'" + rv[1] + "') until 2)"
# query = pq.prolog_query(string_query)
# print("Remove previous value: {}".format(rv[1]))
# pq.print_all_solutions(query)

# query = pq.prolog_query("kb_project(holds(pap:'milk_product_1', soma:'hasMassAttribute', pap:'milk_weight_full') since 2)")
# print("Assert that weight is full since instant 2:")
# pq.print_all_solutions(query)

# query = pq.prolog_query("kb_call(holds(pap:'milk_product_1', soma:'hasMassAttribute', X) since 2)")
# print("Checking weight at instant 2:")
# pq.print_all_solutions(query)


# print("----------------- Conclusions ----------------")

# query = pq.prolog_query("kb_call(holds(pap:'milk_product_1', soma:'hasMassAttribute', X) during [0, 1])")
# print("Mass attribute of milk product 1 during [0, 1]:")
# pq.print_all_solutions(query)

# query = pq.prolog_query("kb_call(holds(pap:'milk_product_1', soma:'hasMassAttribute', X)  during [1, 2])")
# print("Mass attribute of milk product 1 during [1, 2]:")
# pq.print_all_solutions(query)
