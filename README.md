# resturantAPI
# Little Lemon API

## Overview

The **Little Lemon API** provides endpoints for managing restaurant orders, menu items, user roles, and cart management. It allows different users (Managers, Delivery Crew, and Customers) to interact with the system in specific ways, making it suitable for web and mobile application integration. This project aims to provide all necessary backend functionality for Little Lemon restaurant operations.

## Features

- **Menu Items**: Managers can create, update, and delete menu items. Customers and Delivery Crew can view them.
- **Orders**: Customers can place orders, view their orders, and manage their cart. Managers can view and manage all orders. Delivery Crew can update the status of assigned orders.
- **User Roles**: Users are assigned to specific roles (Manager, Delivery Crew, Customer) to restrict access to specific functionalities.
- **Authentication**: JWT-based authentication using Djoser for user registration and login.
- **Error Handling**: Proper HTTP status codes for various errors (e.g., 401 Unauthorized, 404 Not Found, 400 Bad Request).
- **Pagination, Filtering, and Sorting**: Implemented for menu items and orders to handle large datasets.
- **Throttling**: Rate limiting is applied to authenticated and unauthenticated users.
