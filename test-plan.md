# Test Plan

## how i tested it

i used `--word` so i knew what fruit the game picked.

```bash
python src/game.py --word guava
python src/game.py --word lime
python src/game.py --word papaya
```

these are the 23 checks from my earlier test notes. i kept the results short.

## guava - 6 slices

- [x] 1. `A` - shows both a's. no slice lost. first guess message
- [x] 2. `z` - wrong. 5 slices left
- [x] 3. `a` - repeat. still 5 slices
- [x] 4. `12` - rejected. still 5
- [x] 5. `ab` - rejected. still 5
- [x] 6. empty input - rejected. still 5
- [x] 7. `$` - rejected. still 5
- [x] 8. `G` - shows g. no slice lost
- [x] 9. `q` - wrong. 4 slices left
- [x] 10. `x` - third wrong guess message. 3 slices left
- [x] 11. `u` - third right guess message
- [x] 12. `v` - win. shows GUAVA and score
- [x] 13. replay with `y`, then `kiwi` as a guess - new round. whole word rejected

## lime - 4 slices

- [x] 14. `q`, `z`, `x` - 3 wrong guesses. 1 slice left
- [x] 15. `w` - last slice gone. lose and show LIME
- [x] 16. lime starts with 4 slices and Merienda Mode
- [x] 17. `maybe` for replay - rejected and asked again
- [x] 18. `y` - new round, 4 slices, no guesses
- [x] 19. `l`, `i`, `m`, `e` - win. score keeps old results
- [x] 20. `n` - game ends and shows goodbye

## other checks

- [x] 21. papaya + `A` - all 3 a's show
- [x] 22. papaya + `A`, then `a` - second guess is a repeat
- [x] 23. run without `--word` - random fruit, correct slices

## result

all 23 were marked pass in my earlier test notes.

screenshots folder is there but still empty.
