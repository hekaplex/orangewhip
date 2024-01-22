# Orange Whip
A simple python script that will solve most Wordle puzzles in seconds when you have made a valiant attempt and are stuck

## INSTALLATION INSTRUCTIONS
Tested with Python 3.8-3.12 (available at http://python.org/downloads)

1. Run from the command line the following command (no tab necessary):
    ```
            pip install english_words
    ```
    
      There are dependencies on copy and collections libraries but in my test of Python 3.11.1 they were already bundled
      Worst case you may need to run these commands:
    
    ```
            pip install copy
            pip install collections
    ```
1. Navigate to the directory where you save the orangewhip.py file or drag the path into the command line to the directory where you want to keep it


## USAGE INSTRUCTIONS

Once in the same folder as the Python file, run this command (no tab necessary):

   ```
    python orangewhip.py
```

### Usage:

#### NOTE: This code has only been sucessfully tested when you have three green/orange letters in a Wordle guess. USing fewer letters may take a LONG TIME!!!

1. The "guess" should include a * character for each unknown letter
  Example:
  ```
            guess:f*o*k
  ```
1. The "duds" refer to the unique letters attempted that did not come up yellow/blue or green/orange
  Example:
  ```
            duds:abdegh
  ```
1. The output will be a list of words from the english_words dictionary that match the inputs
  Example:
  ```
            ['frock', 'flock'] 
  ```
is an example of two words matching the criteria
  ```
  []
  ```
indicates no words found
