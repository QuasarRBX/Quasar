# Quasar Roblox Tool

<div align="center">
  
![Quasar Banner](https://img.shields.io/badge/QUASAR-2.0.0-purple?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Outdated-red?style=for-the-badge)

</div>

## Overview

Quasar is a comprehensive Roblox utility tool designed for various account management and game-related operations. The tool features a visually appealing interface with multiple modules for different purposes.

## ✨ Features

### Account Management
- **Cookie Checker** - Validate and extract information from Roblox cookies
- **Cookie Generator** - Generate random cookie strings for testing
- **Mass Cookie Checker** - Validate multiple cookies from a file
- **Pin Cracker** - *[Currently Disabled - Roblox removed PIN system]*

### Economic Tools
- **Free Item Buyer** - Automatically purchase all free items on Roblox catalog
- **Robux & Account Info** - Display detailed account information including:
  - Robux balance and credit
  - RAP (Recent Average Price) value
  - Premium status
  - Group funds and ownership
  - Transaction history

### Game Utilities
- **Server IP Grabber** - Extract server IP addresses from Roblox game sessions
- **Group Finder** - Search for unowned, public entry groups

### Account Tools
- **Account Nuker** - Multi-threaded account modification tool with features:
  - Mass friend removal
  - Inventory item deletion
  - Language changing
  - Mass messaging

## 🛠️ Installation

### Prerequisites
- Python 3.x
- pip package manager

### Automatic Installation
The tool automatically installs required dependencies when first run:

```bash
python main.py
```

### Manual Installation
```bash
pip install requests pystyle pyisemail tqdm termcolor rich
```

## 📁 File Structure

```
quasar/
├── main.py               # Main application
├── cookies.txt           # Cookie storage
├── validcookies.txt      # Validated cookies
├── invalidcookies.txt    # Invalid cookies
├── server_ips.txt        # Captured server IPs
├── Gen_cookies.txt       # Generated cookies
└── [username]_cookie.txt # Individual cookie info dumps
```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Select an option from the main menu:

   ```
   [1] Cheats;                           [6] Email validator;                   
   [2] Cookie checker;                   [7] Nucker;                            
   [3] Discord fake site;                [8] BruteForcer;                       
   [4] Roblox Pin cracker;               [9] free-item-buyer;                   
   [5] Group finder                      [10] Cookie Generator;                 
   [11] Get server IP;                   [12] Follower Bot;                 
   [13] Mass-cookie-check;               [14] Mass report;                  
   [15] Group wall spammer;           
   ```

3. Follow the on-screen instructions for each module.

## 🔧 Available Modules

### 1. Cookie Checker (`[2]`)
- Input a single Roblox cookie
- Extracts and displays comprehensive account information
- Saves data to `[username]_cookie.txt`

### 2. Mass Cookie Checker (`[13]`)
- Reads cookies from `cookies.txt`
- Validates each cookie and categorizes them
- Outputs valid cookies to `validcookies.txt`
- Outputs invalid cookies to `invalidcookies.txt`

### 3. Free Item Buyer (`[9]`)
- Uses provided cookie to authenticate
- Scans Roblox catalog for all free items
- Automatically purchases unpurchased free items
- Handles rate limiting and already-owned items

### 4. Server IP Grabber (`[11]`)
- Join a Roblox game
- Run the tool while in-game
- Extracts server IP from Roblox logs
- Saves to `server_ips.txt`

### 5. Group Finder (`[5]`)
- Searches for available groups
- Filters for public entry, unowned groups
- Provides group IDs for potential acquisition

### 6. Account Nuker (`[7]`)
- **WARNING: Potentially destructive to accounts**
- Multi-threaded operations:
  - Theme flashing (rapid theme changes)
  - Friend removal
  - Language modification
  - Inventory cleaning
  - Mass messaging

### 7. Cookie Generator (`[10]`)
- Generates random cookie strings
- Useful for testing and development
- Outputs to `Gen_cookies.txt`

## ⚠️ Important Notes

- **Version 2.0.0 is marked as OUTDATED**
- Some features may not work due to Roblox API changes
- The tool includes automatic update checking
- PIN cracker module is disabled (Roblox removed PIN system)
- Discord fake site module is currently offline

## Security & Legal

- This tool is for educational purposes only
- Unauthorized access to accounts is illegal
- Respect others' privacy and property
- Use only on accounts you own or have permission to test

## Known Issues

1. **Outdated Version**: Some features may not work with current Roblox API
2. **Rate Limiting**: Some modules may hit Roblox rate limits
3. **Dependency Issues**: Automatic installation may fail on some systems
4. **PIN System**: PIN-related features are obsolete

## TODO

- [ ] Create new bypass server
- [ ] Update for current Roblox API
- [ ] Add error handling improvements
- [ ] Implement proxy support
- [ ] Add GUI version

## Developer

**Made by 0x256**
**Api library by gege_hello11**

---
