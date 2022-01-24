import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import CCTVui_2 as mainui
import datetime
import sys
import pandas as pd
import os
import socket


class SocketThread(QThread):
    data = pyqtSignal(dict)         # 수신 데이터 dict 형태로 GUI 전송 변수
    log = pyqtSignal(str)           # 연결 로그 정보 str 형태로 GUI 전송 변수
    status = pyqtSignal(str)        # 현재 연결 상태 str 형태로 GUI 전송 변수
    def __init__(self, ip, port, parent=None):
        QThread.__init__(self)
        self.ip = ip
        self.port = int(port)
        self.close_req = False
        self.thread_list = []
        self.max_recv_timeout_cnt = 100     # X 초간 데이터 수신이 안될 경우

    def run(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 포트 사용중 이라는 WinError 10048 에러 해결을 위해 필요
        #self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        recv_timeout_cnt = 0
        try:
            # Bind
            self.server_socket.bind((self.ip, self.port))
        except Exception as e:
            # Bind 실패 시 > 이미 포트가 열려 있을 경우
            self.log.emit("00")     # 00 = 포트 사용중 알림창 팝업 플래그
        else:
            # 포트 열림, 대기 상태
            self.server_socket.listen(1)
            self.status.emit("wait")    # wait = 데이터 수신 대기중 상태
            try:
                # 연결 시도
                client, addr = self.server_socket.accept()
                self.log.emit(addr[0] + " Connected..")     # client 주소 + 연결 문자열 전송
                client.settimeout(1)    # 매초 데이터 수신 시도
            except Exception as e:
                pass
            else:
                # 연결 시도 후 정상 연결 시
                while True:
                    if self.close_req:
                        # Close 버튼 클릭 시 Flag = False, 연결 종료 수행
                        self.log.emit(addr[0] + " Connection Closed..")     # client 주소 + 연결 종료 문자열 전송
                        self.status.emit("disconnect")      # disconnect = 포트 닫힘 상태
                        client.close()
                        self.server_socket.close()
                        break
                    try:
                        # 데이터 수신
                        recv = client.recv(1024)
                    except socket.timeout as e:
                        # 수신 데이터 없을 경우
                        recv_timeout_cnt += 1
                        if recv_timeout_cnt == self.max_recv_timeout_cnt:
                            # 수신이 1 * self.max_recv_timeout_cnt 동안 되지 않았을 떄 연결 종료 및 수신 대기
                            close_type = " Receive timeout"
                            self.reset_socket(client=client, addr=addr, close_type=close_type)
                    except Exception as e:
                        pass
                    else:
                        if recv == b'':
                            # 클라이언트가 연결 종료 시 b'' 값 수신
                            close_type = " Client disconnect"
                            self.reset_socket(client=client, addr=addr, close_type=close_type)
                        recv_timeout_cnt = 0    # 수신 타임 아웃 카운트 초기화
                        msg = recv.decode(errors='ignore')
                        self.status.emit("connect")     # connect = 포트 연결 상태(데이터 수신 완료)
                        if msg.startswith('(') and msg.endswith(')'):   # STX, ETX 검사
                            try:
                                solar = str(int(msg[1:5]))
                                mark = lambda x : '- ' if x == '-' else '  '
                                temp = mark(msg[9]) + str(int(msg[10:13]))
                                voltage = str(int(msg[17:22])/1000)
                                ch1_current = str(int(msg[22:27])/1000)
                                ch2_current = str(int(msg[27:32])/1000)
                                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                datadict = {'time': now,
                                            'solar': solar,
                                            'temp': temp,
                                            'voltage': voltage,
                                            'ch1_current': ch1_current,
                                            'ch2_current': ch2_current}
                                self.data.emit(datadict)        # dict 형태로 가공한 datadict GUI 전송
                                self.log.emit(" Data received")
                            except Exception as e:
                                self.log.emit(" Invalid format of data received")
                        else:
                            self.log.emit(" Invalid format of data received")

    def reset_socket(self, client, addr, close_type):
        """
        연결 끊김, 수신 대기 시간 초과 시 소켓을 닫고 대기 상태 전환
        :param client: client 정보
        :param addr: addr 정보
        :param close_type: 소켓 닫힌 이유
        :return:
        """
        self.log.emit(addr[0] + close_type)
        self.log.emit(addr[0] + " Connection Closed..")
        self.status.emit("disconnect")
        client.close()
        self.run()

class MainDialog(QMainWindow, mainui.Ui_MainWindow):
    def __init__(self):
        QDialog.__init__(self, None)
        self.setupUi(self)
        self.portnum.setValidator(QIntValidator(0, 65535, self))        # port 입력란 5자리의 정수만 가능하게 설정
        self.listen_btn.clicked.connect(self.set_port)
        self.close_btn.clicked.connect(self.stop_port)
        self.socket_thread = None

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
        self.socket_thread.close_req = True
        self.portnum.setEnabled(True)
        self.close_btn.setEnabled(False)
        self.listen_btn.setEnabled(True)

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
        pddata = pd.DataFrame([data])
        if sys.platform.startswith('win'):
            fpath = os.getcwd() + "\\datalog.csv"
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            fpath = os.getcwd() + "/datalog.csv"
        if os.path.isfile(fpath):
            pddata.to_csv(fpath, index=False, mode='a', encoding='cp949', header=False)
        else:
            pddata.to_csv(fpath, index=False, mode='w', encoding='cp949')


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
            self.logtextedit.appendPlainText(now + "   " + log)

    @pyqtSlot(str)
    def thread_event_status(self, status):
        # Thread 에서 상태 정보가 넘어 올 때
        if status == "connect":
            self.statuslabel.setText("통신 중")
            self.status_alarm.setStyleSheet("background-color: green")
        elif status == "wait":
            self.statuslabel.setText("데이터 수신 대기중...")
            self.status_alarm.setStyleSheet("background-color: yellow")
        elif status == "disconnect":
            self.statuslabel.setText("포트 닫힘")
            self.status_alarm.setStyleSheet("background-color: red")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MainDialog()
    dialog.show()
    app.exec_()