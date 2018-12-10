import smtplib
import mimetypes

import email
import email.mime.application

    

def sendmail():
    
    username = 'sowmiya@guvi.in'
    password = 'GUVIGEEK'
    receiver={"St Joseph's College":"sowmiya@guvi.in"}
    len_rec=len(receiver)
    client = smtplib.SMTP_SSL('smtp.gmail.com')
    client.login(username, password)
    for i in range (len_rec):

        val=list(receiver)[i]
        print(receiver[val])
        rcpt =receiver[val]
        msg = email.mime.Multipart.MIMEMultipart()
        msg['Subject'] = "DBS Bank's ​Campus Hack2Hire for Women ​'​2018 - for"+list(receiver)[i],
        msg['From'] = username
        msg['To'] = receiver[val]
       
        
        textplain =email.mime.Text.MIMEText('Respected Sir/Madam,<br><br> Good Morning..! Hope you have a stunning day, ahead!<br><br>   Our GUVI Team is excited to share the once-in-a-lifetime opportunity for your women students to participate in DBS Bank&lsquo;s Campus Hack2Hire for Women	&lsquo;2018(Outreach Partner - GUVI), to be held on 9th Dec&lsquo;2018 in Hyderabad DBS - Office Campus.<br><br><font color="blue"><b>* Pay package for successful candidates: 6L - 8L per annum</b></font><br><img src="https://s3-ap-southeast-1.amazonaws.com/guvi/Pics+/hack2hire.png" width="50%"><b>DBS Bank - <font color="red">the World’s Best Digital Bank:</font></b><br><br>DBS - Live More, Bank Less is our motto, and we aim to make banking a seamless journey for people.We put digital priorities at the heart of banking, designing and creating products and services to help our customers. With a strong culture of innovation, experimenting with new technology and collaboration with the FinTech community, we aim to simplify banking so as to help others Live More, Bank Less.<br>We	&lsquo;re looking for technologists across all levels and roles (<b>including Scrum Masters, Mobile Application Developers, Full Stack Developers, DevOps Engineers, QA Engineers, UI/UX Developers, and more,..</b>) to join us to drive major digital transformation to re-imagine banking.<br><b>For Participating Colleges:</b><br><br>Please Submit the details by clicking the link <a href="https://goo.gl/xdpSPs">https://goo.gl/xdpSPs</a>, if your students are participating in this opportunity.<br><br>Online Test procedure :<br><br>	1) Create an account in <a href="www.guvi.in">www.guvi.in</a>, and after login, fill-in your GUVI profile details, and upload your resume(under MY PROFILE).<br><br>	2) From the top menu, go to <b>Jobs -> Tech Challenges</b> Page<br><br>	3) Click <b>Apply</b> in <b>DBS Job</b>*<br><br>	4) Click on <b>Take Test, then follow the Tech challenge mentioned.</b><br><br>	5) In the next section while you start the test, mention <b>GUVI</b> in the field<b>Where did you hear about this challenge?</b><br><br><b>Last date for Online Challenge : 1st-Dec-2018, 11:55 PM IST.</b><br><br>	* The candidates shortlisted from this Online Challenge will be invited for the Hackathon, to be held on 9th Dec&lsquo;2018.<br><br><b>Hackathon Date : 9th-Dec-2018</b><br><b>Hackathon Duration &amp; Location: 24 Hours, Hyderabad</b><br><br>* Hiring Selection results to be known on same day of Hackathon.<br><br><b>Participation EDGE:</b><ul><li>Get to <b>acquire skill</b> sets for future industry needs.</li><li><b>&lsquo;Quick Learning&rsquo;</b> of newer technologies, in just a short period of time.</li><li>Apart from appreciations, excellent opportunity to expose abilities and get <b>Placement offers on same day</b>.</li><li>Learning <b>from Industry experts as Mentors,</b> with their valuable knowledge/experience.</li><br><br>Kindly convey/motivate your students to be confident and think wisely, to shine in the coding challenge and expose their caliber!<br><br><font align="center"><b>ALL THE BEST..!!!</b></font><br><br>Regards,<br><b>Gokul.S(Paulson)</b><br>GUVI Geek Network Private Ltd.<br>IITM Research Park, Chennai.<br>Mobile:8056997730<br><img src="https://s3-ap-southeast-1.amazonaws.com/guvi/Pics+/guvi_logo.png" width="20%">')

        msg.attach(textplain)
        filename = "Girish.pdf"
        fp=open(filename,'rb')
        att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
        fp.close()
        att.add_header('Content-Disposition','attachment',filename=filename)
        msg.attach(att)
        
       
        
        try:
            client.sendmail(username,rcpt, msg.as_string())
            print'Email delivered to '+list(receiver)[i]+' successfully!'
        except smtplib.SMTPRecipientsRefused:
            print 'Email delivery failed, invalid recipient'+list(receiver)[i]
        except smtplib.SMTPAuthenticationError:
            print 'Email delivery failed, authorization error'
        except smtplib.SMTPSenderRefused:
            print 'Email delivery failed, invalid sender'+list(receiver)[i]
        except smtplib.SMTPException,e:
            print 'Email delivery failed', e.message
        
sendmail()


