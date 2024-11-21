# GOOAAL: Mobile Pizza Ordering Application

This repository contains the implementation of **GOOAAL**, a mobile application for pizza ordering. The project was developed as part of a university course and features dynamic menu presentation, order processing, and delivery tracking. A robust backend built on MySQL ensures efficient data management.

---

## **Project Overview**

The **GOOAAL** application addresses the need for a modular, restaurant-specific pizza ordering system. It includes:
- A dynamic menu system for browsing items.
- Full order processing with discounts and delivery tracking.
- Integration with a MySQL database for seamless data storage.

### **Key Objectives**
1. Provide an intuitive interface for customers to browse, customize, and place orders.
2. Implement backend logic to handle discounts, customer management, and delivery operations.
3. Optimize the database schema to ensure scalability and performance.

---

## **Features**

### 1. Dynamic Menu
- Displays pizzas, drinks, and desserts.
- Each menu item includes:
  - Ingredients list.
  - Price calculation: `cost + profit margin (40%) + VAT (9%)`.
  - Dietary information (vegetarian/vegan).
- Example Python code for menu generation:
  ```python
  def calculate_price(cost):
      return cost * 1.4 * 1.09  # 40% profit margin + 9% VAT

Video Presentation - https://youtu.be/dfw2CxI7k90
