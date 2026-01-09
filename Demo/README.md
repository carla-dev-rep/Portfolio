<!--- README file --->

# Indoor Digital Twin: Unity3D & Radar Integration via RabbitMQ

## 🎥 Project Demo
<video src="Demo_DT.mp4?raw=true" poster="poster.jpg" height="500" controls>
  Your browser does not support the video tag. 
  <a href="Demo_DT.mp4?raw=true">Click here to download the video</a>.
</video>

## 📝 Project Overview
This project involves the development of a real-time **Digital Twin** for an indoor environment. 
The system synchronizes physical space with a virtual replica built in **Unity3D**, visualizing target movements detected by a hardware radar sensor.

## 🛠 Tech Stack
* **Engine:** Unity3D (C#)
* **Message Broker:** RabbitMQ (AMQP Protocol)
* **Sensor Integration:** Short-range Radar (MIMO)
* **Data Handling:** JSON Parsing / Asynchronous Messaging

## 🏗 System Architecture
The project implements an event-driven architecture designed to ensure low-latency synchronization between the physical and virtual environments:

1.  **Data Acquisition:** The radar sensor captures $(x, y, z)$ coordinates of targets within the physical indoor space.
2.  **Message Brokerage:** Data packets are published to a **RabbitMQ** exchange.
3.  **Unity Subscriber:** A custom C# consumer client within Unity listens to the queue asynchronously to prevent main-thread blocking.
4.  **Spatial Mapping & Rendering:** Upon receiving a message, the system parses the coordinates and updates the Transform properties of virtual GameObjects.

## 🚀 Key Technical Challenges
* **Latency Optimization:** Fine-tuned the RabbitMQ consumer to handle high-frequency data streams while maintaining a stable frame rate in Unity.
* **Coordinate Transformation:** Implemented a mapping layer to translate raw sensor data into Unity’s Cartesian coordinate system, accounting for scale, rotation, and offsets.

---
*Note: The source code is private due to intellectual property restrictions.*
---