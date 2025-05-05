//---------- B A T T L E S H I P ----------
// Battleship game between the player and a bot, 
// ships and positions are generated randomly.
// Win if you hit all the ships before the bot does.
// Game Over if you miss more then maxMiss.

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

const int rows = 4; // Number of rows
const int cols = 4; // Number of columns

// C R E A T E   S H I P S   ----------------------------------------------------------------------
// Function to fill the 2D array with random ships (1s) and water (0s)
void createShips(bool ships[rows][cols], int rows, int cols, int& totalShips) {
    totalShips = 0; // Reset ship count
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            ships[i][j] = rand() % 2; // Randomly assign 0 or 1
            if (ships[i][j] == 1) {
                totalShips++; // Increment ship count
            }
        }
    }
}

// D I S P L A Y   B O A R D   --------------------------------------------------------------------
// Function to display the 2D array
void displayBoard(bool ships[rows][cols], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << ships[i][j] << " "; // Print each element
        }
        cout << endl; // New line for the next row
    }
}

// A T T A C K   ----------------------------------------------------------------------------------
// Function to handle the attack logic
bool attack(bool ships[rows][cols], int row, int column, int& hits, int totalShips) {
    if (ships[row][column]) {
        // If the player hit a ship, remove it by setting the value to zero.
        ships[row][column] = 0;
        // Increase the hit counter
        hits++;
        // Tell the player that they have hit a ship and how many ships are left
        cout << "Hit! " << (totalShips - hits) << " left.\n\n";
        return true; // It was a hit
    } else {
        // Tell the player that they missed
        cout << "Miss\n\n";
        return false; // It was a miss
    }
}

// M Y   T U R N   --------------------------------------------------------------------------------
// Function for the player's turn
void myTurn(bool botShips[rows][cols], int& playerHits, int& playerMiss, int& playerTurns, int totalShips) {
    int row, column;

    cout << "Your turn - selecting coordinates\n";
    // Ask the player for a row
    cout << "Choose a row number between 0 and 3: ";
    cin >> row;
    // Ask the player for a column
    cout << "Choose a column number between 0 and 3: ";
    cin >> column;

    // Call the attack function
    if (attack(botShips, row, column, playerHits, totalShips)) {
        // Hit: nothing more to do
    } else {
        // Miss: increase miss counter
        playerMiss++;
    }

    // Count player's turns
    playerTurns++;
}

// B O T   T U R N   ------------------------------------------------------------------------------
// Function for the bot's turn
void botTurn(bool myShips[rows][cols], int& botHits, int& botMiss, int& botTurns, int totalShips) {
    // The bot choose row and column randomly
    int row    = rand() % 4;
    int column = rand() % 4;
    cout << "Bot's turn - selected row " << row << " and column " << column << endl;

    // Call the attack function
    if (attack(myShips, row, column, botHits, totalShips)) {
        // Hit: nothing more to do
    } else {
        // Miss: increase miss counter
        botMiss++;
    }

    // Count bot's turns
    botTurns++;
}

// C H E C K   V I C T O R Y   --------------------------------------------------------------------
// Function to check if the player or bot has won
bool checkVictory(int playerHits, int totalShipsBot, int botHits, int totalShipsPlayer) {
    if (playerHits >= totalShipsBot) {
        cout << "Victory! You sunk all the bot's ships.\n";
        return true; // Player wins
    }
    if (botHits >= totalShipsPlayer) {
        cout << "Defeat! The bot sank all your ships.\n";
        return true; // Bot wins
    }
    return false; 
}

// C H E C K   G A M E   O V E R   ----------------------------------------------------------------
// Function to check if the game is over due to too many misses
bool checkGameOver(int playerMiss, int maxMiss, int botMiss) {
    if (playerMiss >= maxMiss) {
        cout << "Game Over! You missed too many times.\n";
        return true; // Player game over
    }
    if (botMiss >= maxMiss) {
        cout << "You win! The bot missed too many times.\n";
        return true; // Bot game over
    }
    return false;
}

// M A I N   --------------------------------------------------------------------------------------
int main() {
    bool botShips[rows][cols];
    bool myShips[rows][cols];
    int totalShipsBot, totalShipsPlayer;

    // Player stats
    int playerHits  = 0;
    int playerMiss  = 0;
    int playerTurns = 0;
    const int maxMiss = 3;

    // Bot stats
    int botHits  = 0;
    int botMiss  = 0;
    int botTurns = 0;

    // Seed the random number generator
    srand(static_cast<unsigned int>(time(0)));

    // Create ships for both players and count total ships separately
    createShips(botShips, rows, cols, totalShipsBot);
    createShips(myShips, rows, cols, totalShipsPlayer);

    // Uncomment to display ship positions
    // cout << "Bot Ships:\n"; displayBoard(botShips, rows, cols);
    // cout << "My Ships:\n";  displayBoard(myShips, rows, cols);

    // Game loop: continue until someone wins or misses exceed the limit
    while (true) {
        // Player's turn
        myTurn(botShips, playerHits, playerMiss, playerTurns, totalShipsBot);

        // Check if player won or lost
        if (checkVictory(playerHits, totalShipsBot, botHits, totalShipsPlayer)) {
            break;
        }
        if (checkGameOver(playerMiss, maxMiss, botMiss)) {
            break;
        }

        // Bot's turn
        botTurn(myShips, botHits, botMiss, botTurns, totalShipsPlayer);

        // Check if bot won or lost
        if (checkVictory(playerHits, totalShipsBot, botHits, totalShipsPlayer)) {
            break;
        }
        if (checkGameOver(playerMiss, maxMiss, botMiss)) {
            break;
        }
    }

    return 0;
}