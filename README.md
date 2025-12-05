```markdown
# LoadBalancerMonitor-Python

A simple Python tool that checks the status of nodes inside a subnet.  
It uses ping to see if the master and slave nodes are online.  
This project was created to practice classes, objects, subprocess, and basic networking logic.

---

## Features

- Node class to store an IP address  
- IP validation (check if the address can exist)  
- Ping test with a 2-second timeout  
- LoadBalancerMonitor class with:
  - Master node
  - List of slave nodes
  - Add and remove slaves
  - Print full status report

---

## Project Structure

```

load_balancer_monitor_mebrahimi22.py
README.md

```

---

## How It Works

### 1. Node Class
- Stores an IP address  
- Checks if the IP address is valid  
- Runs a ping test to see if the node is online  

### 2. LoadBalancerMonitor Class
- Stores network address and mask  
- Stores a master node  
- Stores a list of slave nodes  
- Has methods to:
  - Add slave  
  - Remove slave  
  - Print system status  

---

## Example Output

```

Checking.....

# Load Balancer Status

Master: ONLINE
Slaves: 3 ONLINE, 1 OFFLINE

````

---

## Requirements

- Python 3  
- Linux environment for `ping` command  
- subprocess module (built-in)

---

## Running the Program

```bash
python3 load_balancer_monitor_mebrahimi22.py
````

---

## Skills Practiced

* Python classes and objects
* Constructor and instance methods
* Calling OS-level commands from Python
* Network troubleshooting basics
* Git + GitHub + SSH workflow

---

## Author

**Mehran Ebrahimi**
Github: [mehran3b](https://github.com/mehran3b)

---

## License

This project is open-source. You can use it for learning or practice.

```
```

