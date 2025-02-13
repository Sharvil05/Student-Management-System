<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Record Management</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
        .form-container {
            margin-bottom: 20px;
        }
        input {
            padding: 8px;
            margin: 5px;
        }
        button {
            padding: 8px 12px;
            background-color: green;
            color: white;
            border: none;
            cursor: pointer;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
        }
        th {
            background-color: #f4f4f4;
        }
        .delete-btn {
            background-color: red;
            color: white;
            border: none;
            padding: 5px 10px;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <h1>Student Record Management System</h1>

    <!-- Student Form -->
    <div class="form-container">
        <input type="text" id="name" placeholder="Enter Student Name">
        <input type="text" id="age" placeholder="Enter Age">
        <input type="text" id="grade" placeholder="Enter Grade">
        <button onclick="addStudent()">Add Student</button>
    </div>

    <!-- Student Table -->
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Age</th>
                <th>Grade</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody id="studentTableBody">
            <!-- Data will be loaded here from script.js -->
        </tbody>
    </table>

    <script>
        const API_URL = "http://127.0.0.1:5000/students"; // Flask backend URL

        // Fetch and display students
        async function fetchStudents() {
            const response = await fetch(API_URL);
            const students = await response.json();

            const tableBody = document.getElementById("studentTableBody");
            tableBody.innerHTML = "";

            students.forEach(student => {
                const row = `<tr>
                    <td>${student.id}</td>
                    <td>${student.name}</td>
                    <td>${student.age}</td>
                    <td>${student.grade}</td>
                    <td>
                        <button class="delete-btn" onclick="deleteStudent(${student.id})">Delete</button>
                    </td>
                </tr>`;
                tableBody.innerHTML += row;
            });
        }

        // Add a new student
        async function addStudent() {
            const name = document.getElementById("name").value;
            const age = document.getElementById("age").value;
            const grade = document.getElementById("grade").value;

            const response = await fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name, age, grade })
            });

            if (response.ok) {
                fetchStudents(); // Refresh data
            }
        }

        // Delete a student
        async function deleteStudent(id) {
            await fetch(`${API_URL}/${id}`, { method: "DELETE" });
            fetchStudents();
        }

        // Load students on page load
        window.onload = fetchStudents;
    </script>

</body>
</html>
