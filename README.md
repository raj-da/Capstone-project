# Recipe Management API: Endpoint Documentation

## **Endpoints Overview**
This document outlines the planned API endpoints for the Recipe Management API.

---

## **User Management Endpoints**

### **1. Register a New User**
**Endpoint:** `POST /users/register`

**Description:** Allows a new user to register.

**Request Parameters:**
- `username` (string, required): The username for the user.
- `password` (string, required): The password for the user.
- `email` (string, optional): Email address of the user.

**Sample Request:**
```json
{
  "username": "john_doe",
  "password": "password123",
  "email": "john.doe@example.com"
}
```

**Sample Response:**
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john.doe@example.com"
  }
}
```

---

### **2. Authenticate a User**
**Endpoint:** `POST /users/login`

**Description:** Authenticates a user and returns an authentication token.

**Request Parameters:**
- `username` (string, required): The username of the user.
- `password` (string, required): The password of the user.

**Sample Request:**
```json
{
  "username": "john_doe",
  "password": "password123"
}
```

**Sample Response:**
```json
{
  "token": "abcd1234xyz",
}
```

---

## **Recipe Management Endpoints**

### **1. Create a New Recipe**
**Endpoint:** `POST api/create/`

**Description:** Allows authenticated users to create a new recipe.

**Request Parameters:**
- `title` (string, required): The name of the recipe.
- `ingredients` (array of strings, required): A list of ingredients.
- `instructions` (string, required): The steps to prepare the recipe.
- `categories` 

**Sample Request:**
```json
{
  "title": "Spaghetti Carbonara",
  "ingredients": ["spaghetti", "eggs", "parmesan cheese", "bacon"],
  "instructions": "Boil spaghetti. Cook bacon. Mix eggs and cheese. Combine everything.",
  "categories": ["Italian", "Dinner"]
}
```

**Sample Response:**
```json
{
  "message": "Recipe created successfully",
  "recipe": {
    "id": 1,
    "title": "Spaghetti Carbonara",
    "ingredients": ["spaghetti", "eggs", "parmesan cheese", "bacon"],
    "instructions": "Boil spaghetti. Cook bacon. Mix eggs and cheese. Combine everything.",
    "categories": ["Italian", "Dinner"]
  }
}
```

---

### **2. Retrieve All Recipes**
**Endpoint:** `GET api/recipes/`

**Description:** Retrieves a list of all available recipes.

**Request Parameters:** None

**Sample Response:**
```json
[
  {
    "id": 1,
    "title": "Spaghetti Carbonara",
    "categories": ["Italian", "Dinner"]
  },
  {
    "id": 2,
    "title": "Chicken Curry",
    "categories": ["Indian", "Dinner"]
  }
]
```

---

### **3. Retrieve a Recipe by ID**
**Endpoint:** `GET api/recipes/<id>`

**Description:** Retrieves the details of a specific recipe by its ID.

**Path Parameter:**
- `<id>` (integer, required): The ID of the recipe.

**Sample Response:**
```json
{
  "id": 1,
  "title": "Spaghetti Carbonara",
  "ingredients": ["spaghetti", "eggs", "parmesan cheese", "bacon"],
  "instructions": "Boil spaghetti. Cook bacon. Mix eggs and cheese. Combine everything.",
  "categories": ["Italian", "Dinner"]
}
```

---

### **4. Update a Recipe by ID**
**Endpoint:** `PUT api/update/<id>`

**Description:** Updates an existing recipe by its ID.

**Path Parameter:**
- `<id>` (integer, required): The ID of the recipe.

**Request Parameters:**
- `title` (string, optional): Updated title for the recipe.
- `ingredients` (strings, optional): Updated list of ingredients.
- `instructions` (string, optional): Updated instructions.
- `categories`

**Sample Request:**
```json
{
  "title": "Spaghetti Carbonara Deluxe",
  "ingredients": ["spaghetti", "eggs", "parmesan cheese", "bacon", "cream"],
  "instructions": "Boil spaghetti. Cook bacon. Mix eggs, cheese, and cream. Combine everything.",
  "categories": ["Chinese"]
}
```

**Sample Response:**
```json
{
  "message": "Recipe updated successfully",
  "recipe": {
    "id": 1,
    "title": "Spaghetti Carbonara Deluxe",
    "ingredients": ["spaghetti", "eggs", "parmesan cheese", "bacon", "cream"],
    "instructions": "Boil spaghetti. Cook bacon. Mix eggs, cheese, and cream. Combine everything.",
    "categories": ["Chinese"]
  }
}
```

---

### **5. Delete a Recipe by ID**
**Endpoint:** `DELETE api/delete/<id>`

**Description:** Deletes a specific recipe by its ID.

**Path Parameter:**
- `<id>` (integer, required): The ID of the recipe.

**Sample Response:**
```json
{
  "message": "Recipe deleted successfully"
}
```

---

## **Filtered Viewing Endpoints**

### **1. Retrieve Recipes by Publisher**
**Endpoint:** `GET /api/filter/<pk>`

**Description:** Retrieves recipes filtered by a specific publisher.

**Path Parameter:**
- `<pk>` (intiger, required): The publisher id to filter recipes by.

**Sample Response:**
```json
[
  {
    "id": 1,
    "title": "Spaghetti Carbonara",
    "ingredients": ["spaghetti", "eggs", "parmesan cheese", "bacon"]
  }
]
```

---