import os

# List of mentors (2023 and 2024)
mentors_2023 = [
    {"name": "Aya", "bio": "Aya is a dedicated mentor with expertise in [Field]. She has been guiding young scientists since [Year] and has played a key role in [Specific Achievements]."},
    {"name": "Asal", "bio": "Asal is a passionate mentor specializing in [Field]. She has mentored numerous young scientists and contributed to [Specific Achievements]."},
    {"name": "Ayman Radhwan", "bio": "Ayman Radhwan is an experienced mentor with a focus on [Field]. He has been instrumental in [Specific Achievements]."},
    {"name": "Safi Nas", "bio": "Safi Nas is a skilled mentor with expertise in [Field]. He has guided many young scientists to success in [Specific Achievements]."},
    {"name": "Rawan Ihsan", "bio": "Rawan Ihsan is a dedicated mentor with a passion for [Field]. She has been mentoring since [Year] and has contributed to [Specific Achievements]."},
    {"name": "Enes Ercan Enwar Hurmuzlu", "bio": "Enes Ercan Enwar Hurmuzlu is a knowledgeable mentor with expertise in [Field]. He has been guiding young scientists since [Year]."},
    {"name": "Abdullah Hadi", "bio": "Abdullah Hadi is a committed mentor with a focus on [Field]. He has played a key role in [Specific Achievements]."},
]

mentors_2024 = [
    {"name": "Sami Said", "bio": "Sami Said is a dedicated mentor with expertise in [Field]. He has been guiding young scientists since [Year] and has contributed to [Specific Achievements]."},
    {"name": "Haneen Abdulqader", "bio": "Haneen Abdulqader is a passionate mentor specializing in [Field]. She has mentored numerous young scientists and contributed to [Specific Achievements]."},
    {"name": "Zaid Hamed Saqban", "bio": "Zaid Hamed Saqban is an experienced mentor with a focus on [Field]. He has been instrumental in [Specific Achievements]."},
    {"name": "Faisal Basil", "bio": "Faisal Basil is a skilled mentor with expertise in [Field]. He has guided many young scientists to success in [Specific Achievements]."},
    {"name": "Aya Salam", "bio": "Aya Salam is a dedicated mentor with a passion for [Field]. She has been mentoring since [Year] and has contributed to [Specific Achievements]."},
    {"name": "Malak", "bio": "Malak is a knowledgeable mentor with expertise in [Field]. She has been guiding young scientists since [Year]."},
    {"name": "Hasnaa", "bio": "Hasnaa is a committed mentor with a focus on [Field]. She has played a key role in [Specific Achievements]."},
]

# HTML template for mentor pages
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Iraq Youth Scientist Team</title>
    <link rel="stylesheet" href="../css/styles.css">
</head>
<body>
    <header>
        <div class="logo">
            <img src="../images/logo.png" alt="Iraq Youth Scientist Team Logo">
        </div>
        <nav>
            <ul>
                <li><a href="../index.html">Home</a></li>
                <li><a href="../about.html">About Us</a></li>
                <li><a href="../programs.html">Programs</a></li>
                <li><a href="../news.html">News</a></li>
                <li><a href="../contact.html">Contact Us</a></li>
                <li><a href="../mentors.html">Mentors</a></li>
            </ul>
        </nav>
    </header>

    <section class="mentor-profile">
        <h1>{name}</h1>
        <img src="../images/mentors/{image}" alt="{name}">
        <div class="bio">
            <h2>About {name}</h2>
            <p>{bio}</p>
        </div>
        <div class="achievements">
            <h2>Achievements</h2>
            <ul>
                <li>Winner of the [Award Name] in [Year]</li>
                <li>Published [X] papers on [Topic]</li>
                <li>Speaker at [Conference Name]</li>
            </ul>
        </div>
    </section>

    <footer>
        <p>&copy; 2023 Iraq Youth Scientist Team. All rights reserved.</p>
    </footer>

    <script src="../js/scripts.js"></script>
</body>
</html>
"""

# Ensure the mentors folder exists
if not os.path.exists("mentors"):
    os.makedirs("mentors")
    print("Created 'mentors' folder.")

# Generate HTML files for each mentor
for mentor in mentors_2023 + mentors_2024:
    # Create a filename by replacing spaces with hyphens and converting to lowercase
    filename = mentor["name"].replace(" ", "-").lower() + ".html"
    filepath = os.path.join("mentors", filename)
    
    # Write the HTML file
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(template.format(
            name=mentor["name"],
            bio=mentor["bio"],
            image=mentor["name"].replace(" ", "-").lower() + ".jpg"
        ))
    print(f"Generated: {filepath}")

print(f"Successfully generated {len(mentors_2023) + len(mentors_2024)} mentor pages!")