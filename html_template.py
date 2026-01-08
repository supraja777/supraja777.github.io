# html_template.py

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title>{{NAME}} | {{ROLE}}</title>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.95.3/css/materialize.min.css" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" />
    
    <style>
        body { background-color: #ffffff; color: #4f4f4f; font-family: "Roboto", sans-serif; }
        header, main, footer { padding-left: 300px; }
        @media only screen and (max-width : 992px) { header, main, footer { padding-left: 0; } }
        
        nav.side-nav.fixed { width: 300px; background-color: #fff; border-right: 1px solid #e0e0e0; box-shadow: none; }
        .side-nav .logo { margin-bottom: 30px; padding: 40px 20px; text-align: center; }
        .side-nav .logo img { width: 150px; border: 5px solid #009688; }
        
        section { padding-top: 50px; padding-bottom: 50px; }
        .page-title { color: #009688; font-weight: 300; text-transform: uppercase; letter-spacing: 4px; font-size: 2.5rem; }
        
        .skill-tag { 
            display: inline-block; padding: 5px 12px; margin: 4px; 
            background: #e0f2f1; color: #00796b; border-radius: 2px; font-weight: 500; 
        }
        .card { box-shadow: 0 2px 5px 0 rgba(0,0,0,0.16), 0 2px 10px 0 rgba(0,0,0,0.12); }
        .teal-text { color: #009688 !important; }
        .btn-floating.teal { background-color: #009688 !important; }
    </style>
</head>
<body>
    <header>
        <ul id="nav-mobile" class="side-nav fixed">
            <li class="logo">
                <img src="{{PROFILE_IMAGE}}" class="circle responsive-img">
                <h5 class="black-text" style="font-weight: 300;">{{NAME}}</h5>
            </li>
            <li class="bold"><a href="#intro" class="waves-effect waves-dark teal-text"><i class="fa fa-home"></i><span>Home</span></a></li>
            <li class="bold"><a href="#about" class="waves-effect waves-dark teal-text"><i class="fa fa-user"></i><span>About</span></a></li>
            <li class="bold"><a href="#experience" class="waves-effect waves-dark teal-text"><i class="fa fa-briefcase"></i><span>Experience</span></a></li>
            <li class="bold"><a href="#projects" class="waves-effect waves-dark teal-text"><i class="fa fa-code"></i><span>Projects</span></a></li>
            <li class="bold"><a href="#skills" class="waves-effect waves-dark teal-text"><i class="fa fa-wrench"></i><span>Skills</span></a></li>
            <li class="bold"><a href="#education" class="waves-effect waves-dark teal-text"><i class="fa fa-graduation-cap"></i><span>Education</span></a></li>
            <li class="bold"><a href="#contact" class="waves-effect waves-dark teal-text"><i class="fa fa-envelope"></i><span>Contact</span></a></li>
        </ul>
    </header>

    <main>
        <section id="intro" class="section scrollspy full-height" style="background: #263238; color: white; min-height: 100vh; display: flex; align-items: center;">
            <div class="container">
                <h2 style="font-weight: 900;">{{NAME}}</h2>
                <h5>I am a <span class="typing teal-text" style="font-weight: 400;"></span></h5>
                <p style="font-size: 1.2rem; color: #b0bec5; max-width: 600px;">{{INTRO_DESCRIPTION}}</p>
                <div style="margin-top: 30px;">{{SOCIAL_BUTTONS}}</div>
            </div>
        </section>

        <section id="about" class="container section scrollspy">
            <h3 class="page-title">About</h3>
            <div class="card"><div class="card-content">
                <div class="flow-text">{{ABOUT_TEXT}}</div>
                {{ABOUT_BULLETS}}
            </div></div>
        </section>

        <section id="experience" class="container section scrollspy">
            <h3 class="page-title">Experience</h3>
            {{EXPERIENCE_BLOCKS}}
        </section>

        <section id="projects" class="container section scrollspy">
            <h3 class="page-title">Projects</h3>
            <div class="row">{{PROJECT_CARDS}}</div>
        </section>

        <section id="education" class="container section scrollspy">
            <h3 class="page-title">Education</h3>
            {{EDUCATION_BLOCKS}}
        </section>
    </main>

    <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.95.3/js/materialize.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
    <script>
        $(document).ready(function(){
            $('.scrollspy').scrollSpy();
            new Typed('.typing', {
                strings: {{TYPING_STRINGS}},
                typeSpeed: 50, backSpeed: 30, loop: true
            });
        });
    </script>
</body>
</html>
"""