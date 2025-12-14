
---

# 🍰 Bakeroz — Full-Stack Bakery Web Application

Bakeroz is a **full-stack bakery web application** designed to provide a seamless online experience for customers to browse bakery products, search items, manage carts, place orders, make payments, and manage their accounts.

This project was built primarily as a **learning-driven full-stack application**, focusing on backend architecture, authentication, database design, and UI workflows. While the project is currently **archived**, it is **planned to be completed and enhanced in the future** with advanced features and scalability improvements.

---

## 📌 Project Status

**Status:** ⏸️ Archived (Planned for Future Completion)

**Reason:**
The project was paused strategically to focus on:

* Learning the **MERN stack**
* Strengthening **Data Structures & Algorithms (DSA)** for placement preparation

All major architectural decisions, schemas, and workflows have been designed and documented to allow smooth continuation in the future.

---

## 🎯 Project Goals

* Build a **real-world e-commerce style application**
* Implement secure **authentication & authorization**
* Design a **scalable relational database schema**
* Practice **session management**
* Implement **search, cart, orders, and payment workflows**
* Create a **clean, bakery-themed UI**

---

## 🖥️ Application Overview

Bakeroz consists of the following major modules:

* Public Landing Page
* Authentication (Signup / Login / Verification)
* Home Page with Search & Products
* Cart Management
* Order & Payment System
* User Account Dashboard
* Reviews & Ratings
* Admin-ready backend structure

---

## 🎨 UI / Frontend Design

The UI follows a **warm bakery theme**, using soft pastel colors, chocolate brown accents, and elegant fonts.

### 1️⃣ Landing Page (Before Login)

**Purpose:** First impression & brand identity

**UI Elements:**

* Sticky navigation bar
* Logo & brand name (Bakeroz)
* Search bar with animated placeholder:

  * “Search for cakes…”
  * “Search for muffins…”
  * “Search for cookies…”
* Navigation items:

  * Home
  * Products
  * Login / Signup
* Hero section with bakery imagery
* “Order Now” CTA button
* Footer with contact & links

---

### 2️⃣ Authentication Pages

#### Signup Page

* Name
* Email
* Password
* Confirm Password
* Email verification flow using OTP

#### Login Page

* Email
* Password
* Error handling for invalid credentials

#### Email Verification Page

* OTP input
* Backend verification before account activation

---

### 3️⃣ Home Page (After Login)

**Purpose:** Central hub for users

**UI Elements:**

* Navbar with:

  * Home
  * Search bar
  * Cart icon
  * User profile icon
* Product listings
* Category filters
* Search results
* Featured items
* Popular products

---

### 4️⃣ Search System

* Keyword-based search
* Backend query filtering
* Dynamic placeholder animation
* Planned enhancements:

  * Category-based filtering
  * Price range filter
  * Sorting (popularity, price)

---

### 5️⃣ Cart Page

**Purpose:** Manage selected products

**Features:**

* Add items to cart
* Update quantities
* Remove items
* Cart total calculation
* Persistent cart (session-based or DB-based)

---

### 6️⃣ Order & Checkout Page

**Flow:**

1. Cart → Checkout
2. Address confirmation
3. Payment selection
4. Order confirmation

---

### 7️⃣ User Account Page

**Features:**

* Display user details:

  * Name
  * Email
  * Account status
* View past orders
* Delete account option
* Logout functionality

---

## ⚙️ Backend Architecture

The backend is built using **Flask**, following modular design principles.

### Backend Responsibilities:

* Authentication & authorization
* Session management
* Database interactions
* Email verification
* Business logic handling

---

### 🔐 Authentication & Sessions

* Email + password authentication
* Session-based login
* OTP verification using email
* Secure session storage using Flask sessions
* Password hashing (planned improvement)

---

### 📧 Email Verification System

* Random OTP generation
* SMTP-based email delivery
* OTP stored temporarily in session
* Account marked verified upon correct OTP

---

## 🧱 Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Responsive design
* SVG icons

### Backend

* Python
* Flask
* Flask Sessions
* SMTP (Email verification)

### Database

* MySQL
* Relational schema
* Foreign key constraints

### Tools & Utilities

* dotenv (environment variables)
* mysql-connector
* Git & GitHub

---

## 🗄️ Database Schema Design

The database is designed to be **scalable and normalized**.

---

### 🧑‍💻 `user` Table

| Column Name       | Type      | Description               |
| ----------------- | --------- | ------------------------- |
| id                | INT (PK)  | User ID                   |
| name              | VARCHAR   | User name                 |
| email             | VARCHAR   | Unique email              |
| password_hash     | VARCHAR   | Password                  |
| user_role         | VARCHAR   | customer / admin          |
| is_verified       | BOOLEAN   | Email verification status |
| verification_code | VARCHAR   | OTP                       |
| created_at        | TIMESTAMP | Account creation time     |

---

### 🛒 `products` Table

| Column Name | Type      | Description         |
| ----------- | --------- | ------------------- |
| id          | INT (PK)  | Product ID          |
| name        | VARCHAR   | Product name        |
| description | TEXT      | Product description |
| price       | DECIMAL   | Price               |
| image_url   | VARCHAR   | Product image       |
| stock       | INT       | Available quantity  |
| category    | VARCHAR   | Category            |
| created_at  | TIMESTAMP | Added date          |

---

### 🧺 `cart` Table

| Column Name | Type      | Description  |
| ----------- | --------- | ------------ |
| id          | INT (PK)  | Cart ID      |
| user_id     | INT (FK)  | User         |
| created_at  | TIMESTAMP | Created time |

---

### 🧾 `cart_items` Table

| Column Name | Type     | Description |
| ----------- | -------- | ----------- |
| id          | INT (PK) | Item ID     |
| cart_id     | INT (FK) | Cart        |
| product_id  | INT (FK) | Product     |
| quantity    | INT      | Quantity    |

---

### 📦 `orders` Table

| Column Name  | Type      | Description         |
| ------------ | --------- | ------------------- |
| id           | INT (PK)  | Order ID            |
| user_id      | INT (FK)  | User                |
| total_amount | DECIMAL   | Total               |
| status       | VARCHAR   | Pending / Completed |
| created_at   | TIMESTAMP | Order time          |

---

### 📄 `order_items` Table

| Column Name | Type     | Description |
| ----------- | -------- | ----------- |
| id          | INT (PK) | Order item  |
| order_id    | INT (FK) | Order       |
| product_id  | INT (FK) | Product     |
| quantity    | INT      | Quantity    |
| price       | DECIMAL  | Price       |

---

### 💳 `payments` Table

| Column Name | Type      | Description      |
| ----------- | --------- | ---------------- |
| id          | INT (PK)  | Payment ID       |
| order_id    | INT (FK)  | Order            |
| amount      | DECIMAL   | Paid amount      |
| method      | VARCHAR   | Payment method   |
| status      | VARCHAR   | Success / Failed |
| created_at  | TIMESTAMP | Payment time     |

---

### ⭐ `reviews` Table

| Column Name | Type      | Description |
| ----------- | --------- | ----------- |
| id          | INT (PK)  | Review ID   |
| user_id     | INT (FK)  | User        |
| product_id  | INT (FK)  | Product     |
| rating      | INT       | Rating      |
| comment     | TEXT      | Review      |
| created_at  | TIMESTAMP | Date        |

---

## 🔄 Application Workflow

1. User visits landing page
2. Signs up → receives OTP
3. Verifies email
4. Logs in
5. Browses products
6. Searches items
7. Adds items to cart
8. Places order
9. Makes payment
10. Views order history
11. Manages account

---

## 🚀 Future Enhancements

* MERN stack migration
* JWT-based authentication
* Payment gateway integration
* Admin dashboard
* Product recommendations
* Image uploads
* Pagination & caching
* Improved UI animations

---

## 🧠 Key Learnings

* Flask app structuring
* Database schema design
* Session handling
* Authentication flows
* Debugging real backend issues
* End-to-end feature planning

---

## 👤 Author

**Rakshit Bagait**
Aspiring Full-Stack Developer
Focused on Backend, MERN Stack & DSA

---

## 📜 License

This project is for **educational and learning purposes**.

---

If you want next, I can:

* Convert this into a **resume project description**
* Rewrite this README for **MERN version**
* Help you plan **next project cleanly**

Just tell me 👍
