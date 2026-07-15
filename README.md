# Autonomous Fixed-Wing UAV Flight Controller Setup

This repository documents my setup and configuration of an autonomous flying wing using ArduPlane V4.6.3 on an AtomRC F405 NAVI Wing flight controller. 

The project covers a complete bench build, a custom hardware workaround for a damaged UART port, and the parameter configurations required to get a FlySky RC system communicating with ArduPilot over serial i-BUS.

---

## Hardware and System Overview

*   **Airframe Type:** Fixed-Wing / Flying Wing (Aileron + Elevator)
*   **Flight Controller:** AtomRC F405 NAVI Wing (ChibiOS architecture)
*   **Firmware:** ArduPlane V4.6.3
*   **Radio System:** FlySky FS-iA6B Receiver paired with an FS-i6 Transmitter
*   **Control Protocol:** Serial i-BUS
*   **Ground Control Station:** Mission Planner via 3DR Telemetry Radio (57600 baud)
*   **Power Supply:** 14.8V (4S LiPo) battery supplying power to the main board and servo rail

---

## The Hardware Hack: Solder Workaround

During assembly, the primary RX2 (UART2 RX) pad on the flight controller was physically damaged and rendered unusable. To bypass this, I migrated the receiver's digital signal line to an alternative hardware serial port.

I soldered the receiver's signal wire to the **R3 (RX3)** pad on the flight controller. Power and ground are routed to working 5V and GND pads on the board.

### Physical Wiring Matrix

| Component | Source Connection | Target FC Pad | Function |
| :--- | :--- | :--- | :--- |
| **FlySky Receiver** | i-BUS Out (Servo Block) | **R3 (RX3)** | Main RC Control Stream |
| **Servo 1** | Signal / Power / GND | **S1** | ESC / Throttle Control |
| **Servo 4** | Signal / Power / GND | **S4** | Right Aileron |
| **Servo 5** | Signal / Power / GND | **S5** | Left Aileron |
| **Servo 7** | Signal / Power / GND | **S7** | Tail Elevator |

*Wiring diagrams and photos of the solder joints are located in the /media/wiring-diagrams/ folder.*

---

## Mission Planner Configuration

To get ArduPilot to recognize the new serial port routing and map the servos correctly, I modified several parameters in Mission Planner's Full Parameter List.

```ini
; Re-routing the RC Input Serial Port
SERIAL2_PROTOCOL = -1     ; Disabled the damaged RX2 port
SERIAL3_PROTOCOL = 23     ; Allocated UART3 RX (R3 pad) as the RC input port
RC_PROTOCOLS     = 1      ; Kept on Auto-detect for incoming digital streams
FLTMODE_CH       = 6      ; Map flight mode switching to RC Channel 6

; Mapping the Control Surfaces
SERVO1_FUNCTION  = 70     ; S1 assigned to Throttle
SERVO4_FUNCTION  = 4      ; S4 assigned to Right Aileron
SERVO5_FUNCTION  = 24     ; S5 assigned to Left Aileron
SERVO7_FUNCTION  = 19     ; S7 assigned to Elevator

; Bench Testing Overrides
ARMING_CHECK     = 0      ; Bypassed pre-arm safety checks for bench testing
