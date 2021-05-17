<!DOCTYPE html>
{
load static %}

<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Event Management System</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
  <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"> -->

  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Roboto+Mono:400,500,700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Open+Sans&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Muli:500&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="{% static 'css/index.css' %}">
</head>

<body class="bg-success">
<div class="container-fluid header text-center bg-primary">
  <h1 style="color: white;">CHMSC Events Management System</h1>
  <h3 style="color: white;"> Welcome {{ name }} </h3>
  <a href="{% url 'scmapp:user_logout' %}" style="font-size:20; color: white;">Logout</a><br>
  <span style="font-size:18px">{{ status }}</span>
</div>

<div class="container">
  <div class="row">
    <div class="col-lg-6">
      <a href="{% url 'scmapp:user_event' %}">
      <div class="card bg-danger">
        <img src="{% static 'res/event.jpeg' %}" class="card bg-danger">
        <img src="{% static 'res/event.jpeg' %}">
        <div class="card-title text-center" style="color: white;">Events</div>
      </div>
      </a>
    </div>
<div class="col-lg-6">
      <a href="{% url 'scmapp:ground_booking' %}">
      <div class="card bg-danger">
        <img src="{% static 'res/volley.jpg' %}" style="height:312px;">
        <div class="card-title text-center" style="color: white;">Events Booking</div>
      </div>
      </a>
    </div>

  </div>
</div>

<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
<!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script> -->

</body>
</html>
CTYPE html>
{% load static %}
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Registration| Welcome</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
  <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"> -->

  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Roboto+Mono:400,500,700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Open+Sans&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Muli:500&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="{% static "css/registration.css" %}">
  <script type="text/javascript" src="{% static "js/main.js" %}"></script>
</head>
<body class="bg-success">

<div class="container-fluid header text-center bg-primary">
  <h1 style="color: white;">CHMSC Events Management System</h1>
</div>

<div class="container-fluid">
  <div class="row justify-content-center">
    <div class="col-0 btn-bar" onclick="navigation(event)">
      <a href="#" class="myactive" id="registration">Registration</a>
      <a href="#" class="" id="login">Login</a>
    </div>
  </div>
</div>

<div class="container-fluid">
  <div class="row justify-content-center">
    <div class="col-lg-6 box bg-danger" style="display:block;">
      <!-- <span style="font-size:26px;">Registration</span> -->
      <center><h1 class="bg-primary" style="color: white; margin-right: 30px;"> Registration</h1></center>
      <span style="font-size:18px;">{{ status }}</span>

      <div class="row justify-content-center">
        <div class="col-lg-6">
          <div class="inputbox">
            <form action="{% url 'scmapp:test' %}" method="post">
              {% csrf_token %}
              Username<br>
              <input type="text" name="uname" autocomplete="off" required><br>

              E-Mail<br>
              <input type="text" name="email" autocomplete="off" required><br>

              Gender<br>
              <input type="radio" name="gender" value="Male"> Male
              <input type="radio" name="gender" value="Female"> Female<br>

              Password<br>
              <input type="password" name="password" minlength="8" autocomplete="off" required><br>

              Re-enter Password<br>
              <input type="password" name="repassword" minlength="8" autocomplete="off" required>

              <input type="submit" value="Submit" name="submit" style="margin:0 25% 0 25%;">
            </form>
          </div>
        </div>
    </div>
    <a href="#" onclick="navigation(event)" id="loginLink" style="color: white;">Already registered? Login</a>

    </div>
  </div>
</div>

<div class="container-fluid">
  <div class="row justify-content-center">
    <div class="col-lg-6 loginBox bg-danger" style="display:none;">
      <center><h1 class="bg-primary" style="color: white; margin-right: 30px;">Login</h1></center>

      <div class="row justify-content-center">
        <div class="col-lg-6">
          <div class="inputBox" style="font-size:18px;">
            <form action="{% url 'scmapp:login_user' %}" method="post">
              {% csrf_token %}
              Username<br>
              <input type="text" name="name" autocomplete="off" required><br>

              Password<br>
              <input type="password" name="password" minlength="8" autocomplete="off" required>

              <input type="submit" value="Login" name="login" style="margin:0 25% 0 25%;">
            </form>
          </div>
        </div>
      </div>
      <a href="#" onclick="navigation(event)" id="regLink" style="color: white;">Not a registered user? Register</a>

    </div>
  </div>
</div>

<script src="https://code.jquery.coCTYPE html>
{% load static %}

<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>CHMSC Events</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
  <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"> -->

  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Roboto+Mono:400,500,700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Open+Sans&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Muli:500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{% static 'css/admin_event.css' %}">
</head>
<body class="bg-primary">
<div class="container-fluid header text-center bg-success">
 <h2 style="color: white;">CHMSC Events</h2>
</div>

<div class="container box bg-success">
  <h2 class="bg-danger" style="color: white;">Event Details</h2>

  <table>
    <tr class="bg-danger" style="color: white;">
      <td>No</td>
      <td>Event name</td>
      <td>Date</td>
      <td>Time</td>
      <td>Duration(hours)</td>
    </tr>

    {% for e in event %}
      <tr>
        <td>{{ forloop.counter }}</td>
        <td>{{ e.name}}</td>
        <td>{{ e.date }}</td>
        <td>{{ e.time }}</td>
        <td>{{ e.duration }}</td>
      </tr>
    {% empty %}
      <tr>
        <td colspan="5" align="center">No events</td>
      </tr>
    {% endfor %}

  </table>

  <div class="footer">
    <a href="{% url 'scmapp:user_home' %}"><button>Back</button></a>
  </div>

</div>

<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
<!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script> -->

</body>
</html>

