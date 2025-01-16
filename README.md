# Airbnb Clone - The Console

## Project Description

The goal of this project is to create a command-line interface (CLI) to manage objects for a clone of Airbnb. This command interpreter will allow users to manage a variety of objects, such as Users, States, Cities, Places, etc. The project will help you understand object serialization and deserialization, file management, object-oriented programming (OOP), and Python’s `cmd` module to implement a functional command interpreter.

The first step of building the AirBnB clone involves writing the console to manage your objects. The project is divided into multiple phases, each building upon the previous one to eventually create a full web application, including HTML/CSS templating, database storage, and API integration.

---

## Command Interpreter Description

This command interpreter will simulate a basic shell interface where the user can interact with the system by typing commands. It is implemented using Python’s `cmd` module, and each command will perform an operation on the AirBnB objects.

### Features of the Command Interpreter:
- **Create**: Add new objects like `User`, `State`, `City`, and `Place`.
- **Retrieve**: Get information about existing objects.
- **Update**: Modify attributes of objects.
- **Delete**: Remove objects.
- **Count**: Count the number of objects of a particular type.
- **Stats**: Perform operations on objects like calculating statistics.
  
---

## How to Start the Command Interpreter

1. **Clone the repository**:
    ```bash
    git clone https://github.com/alu-AirBnB_clone.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd alu-AirBnB_clone
    ```

3. **Run the interpreter**:
    ```bash
    ./console.py
    ```

Once the command interpreter is running, you will see the `(hbnb)` prompt, indicating that the interpreter is ready for commands.

---

## How to Use the Command Interpreter

Once you are inside the interpreter, you can use the following commands to manage objects:

- **Create a new object**:
    ```bash
    (hbnb) create User
    ```

- **Show an object**:
    ```bash
    (hbnb) show User <object_id>
    ```

- **Update an object**:
    ```bash
    (hbnb) update User <object_id> name "New Name"
    ```

- **Delete an object**:
    ```bash
    (hbnb) destroy User <object_id>
    ```

- **Count the number of objects of a type**:
    ```bash
    (hbnb) count User
    ```

- **Quit the interpreter**:
    ```bash
    (hbnb) quit
    ```

---

## Examples

### Example 1: Create a New User
```
(hbnb) create User
ebfe1f3d-303f-496d-a65f-99491a91fe61
```

### Example 2: Show a User
```
(hbnb) show User ebfe1f3d-303f-496d-a65f-99491a91fe61
User: [ebfe1f3d-303f-496d-a65f-99491a91fe61] {name: "John Doe", email: "johndoe@example.com"}
```

### Example 3: Update a User
```
(hbnb) update User ebfe1f3d-303f-496d-a65f-99491a91fe61 name "Jane Doe"
```

### Example 4: Count Users
```
(hbnb) count User
2
```

### Example 5: Quit the Interpreter
```
(hbnb) quit
$
```

---

## Authors

- **Admire Chagaresango** – *Lead Developer*
- **Maxwel Okoth** – *Co-developer*

---

## Additional Resources

For more details on the tools and concepts used in this project, refer to the following resources:
- [Python `cmd` module documentation](https://docs.python.org/3/library/cmd.html)
- [UUID module documentation](https://docs.python.org/3/library/uuid.html)
- [unittest module documentation](https://docs.python.org/3/library/unittest.html)
