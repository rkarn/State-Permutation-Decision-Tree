def inference_rate(pixels):
 clock_counter=0; state=0; Label=10; ml_inference_completed=0; #assigning dummy default label to 10
 while(Label == 10):
  match state:
    case 0:
           if (pixels[409] <= 0): clock_counter = clock_counter+1; state=1; 
           else: state=256; clock_counter = clock_counter+1;
    case 1:
           if (pixels[434] <= 0): clock_counter = clock_counter+1; state=2; 
           else: state=129; clock_counter = clock_counter+1;
    case 2:
           if (pixels[455] <= 3): clock_counter = clock_counter+1; state=3; 
           else: state=66; clock_counter = clock_counter+1;
    case 3:
           if (pixels[324] <= 13): clock_counter = clock_counter+1; state=4; 
           else: state=35; clock_counter = clock_counter+1;
    case 4:
           if (pixels[518] <= 3): clock_counter = clock_counter+1; state=5; 
           else: state=20; clock_counter = clock_counter+1;
    case 5:
           if (pixels[183] <= 1): clock_counter = clock_counter+1; state=6; 
           else: state=13; clock_counter = clock_counter+1;
    case 6:
           if (pixels[599] <= 0): clock_counter = clock_counter+1; state=7; 
           else: state=10; clock_counter = clock_counter+1;
    case 7:
           if (pixels[467] <= 1):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
           else:  Label=7; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 10:
            if (pixels[220] <= 3):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 13:
            if (pixels[271] <= 5): clock_counter = clock_counter+1; state=14; 
            else: state=17; clock_counter = clock_counter+1;
    case 14:
            if (pixels[245] <= 5):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 17:
            if (pixels[490] <= 36):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 20:
            if (pixels[542] <= 8): clock_counter = clock_counter+1; state=21; 
            else: state=28; clock_counter = clock_counter+1;
    case 21:
            if (pixels[466] <= 54): clock_counter = clock_counter+1; state=22; 
            else: state=25; clock_counter = clock_counter+1;
    case 22:
            if (pixels[128] <= 7):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 25:
            if (pixels[487] <= 11):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 28:
            if (pixels[375] <= 48): clock_counter = clock_counter+1; state=29; 
            else: state=32; clock_counter = clock_counter+1;
    case 29:
            if (pixels[344] <= 5):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 32:
            if (pixels[177] <= 5):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 35:
            if (pixels[284] <= 2): clock_counter = clock_counter+1; state=36; 
            else: state=51; clock_counter = clock_counter+1;
    case 36:
            if (pixels[269] <= 1): clock_counter = clock_counter+1; state=37; 
            else: state=44; clock_counter = clock_counter+1;
    case 37:
            if (pixels[486] <= 163): clock_counter = clock_counter+1; state=38; 
            else: state=41; clock_counter = clock_counter+1;
    case 38:
            if (pixels[266] <= 158):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 41:
            if (pixels[575] <= 132):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 44:
            if (pixels[353] <= 159): clock_counter = clock_counter+1; state=45; 
            else: state=48; clock_counter = clock_counter+1;
    case 45:
            if (pixels[513] <= 84):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 48:
            if (pixels[288] <= 175):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 51:
            if (pixels[180] <= 36): clock_counter = clock_counter+1; state=52; 
            else: state=59; clock_counter = clock_counter+1;
    case 52:
            if (pixels[597] <= 21): clock_counter = clock_counter+1; state=53; 
            else: state=56; clock_counter = clock_counter+1;
    case 53:
            if (pixels[464] <= 205):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 56:
            if (pixels[292] <= 17):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 59:
            if (pixels[298] <= 228): clock_counter = clock_counter+1; state=60; 
            else: state=63; clock_counter = clock_counter+1;
    case 60:
            if (pixels[488] <= 30):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 63:
            if (pixels[323] <= 98):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 66:
            if (pixels[627] <= 1): clock_counter = clock_counter+1; state=67; 
            else: state=98; clock_counter = clock_counter+1;
    case 67:
            if (pixels[359] <= 27): clock_counter = clock_counter+1; state=68; 
            else: state=83; clock_counter = clock_counter+1;
    case 68:
            if (pixels[518] <= 1): clock_counter = clock_counter+1; state=69; 
            else: state=76; clock_counter = clock_counter+1;
    case 69:
            if (pixels[183] <= 3): clock_counter = clock_counter+1; state=70; 
            else: state=73; clock_counter = clock_counter+1;
    case 70:
            if (pixels[570] <= 11):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 73:
            if (pixels[351] <= 3):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 76:
            if (pixels[399] <= 0): clock_counter = clock_counter+1; state=77; 
            else: state=80; clock_counter = clock_counter+1;
    case 77:
            if (pixels[459] <= 50):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 80:
            if (pixels[240] <= 3):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 83:
            if (pixels[239] <= 4): clock_counter = clock_counter+1; state=84; 
            else: state=91; clock_counter = clock_counter+1;
    case 84:
            if (pixels[485] <= 238): clock_counter = clock_counter+1; state=85; 
            else: state=88; clock_counter = clock_counter+1;
    case 85:
            if (pixels[539] <= 35):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 88:
            if (pixels[464] <= 224):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 91:
            if (pixels[689] <= 200): clock_counter = clock_counter+1; state=92; 
            else: state=95; clock_counter = clock_counter+1;
    case 92:
            if (pixels[431] <= 164):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 95:
            if (pixels[576] <= 14):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 98:
            if (pixels[353] <= 144): clock_counter = clock_counter+1; state=99; 
            else: state=114; clock_counter = clock_counter+1;
    case 99:
            if (pixels[489] <= 169): clock_counter = clock_counter+1; state=100; 
            else: state=107; clock_counter = clock_counter+1;
    case 100:
             if (pixels[324] <= 163): clock_counter = clock_counter+1; state=101; 
             else: state=104; clock_counter = clock_counter+1;
    case 101:
             if (pixels[436] <= 34):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 104:
             if (pixels[301] <= 5):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 107:
             if (pixels[345] <= 27): clock_counter = clock_counter+1; state=108; 
             else: state=111; clock_counter = clock_counter+1;
    case 108:
             if (pixels[323] <= 143):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 111:
             if (pixels[386] <= 241):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 114:
             if (pixels[270] <= 63): clock_counter = clock_counter+1; state=115; 
             else: state=122; clock_counter = clock_counter+1;
    case 115:
             if (pixels[512] <= 181): clock_counter = clock_counter+1; state=116; 
             else: state=119; clock_counter = clock_counter+1;
    case 116:
             if (pixels[239] <= 204):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 119:
             if (pixels[400] <= 129):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 122:
             if (pixels[238] <= 66): clock_counter = clock_counter+1; state=123; 
             else: state=126; clock_counter = clock_counter+1;
    case 123:
             if (pixels[294] <= 13):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 126:
             if (pixels[151] <= 254):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 129:
             if (pixels[375] <= 0): clock_counter = clock_counter+1; state=130; 
             else: state=193; clock_counter = clock_counter+1;
    case 130:
             if (pixels[550] <= 0): clock_counter = clock_counter+1; state=131; 
             else: state=162; clock_counter = clock_counter+1;
    case 131:
             if (pixels[234] <= 1): clock_counter = clock_counter+1; state=132; 
             else: state=147; clock_counter = clock_counter+1;
    case 132:
             if (pixels[149] <= 7): clock_counter = clock_counter+1; state=133; 
             else: state=140; clock_counter = clock_counter+1;
    case 133:
             if (pixels[300] <= 15): clock_counter = clock_counter+1; state=134; 
             else: state=137; clock_counter = clock_counter+1;
    case 134:
             if (pixels[493] <= 2):  Label=1; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 137:
             if (pixels[183] <= 2):  Label=1; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 140:
             if (pixels[515] <= 1): clock_counter = clock_counter+1; state=141; 
             else: state=144; clock_counter = clock_counter+1;
    case 141:
             if (pixels[545] <= 210):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 144:
             if (pixels[681] <= 3):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 147:
             if (pixels[713] <= 8): clock_counter = clock_counter+1; state=148; 
             else: state=155; clock_counter = clock_counter+1;
    case 148:
             if (pixels[320] <= 64): clock_counter = clock_counter+1; state=149; 
             else: state=152; clock_counter = clock_counter+1;
    case 149:
             if (pixels[487] <= 9):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 152:
             if (pixels[325] <= 4):  Label=1; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 155:
             if (pixels[601] <= 14): clock_counter = clock_counter+1; state=156; 
             else: state=159; clock_counter = clock_counter+1;
    case 156:
             if (pixels[210] <= 250):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 159:
             if (pixels[348] <= 26):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 162:
             if (pixels[372] <= 3): clock_counter = clock_counter+1; state=163; 
             else: state=178; clock_counter = clock_counter+1;
    case 163:
             if (pixels[685] <= 0): clock_counter = clock_counter+1; state=164; 
             else: state=171; clock_counter = clock_counter+1;
    case 164:
             if (pixels[460] <= 8): clock_counter = clock_counter+1; state=165; 
             else: state=168; clock_counter = clock_counter+1;
    case 165:
             if (pixels[490] <= 58):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 168:
             if (pixels[320] <= 84):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 171:
             if (pixels[543] <= 106): clock_counter = clock_counter+1; state=172; 
             else: state=175; clock_counter = clock_counter+1;
    case 172:
             if (pixels[265] <= 78):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 175:
             if (pixels[349] <= 15):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 178:
             if (pixels[542] <= 49): clock_counter = clock_counter+1; state=179; 
             else: state=186; clock_counter = clock_counter+1;
    case 179:
             if (pixels[439] <= 155): clock_counter = clock_counter+1; state=180; 
             else: state=183; clock_counter = clock_counter+1;
    case 180:
             if (pixels[378] <= 1):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 183:
             if (pixels[268] <= 24):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 186:
             if (pixels[213] <= 14): clock_counter = clock_counter+1; state=187; 
             else: state=190; clock_counter = clock_counter+1;
    case 187:
             if (pixels[294] <= 243):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 190:
             if (pixels[302] <= 15):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 193:
             if (pixels[351] <= 21): clock_counter = clock_counter+1; state=194; 
             else: state=225; clock_counter = clock_counter+1;
    case 194:
             if (pixels[515] <= 48): clock_counter = clock_counter+1; state=195; 
             else: state=210; clock_counter = clock_counter+1;
    case 195:
             if (pixels[468] <= 7): clock_counter = clock_counter+1; state=196; 
             else: state=203; clock_counter = clock_counter+1;
    case 196:
             if (pixels[151] <= 32): clock_counter = clock_counter+1; state=197; 
             else: state=200; clock_counter = clock_counter+1;
    case 197:
             if (pixels[513] <= 245):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 200:
             if (pixels[235] <= 25):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 203:
             if (pixels[464] <= 25): clock_counter = clock_counter+1; state=204; 
             else: state=207; clock_counter = clock_counter+1;
    case 204:
             if (pixels[401] <= 138):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 207:
             if (pixels[567] <= 84):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 210:
             if (pixels[273] <= 9): clock_counter = clock_counter+1; state=211; 
             else: state=218; clock_counter = clock_counter+1;
    case 211:
             if (pixels[661] <= 27): clock_counter = clock_counter+1; state=212; 
             else: state=215; clock_counter = clock_counter+1;
    case 212:
             if (pixels[176] <= 5):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 215:
             if (pixels[400] <= 12):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 218:
             if (pixels[156] <= 109): clock_counter = clock_counter+1; state=219; 
             else: state=222; clock_counter = clock_counter+1;
    case 219:
             if (pixels[354] <= 58):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 222:
             if (pixels[495] <= 1):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 225:
             if (pixels[290] <= 0): clock_counter = clock_counter+1; state=226; 
             else: state=241; clock_counter = clock_counter+1;
    case 226:
             if (pixels[544] <= 5): clock_counter = clock_counter+1; state=227; 
             else: state=234; clock_counter = clock_counter+1;
    case 227:
             if (pixels[513] <= 12): clock_counter = clock_counter+1; state=228; 
             else: state=231; clock_counter = clock_counter+1;
    case 228:
             if (pixels[292] <= 114):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 231:
             if (pixels[657] <= 10):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 234:
             if (pixels[526] <= 11): clock_counter = clock_counter+1; state=235; 
             else: state=238; clock_counter = clock_counter+1;
    case 235:
             if (pixels[275] <= 6):  Label=1; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 238:
             if (pixels[342] <= 24):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 241:
             if (pixels[384] <= 11): clock_counter = clock_counter+1; state=242; 
             else: state=249; clock_counter = clock_counter+1;
    case 242:
             if (pixels[487] <= 1): clock_counter = clock_counter+1; state=243; 
             else: state=246; clock_counter = clock_counter+1;
    case 243:
             if (pixels[521] <= 1):  Label=9; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 246:
             if (pixels[498] <= 28):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 249:
             if (pixels[655] <= 7): clock_counter = clock_counter+1; state=250; 
             else: state=253; clock_counter = clock_counter+1;
    case 250:
             if (pixels[572] <= 10):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 253:
             if (pixels[354] <= 119):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 256:
             if (pixels[155] <= 0): clock_counter = clock_counter+1; state=257; 
             else: state=372; clock_counter = clock_counter+1;
    case 257:
             if (pixels[239] <= 0): clock_counter = clock_counter+1; state=258; 
             else: state=309; clock_counter = clock_counter+1;
    case 258:
             if (pixels[96] <= 0): clock_counter = clock_counter+1; state=259; 
             else: state=290; clock_counter = clock_counter+1;
    case 259:
             if (pixels[183] <= 82): clock_counter = clock_counter+1; state=260; 
             else: state=275; clock_counter = clock_counter+1;
    case 260:
             if (pixels[322] <= 12): clock_counter = clock_counter+1; state=261; 
             else: state=268; clock_counter = clock_counter+1;
    case 261:
             if (pixels[542] <= 139): clock_counter = clock_counter+1; state=262; 
             else: state=265; clock_counter = clock_counter+1;
    case 262:
             if (pixels[267] <= 120):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 265:
             if (pixels[243] <= 0):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 268:
             if (pixels[405] <= 0): clock_counter = clock_counter+1; state=269; 
             else: state=272; clock_counter = clock_counter+1;
    case 269:
             if (pixels[290] <= 27):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 272:
             if (pixels[402] <= 16):  Label=1; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 275:
             if (pixels[492] <= 11): clock_counter = clock_counter+1; state=276; 
             else: state=283; clock_counter = clock_counter+1;
    case 276:
             if (pixels[326] <= 4): clock_counter = clock_counter+1; state=277; 
             else: state=280; clock_counter = clock_counter+1;
    case 277:
             if (pixels[269] <= 117):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 280:
             if (pixels[438] <= 16):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 283:
             if (pixels[203] <= 5): clock_counter = clock_counter+1; state=284; 
             else: state=287; clock_counter = clock_counter+1;
    case 284:
             if (pixels[184] <= 1):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 287:
             if (pixels[539] <= 14):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 290:
             if (pixels[215] <= 2): clock_counter = clock_counter+1; state=291; 
             else: state=302; clock_counter = clock_counter+1;
    case 291:
             if (pixels[575] <= 13): clock_counter = clock_counter+1; state=292; 
             else: state=297; clock_counter = clock_counter+1;
    case 292:
             if (pixels[373] <= 203): clock_counter = clock_counter+1; state=293; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 293:
             if (pixels[491] <= 246):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 297:
             if (pixels[191] <= 28): clock_counter = clock_counter+1; state=298; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 298:
             if (pixels[266] <= 191):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 302:
             if (pixels[544] <= 17): clock_counter = clock_counter+1; state=303; 
             else: state=306; clock_counter = clock_counter+1;
    case 303:
             if (pixels[599] <= 73):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 306:
             if (pixels[370] <= 42):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 309:
             if (pixels[432] <= 0): clock_counter = clock_counter+1; state=310; 
             else: state=341; clock_counter = clock_counter+1;
    case 310:
             if (pixels[377] <= 0): clock_counter = clock_counter+1; state=311; 
             else: state=326; clock_counter = clock_counter+1;
    case 311:
             if (pixels[486] <= 18): clock_counter = clock_counter+1; state=312; 
             else: state=319; clock_counter = clock_counter+1;
    case 312:
             if (pixels[539] <= 9): clock_counter = clock_counter+1; state=313; 
             else: state=316; clock_counter = clock_counter+1;
    case 313:
             if (pixels[581] <= 23):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 316:
             if (pixels[624] <= 111):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 319:
             if (pixels[428] <= 0): clock_counter = clock_counter+1; state=320; 
             else: state=323; clock_counter = clock_counter+1;
    case 320:
             if (pixels[570] <= 123):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 323:
             if (pixels[209] <= 11):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 326:
             if (pixels[218] <= 4): clock_counter = clock_counter+1; state=327; 
             else: state=334; clock_counter = clock_counter+1;
    case 327:
             if (pixels[491] <= 15): clock_counter = clock_counter+1; state=328; 
             else: state=331; clock_counter = clock_counter+1;
    case 328:
             if (pixels[176] <= 2):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 331:
             if (pixels[294] <= 164):  Label=9; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 334:
             if (pixels[328] <= 6): clock_counter = clock_counter+1; state=335; 
             else: state=338; clock_counter = clock_counter+1;
    case 335:
             if (pixels[298] <= 217):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 338:
             if (pixels[456] <= 141):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 341:
             if (pixels[569] <= 0): clock_counter = clock_counter+1; state=342; 
             else: state=357; clock_counter = clock_counter+1;
    case 342:
             if (pixels[317] <= 0): clock_counter = clock_counter+1; state=343; 
             else: state=350; clock_counter = clock_counter+1;
    case 343:
             if (pixels[178] <= 4): clock_counter = clock_counter+1; state=344; 
             else: state=347; clock_counter = clock_counter+1;
    case 344:
             if (pixels[319] <= 187):  Label=9; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 347:
             if (pixels[343] <= 66):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 350:
             if (pixels[237] <= 18): clock_counter = clock_counter+1; state=351; 
             else: state=354; clock_counter = clock_counter+1;
    case 351:
             if (pixels[182] <= 76):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 354:
             if (pixels[191] <= 4):  Label=9; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 357:
             if (pixels[104] <= 2): clock_counter = clock_counter+1; state=358; 
             else: state=365; clock_counter = clock_counter+1;
    case 358:
             if (pixels[488] <= 9): clock_counter = clock_counter+1; state=359; 
             else: state=362; clock_counter = clock_counter+1;
    case 359:
             if (pixels[354] <= 9):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 362:
             if (pixels[657] <= 2):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 365:
             if (pixels[271] <= 25): clock_counter = clock_counter+1; state=366; 
             else: state=369; clock_counter = clock_counter+1;
    case 366:
             if (pixels[235] <= 22):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 369:
             if (pixels[350] <= 1):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 372:
             if (pixels[656] <= 2): clock_counter = clock_counter+1; state=373; 
             else: state=436; clock_counter = clock_counter+1;
    case 373:
             if (pixels[319] <= 0): clock_counter = clock_counter+1; state=374; 
             else: state=405; clock_counter = clock_counter+1;
    case 374:
             if (pixels[344] <= 43): clock_counter = clock_counter+1; state=375; 
             else: state=390; clock_counter = clock_counter+1;
    case 375:
             if (pixels[321] <= 9): clock_counter = clock_counter+1; state=376; 
             else: state=383; clock_counter = clock_counter+1;
    case 376:
             if (pixels[489] <= 0): clock_counter = clock_counter+1; state=377; 
             else: state=380; clock_counter = clock_counter+1;
    case 377:
             if (pixels[351] <= 38):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 380:
             if (pixels[342] <= 54):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 383:
             if (pixels[487] <= 19): clock_counter = clock_counter+1; state=384; 
             else: state=387; clock_counter = clock_counter+1;
    case 384:
             if (pixels[265] <= 123):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 387:
             if (pixels[324] <= 101):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 390:
             if (pixels[180] <= 1): clock_counter = clock_counter+1; state=391; 
             else: state=398; clock_counter = clock_counter+1;
    case 391:
             if (pixels[296] <= 5): clock_counter = clock_counter+1; state=392; 
             else: state=395; clock_counter = clock_counter+1;
    case 392:
             if (pixels[243] <= 9):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 395:
             if (pixels[570] <= 17):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 398:
             if (pixels[99] <= 0): clock_counter = clock_counter+1; state=399; 
             else: state=402; clock_counter = clock_counter+1;
    case 399:
             if (pixels[601] <= 5):  Label=9; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 402:
             if (pixels[242] <= 5):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 405:
             if (pixels[270] <= 3): clock_counter = clock_counter+1; state=406; 
             else: state=421; clock_counter = clock_counter+1;
    case 406:
             if (pixels[572] <= 0): clock_counter = clock_counter+1; state=407; 
             else: state=414; clock_counter = clock_counter+1;
    case 407:
             if (pixels[520] <= 56): clock_counter = clock_counter+1; state=408; 
             else: state=411; clock_counter = clock_counter+1;
    case 408:
             if (pixels[101] <= 49):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 411:
             if (pixels[349] <= 195):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 414:
             if (pixels[623] <= 0): clock_counter = clock_counter+1; state=415; 
             else: state=418; clock_counter = clock_counter+1;
    case 415:
             if (pixels[430] <= 0):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 418:
             if (pixels[273] <= 10):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 421:
             if (pixels[571] <= 1): clock_counter = clock_counter+1; state=422; 
             else: state=429; clock_counter = clock_counter+1;
    case 422:
             if (pixels[293] <= 10): clock_counter = clock_counter+1; state=423; 
             else: state=426; clock_counter = clock_counter+1;
    case 423:
             if (pixels[182] <= 125):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 426:
             if (pixels[402] <= 8):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 429:
             if (pixels[462] <= 98): clock_counter = clock_counter+1; state=430; 
             else: state=433; clock_counter = clock_counter+1;
    case 430:
             if (pixels[351] <= 88):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 433:
             if (pixels[374] <= 13):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 436:
             if (pixels[488] <= 1): clock_counter = clock_counter+1; state=437; 
             else: state=468; clock_counter = clock_counter+1;
    case 437:
             if (pixels[290] <= 23): clock_counter = clock_counter+1; state=438; 
             else: state=453; clock_counter = clock_counter+1;
    case 438:
             if (pixels[296] <= 0): clock_counter = clock_counter+1; state=439; 
             else: state=446; clock_counter = clock_counter+1;
    case 439:
             if (pixels[299] <= 1): clock_counter = clock_counter+1; state=440; 
             else: state=443; clock_counter = clock_counter+1;
    case 440:
             if (pixels[267] <= 49):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 443:
             if (pixels[380] <= 129):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 446:
             if (pixels[485] <= 197): clock_counter = clock_counter+1; state=447; 
             else: state=450; clock_counter = clock_counter+1;
    case 447:
             if (pixels[378] <= 2):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 450:
             if (pixels[379] <= 22):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 453:
             if (pixels[298] <= 0): clock_counter = clock_counter+1; state=454; 
             else: state=461; clock_counter = clock_counter+1;
    case 454:
             if (pixels[267] <= 139): clock_counter = clock_counter+1; state=455; 
             else: state=458; clock_counter = clock_counter+1;
    case 455:
             if (pixels[328] <= 107):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 458:
             if (pixels[188] <= 28):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 461:
             if (pixels[379] <= 0): clock_counter = clock_counter+1; state=462; 
             else: state=465; clock_counter = clock_counter+1;
    case 462:
             if (pixels[457] <= 23):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 465:
             if (pixels[485] <= 69):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 468:
             if (pixels[376] <= 0): clock_counter = clock_counter+1; state=469; 
             else: state=484; clock_counter = clock_counter+1;
    case 469:
             if (pixels[321] <= 58): clock_counter = clock_counter+1; state=470; 
             else: state=477; clock_counter = clock_counter+1;
    case 470:
             if (pixels[373] <= 7): clock_counter = clock_counter+1; state=471; 
             else: state=474; clock_counter = clock_counter+1;
    case 471:
             if (pixels[569] <= 4):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 474:
             if (pixels[185] <= 11):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 477:
             if (pixels[267] <= 244): clock_counter = clock_counter+1; state=478; 
             else: state=481; clock_counter = clock_counter+1;
    case 478:
             if (pixels[406] <= 1):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 481:
             if (pixels[486] <= 24):  Label=1; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 484:
             if (pixels[295] <= 245): clock_counter = clock_counter+1; state=485; 
             else: state=492; clock_counter = clock_counter+1;
    case 485:
             if (pixels[407] <= 0): clock_counter = clock_counter+1; state=486; 
             else: state=489; clock_counter = clock_counter+1;
    case 486:
             if (pixels[462] <= 103):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 489:
             if (pixels[515] <= 8):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 492:
             if (pixels[494] <= 1): clock_counter = clock_counter+1; state=493; 
             else: state=496; clock_counter = clock_counter+1;
    case 493:
             if (pixels[545] <= 224):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 496:
             if (pixels[383] <= 249):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case _:
           import random; Label=random.randint(0,9); state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
 return (Label,clock_counter)
