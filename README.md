Design and Developed by Mauricio Aragon Ramos

UCD Full Stack Development Course
Python Module - Final Assessment

>>Github Repository (link to page)
https://github.com/aragon023/Python-Module-Final-Assesment.git

>>Deployment in Render (link to page)
https://python-module-final-assesment.onrender.com

Planning Analysis Sheet

Website Goal
Goals: 
Showcase My Work
Demonstrate my professional experience and skills
Present past projects, designs, articles, tools, and case studies.

Establish Credibility & Personal Brand
Communicate who I am, what I do, and what makes my work unique.
Build trust through client stories, certifications, and recognitions.
Use blog posts, tools, or writing to demonstrate thought leadership.

Attract Opportunities
Generate freelance inquiries, collaborations, speaking gigs, etc.


Website Page Structure and Information:
Website and project requirements:
- General information and structure
- Description of each page, sections and elements.
- Final text per page
- Responsive planning and analysis
- Technology and Resources

General information and structure:

This project is built primarily with Python using the Flask framework to handle the backend logic, routing, and integration with the database. 
Python is used to manage both the server-side application and data handling, making the site dynamic and interactive.

Framework: Flask project (app.py as the entry point, templates/ folder for Jinja2 HTML templates, and static/ for CSS/JS/images).
Flask powers the project’s backend. It is used to define routes (@app.route) that serve each page (e.g., Home, About, Projects, Articles, Tools, and Contact). 
Through Flask's templating system (Jinja2), Python dynamically renders HTML templates, allowing content such as articles and featured sections to be fetched from the database and displayed on the site. 
This ensures that updates or new content are automatically reflected on the website without modifying static HTML files.

Pages/Templates:
index.html (likely homepage)
about.html
articles.html + article_detail.html
projects.html
contact.html
tools.html

Styling:
CSS is modular (per-page CSS files + main.css and responsive.css).

Assets:
Dedicated folders for images (about, home, projects, etc.), videos, and icons.

Javascript:
Page-specific scripts (e.g., about.js, articles.js, tools.js) indicate interactive components.

Database: 
This project uses SQL lite as the database engine and SQLAlchemy as the Object Relational Mapper. 
Python integrates SQLAlchemy to manage the SQLite database used for storing articles and comments. Python classes define models like Article and Comment, which represent database tables. These models are queried directly within Python routes (e.g., Article.query.all()), demonstrating Python’s application in object-relational mapping (ORM). This allows for easy data retrieval, creation, and updates. 
    
    SQLite:
    The database file is stored locally at instance/site.db.

    SQLAlchemy:
    Manages table creation, queries, and relationships in a Pythonic way.
    Integrated with Flask using Flask-SQLAlchemy.

    How it's used in this project:
    Articles:
    Python script populate_articles.py is used to seed initial article data into the database
    Articles.py is used to dynamically display articles on the Articles page and Featured Articles section on the homepage.
    Includes fields like title, slug, tag, summary, image, author, published_on, and content.

    Comments:
    Implemented via a Comment model related to Article. 
    When a user submits a comment form, Flask captures the data via a POST request, validates it in Python, and saves it into the database.
    Allows users to post comments on individual articles.

    ORM Features Used:
    Table creation using db.create_all().


Description of each page, sections and elements.
1. Homepage (index.html)
1.1 Navigation Bar
Elements:
Logo (clickable, returns to homepage)
Nav links: About, Articles, Projects, Tools
CTA button: "Get in touch"
Hamburger menu for mobile
Goal: Easy access to key sections and pages; ensure responsiveness.

1.2 Intro Section
Headline: Innovation + Business + Technology
Description: A welcome message that explains the purpose of the site and what users can find here.
Image: 3D figure with chart, symbolising strategy and insight.
Goal: Establish context and set tone for visitors.

1.3 Logo Carousel
Contents: Logos of technologies/tools used (e.g., HTML, JavaScript, Adobe suite, HubSpot, Asana).
Goal: Show technical fluency and tool familiarity in a dynamic, visual way.

1.3. About Section (Home Preview)
Title: About Me
Text Summary:
Multidisciplinary background in design, tech, marketing, and customer success.
Currently working at HubSpot; experience spans teaching, consulting, and creative work.
Site as a space for sharing frameworks, tools, reflections, and case studies.
CTA: “Know More” button linking to full About page.
Goal: Build credibility, humanise the brand, and communicate your unique skillset.

1.4. Articles Section
Title: Featured Articles
Text Summary:
Content focuses on trends at the intersection of innovation, design, tech, and strategy.
Dynamic Grid: Use Python to create a dynamic gallery from Articles.html. 
Goal: Thought leadership; attract recurring visitors and demonstrate expertise.

1.5. Projects Section
Title: Projects
Text Summary: Showcase of creative, strategic, and design projects.
Project Cards: Each with:
Image
Title + Tag (e.g., Product Design, Graphic Design)
Rich description of context, tools, results
CTA: “View Project” (links to Behance)
Goal: Demonstrate skills, problem-solving, and design thinking with tangible examples.

1.6 Tools Section
Title: Ready to Start Innovating?
Text Summary: Brief invitation to explore practical tools and frameworks.
Image: Toolkit photo
CTA: “Explore” linking to tools.html
Goal: Encourage interaction, offer value, and reinforce practical expertise.

1.7. Footer Section
Contents:
Logo (clickable)
Quick nav links
Contact email: contact@holisk.com
Copyright
Goal: Close the page with essential contact info and secondary navigation.

Structure 

├── css/
│   ├── main.css
│   ├── index.css
│   ├── responsive.css
│   ├── about.css
│   ├── articles.css
│   ├── contact.css
│   ├── projects.css
│   ├── tools.css
│   └── individual_articles.css
├── images/
│   ├── home/
│   ├── projects/
│   ├── social_media_icons/
│   ├── tools/
│   └── about/
├── javascript/
│   ├── navigation.js
│   ├── articles.js
│   ├── about.js
│   ├── contact.js
│   ├── carousel.js
│   └── tools.js
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── articles.html
│   ├── article_detail.html
│   ├── projects.html
│   ├── tools.html
│   └── contact.html
├── instance/
│   └── site.db
├── videos/
├── _pycache_/
├── venv/
├── app.py
├── articles_data.py
├── populate_articles.py
├── project_data.py
├── README.md
└── requirements.txt


Responsive Design Analysis
To ensure optimal user experience across devices, the website follows a mobile-first, responsive design approach. Layouts and components dynamically adapt based on screen size and device capabilities. The site is designed with three primary responsive breakpoints:

1. Standard Tablet and Small Desktop (Max Width: ≤960px)
Use Case: Small laptops, tablets in landscape mode, and large mobile devices.
Key Adjustments:
- Grid layouts (e.g., projects and articles) reduce column count or switch to stacked formats.
- The navigation menu displays as an inline horizontal layout with a CTA button aligned to the right. 
- Font sizes scale down slightly for improved readability without overwhelming screen real estate.
- Image sizes and aspect ratios are preserved but scaled to fit the container width.
- Margins and padding adjust for better spacing on narrower viewports.

2. Mobile Devices (Max Width: ≤760px)
Use Case: Smartphones in portrait mode and smaller tablets.
Key Adjustments:
- The navigation menu displays switches from an inline horizontal layout to a collapsible hamburger menu.
- Full stacking of content sections for a vertical scroll experience for both projects and articles.
- Text is optimised for readability: larger line height, balanced font sizing.
- Interactive elements (buttons, links) maintain touch-friendly size and spacing.
- The intro section image moves below or above the text content, depending on the UX flow.


3. Ultra-Thin Screens (Max Width: ≤ 360px)
Use Case: Older smartphones, compact wearable browsers, and mini display windows.
Key Adjustments:
- All layout elements are stacked vertically with reduced padding and margin.
- Fonts scale for legibility while conserving space (e.g., headings drop one level).
- Navigation prioritises icon-based buttons, keeping the collapsible hamburger menu.
- Images may be hidden, replaced with icons, or resized to avoid horizontal scrolling.
- Containers use 100vw and 100% width to eliminate overflow or clipping.

Additional Notes
- Media queries are used to adjust layout styles at each breakpoint:@media (max-width: 860px), 600px, 400px).
- Flexbox and CSS Grid are leveraged to create fluid layouts that respond to changes in screen dimensions.
- Image assets use the loading = "lazy" attribute and max-width: 100% for performance and fluid scaling.
- Design is tested on both physical devices and emulators to ensure fidelity across operating systems and browsers.

Technology and Resources
Technology:
- Flask, Python, HTML5, CSS3, JavaScript 
- Google Fonts and Icons
- Responsive media queries
- Render for Deployment

Resources:
List of sources (facts, text, graphics, sound, video) you will use in the pages above
Additional sources - Text has been described in the section above. 


AI Image generation:
 www.firefly.adobe.com

Videos: Royalty Free Videos
https://pixabay.com/videos/

Images: Royalty Free Photos
https://pixabay.com/photos/

Image retouching and wireframes: 
Adobe Photoshop and Uizard.io

Metatags:
https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Webpage_metadata

Accessibility:
Overall:
https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML






 
