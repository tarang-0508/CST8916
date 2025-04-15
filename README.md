# Real-time-Monitoring-System-for-Rideau-Canal-Skateway

## Scenario Description

The Rideau Canal Skateway in Ottawa, Ontario attracts worldwide visitors as it presents itself as the longest naturally frozen skating rink on Earth. Thousands of residents together with tourists make use of the canal during every winter season for activity purposes and for transportation needs. Public safety monitoring becomes necessary due to changing climate conditions that require constant ice surface analyses.

This project establishes a constant ice condition monitoring system which provides updated reports regarding canal ice conditions. As employee of National Capital Commission you will create a model to replicate Internet of Things (IoT) sensors which will be stationed at critical points along the skateway route.

These sensors capture vital environmental metrics such as:
- Ice Thickness (cm) : A meter uses to measure ice depth for determining skating safety.
- Surface Temperature (°C) : Measures the status between ice preservation and the beginning of its melting process.
- Snow Accumulation (cm) : Ice thickness determines the accumulation of snow that creates hazardous conditions for vision and safety on the ice.
- External Temperature (°C) : Weather conditions create the contextual framework that challenges ice structural stability.

 ## System Architecture

- **IoT Sensors:**  A Python script operates three virtual sensor positions at Dow’s Lake, Fifth Avenue, and NAC while generating environmental measurements of ice thickness and surface temperature and snow accumulation as well as external temperature at 10-second intervals.
- **Azure IoT Hub:** The system serves as the communication gateway between simulated devices and cloud infrastructure for obtaining their transmitted data. The system registers devices which transmit their data through secure protocols.
- **Azure Stream Analytics:** This application receives real-time data through the IoT Hub. It operates on the information by executing 5-minute average computations for ice thickness and maximum snow levels then delivers the results. The solution receives information through the IoT Hub while it aggregates data within 5-minute periods to generate statistical outcomes about ice thickness and snow accumulation before producing results.
- **Azure Blob Storage:** The system uses JSON format to store processed data organized through dates and times in structured format. The calculated data gets stored in a structured JSON format by date and time to establish itself as a data lake that supports analysis.
  

![Image](https://github.com/user-attachments/assets/4a0fe9ed-73ba-44ff-bfc6-be82f18256dd)

## Implementation Details

### IoT Sensor Simulation
A Python script simulates environmental data from three canal locations: **Dow's Lake**, **Fifth Avenue**, and **NAC**. Each device sends the following metrics every 10 seconds:
- Ice Thickness (cm): Measures safety of ice for skating.
- Surface Temperature (°C): Helps detect potential melting.
- Snow Accumulation (cm): Affects ice insulation and surface condition.
- External Temperature (°C): Adds broader weather context.

Sample JSON payload:
```json
{
  "location": "Dow's Lake",
  "iceThickness": 27,
  "surfaceTemperature": -1,
  "snowAccumulation": 8,
  "externalTemperature": -4,
  "timestamp": "2024-11-23T12:00:00Z"
}



  
