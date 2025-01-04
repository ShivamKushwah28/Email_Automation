import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email details
sender_email = "shivam_2311ai41@iitp.ac.in"
receiver_email = "aayush_2311ai21@iitp.ac.in"
cc_email = ["rajat_2311ai57@iitp.ac.in"]
password = "Shiv#2820"  # Replace with your email password or app password

# Email content
subject = "Testing --- Invitation for Campus Placement and Internship Recruitment - IIT Patna"
body = """
<html>
<body>
<p><b>Dear Sir,</b></p>
<br>
<p>Greetings from the <b>Indian Institute of Technology, Patna!</b></p>

<p>We hope you're doing well and staying safe.</p>

<p><b>Indian Institute of Technology, Patna</b>, is developing fast and emerging as an institute of excellence promoting brilliant, hardworking, technologically curious minds, and holding up high as an institute of national importance. The students have continuously accomplished milestones and have excelled in honing all kinds of skills. The institute possesses a distinct vision and is highly aligned with industries.</p>

<p>We cordially invite your esteemed organization to participate in our </b>campus placement program for Full-Time Employment for students graduating in 2025 and Internship Recruitment for students graduating in 2026.</b></p>
<br>
<p>The tentative timeline for the season is as follows:</p>
<br>
<table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; width: 100%;">
    <tr style="background-color: #ffd480;">
      <th style="background-color: #ffd480">Timeline</th>
      <th style="background-color: #ffd480">PPT Session</th>
      <th style="background-color: #ffd480" >Online Assessment</th>
      <th style="background-color: #ffd480">Interviews</th>
    </tr>
    <tr style="background-color: #f2f2f2;">
      <th style="background-color: #ffd480">Placement Drive</th>
      <td>December</td>
      <td>December</td>
      <td>Mid-December</td>
    </tr>
    <tr>
      <th style="background-color: #ffd480">Internship Drive</th>
      <td>December</td>
      <td>December</td>
      <td>December</td>
    </tr>
    </table>
    
    
<br>
<p>Kindly fill out the below-mentioned <b>Job-Notification Form (JNF)</b> and <b>Internship-Notification Form (INF)</b> so we could get to comprehend your expectations from our institution and candidates:</p>
<br>
<ul>
  <li><a href="https://docs.google.com/forms/d/e/1FAIpQLSeS_9yWJxpWWTHvs-MnD_mMd07rcyLwC9anuSB4E31-RA7VQw/viewform?vc=0&c=0&w=1&flr=0">Link to JNF - <b>For Full-Time Employment (FTE)</b></a></li>
<br>
  <li><a href="https://docs.google.com/forms/d/e/1FAIpQLSdK74kAg2ZWfsodJxci6TbKAxIalCi8WHRmcuaKkvJH87k59A/viewform?vc=0&c=0&w=1&flr=0">Link to INF - <b>For Internship</b></a></li>
</ul>
<br>

<p>Students are available from the following disciplines from the 2024-25 session (for FTE & Internship):</p>
<table border="1" cellpadding="5" cellspacing="0">
<tr>
  <th style="background-color: #ffd480">B. Tech/B.S Program (Passing Out Year - 2025-26)</th>
  <th style="background-color: #ffd480">M. Tech Program (Passing Out Year - 2025-26)</th>
  <th style="background-color: #ffd480">M. Sc Program (Passing Out Year - 2025-26)</th>
</tr>
<tr>
  <td>
    <ul>
      <li>Computer Science & Engineering <a href="https://drive.google.com/file/d/1fX9rXjqUvbN2l01dbDC68mRNu1mD1rv3/view?usp=drive_link">[Link]</a></li>
      <li>Artificial Intelligence and Data Science <a href="https://drive.google.com/file/d/1tgWmpGNkAARaH2-SbeKyIb0980tLnogX/view?usp=drive_link">[Link]</a></li>
      <li>Electrical and Electronics Engineering <a href="https://drive.google.com/file/d/1oMSeWoyr-INe5Dnxppf-al4iZRMGV05l/view?usp=drive_link">[Link]</a></li>
      <li>Mathematics and Computing <a href="https://drive.google.com/file/d/1JP4C3OWoPn4TXtMuYPd2Hw5pHH86lNVO/view">[Link]</a></li>
      <li>Mechanical Engineering <a href="https://drive.google.com/file/d/1Wvg8V586iESVPKxMT5sSTTCV5RYcqY25/view?usp=drive_link">[Link]</a></li>
      <li>Chemical and Biochemical Engineering <a href="https://drive.google.com/file/d/1_KKHnwVJV5x90vDt2o_BMrlTtTXa8ZYl/view?usp=drive_link">[Link]</a></li>
      <li>Engineering Physics <a href="https://drive.google.com/file/d/1oIGWHj0cHeqfsBAllhAjePsj3xXMglXX/view?usp=drive_link">[Link]</a></li>
      <li>Civil and Environmental Engineering <a href="">[Link]</a></li>
      <li>Metallurgical and Materials Engineering <a href="https://drive.google.com/file/d/1xnI8OIFEU7c1A3kHIHOUbhSVQdRFDKuL/view?usp=drive_link">[Link]</a></li>
    </ul>
  </td>
  <td>
    <ul>
      <li>Artificial Intelligence <a href="https://drive.google.com/file/d/1_s1BVSucO_n6vWZNv_eaL8w3e7zEBddJ/view?usp=sharing">[Link]</a></li>
      <li>Computer Science and Engineering <a href="https://drive.google.com/file/d/1Jw2h7frApugCsyCm9ig1PbuxbsznYgiD/view">[Link]</a></li>
      <li>Mathematics and Computing <a href="https://drive.google.com/file/d/1byeoqmAWmRAYglyOhRqixRQmuNwhv6lQ/view?usp=sharing">[Link]</a></li>
      <li>Communication Systems Engineering <a href="https://drive.google.com/file/d/18Y7Xi-AawmyJe9vKdBav4SaWw9Pclo5U/view?usp=sharing">[Link]</a></li>
      <li>VLSI and Embedded Systems <a href="https://drive.google.com/file/d/1HfIWblE_2CheUfdMEayIhu_DTbIA7Z0G/view?usp=sharing">[Link]</a></li>
      <li>Mechatronics <a href="https://drive.google.com/file/d/1KFoW00DAqn9lA5WtQNPuF8i0AcmRyQCe/view?usp=drive_link">[Link]</a></li>
      <li>Mechanical Design <a href="https://drive.google.com/file/d/1MeKVPzDIvOsq1DAfSRa_YgX_uyrlWsJB/view?usp=drive_link">[Link]</a></li>
      <li>Thermal and Fluids Engineering <a href="https://drive.google.com/file/d/1m91Q9VCPa6eHK3z92BX80P8SmV00dTz1/view?usp=sharing">[Link]</a></li>
      <li>Advanced Manufacturing Technology <a href="https://drive.google.com/file/d/1P5zhk6FbY1TVNs4K9A0KAbIbmVU6LXWs/view?usp=drive_link">[Link]</a></li>
      <li>Civil and Environmental Engineering <a href="https://drive.google.com/file/d/19hmxfafUTEyEUXGqR2GG37UMYJEdvMVg/view?usp=sharing">[Link]</a></li>
      <li>Material Sciences and Engineering <a href="https://drive.google.com/file/d/1qP-6gzj9Qz9Sn2eY29E2e79DjRIv_bl_/view?usp=sharing">[Link]</a></li>
      <li>Power and Control <a href="https://drive.google.com/file/d/1iPsewzZIfJUDI8z_jvWRmSbqfpOL81CJ/view?usp=sharing">[Link]</a></li>
      <li>Structural Engineering <a href="https://drive.google.com/file/d/1mL_G6-Cabv-3LcjtegYU5RgHMx-9CTRI/view?usp=sharing">[Link]</a></li>
      <li>Geotechnical Engineering <a href="https://drive.google.com/file/d/1GmFb2whSk-149gzY7OPSsy7iKAz1eZ3a/view?usp=sharing">[Link]</a></li>
      <li>Chemical  Engineering <a href="">[Link]</a></li>
    </ul>
  </td>
  <td>
    <ul>
      <li>Mathematics <a href="https://drive.google.com/file/d/1PUklSr3_K2jmUM8MoBcTAHXjITiXy6D9/view?usp=drive_link">[Link]</a></li>
      <li>Physics <a href="https://drive.google.com/file/d/1dxkMiTZxaR65Zodn10j2LUwC_uM70hiU/view?usp=drive_link">[Link]</a></li>
      <li>Chemistry <a href="https://drive.google.com/file/d/17fYT0uQFZJpoJtdoGaR3m62_lEIKQOlh/view?usp=drive_link">[Link]</a></li>
    </ul>
  </td>
</tr>
</table>
<br>

<p>We look forward to strengthening our association and would be grateful to have your firm on campus. As the season is yet to commence, your early reply would help us provide you with an early slot for an FTE and Intern. 
<br>    
Please fill out the <b>JNF and INF</b> as soon as possible so that we can provide your <b>esteemed firm with the best slot</b> for the students of IIT Patna.</p>

<p>Please feel free to contact the undersigned if any further information or any kind of assistance is required.</p>

<p>______________________________</p>
<p>With Best Regards,</p>
<p>
<b>Shivam</b><br>
Assistant Head Coordinator<br>
Centre for Career Development and Counselling <br>
(formerly Training and Placement Cell)<br>
Indian Institute of Technology Patna | भारतीय प्रौद्योगिकी संस्थान पटना<br>
Bihta, Patna | बिहता, पटना<br>
Phone: 7900645725<br>
<a href="https://www.iitp.ac.in/placement/">https://www.iitp.ac.in/placement/</a>
<br>

</p>
</body>
</html>
"""

# Create the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Cc'] = ", ".join(cc_email)
message['Subject'] = subject

# Add the email body
message.attach(MIMEText(body, 'html'))

# Convert message to string
email_content = message.as_string()

# Sending the email
try:
    with smtplib.SMTP('smtp.office365.com', 587) as server:
        server.starttls()  # Encrypt the connection
        server.login(sender_email, password)  # Login with sender's email and password
        server.sendmail(sender_email, [receiver_email] + cc_email, email_content)  # Send the email
        print("Email sent successfully.")
except Exception as e:
    print(f"Error: {e}")
