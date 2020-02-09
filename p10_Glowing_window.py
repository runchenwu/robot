"""__CONFIG__
{"version":20,"widgetInfos":[{"hwid":"7","name":"motor_7","typeName":"motor","extraConfig":null,"bufferIndex":0},{"hwid":"8","name":"motor_8","typeName":"motor_rp","extraConfig":null,"bufferIndex":1},{"hwid":"9","name":"motor_9","typeName":"motor","extraConfig":null,"bufferIndex":2},{"hwid":"11","name":"motor_11","typeName":"motor","extraConfig":null,"bufferIndex":3},{"hwid":"12","name":"motor_12","typeName":"motor_rp","extraConfig":null,"bufferIndex":4},{"hwid":"drivetrain","name":"dt","typeName":"drivetrain","extraConfig":{"leftMotorHwId":"7","rightMotorHwId":"12","wheelTravel":200,"trackWidth":176},"bufferIndex":5},{"hwid":"lcd","name":"lcd","typeName":"lcd","extraConfig":null,"bufferIndex":6},{"hwid":"sound","name":"sound","typeName":"sound","extraConfig":null,"bufferIndex":7},{"hwid":"btn_chk","name":"button_check","typeName":"face_button","extraConfig":null,"bufferIndex":8},{"hwid":"btn_up","name":"button_up","typeName":"face_button","extraConfig":null,"bufferIndex":9},{"hwid":"btn_down","name":"button_down","typeName":"face_button","extraConfig":null,"bufferIndex":10}]}"""
"""__BLOCKLY__
<xml xmlns="http://www.w3.org/1999/xhtml"><block type="when_run" id="1" x="100" y="29"><next><block type="variables_set" id="=:h%9_fD|]3f|ZRMV^2w"><field name="VAR">item</field><value name="VALUE"><block type="math_number" id="02i;l?C8X;yk;a0-5yjZ"><field name="NUM">0</field></block></value><next><block type="vexiq_Drivetrain_turn_until" id="gPKbwe:#vwwW;e`]R/uI"><field name="DIRECTION">fwd</field><value name="POWER"><block type="math_number" id="qx2MD_t^hXB_qMo.NqUY"><field name="NUM">100</field></block></value><value name="ANGLE"><block type="math_number" id="V#Ml,*k0j!B8Aoyku!-q"><field name="NUM">45</field></block></value><next><block type="vexiq_Drivetrain_drive_until" id="swA7sXTd?%BQPVVi=]ET"><field name="DIRECTION">fwd</field><value name="POWER"><block type="math_number" id="-]qnYo^U65Ed#b%|DbnY"><field name="NUM">100</field></block></value><value name="DISTANCE"><block type="math_number" id="Na/.h)u;XI-SJ[OMJnlw"><field name="NUM">190</field></block></value><next><block type="vexiq_Drivetrain_turn_until" id="f`|GY8o)3RjqB0RTxKV{"><field name="DIRECTION">rev</field><value name="POWER"><block type="math_number" id="1/V+E^bKhO[Xyoq{mr_i"><field name="NUM">80</field></block></value><value name="ANGLE"><block type="math_number" id="!b*7yz|{==8_#v?Ac)a;"><field name="NUM">70</field></block></value><next><block type="vexiq_Drivetrain_drive_until" id="#F)j!zw5k]_t0#3;trO,"><field name="DIRECTION">fwd</field><value name="POWER"><block type="math_number" id="bjW2c,*NP8_M@!LcNWG#"><field name="NUM">50</field></block></value><value name="DISTANCE"><block type="math_number" id="@UG^o.Hl-D1L^HU93)o%"><field name="NUM">60</field></block></value><next><block type="variables_set" id=";41F!_gI|e1M_d7[1g:8"><field name="VAR">item</field><value name="VALUE"><block type="math_number" id="UWcy[dMf0+P#y.KMjwwc"><field name="NUM">1</field></block></value><next><block type="vexiq_Motor_run_until_time" id="(YZp5HKye5%8]yg^qtSk"><field name="WIDGET_ID">8</field><field name="DIRECTION">fwd</field><value name="POWER"><block type="math_number" id="@+C0J7Jm2).0;tTWcm``"><field name="NUM">100</field></block></value><value name="TIME"><block type="math_number" id=")(Zbz9MPu6e:IC-:]c{8"><field name="NUM">1</field></block></value><value name="HOLD"><block type="logic_boolean" id="j?Sb)m=#KoKVnM!|rIb4"><field name="BOOL">TRUE</field></block></value><next><block type="vexiq_Drivetrain_turn_until" id="H;iE8*fMcSGanzbv!#9|"><field name="DIRECTION">fwd</field><value name="POWER"><block type="math_number" id="p#4(VF+]^+8-u3.mg-hr"><field name="NUM">100</field></block></value><value name="ANGLE"><block type="math_number" id=",:!Cmx]+y{aj_GKK/]b/"><field name="NUM">25</field></block></value><next><block type="vexiq_Drivetrain_drive_until" id="G7D{i`/c.L7lzeMkA8Fu"><field name="DIRECTION">fwd</field><value name="POWER"><block type="math_number" id="OLW)c%bA{U*nG/W_`Hdi"><field name="NUM">100</field></block></value><value name="DISTANCE"><block type="math_number" id="F|/7Fq^s*1.3ZC@:X7GM"><field name="NUM">480</field></block></value><next><block type="variables_set" id="yy/d^K-_{:m2t*g:{B)x"><field name="VAR">item</field><value name="VALUE"><block type="math_number" id="wNzy!|sIq=AwMkZ;E4?,"><field name="NUM">0</field></block></value><next><block type="vexiq_Motor_run_until_time" id="SKlhlv.=Y~f4rn#h5_RK"><field name="WIDGET_ID">8</field><field name="DIRECTION">rev</field><value name="POWER"><block type="math_number" id="UbNt6}F]Ed~7`5!OP3{_"><field name="NUM">50</field></block></value><value name="TIME"><block type="math_number" id="XDA@Xj{DItoU_=cEsf;p"><field name="NUM">0.8</field></block></value><value name="HOLD"><block type="logic_boolean" id="lq[hUEJnu+rv4s`,v6Ms"><field name="BOOL">TRUE</field></block></value><next><block type="vexiq_Drivetrain_drive_until" id="{uGyw9)Y44`=t5UdC;fL"><field name="DIRECTION">rev</field><value name="POWER"><block type="math_number" id="g(W7YjAyMiq+*UV:xtGf"><field name="NUM">100</field></block></value><value name="DISTANCE"><block type="math_number" id="L~DR3P*(..`vx-UV_-=e"><field name="NUM">400</field></block></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="when_run" id="hA%gA@b:E}?/Df7f.Rz(" x="543" y="6"><next><block type="wait_until" id="(O+c#1rm:ilXh;)gyzI?"><value name="EXPR"><block type="logic_compare" id="U:d`y,F3:A[idp,/(Hcx"><field name="OP">EQ</field><value name="A"><block type="variables_get" id="Fh[~P4}muim[ofIPR_g@"><field name="VAR">item</field></block></value><value name="B"><block type="math_number" id="BLog82qwVJVFaa=Gi/iV"><field name="NUM">1</field></block></value></block></value><next><block type="vexiq_Motor_run_until_time" id=":9p(yRGJy4r{`]%#*Glx"><field name="WIDGET_ID">11</field><field name="DIRECTION">fwd</field><value name="POWER"><block type="math_number" id="m2B,~z}d2-F0AySqvl32"><field name="NUM">100</field></block></value><value name="TIME"><block type="math_number" id="m@8sYTh6F3wBmar(o3VV"><field name="NUM">1</field></block></value><value name="HOLD"><block type="logic_boolean" id="ZvfLrjP}/}p/70sO9Jrs"><field name="BOOL">TRUE</field></block></value><next><block type="wait_until" id="Ju~LxQxFdE,RLn?L,WT8"><value name="EXPR"><block type="logic_compare" id="):V*qBhz[y.eydwf=v+i"><field name="OP">EQ</field><value name="A"><block type="variables_get" id="waiUc=#?}}iFOW.n~*_W"><field name="VAR">item</field></block></value><value name="B"><block type="math_number" id="9CXG8#J:nTn,24`.)n94"><field name="NUM">0</field></block></value></block></value><next><block type="vexiq_Motor_run_until_time" id="]eCJ1(`kL?Ur3O=vPPcn"><field name="WIDGET_ID">11</field><field name="DIRECTION">rev</field><value name="POWER"><block type="math_number" id="_(A*^6F/Kp44[P2Lqbxe"><field name="NUM">50</field></block></value><value name="TIME"><block type="math_number" id="8~LxSN@YuW,_H@qTEQh8"><field name="NUM">0.8</field></block></value><value name="HOLD"><block type="logic_boolean" id="nqq{ksEuBNtkD~DrE#fM"><field name="BOOL">TRUE</field></block></value></block></next></block></next></block></next></block></next></block></xml>
"""

import vexiq
import sys

#region config
motor_7  = vexiq.Motor(7)
motor_8  = vexiq.Motor(8, True) # Reverse Polarity
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
  motor_11.run_until_time(100, 1, True)
  sys.wait_for(lambda: item == 0)
  motor_11.run_until_time(-(50), 0.8, True)
sys.run_in_thread(thread2)


# main thread
item = 0
dt.turn_until(100, 45)
dt.drive_until(100, 190)
dt.turn_until(-(80), 70)
dt.drive_until(50, 60)
item = 1
motor_8.run_until_time(100, 1, True)
dt.turn_until(100, 25)
dt.drive_until(100, 480)
item = 0
motor_8.run_until_time(-(50), 0.8, True)
dt.drive_until(-(100), 400)

