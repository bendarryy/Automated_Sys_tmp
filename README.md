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
