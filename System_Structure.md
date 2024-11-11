### **Overview of Real-Time Weather Reporting System Architecture**

```plaintext
                    +------------------------+
                    |    Weather API         |
                    | (Real-Time Weather Data)|
                    +-----------+------------+
                                |
                                | Fetch Weather Data
                                |
+-------------------------------v-----------------------------+
|                                                             |
|                Azure Function for Data Ingestion            |
|                                                             |
+-------------------------------+-----------------------------+
                                |
                                | Sends Data to Event Hub
                                |
                     +----------v-----------+
                     |     Azure Event Hub  |
                     |   (Data Stream Hub)  |
                     +----------+-----------+
                                |
                                | Streams Data
                                |
              +-----------------v-----------------+
              |                                   |
              |   Azure Databricks for Processing |
              |                                   |
              +-----------------+-----------------+
                                |
                                | Processes and Models Data
                                |
              +-----------------v-----------------+
              |                                   |
              |        Microsoft Fabric           |
              |    (Real-Time Analytics & KQL)    |
              +-----------------+-----------------+
                                |
                                | Visualizes Data
                                |
                     +----------v-----------+
                     |     Power BI         |
                     | (Real-Time Dashboards)|
                     +-----------------------+
```

### **Tool Summary**

1. **Azure Function**: Automates data fetching from the Weather API, preprocesses it, and pushes it to Event Hub for real-time streaming.
2. **Azure Event Hub**: Serves as the central ingestion point for streaming data, enabling real-time data handling for downstream services.
3. **Azure Databricks**: Processes, transforms, and enriches streaming data into Bronze, Silver, and Gold data layers, improving data quality and reliability.
4. **Microsoft Fabric**: Ingests and analyzes real-time data from Databricks via EventStream and KQL Database, supporting complex querying and interactive analytics.
5. **Power BI**: Builds real-time dashboards and visualizations connected to Microsoft Fabric, providing interactive insights into weather patterns and alerts.

This pipeline leverages Azure’s tools for ingestion, processing, analytics, and visualization, creating a robust real-time weather monitoring solution.
