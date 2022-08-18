# Detalhes para o balanceamento:

O balanceamento dos  nós são feitos 
com rotações, seja elas simples ou não,
para identificar o local da rotação, será
necessario averiguar o equilibro de cada
nó! nós a esquerda pesam(+1) e direita (-1).

Em uma arvore AVL/Balanceada, ós esqui_
librios de cada nó de se entre -1 e 1,
(1 >= x >= -1), caso o equilibrio x esteja
fora desse range, o nó está apresentando um
desequilibrio.

Rotação RR(simples esquerda) é quando os
nós da direita pesam em um desequilibrio de -2
sendo necessario uma RR, vale o mesmo para a
LL(simples a direita), já que o desequilibrio 
seria +2.