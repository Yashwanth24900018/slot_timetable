# Ex03 Time Table
## Date:01-11-2025

## AIM
To write a html webpage page to display your slot timetable.

## ALGORITHM
### STEP 1
Create a Django-admin Interface.

### STEP 2
Create a static folder and inert HTML code.

### STEP 3
Create a simple table using ```<table>``` tag in html.

### STEP 4
Add header row using ```<th>``` tag.

### STEP 5
Add your timetable using ```<td>``` tag.

### STEP 6
Execute the program using runserver command.

## PROGRAM
````
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saveetha College Timetable</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #eaf3ff;
            margin: 0;
            padding: 0;
        }
        .header {
            text-align: center;
            background-color: white;
            padding: 15px;
        }
        .header img {
            width: 300px;
        }
        .header h2 {
            color: #004aad;
            margin: 5px 0;
        }
        .timetable {
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
            text-align: center;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .timetable th, .timetable td {
            border: 1px solid black;
            padding: 10px;
        }
        .timetable th {
            background-color: #FFD700; /* yellow */
        }
        .timetable td {
            background-color: #00FFFF; /* cyan */
        }
        .timetable caption {
            font-weight: bold;
            font-size: 18px;
            margin-bottom: 10px;
        }
        .subjects {
            width: 80%;
            margin: 30px auto;
            border-collapse: collapse;
            background-color: #fff;
        }
        .subjects th, .subjects td {
            border: 1px solid black;
            padding: 8px;
        }
        .subjects th {
            background-color: #f2f2f2;
        }
        .footer {
            text-align: center;
            padding: 15px;
            color: white;
            background-color: #004aad;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="header">
        <img src="{% static 'saveetha logo.png' %}" alt="College Logo"><br>
        <h2>Saveetha Engineering College</h2>
        <p>(Autonomous Institution Affiliated to Anna University)</p>
    </div>

    <table class="timetable">
        <caption>SLOT TIME TABLE - YASHWANTH ASV (212224230309)</caption>
        <tr>
            <th>Day/Time</th>
            <th>Monday</th>
            <th>Tuesday</th>
            <th>Wednesday</th>
            <th>Thursday</th>
            <th>Friday</th>
        </tr>
        <tr>
            <th>8-10</th>
            <td>FREE SLOT</td>
            <td>FREE SLOT</td>
            <td>FWAD</td>
            <td>PHY</td>
            <td>CHE</td>
        </tr>
        <tr>
            <th>10-12</th>
            <td>GER</td>
            <td>FREE SLOT</td>
            <td>FWAD</td>
            <td>FWAD</td>
            <td>PHY</td>
        </tr>
        <tr>
            <th>12-1</th>
            <td colspan="5"><b>LUNCH</b></td>
        </tr>
        <tr>
            <th>1-3</th>
            <td>FREE SLOT</td>
            <td>MAT</td>
            <td>MAT</td>
            <td>SS</td>
            <td>FREE SLOT</td>
        </tr>
        <tr>
            <th>3-5</th>
            <td>FREE SLOT</td>
            <td>GER</td>
            <td>CHE</td>
            <td>FWAD</td>
            <td>FREE SLOT</td>
        </tr>
    </table>

    <table class="subjects">
        <tr>
            <th>S. No.</th>
            <th>Subject Code</th>
            <th>Subject Name</th>
        </tr>
        <tr>
            <td>1</td>
            <td>19AI414</td>
            <td>Fundamentals of Web Application Development (FWAD)</td>
        </tr>
        <tr>
            <td>2</td>
            <td>19EN612</td>
            <td>German Basic (GER)</td>
        </tr>
        <tr>
            <td>3</td>
            <td>19PH206</td>
            <td>Physics for Information Technology (PHY)</td>
        </tr>
        <tr>
            <td>4</td>
            <td>19CY205</td>
            <td>Principles of Chemistry in Engineering (CHE)</td>
        </tr>
        <tr>
            <td>5</td>
            <td>19MA201</td>
            <td>Calculus and Matrix Algebra (MAT)</td>
        </tr>
        <tr>
            <td>6</td>
            <td>19EY701</td>
            <td>Soft Skills (SS)</td>
        </tr>
    </table>

    <div class="footer">
        © 2025 Saveetha Engineering College | All Rights Reserved
    </div>
</body>
</html>

````


## OUTPUT

<img width="1912" height="965" alt="Screenshot 2025-11-01 124635" src="https://github.com/user-attachments/assets/814556c3-a7a5-41dd-96a2-cd0385a80e15" />


## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
