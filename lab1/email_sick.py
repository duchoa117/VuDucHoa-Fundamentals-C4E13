# cout = 0
start = input('Nhập ngày, tháng, năm bắt đầu gửi?( ngăn cách bởi /) ')
start_list = list(start.strip().split('/'))
int_start_list = [int(x) for x in start_list]
# print(int_start_list)
import datetime
now= datetime.datetime.now()
n = now.hour
while True:
    if now.year == int_start_list[2] and now.month == int_start_list[1] and now.day == int_start_list[0]:
        while True:


            if n == 7:
                # while True:


                from random import choice
                reasons_list = ['quên đường đến trường','quên cách đi xe', 'quên không mặc quần']
                choice_reason = choice(reasons_list)
                tâm_thư = """
                    <h1 style="text-align: center;"><strong>Đơn xin nghỉ học</strong></h1>
                <p style="text-align: left;">Em ch&agrave;o thầy&nbsp;</p>
                <p style="text-align: left;">Em t&ecirc;n l&agrave;<span style="background-color: #ffffff; color: #ff0000;"> Vũ Đức H&ograve;a</span></p>
                <p style="text-align: left;">H&ocirc;m nay {{0}} n&ecirc;n e xin nghỉ học&nbsp;<img src="http://htmleditor.tools/tinymce465/plugins/emoticons/img/smiley-frown.gif" alt="frown" /></p>
                <p style="text-align: left;">Đức H&ograve;a</p>
                <p style="text-align: left;"></p>
                """
                tâm_thư.replace('{{0}}', choice_reason)
                print(tâm_thư)
                from gmail import GMail, Message
                gmail = GMail('duchoapc99techkids@gmail.com', 'duchoa119')
                msg = Message('Đơn xin nghỉ học', to='techkidsc4e16@gmail.com', html=tâm_thư)
                gmail.send(msg)

                n = 8
            if now.hour == 6:
                n= now.hour
