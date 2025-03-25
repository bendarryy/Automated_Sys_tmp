# Automated_Sys_tmp



## API_Documentation
#graduatoin


### Account Managment 

**POST** `/api/core/register/`

**Request Body:**

```json
	{
	"username":  "user80",
	"password": "password"   
	}
```
**Responses:**

- **201 Created**: User registered successfully.
- **400 Bad Request**: Errors with the registration data.

---

**POST** `/api/core/login/`

**Request Body:**

```json
	{
	"username":  "user80",
	"password": "password"   
	}
```

**Responses:**

- **200 OK**: Login successful.
- **400 Bad Request**: Errors related to credentials.

---

**GET** `/api/core/logout/`

**Responses:**

- **200 OK**:    Logged out successfully

---

**GET** `/admin/`

**Description:**  
This endpoint provides a custom admin panel for each user to manage their resources 

---

**POST** `/api/core/create-system/`

**Request Body:**
- *==Don't touch its Under Development==*   
```json
# Don't touch its Under Devolpment 
{
    "name": "new_systemmm",
    "category": "restaurant"
}
```

**Responses:**

- **201 Created**: System created successfully.
- **400 Bad Request**: Missing required fields.

---

## System 
 
- GET  ` /api/core/systems`   → List all systems


## Menu Items

- GET   ` /api/restaurant/{system_id}/menu-items/  `       → List all menu items
	- ` /api/restaurant/{system_id}/menu-items/?category=food ` → filter menu based on (food or dirnk or soups or dessert)
- POST    `/api/restaurant/{system_id}/menu-items/  `         → Create a new menu item
- GET     ` /api/restaurant/{system_id}/menu-items/{id}/`     → Retrieve a specific item
- PUT    ` /api/restaurant/{system_id}/menu-items/{id}/`     → Update an item
- PATCH  ` /api/restaurant/{system_id}/menu-items/{id}/`     → Partially update an item
- DELETE  ` /api/restaurant/{system_id}/menu-items/{id}/`     → Delete an item





