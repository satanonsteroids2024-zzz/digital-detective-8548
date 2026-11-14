# Mission 1 — Computer Basics

## 1. Task / objective
Explain how a computer takes input, processes it, gives output and stores the result (IPOS). Then list hardware and software I actually use and sort them into types, and name three computer systems from everyday life that are not a laptop or phone.

## 2. Work completed
- Traced one real activity, typing and saving a note in a text editor, through the four IPOS stages.
- Made a table of five hardware items and six software items from my own MacBook and classified each one.
- Listed three everyday computer systems with their purpose, one input and one output.
- Looked at what apps and utilities are actually installed on this Mac before writing the software table, so nothing in it is guessed.

## 3. Commands / tools used
| Tool | Why |
|---|---|
| `ls /Applications` | Check which apps are really installed |
| `system_profiler SPHardwareDataType` | See the Mac model, chip and memory (I left out the serial number and device name) |
| `df -h /` | Confirm the main storage is a built-in disk |
| Text editor (VS Code) | Used as the example application for the IPOS trace |

## 4. My understanding

### Task 1.1 — IPOS trace: typing and saving a note

| Stage | What happens in my example | Hardware / component |
|---|---|---|
| Input | I press keys. Each key press is turned into an electrical signal that the keyboard sends to the computer as a code for that key. | Built-in keyboard |
| Processing | The operating system hands the key code to the editor, which decides what to do with it (add a letter, move the cursor). All of this runs as instructions on the processor, using memory to hold the text I have typed so far. | Apple M5 processor, 16 GB RAM |
| Output | The editor redraws the window so the new letter appears on screen straight away. | Retina display |
| Storage | When I press Save, the text in memory is written to a file on the built-in SSD. Before that it only exists in RAM and would be lost if the power went off. | Internal SSD |
| Extra step: cloud/sync | If the folder is pushed to GitHub, a copy goes over the internet to a remote server too. | Wi-Fi, GitHub's servers |

So the activity travels like this: keyboard (input), processor and RAM (processing), screen (output), then SSD (storage). The result stays on the screen and on the disk, and the text I typed is what the processor worked on in between.

### Task 1.2 — Hardware and software I use

| Item / software name | Hardware or software? | Software type | Purpose |
|---|---|---|---|
| Keyboard | Hardware | Not applicable | Used to enter text and shortcuts |
| Trackpad | Hardware | Not applicable | Moves the pointer and clicks |
| Display (Retina screen) | Hardware | Not applicable | Shows everything I am working on |
| Internal SSD | Hardware | Not applicable | Stores my files and apps permanently |
| Built-in speakers | Hardware | Not applicable | Play sound |
| macOS | Software | Operating system | Manages the hardware, memory, files and running programs |
| Google Chrome | Software | Application | Browsing websites and GitHub |
| Visual Studio Code | Software | Application | Writing and editing the README and Python files |
| Terminal | Software | Utility | Typing commands to manage files and run tools |
| Activity Monitor | Software | Utility | Shows which processes use CPU and memory |
| Disk Utility | Software | Utility | Checks and manages the storage drive |

I put Terminal under utility because I mostly use it to manage and check the computer rather than to produce a document.

### Task 1.3 — Computer systems around me

| System | Main purpose | One input | One output |
|---|---|---|---|
| ATM | Lets people withdraw cash and check balance without going into a bank | Card and PIN typed on the keypad | Cash and a printed receipt |
| Smart TV | Plays video and streaming apps | Remote control button press | Picture on the screen and sound |
| Traffic signal controller | Controls the order of red, yellow and green lights at a junction | Timer or a sensor that detects waiting vehicles | The colour of the lights |

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [evidence/mission-01/system-check.txt](../evidence/mission-01/system-check.txt): the hardware model, memory and storage output I used to fill in the tables, with personal details removed.

## 8. Commit details
- Commit message: `Complete computer basics and IPOS mission`
- Pushed to `main` on GitHub and checked there.
