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

## **Snapshots**
![pizza1](https://github.com/user-attachments/assets/8bc520b7-9548-48c3-8c65-fe3afa0e3733)
![pizza2](https://github.com/user-attachments/assets/083a4c25-ce59-4b92-b63a-e5e955c6bd6e)
![pizza3](https://github.com/user-attachments/assets/ca37f2ec-94b6-44ec-a728-fd1a0a51c43a)
![pizza4](https://github.com/user-attachments/assets/22304a5a-f4b7-4961-a2ac-a097656bd84d)
![pizza5](https://github.com/user-attachments/assets/cc4ca895-757e-447b-87f8-6457a3ea4a4f)
![pizza6](https://github.com/user-attachments/assets/a8792ebb-bb38-4fb4-9a51-8fef328b7f9d)



