# Car Sales Website - Mid Term Exam

## Overview

This project aims to create a fully functional car sales website that facilitates car listings, user authentication, and order management. The website will allow users to view and filter cars by brand, create accounts, log in, log out, buy cars, and view order history.

## Features

### 1. User-Facing Features (35 Marks)

#### Navbar:
- Authenticated users will see options for Home, Profile, and Logout.
- Unauthenticated users will see options for Home, Signup, and Login.

#### Home Page:
- Display introductory text and an appealing image.
- List cars with their images, prices, and allow users to filter cars by brand.

#### Car Details Page:
- Display detailed information about a selected car, including image, name, description, quantity, price, and brand name.
- Authenticated users can see a "Buy Now" button to purchase the car.
- Allow users to comment on cars, providing their name and comment.

### 2. User Registration and Authentication (10 Marks)

- Implement a user registration and login system.
- Authenticated users can edit their profile details.

### 3. Placing Orders (20 Marks)

- Authenticated users can buy cars.
- Unauthorized users cannot see the "Buy Now" button.
- When an authenticated user clicks "Buy Now," the item is purchased, and the total quantity of that car is reduced by one.

### 4. Order History (15 Marks)

- In the profile page, users can view a list of bought cars.

### Notes

- Establish a relationship between Car Model and Brand Model. A brand can have multiple cars, but a car must have only one brand.
- Additional apps/models can be added if necessary.
- Utilize at least 3 class-based views for various functionalities.

## Project Structure

```plaintext
car_sales_website/
|-- car_listing/
|   |-- models.py
|   |-- views.py
|   |-- templates/
|       |-- home.html
|       |-- car_details.html
|-- user_authentication/
|   |-- models.py
|   |-- views.py
|   |-- templates/
|       |-- registration/
|           |-- signup.html
|       |-- login.html
|       |-- profile.html
|-- orders/
|   |-- models.py
|   |-- views.py
|   |-- templates/
|       |-- order_history.html
|-- manage.py
|-- requirements.txt
|-- README.md
