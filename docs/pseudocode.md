Pseudocode
these are the steps for the game. not the actual python code.

start
start
set wins, losses and streaks to 0
show game title

while player wants to play
    pick a random fruit (or use --word for testing)
    play 1 round
    update score
    show scoreboard
    ask to play again

show goodbye message
end
1 round
get fruit
get slices from word length
set guessed letters to empty
set right and wrong count to 0

repeat
    show blanks and slices left
    ask for 1 letter
    if input is bad or repeated
        show message
        ask again (no slice lost)
    else
        save the letter
        if letter is in fruit
            show all copies of that letter
            add 1 to right count
            keep slices
        else
            take away 1 slice
            add 1 to wrong count

        show special host messages when needed

    if all letters are found
        show win and return True
    if slices are 0
        show the answer and return False
until game ends
check input
remove spaces and make guess lowercase
if empty -> reject
if more than 1 letter -> reject
if not a-z -> reject
if already guessed -> reject
otherwise -> accept
show the word
for each letter in the fruit
    if letter was guessed -> show letter
    otherwise -> show _
put spaces between letters
score
if player won
    add 1 win
    add 1 to streak
    update best streak if needed
else
    add 1 loss
    reset streak to 0
play again
ask y or n
y / yes -> play again
n / no -> quit
anything else -> ask again
