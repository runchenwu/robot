"""__CONFIG__
{"version":20,"widgetInfos":[{"hwid":"7","name":"motor_7","typeName":"motor","extraConfig":null,"bufferIndex":0},{"hwid":"8","name":"motor_8","typeName":"motor","extraConfig":null,"bufferIndex":1},{"hwid":"9","name":"motor_9","typeName":"motor","extraConfig":null,"bufferIndex":2},{"hwid":"11","name":"motor_11","typeName":"motor","extraConfig":null,"bufferIndex":3},{"hwid":"12","name":"motor_12","typeName":"motor_rp","extraConfig":null,"bufferIndex":4},{"hwid":"drivetrain","name":"dt","typeName":"drivetrain","extraConfig":{"leftMotorHwId":"7","rightMotorHwId":"12","wheelTravel":200,"trackWidth":176},"bufferIndex":5},{"hwid":"lcd","name":"lcd","typeName":"lcd","extraConfig":null,"bufferIndex":6},{"hwid":"sound","name":"sound","typeName":"sound","extraConfig":null,"bufferIndex":7},{"hwid":"btn_chk","name":"button_check","typeName":"face_button","extraConfig":null,"bufferIndex":8},{"hwid":"btn_up","name":"button_up","typeName":"face_button","extraConfig":null,"bufferIndex":9},{"hwid":"btn_down","name":"button_down","typeName":"face_button","extraConfig":null,"bufferIndex":10}]}"""
"""__BLOCKLY__
<xml xmlns="http://www.w3.org/1999/xhtml"><block type="when_run" id="1" x="-96" y="-115"><next><block type="variables_set" id="{%~puW~O7k9e/b4afLc:"><field name="VAR">item</field><value name="VALUE"><block type="math_number" id="*.OC80%zoa9f`O]49eCU"><field name="NUM">0</field></block></value><next><block type="vexiq_Drivetrain_turn_until" id="2wC?~RW4/Lb00=tqrGI`"><field name="DIRECTION">fwd</field><value name="POWER"><block type="math_number" id="q?OOY]rtm|c@3V}o:C]b"><field name="NUM">100</field></block></value><value name="ANGLE"><block type="math_number" id="2.-lA(Cc%2g~:/8#gRmm"><field name="NUM">52.5</field></block></value><next><block type="vexiq_Drivetrain_drive_until" id="7~:?T%PfS!jL7_k+^d}I"><field name="DIRECTION">fwd</field><value name="POWER"><block type="math_number" id="VN=cLgqN7N:IBn.:io@6"><field name="NUM">100</field></block></value><value name="DISTANCE"><block type="math_number" id="[b;jQ5)mpD}ViI2!CvXW"><field name="NUM">435</field></block></value><next><block type="variables_set" id="7Dw8N)D~CKJHV~c`^Dlm"><field name="VAR">item</field><value name="VALUE"><block type="math_number" id="c)iXXV/zS#T_I)ucI^X="><field name="NUM">1</field></block></value><next><block type="vexiq_Motor_run_until_time" id="bbk/5WD=6s{lgWu(xOS/"><field name="WIDGET_ID">8</field><field name="DIRECTION">rev</field><value name="POWER"><block type="math_number" id="1*#_6:=xZ=X),4MpuOLQ"><field name="NUM">100</field></block></value><value name="TIME"><block type="math_number" id="vH)%J2bZ`^3A4cTI.{Q_"><field name="NUM">1.12</field></block></value><value name="HOLD"><block type="logic_boolean" id="N@SM2_*P(26UKTbH/D!1"><field name="BOOL">TRUE</field></block></value><next><block type="vexiq_Drivetrain_turn_until" id="{c+m0*soG)k:aVuNKq?Q"><field name="DIRECTION">fwd</field><value name="POWER"><block type="math_number" id=".)U4-Es~SaGpfUfUtj?0"><field name="NUM">50</field></block></value><value name="ANGLE"><block type="math_number" id=",eP!}TA#9^^leNlNKHqM"><field name="NUM">92</field></block></value><next><block type="vexiq_Drivetrain_drive_until" id="m#lYq0N9!]~^_;3IUbT{"><field name="DIRECTION">fwd</field><value name="POWER"><block type="math_number" id="^As0I!|(}%XTjUQ%PJ{O"><field name="NUM">100</field></block></value><value name="DISTANCE"><block type="math_number" id="zpYO.7E^IuWPY_x5G-vT"><field name="NUM">100</field></block></value><next><block type="variables_set" id="Nol/_]NiAF,P}=,mq)t0"><field name="VAR">item</field><value name="VALUE"><block type="math_number" id="eM,%9]QRl1Tw=WlHN{+R"><field name="NUM">0</field></block></value><next><block type="vexiq_Motor_run_until_time" id=")o/+w=sG4-{Tg#.odXIU"><field name="WIDGET_ID">8</field><field name="DIRECTION">fwd</field><value name="POWER"><block type="math_number" id="KU7}jz5V(./:S[/D.5zI"><field name="NUM">100</field></block></value><value name="TIME"><block type="math_number" id="bcGf8T[YKkE{QPgEyV=b"><field name="NUM">0.25</field></block></value><value name="HOLD"><block type="logic_boolean" id="dg^5k@STcflbtr~%;l!q"><field name="BOOL">TRUE</field></block></value><next><block type="vexiq_Drivetrain_drive_until" id="s#4)KPM5oeXU5jXsB*t]"><field name="DIRECTION">rev</field><value name="POWER"><block type="math_number" id="Sn7.FxeDDI;0J`kq[]*m"><field name="NUM">50</field></block></value><value name="DISTANCE"><block type="math_number" id="bCH96sz17RgT`#cwG-td"><field name="NUM">200</field></block></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="when_run" id="=])8A(dD9GJN},!nL^K(" x="484" y="-134"><next><block type="wait_until" id="9LYFWorpWiV7V7LX=]zG"><value name="EXPR"><block type="logic_compare" id="Q7SPEVkoz6Q]^(ez3MWY"><field name="OP">EQ</field><value name="A"><block type="variables_get" id="6zZYEIj){L*JK{j.KQVC"><field name="VAR">item</field></block></value><value name="B"><block type="math_number" id=".b.=+4#ypc+*:ri2^-b#"><field name="NUM">1</field></block></value></block></value><next><block type="vexiq_Motor_run_until_time" id="0PG=6]0uLc9r0^lCaQYe"><field name="WIDGET_ID">11</field><field name="DIRECTION">fwd</field><value name="POWER"><block type="math_number" id="=/3E?Uge,vyDM%1vEIy7"><field name="NUM">100</field></block></value><value name="TIME"><block type="math_number" id="Dt#qu!IG,U)GO97kz@*a"><field name="NUM">1.12</field></block></value><value name="HOLD"><block type="logic_boolean" id=":]|Z#Wq|qCc~OGYvn*In"><field name="BOOL">TRUE</field></block></value><next><block type="wait_until" id="_s;a_.:TXaFntOCI.yeQ"><value name="EXPR"><block type="logic_compare" id="Hca:|2VhTWeClmHfR6n-"><field name="OP">EQ</field><value name="A"><block type="variables_get" id=")-D66Pt[x`i([Weot/N["><field name="VAR">item</field></block></value><value name="B"><block type="math_number" id="nw^-GN{2;*b.D7kU8u(J"><field name="NUM">0</field></block></value></block></value><next><block type="vexiq_Motor_run_until_time" id="ldt,!Qcm/wpg|lPcbPSf"><field name="WIDGET_ID">11</field><field name="DIRECTION">rev</field><value name="POWER"><block type="math_number" id="zV@rMkyx*),/k|9CIvff"><field name="NUM">100</field></block></value><value name="TIME"><block type="math_number" id="~wHJ@1i_m;_IR^w=E45j"><field name="NUM">0.25</field></block></value><value name="HOLD"><block type="logic_boolean" id="a6[Z=:]nD*c+DA}L3y6e"><field name="BOOL">TRUE</field></block></value></block></next></block></next></block></next></block></next></block></xml>
"""

import vexiq
import sys

#region config
motor_7  = vexiq.Motor(7)
motor_8  = vexiq.Motor(8)
motor_9  = vexiq.Motor(9)
motor_11 = vexiq.Motor(11)
motor_12 = vexiq.Motor(12, True) # Reverse Polarity

import drivetrain
dt       = drivetrain.Drivetrain(motor_7, motor_12, 200, 176)
#endregion config

item = None

def thread2():
  global item
  sys.wait_for(lambda: item == 1)
  motor_11.run_until_time(100, 1.12, True)
  sys.wait_for(lambda: item == 0)
  motor_11.run_until_time(-(100), 0.25, True)
sys.run_in_thread(thread2)


# main thread
item = 0
dt.turn_until(100, 52.5)
dt.drive_until(100, 435)
item = 1
motor_8.run_until_time(-(100), 1.12, True)
dt.turn_until(50, 92)
dt.drive_until(100, 100)
item = 0
motor_8.run_until_time(100, 0.25, True)
dt.drive_until(-(50), 200)

