                                                                           
      █████   █    ██  ▄▄▄        ██████  ▄▄▄       ██▀███  
    ▒██▓  ██▒ ██  ▓██▒▒████▄    ▒██    ▒ ▒████▄    ▓██ ▒ ██▒
    ▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ░ ▓██▄   ▒██  ▀█▄  ▓██ ░▄█ ▒
    ░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██   ▒   ██▒░██▄▄▄▄██ ▒██▀▀█▄  
    ░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒▒██████▒▒ ▓█   ▓██▒░██▓ ▒██▒
    ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░
     ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░░ ░▒  ░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░
       ░   ░  ░░░ ░ ░   ░   ▒   ░  ░  ░    ░   ▒     ░░   ░ 
        ░       ░           ░  ░      ░        ░  ░   ░     
                                                            

<div align="center">

![Quasar Banner](https://img.shields.io/badge/QUASAR-2.0.0-purple?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Enhanced-blue?style=for-the-badge)

</div>

<div align="center">

<img width="1000" height="500" alt="main" src="https://github.com/user-attachments/assets/9068dc73-e27c-40c4-9f42-7c7e483a4cdd" />

## **Revolutionary Roblox Utility with Advanced Features**

</div>

## 📌 Overview

Quasar is a powerful multifunctional tool for Roblox, providing advanced capabilities for account management, in-game economy operations, and data analysis. The updated version includes integration with external services and enhanced functionality.

## 🚀 Core Features

### 🔐 Account Management
- **Cookie Checker** — Detailed analysis of information from Roblox cookies
- **Mass Cookie Checker** — Validation of multiple cookies from `cookies.txt` file
- **Immortal Integration** — Direct access to 2FA bypass service
- **Cookie Generator** — Random cookie string generation for testing

### 💰 Economic Tools
- **Free Item Buyer** — Automatic purchase of all free items in Roblox catalog
- **Robux & Account Info** — Display detailed account information including:
  - Robux balance and credit
  - RAP (Recent Average Price) value
  - Premium status
  - Group funds and ownership
  - Transaction history
  - Followers count

### 🛠️ Advanced Tools
- **Account Nuker** — Multi-threaded account modification tool:
  - Mass friend removal
  - Inventory item deletion
  - Theme flashing (rapid changes)
  - Language modification
  - Mass messaging
- **Group Finder** — Search for available, unowned, public-entry groups
- **2FA Bypass** — Age restriction and security bypass via Immortal API

### 🎮 Game Utilities
- **Quasar Injector** — Download external cheating utilities
- **Quasar Mass Checker** — Download C# version for advanced cookie checking

## 🛠️ Installation

### Prerequisites
- Python 3.x
- pip package manager
- Internet connection for auto-dependency installation

### Automatic Installation
The tool automatically installs required dependencies on first run:

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
├── main.py                      # Main application
├── cookies.txt                  # Cookie storage
├── validcookies.txt             # Validated cookies
├── invalidcookies.txt           # Invalid cookies
├── Gen_cookies.txt              # Generated cookies
├── [username]_cookie.txt        # Individual cookie info dumps
├── Injector.zip                 # Downloaded cheating utility
├── quasarmasscookiechecker/     # C# mass checker directory
└── quasar_mass_checker.exe      # External mass checker
```

## 🎮 Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Select an option from the main menu:

   ```
   [1] Cheats (Quasar)    [ONLINE];                [6] Email validator  [OFFLINE];               [11] Get server IP           [OFFLINE];                 
   [2] Cookie checker     [ONLINE];                [7] Nucker           [ONLINE];                [12] Bypass age              [ONLINE];                 
   [3] Immortal           [ONLINE];                [8] BruteForcer      [OFFLINE];               [13] Bypass all              [ONLINE];            
   [4] Roblox Pin cracker [OFFLINE];               [9] free-item-buyer  [ONLINE];                [14] C# QMCC                 [ONLINE];                  
   [5] Group finder       [ONLINE];                [10] Cookie Gen.     [OFFLINE];               [15] Group wall spammer      [OFFLINE];
   ```

3. Follow on-screen instructions for each module.

## 🔧 Available Modules (Updated)

### 1. Quasar Cheats (`[1]`)
- Downloads Quasar Injector (external cheating utility)
- Provides direct access to game modification tools
- Saves as `Injector.zip` in current directory

### 2. Cookie Checker (`[2]`)
- Input a single Roblox cookie
- Extracts comprehensive account information:
  - Username, Display Name, User ID
  - Robux balance and pending transactions
  - Premium status and credit
  - Email verification status
  - Group ownership and funds
  - RAP value and inventory statistics
- Saves detailed report to `[username]_cookie.txt`

### 3. Immortal Integration (`[3]`)
- Direct browser opening to `https://immortal.rs/dashboard/`
- Access to premium 2FA bypass services
- External account security tools

### 4. Group Finder (`[5]`)
- Searches for available Roblox groups
- Filters for:
  - Public entry allowed
  - No current owner
  - Not locked/private
- Configurable search repetitions

### 5. Account Nuker (`[7]`)
- **WARNING: Potentially destructive to accounts**
- Multi-threaded operations:
  - Theme flashing (rapid light/dark theme changes)
  - Mass friend removal
  - Language modification to Japanese/Korean
  - Inventory item deletion
  - Mass messaging to all conversations
- Real-time operation display

### 6. Free Item Buyer (`[9]`)
- Uses provided cookie for authentication
- Scans entire Roblox catalog for free items
- Automatically purchases all unpurchased free items
- Handles rate limiting and already-owned items
- Real-time progress display

### 7. C# Quasar Mass Checker (`[14]`)
- Downloads external C# mass cookie checker
- Provides enhanced performance for bulk operations
- Requires `cookies.txt` file with one cookie per line
- Separate executable with dedicated interface

### 8. 2FA Bypass (`[12]` & `[13]`)
- Age restriction bypass (`[12]`)
- Complete security bypass (`[13]`)
- Integration with Immortal API
- Handles rate limiting and API responses

## ⚠️ Important Notes

- **Enhanced Version 2.0.0** — Includes external service integrations
- **External Downloads** — Some modules download external executables
- **API Dependencies** — Requires stable internet connection
- **Rate Limiting** — Roblox API has strict rate limits
- **Security** — Use only on accounts you own or have permission to test

## 🔒 Security & Legal

- **Educational Purpose Only** — This tool is for learning and research
- **Authorized Use Only** — Only test on accounts you own
- **Respect Privacy** — Do not access others' accounts without permission
- **Compliance** — Follow Roblox Terms of Service and applicable laws

## 🐛 Known Issues & Limitations

1. **Offline Modules** — Some original features are disabled (PIN cracker, email validator)
2. **External Dependencies** — Requires internet for downloads and API calls
3. **Rate Limiting** — Some operations may hit Roblox API limits
4. **Windows Focus** — Some features optimized for Windows environment

## 📝 TODO & Future Development

- [ ] Create new bypass methods
- [ ] Update for current Roblox API changes
- [ ] Add proxy support for all modules
- [ ] Implement GUI version
- [ ] Add error recovery mechanisms
- [ ] Enhance multi-threading performance

## 🧩 Dependencies

The tool automatically installs:
- `requests` — HTTP requests handling
- `pystyle` — Console interface styling
- `pyisemail` — Email validation (currently unused)
- `tqdm` — Progress bars
- `termcolor` — Colored console output
- `rich` — Enhanced console formatting
- `socket` — Network operations

## 👨💻 Developer

**Created by 0x256**

- **Website**: quasar.gt.tc
- **GitHub**: [QuasarRBX](https://github.com/QuasarRBX)
- **API Library**: [RobloxAPI](https://github.com/QuasarRBX/RobloxAPI)

## 🔄 Auto-Update System

The tool includes version checking:
- Automatically checks GitHub for updates
- Notifies when new versions are available
- Provides update instructions

---

**Disclaimer**: This tool is provided for educational purposes only. The developers are not responsible for any misuse or damage caused by this software. Always ensure you have proper authorization before testing on any accounts.
