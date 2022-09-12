# Development Log
> A successful final project is built slowly over many weeks not thrown together at the last minute. To incentivize good project pacing and to let your project mentor stay informed about the status of your work, each week you should add an entry to your log.md file in the development directory.

> Each entry should describe:

> - What goals you had set for the week and whether they were accomplished or not
> - What problems you encountered (if any) that prevented you from meeting your goals
> - What you plan to accomplish or attempt next week

> The development log will be graded for completion, detail, and honesty – not progress. It is much better to truthfully evaluate the work you completed in a week then lie to make the project sound further along then it really is. It is totally acceptable to have an entry that says you tried nothing and accomplished nothing. However if every week starts to say that, both yourself and your project mentor will be able to identify the issue before it becomes impossible to fix.

[Example of Good/Bad Changelist descriptions](https://google.github.io/eng-practices/review/developer/cl-descriptions.html)

> Oops I kind of did not realise we had to fill in this as we go along, and also that I kind of procrastinated till the very last moment so...for context I am writing this after somewhat completing the code

## Week 5 (26 Jul - 1 Aug)
> Initial idea for OOP

> My initial idea for how I was going to implement OOP was to have a class for the entire game, where the run() function (which manages the rules/operation of the game) is located there. It would also have a list of Players(), while players would have a list of Hands(). I thought that this would allow for many helpful methods, such as both the Player and Hand class haing a check for whether they are still alive, which could be called easily.

> I also initially decided to have a minimax class (but was never coded out), which would serve more of a "container" for the various functions involved rather than a "real" class.

## Week 6 (2 Aug - 8 Aug)

## Week 7 (9 Aug - 15 Aug)
### Started coding out the stuff
If i remember correctly, I started writing the code around here (yes very late). The primary difficulty I had (and this will apply to later segments too) was trying to transfer the variables and data between the various layers of classes. For example, in the Game class, often I would need to access the values for the hands of a specific player. Not very sure what the "typical"/convention was, this I believe this led to a lot of indecision and inconsistencies. Although the code is not there anymore, sometimes I would create a special function in the Player class to access the data, while other times I would just access the data directly.

```python
# Special method
player.get_hand(index)

# direct
player.hands[index]
```
### Reading and checking input
One really cool thing I learned from Yunze was the use of `while True` loops and try-except blocks to check for input validity. This is used extensively to check for valid input (e.g. choosing game options, choosing player moves etc.)

```python
while True:
    try:
        #input

        #checks -> raise errors if input is invalid
        break
    except:
        #exception handling
```

## Week 8 (16 Aug - 22 Aug)

## Week 9 (23 Aug - 29 Aug)

## Week 10 (30 Aug - 5 Sep)

## Sep Holiday (5 Sep - 10 Sep)
> Started rushing a few days before submission :(

### Restarting the code :O 
When I started looking at the code and trying to continue writing it, I decided to restart because I felt that the many functions/inconsistencies were very confusing (especially since there were 3 "layers" of classes). For example, I got stuck on a part where I placed the function in the Player class, but it required the data for the entire board, which was instead stored in the Game class. While in the current implementation such functions also exist (e.g. `player.move(board, player`), the way I solved this was to pass the data in as a parameter for the function. While it works, it still feels a bit awkward, inconsistent and somewhat annoying (back then I just thought it would not work). Therefore, when rewriting the code I decided to store the data as a list of Player() classes, each of which would have a list of integers, representing the number of fingers on each hand. 

### Indexing
To make the indexing more intuitive and the data storage simpler, the data for the hands were stored 0-indexed (i.e. the first hand is 0, the second hand is 1, etc), but when printing the values/asking users for input this was converted to 1-indexed values by adding one, then subtracting 1 after the input was taken. This can be seen in the Player move() function, where the integer input is subtracted by 1, and in all places where indexs are printed, where the index is incremented by 1.

### Pass by value vs pass by reference
I felt that a lot of confusion arose from whether the data was passed by value or by reference, especialy since I did not really know when or where each happened. One notable case is in the `Minimax.run()` function, where in the idea is to recurse on all the possible next-moves. How I implemented this was to create a new variable `replica`, which would be a value-copy of the board variable (a list of Players), change the values in `replica`, then pass `replica` into the recursive call. However, unfortunately, it turned out that while I did do `replica = board.copy()`, and `id(replica)` was different from `id(board)`, changing the values in `replica` would somehow still affect those in `board` :O 

After asking in chat and experimenting on test classes, it turned out that while the lists were indeed passed by value, the `Player` classes inside were actually passed by reference, meaning that the entire thing was effectively still pass by reference. My solution for this was to initialise `replica` as an empty list, then for every Player, create a new instance of the class and append it to `replica`. This can be found in the `Minimax.run()` method as well as the `Player.copy()` method. 

### Memoisation
When implementing Minimax, while time complexity is not really a concern, I felt that it would be cool to implement some kind of memoisation, so that if the identical board has been processed before, the result would be stored, allowing for much faster speed. How I tried to do this was by having a dictionary (that is "linked" to the entire `Minimax` class), where the keys are `(player, board)`. For infomation, `player` is the index of the player who is playing, and `board` is the list of Players. This values would be the output of the `Minimax.run()` method, which is a list of size 3 containing the expected score, the index of the tapping-hand and the index of the target-hand.

However, the reason I did not continue with this was that it would give an error whenever the code was run.

```python
TypeError: unhashable type: 'list'
```

According to [this question on stack overflow](https://stackoverflow.com/questions/19371358/python-typeerror-unhashable-type-list), this problem arised because dictionaries are implemented as hast-tables (keys must be immutable) and python lists do not have built-in hash functions. Similarly, the `Player` class is mutable and therefore cannot be included in the dictionary, even if a tuple is used instead of a list.

Now that I think about it, it might be possible to convert the hand data in the `Player` class to a tuple, and store that in the dictionary. However, this would mean that this conversion has to take place every time the check is run, which is not very efficient and might make memoisation useless (and it probably does not really benefit significantly either ways).

> *I ended up implementing memoisation, especially since I wanted to try splitting but made use of an extremly ineffieicnt algorithm. Memoisation was done by having two lists, one for the "key" and one for the "value". The `in` keyword was used to determine whether the key was in the list, then `list.index()` was used to get the index and therefore corresponding index of the value in the second list. Initially, I tried using a dictioanry with a similar strategy but it gave the `TypeError` again :(

### Splitting
One element of gameplay that I really wanted to make is allowing for splitting to take place both for the player and for the minimax algorithm. For the minimax algorithm, I used some kind of brute force solution to find all the possible "splits" of the fingers on the hands. The method often results in unnecessary duplicates, which explains the need for memoisation to return quick answers for identical queries. Unfortunately, there is some kind of bug involved with the splitting algorithm, causing it to give weird impossible answers, but I could not reason out why it happened.

As for implementing splitting for the player, while possible I could not decide on where to query the user for options. One idea I have is to include it as part of the 3-layer while loop, such that there is a while loop on the fourth layer which queries for whether the player wants to split or tap. If they choose to tap, it could then proceed to the third layer and continue as before. If they choose to split, there can be some toggle to break it out of the 3 while loops to get to one for splitting.

```python
split = False
while True:
    while True:
        while True:
            while True:
                # query for whether player wants to split or tap
            
            if split:
                break
        if split:
            break
    if split:
        break
while True:
    # while loop input for handling special inputs with splitting
```