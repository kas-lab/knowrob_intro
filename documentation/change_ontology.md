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
