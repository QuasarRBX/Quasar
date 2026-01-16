<div align="center">    

<img width="1920" height="514" alt="изображение" src="https://github.com/user-attachments/assets/ce1bf379-4822-40eb-becf-f190f7614fce" />

</div>

###

---

<div align="center">

<img width="2127" height="134" alt="изображение" src="https://github.com/user-attachments/assets/09922bea-1857-4857-a62d-0966cf993541" />

</div>

<div align="center">
  
## **Revolutionary Roblox Utility with Advanced Features**

###

**‼️Development of the quasar app has been suspended indefinitely until new systems are available‼️**

</div>

## Overview

Quasar is a powerful multifunctional tool for Roblox, providing advanced capabilities for account management, in-game economy operations, and data analysis. The updated version 2.2.0 includes enhanced API integrations, improved performance, and new bypass methods.

<div align="center">
  
## [Usage](#usage-1)
## [Installation](#installation-1)
## [Developer](#developer-1)

</div>

## Core Features

### Account Management
- **Cookie Checker** — Comprehensive analysis of Roblox cookies with detailed account information extraction
- **Mass Cookie Checker** — Batch validation of multiple cookies from `cookies.txt` file
- **Cookie Refresh** — Two methods for refreshing expired cookies (Ticket Method & Website Method)
- **Cookie Generator** — Random cookie string generation for testing purposes

### Economic Tools
- **Free Item Buyer** — Automatic purchase of all free items in Roblox catalog with rate limiting handling
- **Robux & Account Info** — Display detailed account information including:
  - Real-time Robux balance and pending transactions
  - Premium status and credit balance
  - RAP (Recent Average Price) value calculation
  - Group funds and ownership details
  - Transaction history and developer exchange totals
  - Followers count and account creation date

### Advanced Tools
- **Account Nuker** — Multi-threaded account modification tool with destructive capabilities:
  - Mass friend removal with threading optimization
  - Inventory item deletion with rate limit handling
  - Theme flashing (rapid light/dark theme changes)
  - Language modification to Japanese/Korean
  - Mass messaging to all conversations
- **Group Finder** — Intelligent search for available, unowned, public-entry groups
- **2FA & Age Bypass** — Multiple bypass methods via external APIs:
  - 18+ Age restriction bypass with passport verification
  - All ages restriction bypass
  - Complete security system bypass
  - Immortal API integration

### Game Utilities
- **Quasar Injector** — Direct download of external game modification utilities
- **C# Quasar Mass Checker** — High-performance cookie validation tool
- **External Service Integration** — Direct browser access to premium bypass services

## Installation

### Prerequisites
- Python 3.x (3.8 or higher recommended)
- pip package manager
- Internet connection for auto-dependency installation
- Windows OS for optimal functionality (Linux support available)

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
├── main.py                      # Main application entry point
├── cookies.txt                  # Cookie storage (one per line)
├── validcookies.txt             # Successfully validated cookies
├── invalidcookies.txt           # Invalid/failed cookies
├── Gen_cookies.txt              # Generated testing cookies
├── [username]_cookie.txt        # Individual cookie information dumps
├── Injector.zip                 # Downloaded game modification utility
├── quasarmasscookiechecker/     # C# mass checker directory
│   └── QuasarMassChecker.exe    # External mass checker executable
└── version                      # Version tracking file
```

## Usage

<div align="center">    

<img width="3840" height="2160" alt="изображение" src="https://github.com/user-attachments/assets/4d481d1f-bd13-4204-bc8d-bba7ab7d3999" />

</div>

## Available Modules (Updated v2.2.0)

### 1. Quasar Cheats (`[1]`)
- Downloads Quasar Injector (external game modification utility)
- Direct GitHub release integration with progress tracking
- Saves as `Injector.zip` in current directory with unpacking instructions
- Built-in download error handling and validation

### 2. Cookie Checker (`[2]`)
- Comprehensive single cookie analysis with detailed output
- Extracts 20+ account metrics including:
  - Account creation date and age
  - Email verification status and address
  - Pin security status with actionable advice
  - Premium membership validation
  - Thumbnail image URL extraction
  - Group ownership and fund tracking
- Automatic report generation to `[username]_cookie.txt`
- Real-time progress indication for each data point

### 3. Immortal Integration (`[3]`)
- Direct browser opening to `https://immortal.rs/dashboard/`
- Access to premium 2FA bypass and account security services
- Seamless integration with bypass modules
- External service coordination

### 4. Group Finder (`[5]`)
- Intelligent group discovery with configurable search repetitions
- Advanced filtering for:
  - Public entry permission verification
  - Owner status checking
  - Group lock detection
- API rate limit handling with retry logic
- Real-time hit reporting with group ID tracking

### 5. Account Nuker (`[7]`)
- **WARNING: Potentially destructive to accounts - Use with caution**
- Multi-threaded architecture with simultaneous operations:
  - Theme flashing with keyboard interrupt support
  - Mass friend removal with user ID tracking
  - Language cycling between Japanese and Korean
  - Inventory item deletion with rate limit compensation
  - Mass messaging to all conversations with custom messages
- Real-time operation status display
- Thread-safe API request management

### 6. Free Item Buyer (`[9]`)
- Advanced catalog scanning with pagination handling
- Intelligent purchase system with:
  - Already-owned item detection
  - Rate limiting with exponential backoff
  - CSRF token management
  - Session persistence
- Progress tracking with colorful console output
- Comprehensive error handling and recovery

### 7. C# Quasar Mass Checker (`[10]`)
- Downloads external C# mass cookie checker from GitHub releases
- Includes setup tutorial and file structure guidance
- Requires `cookies.txt` in checker directory
- Separate executable with enhanced performance for bulk operations

### 8. Bypass System (`[11]`, `[12]`, `[13]`, `[15]`)
- **Age Restriction 18+ Bypass** (`[11]`) - With password verification
- **General Age Bypass** (`[12]`) - For standard age restrictions
- **Complete Security Bypass** (`[13]`) - Full 2FA and security removal
- **All Ages Bypass** (`[15]`) - Comprehensive age restriction removal
- Multiple API endpoint integration with fallback support
- 1-5 minute processing time with real-time status updates

### 9. Cookie Refresh (`[14]`)
- **Ticket Method**: Advanced CSRF token and authentication ticket handling
- **Website Method**: External service integration for cookie renewal
- Dual-method approach for maximum compatibility
- Detailed error reporting and troubleshooting

## Important Notes

- **Version 2.2.0** — Includes enhanced API integrations and improved stability
- **Auto-Update System** — Built-in version checking with GitHub integration
- **External Dependencies** — Some modules require internet for downloads and API calls
- **Rate Limiting** — Comprehensive handling of Roblox API rate limits
- **Multi-Threading** — Optimized threading for performance-critical operations

## Security & Legal

- **Educational Purpose Only** — This tool is for learning and research purposes
- **Authorized Use Only** — Only test on accounts you own or have explicit permission
- **Respect Privacy** — Never access others' accounts without authorization
- **Compliance** — Follow Roblox Terms of Service and all applicable laws
- **Disclaimer** — Developers are not responsible for misuse or damage

## Known Issues & Limitations

1. **Offline Modules** — PIN cracker and email validator remain disabled due to API changes
2. **API Dependencies** — Requires stable internet connection for full functionality
3. **Rate Limiting** — Intensive operations may trigger Roblox API protections
4. **Windows Focus** — Some features optimized for Windows environment
5. **External Service Reliability** — Bypass services depend on third-party API availability

## Dependencies

Automatically installed packages:
- `requests` — Advanced HTTP requests with session management
- `pystyle` — Console interface styling and color management
- `pyisemail` — Email validation (legacy support)
- `tqdm` — Progress bars for downloads and operations
- `termcolor` — Colored console output
- `rich` — Enhanced console formatting and layout
- `socket` — Network operations and connectivity checks
- `threading` — Multi-threaded operation support
- `json` — API response parsing and data handling

## Developer

**Made with love by [0x256](https://github.com/jealleal)**

- **GitHub**: [QuasarRBX](https://github.com/QuasarRBX)
- **API Library**: [RobloxAPI](https://github.com/QuasarRBX/RobloxAPI)

## Auto-Update System

Built-in update checking:
- Automatic GitHub version comparison
- Update notifications with direct links
- Seamless version tracking
- Update instructions and changelog access

---

**Disclaimer**: This tool is provided strictly for educational and research purposes. The developers assume no responsibility for any misuse, damage, or violations of terms of service. Users are solely responsible for ensuring they have proper authorization before testing any functionality. Always respect digital property rights and privacy laws.
