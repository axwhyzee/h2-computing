## Description

In a map given by a `WIDTH` by `HEIGHT` grid, there are 2 possible types of entities - `Player` & `Pokemon`

A `Player` can attempt to catch `Pokemon`s within his field of vision. A `player`'s field of vision depends on his level, and whether he is a premium user.

-   For premium players, field of vision is a square of length = (level \* 2) + 1, with the player in the center of the square.
-   For non-premium players, field of vision is a circle with diameter = (level \* 2) + 1, with the player in the center of the circle.

> Formula of circle: (x−h)^2 + (y−k)^2 = r^2, where center is (h, k)

A helper function is given to calculate the 2 X-coordinates of a circle's perimeter given a 1) Y-coordinate, 2) radius and 3) coordinates of circle's center.
> Think: Is there a need for another helper function to calculate the Y-coordinates given an X-coordinate?

## Example

In our playing field, we have the following `Pokemon`s

-   A @ (2, 4)
-   B @ (2, 3)
-   C @ (6, 4)
-   D @ (5, 4)
-   E @ (9, 1)
-   F @ (14, 2)
-   G @ (3, 1)
-   H @ (11, 11)
-   I @ (3, 2)
-   J @ (39, 13)
-   K @ (41, 10)
-   L @ (45, 2)
<br/>

There are also 2 `Player`s:

-   NonPremiumPlayer, lvl 4, **Player 1** @ (5, 5)
-   PremiumPlayer, lvl 8, **Player 2** @ (39, 8)
<br/>

```
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . * . . . . . . . . . .
. * * G * * * * * E . . . . . . . . . . . . . . . . . . . . . . . . . . * * * . * * * . . . . . . .
. * . I . . . . . * . . . . F . . . . . . . . . . . . . . . . . . . * * . . . . . . . * * L . . . .
. * B . . . . . . * . . . . . . . . . . . . . . . . . . . . . . . * . . . . . . . . . . . * . . . .
. * A . . D C . . * . . . . . . . . . . . . . . . . . . . . . . . * . . . . . . . . . . . * . . . .
. * . . . 1 . . . * . . . . . . . . . . . . . . . . . . . . . . * . . . . . . . . . . . . . * . . .
. * . . . . . . . * . . . . . . . . . . . . . . . . . . . . . . * . . . . . . . . . . . . . * . . .
. * . . . . . . . * . . . . . . . . . . . . . . . . . . . . . . * . . . . . . . . . . . . . * . . .
. * . . . . . . . * . . . . . . . . . . . . . . . . . . . . . * . . . . . . . 2 . . . . . . . * . .
. * * * * * * * * * . . . . . . . . . . . . . . . . . . . . . . * . . . . . . . . . . . . . * . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . * . . . . . . . . K . . . . * . . .
. . . . . . . . . . . H . . . . . . . . . . . . . . . . . . . . * . . . . . . . . . . . . . * . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . * . . . . . . . . . . . * . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . * . . . . . J . . . . . * . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . * . . . . . . . . . * . . . . .
```
*  The fields of vision are marked with `*`
*  `Pokemon`s are marked with alphabets
*  `Player`s are marked with numbers
<br>

Player 1 can capture A, B, C, D, E, G, I

Player 2 can capture K, J

## Task
Complete the Player, PremiumPlayer & NonPremiumPlayer classes in [template.py](https://github.com/axwhyzee/h2-computing-practical/blob/main/pokemon_go/template.py). Some methods are declared but implementation is left empty, while other methods are entirely excluded in the classes. Identify these methods, declare them and implement accordingly.

Finally, test your code by running the file. 