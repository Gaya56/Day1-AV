# Connecting Power BI to Databricks for Real-Time Streaming Analytics

## 1. Configure Databricks SQL Endpoint
- Go to the Databricks workspace.
- Navigate to **SQL Endpoints** and create an endpoint that has access to your Delta Lake tables.
- Note down the **JDBC URL** and **authentication token** for Power BI.

## 2. Connect Power BI to Databricks
- Open Power BI Desktop.
- Go to **Get Data** > **Azure** > **Azure Databricks**.
- Enter the JDBC URL from the SQL Endpoint and the authentication token.
- Choose **DirectQuery** mode for live data access.

## 3. Build Your Dashboard
- Use Power BI visuals to create charts and tables that display metrics such as average temperature per device.
- Set up refresh intervals as needed for real-time monitoring.