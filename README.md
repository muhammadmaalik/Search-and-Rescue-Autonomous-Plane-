# Autonomous Fixed-Wing UAV Flight Controller Setup

An advanced deployment of the **ArduPlane (v4.6.3)** autopilot firmware onto an **AtomRC F405 NAVI Wing** flight control board. This project demonstrates custom hardware pin re-routing, digital protocol conversion (FlySky i-BUS), and systematic bench configuration using Mission Planner for manual and autonomous flight operations.

---

## 🎛️ Project Overview & Architecture

This build focuses on configuring a reliable fixed-wing flight control system with physical and software-based safety redundancies. Due to a damaged hardware pad on the primary UART, the system architecture utilizes low-level parameter remapping to establish communication over alternative hardware serial ports without compromising signal integrity.

### System Specifications
*   **Airframe Type:** Fixed-Wing / Flying Wing (Aileron + Elevator configuration)
*   **Flight Controller:** AtomRC F405 NAVI Wing (ChibiOS architecture)
*   **Firmware:** ArduPlane V4.6.3
*   **Radio System:** FlySky FS-iA6B Receiver & FS-i6 Transmitter
*   **Control Protocol:** Digital i-BUS (Serial)
*   **Ground Control Station (GCS):** Mission Planner via 3DR Telemetry Radio (57600 baud)
*   **Power System:** 14.8V (4S LiPo) main rail with integrated 5V/BEC servo rail

---

## 🛠️ Hardware Mapping & Custom Solder Workaround

During development, the primary `RX2` (UART2 RX) pad on the flight controller sustained physical damage. To bypass this, the digital receiver stream was successfully migrated to an alternative hardware serial port.

### Solder & Connection Matrix
| Component | Source Connection | Target FC Pad | Protocol / Function |
| :--- | :--- | :--- | :--- |
| **FlySky Receiver** | i-BUS Out (Servo Block) | **R3 (RX3)** | RC Input Stream |
| **Servo 1** | Signal / Power / GND | **S1** | Throttle Control |
| **Servo 4** | Signal / Power / GND | **S4** | Right Aileron |
| **Servo 5** | Signal / Power / GND | **S5** | Left Aileron |
| **Servo 7** | Signal / Power / GND | **S7** | Tail Elevator |

*Photos of the custom soldering and pin layout can be found in the `/media/wiring-diagrams/` folder.*

---

## 💻 Critical Parameter Configuration (Mission Planner)

The following parameters were modified within the ArduPlane Full Parameter List to override default behaviors, execute the custom pin-mapping, and prepare the bench for testing:

```ini
; Port Re-routing & Protocols
SERIAL2_PROTOCOL = -1     ; Disabled damaged RX2 port
SERIAL3_PROTOCOL = 23     ; Allocated UART3 RX (R3 pad) exclusively for RC Input
RC_PROTOCOLS     = 1      ; Set to Auto-detect incoming digital RC streams
FLTMODE_CH       = 6      ; Assigned Flight Mode switching to RC Channel 6

; Physical Servo Function Assignments
SERVO1_FUNCTION  = 70     ; S1 Pin = Throttle
SERVO4_FUNCTION  = 4      ; S4 Pin = Right Aileron
SERVO5_FUNCTION  = 24     ; S5 Pin = Left Aileron
SERVO7_FUNCTION  = 19     ; S7 Pin = Elevator

; Bench Testing Safety Modifiers
ARMING_CHECK     = 0      ; Temporarily bypassed pre-arm hardware blocks for safe bench debugging
