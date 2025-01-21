# Meteo Alarm Automation

## Overview
This project automates the process of monitoring weather alerts from the [Meteo Alarm](https://meteoalarm.org/en/live/) website. The automation checks for alarms in a specified country using API calls, extracts details about awareness levels and alert types, and generates a report in Excel format. The report is sorted alphabetically by region and sent via email to the people located in that areas.

## Features
1. **Alarm Check** - Verifies if there are active alarms for the specified country.
2. **Data Extraction** - Captures awareness levels and alert types for all pinned regions.
3. **Excel Report Generation** - Creates an Excel file with the following columns:
   - `Region`
   - `Awareness Level`
   - `Alert Type`
4. **Sorting** - Sorts the Excel report alphabetically (A-Z) based on regions.
5. **Email Notification** - Sends the report as an email attachment with:
   - `Importance: High`
   - `Sensitivity: Personal`

## Output
- An Excel report named `Meteo_Alarm_Report.xlsx` containing:
  - `Region`
  - `Awareness Level`
  - `Alert Type`
- An email sent with the report attached.

## Future improvements
- Parallel Processing
    - Use **parallel workflows** in UiPath to handle multiple users or regions simultaneously.
    - Divide the task of checking alarms or extracting data into smaller chunks and process them concurrently.
    - Use queues in UiPath Orchestrator to manage tasks more efficiently.
- Dynamic Queue Management
   - Leverage UiPath **Orchestrator queues** to distribute tasks.
   - Push tasks for each user or region into a queue.
   - Assign robots to process these tasks concurrently, ensuring faster processing
- Scalable Report Generation
   - Generate reports in formats suitable for large datasets (e.g., CSV, Parquet).
   - Store historical reports in a centralized repository (e.g., cloud storage) for easy access and sharing.
- Database Integration
   - Replace Excel files with a **database** for better scalability and performance.
   - Store user data, regions, alarms, and reports in a relational database (e.g., PostgreSQL, MySQL, Data Service from Orchestrator).




