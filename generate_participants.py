# List of participants (2023 and 2024)
participants = [
    {"name": "علي محمد جبار", "bio": "علي محمد جبار is a talented young scientist..."},
    {"name": "Atheer Bassam Qasim", "bio": "Atheer Bassam Qasim has worked on..."},
    {"name": "وضاح احمد عوده", "bio": "وضاح احمد عوده is passionate about..."},
    {"name": "Hala Abd Al Hameed Mahdi", "bio": "Hala Abd Al Hameed Mahdi is passionate about..."},
    {"name": "نور عبدالزهرة مشتت", "bio": "نور عبدالزهرة مشتت has contributed to..."},
    {"name": "Islam Raed Khudhair", "bio": "Islam Raed Khudhair is a rising star in..."},
    {"name": "Sara Salim Al Mahdi", "bio": "Sara Salim Al Mahdi specializes in..."},
    {"name": "احمد وليد داود", "bio": "احمد وليد داود is passionate about..."},
    {"name": "فاطمة بهجت كاظم", "bio": "فاطمة بهجت كاظم has worked on..."},
    {"name": "طه طالب رشيد", "bio": "طه طالب رشيد is passionate about..."},
    {"name": "Ghada Hashim Abbas", "bio": "Ghada Hashim Abbas is a talented young scientist..."},
    {"name": "زهراء اسامة", "bio": "زهراء اسامة has worked on..."},
    {"name": "Maryam Rasim", "bio": "Maryam Rasim specializes in..."},
    {"name": "مصطفى فراس طارق", "bio": "مصطفى فراس طارق has contributed to..."},
    {"name": "بنين جليل اسماعيل", "bio": "بنين جليل اسماعيل is a talented young scientist..."},
    {"name": "Zaid Hamed", "bio": "Zaid Hamed has worked on..."},
    {"name": "منى زين العابدين", "bio": "منى زين العابدين specializes in..."},
    {"name": "Zahraa Muqdad Sami", "bio": "Zahraa Muqdad Sami has worked on..."},
    {"name": "مصطفى كاظم جواد", "bio": "مصطفى كاظم جواد has contributed to..."},
    {"name": "Dania Hassan Abbas Shamsallah", "bio": "Dania Hassan Abbas Shamsallah specializes in..."},
    {"name": "اثير محمد خضير عباس", "bio": "اثير محمد خضير عباس has contributed to..."},
    {"name": "Noor Al Hassan Emad Khalaf", "bio": "Noor Al Hassan Emad Khalaf is a talented young scientist..."},
    {"name": "Ghasaq Ehab Hasan", "bio": "Ghasaq Ehab Hasan has worked on..."},
    {"name": "MohamedEzuldin Naser Ibrahim", "bio": "MohamedEzuldin Naser Ibrahim specializes in..."},
    {"name": "Sami Basil Moaid", "bio": "Sami Basil Moaid is passionate about..."},
    {"name": "احمد عمر صبحي حميد", "bio": "احمد عمر صبحي حميد has worked on..."},
    {"name": "Bakr Amjed Ramadhan Al-Rawi", "bio": "Bakr Amjed Ramadhan Al-Rawi has contributed to..."},
    {"name": "Mustafa Kadhum Jawad", "bio": "Mustafa Kadhum Jawad has worked on..."},
    {"name": "Haneen Abdulkhader Mahmood", "bio": "Haneen Abdulkhader Mahmood is a rising star in..."},
    {"name": "Hajir Marwan Mahdi", "bio": "Hajir Marwan Mahdi is passionate about..."},
    {"name": "Mohammed Mazin", "bio": "Mohammed Mazin has worked on..."},
    {"name": "ملاك مهند بريسم", "bio": "ملاك مهند بريسم specializes in..."},
    {"name": "Mustafa Hameed Khalaf", "bio": "Mustafa Hameed Khalaf has contributed to..."},
    {"name": "Manar Shehab Ahmed", "bio": "Manar Shehab Ahmed has contributed to..."},
    {"name": "علي محمد عزيز", "bio": "علي محمد عزيز is a rising star in..."},
    {"name": "زيد احمد عمار", "bio": "زيد احمد عمار has worked on..."},
    {"name": "Kawther Alobaidy", "bio": "Kawther Alobaidy is a rising star in..."},
    {"name": "Ameer Saheb Khalaf", "bio": "Ameer Saheb Khalaf specializes in..."},
    {"name": "Taha Talib Rasheed", "bio": "Taha Talib Rasheed is a talented young scientist..."},
    {"name": "احمد عمر صبحي", "bio": "احمد عمر صبحي specializes in..."},
    {"name": "Zaid Ahmed Ammar", "bio": "Zaid Ahmed Ammar is passionate about..."},
    {"name": "Mustafa Nazar Qasim", "bio": "Mustafa Nazar Qasim has contributed to..."},
]

# HTML template for participant pages
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
            </ul>
        </nav>
    </header>

    <section class="participant-profile">
        <h1>{name}</h1>
        <img src="../images/participants/{image}" alt="{name}">
        <div class="bio">
            <h2>About {name}</h2>
            <p>{bio}</p>
        </div>
    </section>

    <footer>
        <p>&copy; 2023 Iraq Youth Scientist Team. All rights reserved.</p>
    </footer>

    <script src="../js/scripts.js"></script>
</body>
</html>
"""

# Generate HTML files for each participant
for participant in participants:
    # Create a filename by replacing spaces with hyphens and converting to lowercase
    filename = participant["name"].replace(" ", "-").lower() + ".html"
    # Write the HTML file
    with open(f"participants/{filename}", "w", encoding="utf-8") as file:
        file.write(template.format(
            name=participant["name"],
            bio=participant["bio"],
            image=participant["name"].replace(" ", "-").lower() + ".jpg"
        ))

print("Participant pages generated successfully!")