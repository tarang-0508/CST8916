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

### 1.IoT Sensor Simulation
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
```

### 2. IoT Hub Configuration: 

- IoT Hub Name: rideau-iothub
- Resource Group: rideau-monitoringg
- Status: Active
- Region: Canada Central
- Tier: Standard

The three devices DowsLakeSensor, FifthaveSensor, NACSensor received individual additions through manual entries in the Azure portal. Each device authenticates using Shared Access Signature (SAS) keys that the simulation script applied as part of its authentication process.

### 3.Azure Stream Analytics Job
The Azure Stream Analytics job operates as the real-time processor of data sent from the IoT Hub. This system combines aggregation with a 5-minute time frame before it saves processed information in Azure Blob Storage for evaluation purposes.

- Job Name : rideauStreamJob
- Resource Group :  rideau-monitoringg
- Location : Canada Central
- Hosting Environment :  Cloud (Shared Cluster)

#### Input Source
- Source: Azure IoT Hub
- Alias: iotInput
- Data: Simulated IoT sensor readings
- Fields: location, iceThickness, snowAccumulation, timestamp

#### Output source
- Destination: Azure Blob Storage
- Alias: blobOutput
- Container: canal-output
- Path Format: rideau/{date}/{time}
- Format: JSON

#### Query Logic
```
SELECT
    location,
    System.Timestamp AS windowEnd,
    AVG(iceThickness) AS avgIceThickness,
    MAX(snowAccumulation) AS maxSnowAccumulation
INTO
    blobOutput
FROM
    iotInput
TIMESTAMP BY timestamp
GROUP BY
    TumblingWindow(minute, 5), location
```
### Azure Blob Storage

- Storage Account : rideaucanalstorageacc
- Container : streamcontainer
- Access Tier : Hot (default)
- Replication : Locally-redundant storage (LRS)
- Output Path Format : rideau/{date}/{time}
- File Format : JSON

##  Usage Instructions
### 1. Running the IoT Sensor Simulation  

To simulate sensor data from Dow's Lake, Fifth Avenue, and NAC locations:  

1. Open Visual Studio Code.  
2. Ensure Python 3.11 or above is installed.  
3. Install the required Azure IoT Device SDK using pip:  
```
pip install azure-iot-device
```
4. Navigate to the folder containing simulate_sensors.py.  
5. Make sure your simulate_sensors.py contains device connection strings for:

<li>DowsLakeSensor</li>  
<li>FifthaveSensor</li>  
<li>NACSensor</li>  


6. Run the simulation script:  
```
python simulate_sensors.py
```
### 2.Configuring Azure Services: 

- Create Iot Hub 
- Implement three sensors located at Dow'sLake and FifthAvenue and NAC in the registered devices section of device management.
- Execute the following steps to obtain the primary connection strings for each sensor towards python script creation. Then develop Stream Analytics.
- The Job Topology section in Input contains two components: IoT Hub 
- A blog storage output has been added under the Job Topology under Output selection.
- The Job Topology under Query section allows users to create queries which they can save before executing them.
  
### 3.Accessing Stored Data:

- The next step is to visit Storageaccount where users must choose conatiner.
- A json file can be found inside this container after executing the previous query.

## Results

### Key Findings

The Stream Analytics job completed its execution by processing IoT sensor data in real-time before it stored aggregated values in Azure Blob Storage. Azure Stream Analytics produces several metrics from processed data.

- **Average Ice Thickness**: Offers insights into ice conditions over specific time intervals.
- **Maximum Snow Accumulation**: Shows the highest snow accumulation during those intervals.

## Reflection

I faced issues when running Python scripts within a virtual environment because the selection of the requirements.txt file was improper and resulted in missing dependencies. The successful execution of the scripts was prevented by this failure. I watched a video instruction to establish the virtual environment properly before downloading dependencies from the requirements.txt file. Following these steps I managed to execute the simulation scripts without problems.
