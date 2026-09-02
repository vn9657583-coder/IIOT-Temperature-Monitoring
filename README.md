# IIoT Machine Temperature Monitoring System

## Project Overview

This project simulates an Industrial Internet of Things (IIoT) system for monitoring machine temperature.

A simulated temperature sensor generates readings, MQTT is used for communication, SQLite stores data, and Python is used for analysis and visualization.

## Technologies Used

- Python
- MQTT
- SQLite
- Pandas
- Matplotlib

## System Flow

Sensor → Python → MQTT → Database → Data Analysis → Alert

## Features

- Simulated machine temperature sensor
- MQTT communication
- Temperature data storage
- High-temperature detection
- Temperature analysis
- Graph visualization

## Alert Condition

A temperature above 40°C is considered a high-temperature condition.

## Future Improvements

- Add real hardware sensors
- Add a web dashboard
- Add cloud database storage
- Send notifications for high temperature
