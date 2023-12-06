# Overview
I have split the code into 5 stages, where each stage is a standalone milestone. They are meant to built up to the final application by starting from the bare minimum and adding more features/fixing bugs along the way.

## Stage 1 (Client)
- Purpose: 
    -  To create a skeletal html page with minimal crazy button logic
- Key points:
    - How to set the webpage title
    - Simple HTML elements
        - Button
        - List
    - Manipulating DOM using JS
        - How to change the position of button
    - Inline CSS
        - position:absolute and what it means

## Stage 2 (Client)
- Purpose: 
    - Add score counting and fix some leftover issues
- Key points:
    - JS
        - Global variables
        - How to load data from variables into DOM
        - Template literals
        - Conditional (ternary) operator
    - Manipulating DOM using JS
        - How to change element values (score)
        - Why do we need to cut the offset to 0.95?

## Stage 3 (Server)
- Purpose: 
    - Set up the basic operations on the backend
- Key points:
    - Initialise server basics
        - How to serve the html we created in stage 2
    - Routing

## Stage 4 (Server + Client)
### Server
- Purpose: 
    - Set up sockets, socket logic, and logging
- Key points:
    - Websockets
        - Listen to and emit signals
    - Logic
    - Logging
    - Type alias/hinting
### Client
- Purpose: 
    - Linking client to server with socket
- Key points:
    - How to import libraries
    - How to listen to and emit socket signals
    - Transferring logic from client to server
    - String slicing

## Stage 5 (Server + Client)
### Server
- Purpose: 
    - Clean up and fix button initial location bug
- Key points:
    - Sending signals to specific users
### Client
- Purpose: 
    - CSS and polish
- Key points:
    - How to use css
    - Mark player on playerList

# Talking points
Here are some points of interest that can be engaged upon

- What is `async` and `await`?
- Are there cases where the `index()` function should be a coroutine function?
- Why is `logging` preferred over `print`?
- What are type aliases and how are they different from type hinting?
- Why do we use tailwind css instead of our own css?
- What is the difference between `var` and `let`?
- What are the bunch of meta data in index.html for?

Some additional coding challenges
- How to migrate js and css out of html into their own files?
- How to sort the list accoding to score?
- Polish the app using css
- How to prevent the button from blocking the scoreboard?
- How to bold your name?
