## Mission: AI-Driven Search and Rescue (SAR)
This platform is not just an RC aircraft; it is a rapidly deployable, autonomous Search and Rescue (SAR) UAV. The primary mission of this hardware is to execute autonomous aerial grid sweeps over extreme environments (dense forests and deserts) to locate lost individuals when traditional rescue helicopters are unavailable or too expensive.

## Edge AI & Computer Vision Integration
To move beyond basic GPS flight, this airframe is engineered to carry and power an **Nvidia Jetson** edge-computing module. 
* **Real-Time Detection:** The Jetson is trained with custom computer vision models to process live camera feeds and identify human heat signatures or visual anomalies in real-time during flight.
* **Decentralized Network Potential:** For the Solana Microgrant ecosystem, this UAV acts as a proof-of-concept for a DePIN (Decentralized Physical Infrastructure Network) node. It can securely log search-grid coverage, flight data, and positive target identification directly to the blockchain, allowing decentralized, trustless coordination for emergency response teams.


# Autonomous Fixed-Wing UAV Platform: A Hardware Proof-of-Concept




## Project Overview
This repository details the development of an autonomous, fixed-wing Unmanned Aerial Vehicle (UAV). Built on the ArduPilot ecosystem, this project serves as a low-cost, highly programmable hardware platform capable of executing autonomous GPS-guided flight paths. 

The immediate goal of this phase was to successfully integrate custom hardware routing, establish reliable serial digital communications, and validate autonomous flight modes on a custom-designed airframe. This platform lays the groundwork for future integrations into decentralized physical infrastructure networks (DePIN) and autonomous data collection.

## Technical Specifications

### Hardware Architecture
*   **Flight Controller:** AtomRC F405 NAVI Wing (ChibiOS)
*   **Radio Control System:** FlySky FS-iA6B Receiver & FS-i6 Transmitter
*   **Telemetry:** 3DR Telemetry Radio (57600 baud) for remote Ground Control Station data
*   **Power System:** 14.8V (4S LiPo) providing dual-rail power to logic and servos
*   **Airframe:** [Insert link to the plane frame/wing here]
*   **Propulsion:** [Insert link to motor/ESC here]

### Software & Firmware
*   **Firmware:** ArduPlane V4.6.3
*   **Control Protocol:** i-BUS (Serial Digital Output)
*   **Ground Control Station:** Mission Planner

## Custom Engineering & Problem Solving

### Hardware Level Serial Re-routing
During development, the primary UART RX port was damaged. To maintain digital i-BUS communication without replacing the mainboard, I successfully re-engineered the pinout at the hardware and firmware level. The receiver's digital stream was manually soldered to the R3 (RX3) pad, and the ArduPilot parameter tree was modified to dedicate `SERIAL3_PROTOCOL` specifically for RC input. 

### Custom CAD & 3D Printed Integration
Standard off-the-shelf mounts were insufficient for the required hardware layout. I utilized Fusion 360 to design and manufacture custom mounting solutions to secure the flight controller and organize the telemetry components. 

*CAD render files and source models can be viewed in the `/cad-design/` directory.*

## Autonomous Flight Modes Validated
The system is programmed with a physical channel override to switch between three core operational states:
1.  **Manual / Direct Passthrough:** Full pilot control for testing and emergency recovery.
2.  **Fly-By-Wire A (FBWA):** Autopilot-assisted stabilization with electronic pitch and roll limits.
3.  **Autonomous Loiter & Return-to-Launch (RTL):** GPS-guided holding patterns and automated home-point navigation.

## Bill of Materials (BoM)
| Component | Description | Reference Link |
| :--- | :--- | :--- |
| **Flight Controller** | AtomRC F405 NAVI Wing | [Link to FC] |
| **Transmitter/Receiver** | FlySky FS-i6 + FS-iA6B | [Link to Radio] |
| **Telemetry System** | 3DR Radio V2 | [Link to Telemetry] |
| **Servos** | [Insert servo brand/size] | [Link to Servos] |
| **Battery** | [Insert battery size] 4S LiPo | [Link to Battery] |
| **Airframe** | [Insert plane name] | [Link to Plane] |

## Directory Structure
*   `/cad-design/`: Contains Fusion 360 renders and custom mount designs.
*   `/firmware-config/`: Contains the base ArduPlane parameter backup files.
*   `/media/`: Photographic documentation of the wiring layout and bench testing.
