# Portfolio
<!-- portfolio -->

{% extends 'base.html' %}
{% load static %}


{% block content %}
    

    
        <div class="infocontainer">
            <div class="devinfo">
               <div class="hello">Hi I am</div>
               <div class="name">S P Singh</div>
               <div class="about"> Web Developer</div>
               <div class="moreabout">I am a Software Devloper & I Love Coding.</div>
               <div class="buttons"><a href="sindhu pratap singh resume1.pdf">
                <button class="btn">Download CV</button></a>
                <a href="contact"><button class="btn">Contact Us</button></a>
               </div>
            </div>
            <div class="devpic"><img src="{% static 'img/sindhupng.png' %}" alt="S P Singh">>

            </div>

        </div>

      
        <div class="infocontainer">
            <dev class="info">
              <h1>About Me</h1>
              <p>Python Django developer-fresher looking for new opportunities.</p>
              <h3>My Skills</h3>
              <div class="skillcontainer">
                <div class="skillitem">PYTHON: <div class="skill eighty"></div></div>
                <div class="skillitem">DJANGO: <div class="skill ninety"></div></div>
                <div class="skillitem">HTML: <div class="skill seventy"></div></div>
                <div class="skillitem">CSS: <div class="skill fifty"></div></div>
                <div class="skillitem">JavaScript: <div class="skill fifty"></div></div>
                 
                    
              </div>

            </dev>
            <div class="devpic"><img src="{% static 'img/sindhupng.png' %}" alt="S P Singh">>

            </div>

        </div>

        <div class="contactform">
            <h2>Contact me for work/general Enquiries.</h2>
              <form method="post" action="#" id="contact" is_valid="is_valid" class="bv-form">
                {% csrf_token %}
                  <div class="mb-3">
                    <label for="clientemail" class="form-label">Name</label>
                    <input name="name" type="name" class="form-control" id="clientemail" aria-describedby="emailHelp">
                    <div id="emailHelp" class="form-text"></div>
                  </div>
                  <div class="mb-3">
                    <label for="clientemail" class="form-label">Email address</label>
                    <input type="email" name="email" class="form-control" id="clientemail" aria-describedby="emailHelp">
                    <div id="emailHelp" class="form-text">We'll never share your email & Phone with anyone else.</div>
                  </div>
                  <div class="mb-3">
                    <label for="clientphone" class="form-label">phone No.</label>
                    <input type="phone" name="phone" class="form-control" id="clientphone">
                  </div>
                  <div class="mb-3">
                    <label for="clientemail" class="form-label">Enquiry</label>
                    <input type="email" name="Enquiry" class="form-control" id="clientemail" aria-describedby="emailHelp">
                    <div id="emailHelp" class="form-text"></div>
                  </div>
                  <div class="mb-3" id="form-check">
                    <input type="checkbox" class="form-check-input" id="Isclient">
                    <label name="checkbox" class="form-check-label" for="Isclient">I want you to work on a project with me</label>
                  </div>
                  <!-- <div class="buttons">
  
                  </div> -->
                  <button type="submit" class="btn btn-sm">Submit</button>
                </form>
          </div>

          <div class="projectcontainer">
            <div class="card" style="width: 18rem;">
              <img src="{% static 'img/lms.png' %}" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">LMS Website</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-sm">Check Now</a>
              </div>
            </div>
  
  
            <div class="card" style="width: 18rem;">
              <img src="{% static 'img/todo.jpg' %}" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">TO DO</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-sm">Check Now</a>
              </div>
            </div>
  
            <div class="card" style="width: 18rem;">
              <img src="{% static 'img/ecom.avif' %}" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">E-com Website</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-sm">Check Now</a>
              </div>
            </div>
  
            <div class="card" style="width: 18rem;">
              <img src="{% static 'img/portfolio.jpg' %}" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">Portfolio</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-sm">Check Now</a>
              </div>
            </div>
  
             
  
          </div>
        {% endblock  %}
