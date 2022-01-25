from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import CCTVui_2 as MainUi
import datetime
import sys
import pandas as pd
import os
import socket
import threading

open_client = True
open_data = True

class SocketThread(QThread):
    data = pyqtSignal(dict)         # 수신 데이터 dict 형태로 GUI 전송 변수
    log = pyqtSignal(str)           # 연결 로그 정보 str 형태로 GUI 전송 변수
    status = pyqtSignal(str)        # 현재 연결 상태 str 형태로 GUI 전송 변수

    def __init__(self, ip, port, parent=None):
        QThread.__init__(self)
        self.ip = ip
        self.port = int(port)
        self.client_list = []
        self.thread_list = []
        self.max_recv_timeout_cnt = 120     # X*2 초간 데이터 수신이 안될 경우
        self.server_socket = None
        self.reconnect = "reconnect"
        self.listen_thread = threading.Thread

    def run(self):
        global open_client, open_data
        open_client, open_data = True, True
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.settimeout(0.2)
        try:
            # Bind
            self.server_socket.bind((self.ip, self.port))
            # Socket > GUI 포트 OPEN 정보 전송
            self.log.emit("{port} Port Opened".format(port=str(self.port)))
            self.status.emit("clientwait")  # clienwait = 클라이언트 대기 상태
            self.reconnect = "client"
        except Exception as e:
            # Bind 실패 시 > 이미 포트가 열려 있을 경우
            self.log.emit("00")     # 00 = 포트 사용중 알림창 팝업 플래그
        else:
            self.listen_thread = threading.Thread(target=self.listen, args=(self.server_socket,))
            self.listen_thread.start()

    def listen(self, server):
        global open_client
        client, addr = None, None
        while open_client:
            server.listen(5)
            try:
                client, addr = server.accept()
                client.settimeout(0.5)
                self.status.emit("wait")  # clienwait = 클라이언트 대기 상태
                self.log.emit("{addr} Connected".format(addr=addr[0]))     # client 주소 + 연결 문자열 전송
            except Exception as e:
                pass
            else:
                self.client_list.append(client)
                receive_thread = threading.Thread(target=self.receive, args=(addr, client))
                self.thread_list.append(receive_thread)
                receive_thread.start()

        self.log.emit("{port} Disconnected".format(port=self.port))
        self.status.emit("disconnect")
        self.server_socket.close()

    def receive(self, addr, client):
        """
        소켓 데이터 수신 스레드
        :param addr: 주소, 포트 정보
        :param client:  클라이언트 정보
        :return:
        """
        global open_data
        recv_timeout_cnt = 0
        while open_data:
            # GUI > Close 버튼 클릭 시 Flag 전환
            try:
                # 데이터 수신
                recv = client.recv(1024)
            except socket.timeout as e:
                # 수신 데이터 없을 경우
                recv_timeout_cnt += 1
                if recv_timeout_cnt == self.max_recv_timeout_cnt:
                    # 수신이 1 * self.max_recv_timeout_cnt 동안 되지 않았을 떄 연결 종료 및 수신 대기
                    client.close()
                    break
            except Exception as e:
                break
            else:
                if recv == b'':
                    # 클라이언트가 연결 종료 시 b'' 값 수신 > 해당 클라이언트 종료
                    self.log.emit("{addr} Disconnected".format(addr=addr[0]))
                    break
                recv_timeout_cnt = 0  # 수신 타임 아웃 카운트 초기화
                msg = recv.decode(errors='ignore')
                self.status.emit("connect")  # connect = 포트 연결 상태(데이터 수신 완료)
                if msg.startswith('(') and msg.endswith(')'):  # STX, ETX 검사
                    try:
                        solar = str(int(msg[1:5]))
                        mark = lambda x: '- ' if x == '-' else '  '  # 온도 양수 음수 부호
                        temp = "{mark} {temp}".format(mark=mark(msg[9]),
                                                      temp=str(int(msg[10:13]) / 10))
                        voltage = str(int(msg[17:22]) / 1000)
                        ch1_current = str(int(msg[22:27]) / 1000)
                        ch2_current = str(int(msg[27:32]) / 1000)
                        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        datadict = {'time': now,
                                    'solar': solar,
                                    'temp': temp,
                                    'voltage': voltage,
                                    'ch1_current': ch1_current,
                                    'ch2_current': ch2_current}
                        self.data.emit(datadict)  # dict 형태로 가공한 datadict GUI 전송
                        self.log.emit("{addr} Data received".format(addr=addr[0]))
                    except Exception as e:
                        self.log.emit(" Invalid format of data received(Data)")
                else:
                    self.log.emit(" Invalid format of data received(Header, Tail)")


class MainDialog(QMainWindow, MainUi.Ui_MainWindow):
    def __init__(self):
        QDialog.__init__(self, None)
        self.setupUi(self)
        self.portnum.setValidator(QIntValidator(0, 65535, self))        # port 입력란 5자리의 정수만 가능하게 설정
        self.listen_btn.clicked.connect(self.set_port)
        self.close_btn.clicked.connect(self.stop_port)
        self.socket_thread = None
        self.save_flag = False

    def set_port(self):
        # Listen 버튼 클릭 시
        port = self.portnum.text()
        ip = '0.0.0.0'
        if port:
            # Listen > Thread 시작
            self.socket_thread = SocketThread(ip=ip, port=port)
            self.socket_thread.data.connect(self.thread_event_value)
            self.socket_thread.log.connect(self.thread_event_log)
            self.socket_thread.status.connect(self.thread_event_status)
            self.socket_thread.start()
            # GUI 설정
            self.portnum.setEnabled(False)
            self.close_btn.setEnabled(True)
            self.listen_btn.setEnabled(False)

        else:
            # Port 입력란 공란일 경우
            QMessageBox.warning(self, "Port 입력 오류", "Port 번호를 설정 해주세요.")

    def stop_port(self):
        # Close 버튼 클릭 시
        global open_client, open_data
        # self.socket_thread.close_req = True
        open_client = False
        open_data = False
        self.portnum.setEnabled(True)
        self.close_btn.setEnabled(False)
        self.listen_btn.setEnabled(True)
        # self.socket_thread.closeport()

    def write_value(self, data):
        # 소비 전류 Ch1
        self.current_voltage_1.setText(data['voltage'])
        self.current_current_1.setText(data['ch1_current'])
        # 소비 전류 Ch2
        self.current_voltage_2.setText(data['voltage'])
        self.current_current_2.setText(data['ch2_current'])
        # 배터리
        self.battery_voltage.setText(data['voltage'])
        # 정보
        self.receive_time.setText(data['time'])
        # 환경 센서
        self.sensor_solar.setText(data['solar'])
        self.sensor_temp.setText(data['temp'])

    def save_data(self, data):
        """
        저장 체크 시 수신 데이터를 csv 형식 엑셀파일로 저장하는 함수
        :param data: dict 형태의 수신 데이터
        :return: 엑셀 파일 저장
        """
        self.save_flag = False
        if self.autosave.isChecked():
            try:
                pddata = pd.DataFrame([data])
                if sys.platform.startswith('win'):
                    fpath = "{path}\\datalog.csv".format(path=os.getcwd())
                elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
                    fpath = "{path}/datalog.csv".format(path=os.getcwd())
                else:
                    fpath = None
                if os.path.isfile(fpath):
                    pddata.to_csv(fpath, index=False, mode='a', encoding='cp949', header=False)
                else:
                    pddata.to_csv(fpath, index=False, mode='w', encoding='cp949')
            except Exception as e:
                self.save_flag = True

    @pyqtSlot(dict)
    def thread_event_value(self, data):
        # Thread 에서 정상 수신 데이터 dict 가 넘어 올 때
        self.write_value(data)
        self.save_data(data)

    @pyqtSlot(str)
    def thread_event_log(self, log):
        if log == "00":
            # Thread 에서 이미 포트가 사용 중 로그가 넘어 올 때
            QMessageBox.warning(self,
                                "Port Listen Fail",
                                "[WinError 10048] 각 소켓 주소(프로토콜/네트워크 주소/포트)는 하나만 사용할 수 있습니다")
            self.close_btn.click()
        else:
            # Thread 에서 연결 로그가 넘어 왔을 경우
            now = datetime.datetime.now().strftime("%H:%M:%S")
            self.logtextedit.appendPlainText("{now}   {log}".format(now=now, log=log))
            if "received" in log and self.save_flag:
                self.logtextedit.appendPlainText("Data save Failed")

    @pyqtSlot(str)
    def thread_event_status(self, status):
        # Thread 에서 상태 정보가 넘어 올 때
        if status == "connect":
            self.statuslabel.setText("통신 중")
            self.status_alarm.setStyleSheet("background-color: green")
        elif status == "clientwait":
            self.statuslabel.setText("클라이언트 연결 대기중.")
            self.status_alarm.setStyleSheet("background-color: yellow")
        elif status == "wait":
            self.statuslabel.setText("데이터 수신 대기중")
            self.status_alarm.setStyleSheet("background-color: yellow")
        elif status == "disconnect":
            self.statuslabel.setText("포트 닫힘")
            self.status_alarm.setStyleSheet("background-color: red")
        elif status == "reconnect":
            self.close_btn.click()
            self.listen_btn.click()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MainDialog()
    dialog.show()
    app.exec_()
