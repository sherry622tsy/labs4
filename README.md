## ✅ Lab 4 Flask API 

### 🧪 Test Suite: `test_app.py`

This test suite validates the CRUD operations of a simple Flask-based REST API for managing tasks.

---

### 📋 Summary

| Test Case              | Description                                   | Status   |
| ---------------------- | --------------------------------------------- | -------- |
| `test_get_all_tasks`   | Tests retrieving all tasks via `GET /tasks`   | Passed |
| `test_create_task`     | Tests creating a new task via `POST /tasks`   | Passed |
| `test_get_single_task` | Tests fetching a specific task by ID          | Passed |
| `test_update_task`     | Tests updating an existing task via `PUT`     | Passed |
| `test_delete_task`     | Tests deleting a task via `DELETE /tasks/:id` | Passed |

---

### 🔎 Detailed Results

####  `test_get_all_tasks`

* **Purpose**: Ensure that the `/tasks` endpoint returns a list of tasks.
* **Expected**: 200 OK, JSON with key `data` as a list.
* **Result**: Passed.

---

####  `test_create_task`

* **Purpose**: Test the creation of a task with `title` and `description`.
* **Expected**: 201 Created, JSON contains the created task.
* **Result**: Passed.

---

####  `test_get_single_task`

* **Purpose**: Validate fetching an existing task using `/tasks/<id>`.
* **Expected**: 200 OK, task with correct `id` returned.
* **Result**: Passed.

---

####  `test_update_task`

* **Purpose**: Update a task’s title and `done` status.
* **Expected**: 200 OK, JSON contains updated fields.
* **Result**: Passed.

---

#### ✅ `test_delete_task`

* **Purpose**: Delete an existing task by ID.
* **Expected**: 200 OK on delete, then 404 Not Found on subsequent GET.
* **Result**: Passed.

---

### ✅ Overall Status: `All 5 tests passed`

---

###  Notes

* All requests are tested via Flask’s `test_client()` in-memory.
* This test suite does not rely on external files or databases.
* Optional tests for error handling (e.g., missing `title`) can be added for robustness.

---

### Tools Used

* Language: Python 3.x
* Framework: Flask (development server)
* Testing: `unittest` (standard library)
