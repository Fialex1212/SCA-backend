# **Spy Cat Agency (SCA) Backend API**

## Description

This backend API provides a management system for the Spy Cat Agency to manage their spy cats, missions, and targets efficiently. It supports CRUD operations on cats and missions, enforces business rules, and integrates with TheCatAPI for breed validation.

## **Features**

### Spy Cats

- Create a spy cat with:
  - Name
  - Years of Experience
  - Breed (validated via TheCatAPI)
  - Salary
- Update spy cat salary
- Delete spy cats
- List all spy cats
- Retrieve details of a single spy cat

### Missions and Targets

- Create missions along with 1 to 3 targets in a single request
- Assign a mission to a cat (one mission per cat at a time)
- Update targets by:
  - Adding/updating notes (only if target and mission are not completed)
  - Marking targets as completed (once all targets complete, mission is marked completed)
- Delete missions (only if not assigned to a cat)
- List all missions
- Retrieve a single mission's details

### Validations & Business Rules

- Breed validation via [TheCatAPI](https://api.thecatapi.com/v1/breeds)
- One cat can have only one mission at a time
- Each mission must have between 1 and 3 targets
- Completed targets' notes cannot be updated
- Mission is marked completed only when all its targets are completed
- Missions cannot be deleted if assigned to a cat

---

## Technology Stack

- Framework: FastAPI
- Database: PostgreSQL
- External Integration: TheCatAPI for breed validation

---

## Running the Project

1. **Clone the repository:**

```cmd
    git clone https://github.com/Fialex1212/react-fastapi-todo.git
```

2. **Build the image:**

```cmd
    docker build -t my-postgres .
```

3. **Run the container:**

```cmd
    docker run -d -p 5432:5432 --name my-postgres-container my-postgres
```

4. **Create and activate a virtual environment:**

```cmd
    python -m venv venv
    .\venv\scripts\activate
```

5. **Install dependencies:**

```cmd
    pip install -r requirements.txt
```

6. **Start the server:**

```cmd
    uvicorn app.main:app --port 8001
```


## **API Endpoints Summary**

### Spy Cats

| Method | Endpoint         | Description             |
|--------|------------------|-------------------------|
| POST   | /cats            | Create a new spy cat    |
| GET    | /cats            | List all spy cats       |
| GET    | /cats/{cat_id}   | Get single spy cat details |
| PATCH  | /cats/{cat_id}   | Update spy cat salary   |
| DELETE | /cats/{cat_id}   | Delete a spy cat        |

### Missions

| Method | Endpoint                     | Description                          |
|--------|------------------------------|------------------------------------|
| POST   | /missions                   | Create a mission with targets       |
| GET    | /missions                   | List all missions                   |
| GET    | /missions/{mission_id}      | Get details of a single mission    |
| PATCH  | /missions/{mission_id}      | Update mission targets (notes, complete) |
| DELETE | /missions/{mission_id}      | Delete a mission (if not assigned)  |
| POST   | /missions/{mission_id}/assign | Assign a cat to a mission         |



## Validation Notes

- Cat breed must be validated against TheCatAPI breed list before creation.
- Mission creation requires 1 to 3 targets.
- Target notes cannot be updated if the target or mission is completed.
- A cat cannot be assigned to more than one mission at a time.

## Contact

For questions or contributions, please contact:

- **Developer:** - [@Aleks Seriakov](https://github.com/Fialex1212) 
- **Email:** aleks.seriakov@gmail.com