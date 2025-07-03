### 🧭 Trace Decorator

The `@trace` decorator provides powerful logging functionality to trace function execution in your FastAPI services. By simply adding the decorator to any function, you gain detailed visibility into **function start**, **end**, **input parameters**, **output result**, and execution **duration**—each uniquely tagged for clear traceability.

---

#### ✨ Features

- 🔍 Logs function **START** and **END** with execution time
- 📥 Logs **ARGS** (input) and 📤 **RESULT** (output)
- 🧩 Generates a unique `FuncID` for each decorated function
- 🧵 Supports **async** and **sync** functions
- 🪵 Works with structured logging and includes `RequestID` for full request tracing
- ⚙️ Fully customizable via configuration

---

#### 🧑‍💻 Usage

Import the decorator in your code:

```python
from app import trace
````

Decorate your functions:

```python
@trace(name="sample_function")
async def sample_function(self, temp_arg: str) -> str:
    """Convert input string to uppercase."""
    return temp_arg.upper()

@trace(name="create_user_service")
async def create_user_service(self, request_params: CreateUserRequest) -> Tuple[Any, str, int]:
    """Create a new user from request parameters."""
    await self.sample_function(temp_arg=request_params.name)

    payload = {
        "user_id": 1,
        "name": request_params.name,
        "email": request_params.email,
    }
    message = "User created successfully"
    status_code = 201
    return payload, message, status_code
```

---

#### 🪵 Example Output (Trace Logs)

```
2025-06-15 03:33:37.308 | TRACE | RequestID=8a29...ae5 | FuncID=5268...8624 | 🔍 [create_user_service] START
2025-06-15 03:33:37.309 | TRACE | RequestID=8a29...ae5 | FuncID=5268...8624 | 📥 [create_user_service] ARGS: {"request_params": "name='John Doe' email='johndoe@example.com'"}
2025-06-15 03:33:37.309 | TRACE | RequestID=8a29...ae5 | FuncID=ec33...e161 | 🔍 [sample_function] START
2025-06-15 03:33:37.309 | TRACE | RequestID=8a29...ae5 | FuncID=ec33...e161 | 📥 [sample_function] ARGS: {"temp_arg": "John Doe"}
2025-06-15 03:33:37.309 | TRACE | RequestID=8a29...ae5 | FuncID=ec33...e161 | 📤 [sample_function] RESULT: "JOHN DOE"
2025-06-15 03:33:37.309 | TRACE | RequestID=8a29...ae5 | FuncID=ec33...e161 | ✅ [sample_function] END (0.00s)
2025-06-15 03:33:37.310 | TRACE | RequestID=8a29...ae5 | FuncID=5268...8624 | 📤 [create_user_service] RESULT: [{"user_id": 1, "name": "John Doe", "email": "johndoe@example.com"}, "User created successfully", 201]
2025-06-15 03:33:37.310 | TRACE | RequestID=8a29...ae5 | FuncID=5268...8624 | ✅ [create_user_service] END (0.00s)
```

---

#### ⚠️ Configuration

Ensure **trace-level logs** are enabled in your app’s config file (`config.py`) or env file.

```env
LOG_LEVEL=TRACE
```

---

#### ✅ Tip

Even when multiple functions are nested and traced, each function retains its own `FuncID`, so their logs remain cleanly separated and trackable under the same `RequestID`.
