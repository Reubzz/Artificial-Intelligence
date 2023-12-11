% Defining facts
female(pam).
female(liz).
female(pat).
female(ann).

male(tom).
male(bob).
male(peter).

parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).
parent(tom, peter).


% Defining Rules
mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).

sister(X, Y) :- parent(Z, X), parent(Z, Y), female(X), X \== Y.
brother(X, Y) :- parent(Z, X), parent(Z, Y), male(X), X \== Y.

grandmother(X, Z) :- mother(X, Y), parent(Y, Z).
grandfather(X, Z) :- father(X, Y), parent(Y, Z).

uncle(X, Z) :- brother(X, Y), parent(Y, Z).
aunt(X, Z) :- sister(X, Y), parent(Y, Z).