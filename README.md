# Warehouse Management System (WMS) MVP

## Overview
This project is a Minimum Viable Product (MVP) for a **Warehouse Management System (WMS)**.  
It enables:
- Standardizing marketplace SKUs to Master SKUs.
- Storing and managing mapped sales data in a relational database.
- Providing quick insights through an interactive dashboard.
- Allowing AI-powered natural language queries on sales data.

---

## Features
1. **Data Exploration**
   - Python script to check raw data format and column names.

2. **SKU Mapping**
   - Maps marketplace-specific SKUs to Master SKUs.
   - Generates a cleaned dataset with standardized product identifiers.

3. **GUI for SKU Mapping**
   - Simple graphical interface built with **CustomTkinter**.
   - Non-technical users can easily map SKUs without coding.

4. **Database Storage**
   - Mapped sales data is stored in **SQLite** using **SQLAlchemy**.

5. **Dashboard**
   - Built with **Streamlit** + **Plotly**.
   - Shows total sales quantity, unique SKUs, top-selling products, and interactive charts.

6. **AI-Powered Queries**
   - Uses **PandasAI + OpenAI API** to run natural language queries on sales data.
   - Example: `Show total quantity sold by MSKU`.

---

## Tech Stack
- **Python 3.10+**
- **Pandas**, **OpenPyXL**, **SQLAlchemy**
- **CustomTkinter** for GUI
- **Streamlit**, **Plotly** for Dashboard
- **PandasAI** + **OpenAI** for AI queries
- **SQLite** database

---

## Project Structure
