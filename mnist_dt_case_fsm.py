def inference_rate(pixels):
 clock_counter=0; state=0; Label=10; ml_inference_completed=0; #assigning dummy default label to 10
 while(Label == 10):
  match state:
    case 0:
           if (pixels[350] <= 124): clock_counter = clock_counter+1; state=1; 
           else: state=252; clock_counter = clock_counter+1;
    case 1:
           if (pixels[568] <= 0): clock_counter = clock_counter+1; state=2; 
           else: state=127; clock_counter = clock_counter+1;
    case 2:
           if (pixels[430] <= 0): clock_counter = clock_counter+1; state=3; 
           else: state=66; clock_counter = clock_counter+1;
    case 3:
           if (pixels[405] <= 1): clock_counter = clock_counter+1; state=4; 
           else: state=35; clock_counter = clock_counter+1;
    case 4:
           if (pixels[484] <= 56): clock_counter = clock_counter+1; state=5; 
           else: state=20; clock_counter = clock_counter+1;
    case 5:
           if (pixels[154] <= 0): clock_counter = clock_counter+1; state=6; 
           else: state=13; clock_counter = clock_counter+1;
    case 6:
           if (pixels[594] <= 21): clock_counter = clock_counter+1; state=7; 
           else: state=10; clock_counter = clock_counter+1;
    case 7:
           if (pixels[156] <= 0):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
           else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 10:
            if (pixels[491] <= 55):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 13:
            if (pixels[454] <= 15): clock_counter = clock_counter+1; state=14; 
            else: state=17; clock_counter = clock_counter+1;
    case 14:
            if (pixels[571] <= 4):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 17:
            if (pixels[408] <= 1):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 20:
            if (pixels[211] <= 53): clock_counter = clock_counter+1; state=21; 
            else: state=28; clock_counter = clock_counter+1;
    case 21:
            if (pixels[487] <= 135): clock_counter = clock_counter+1; state=22; 
            else: state=25; clock_counter = clock_counter+1;
    case 22:
            if (pixels[572] <= 66):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 25:
            if (pixels[399] <= 2):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 28:
            if (pixels[437] <= 1): clock_counter = clock_counter+1; state=29; 
            else: state=32; clock_counter = clock_counter+1;
    case 29:
            if (pixels[489] <= 15):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 32:
            if (pixels[427] <= 1):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 35:
            if (pixels[516] <= 7): clock_counter = clock_counter+1; state=36; 
            else: state=51; clock_counter = clock_counter+1;
    case 36:
            if (pixels[353] <= 2): clock_counter = clock_counter+1; state=37; 
            else: state=44; clock_counter = clock_counter+1;
    case 37:
            if (pixels[322] <= 12): clock_counter = clock_counter+1; state=38; 
            else: state=41; clock_counter = clock_counter+1;
    case 38:
            if (pixels[355] <= 12):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 41:
            if (pixels[546] <= 2):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 44:
            if (pixels[346] <= 1): clock_counter = clock_counter+1; state=45; 
            else: state=48; clock_counter = clock_counter+1;
    case 45:
            if (pixels[652] <= 59):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 48:
            if (pixels[210] <= 6):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 51:
            if (pixels[376] <= 3): clock_counter = clock_counter+1; state=52; 
            else: state=59; clock_counter = clock_counter+1;
    case 52:
            if (pixels[208] <= 1): clock_counter = clock_counter+1; state=53; 
            else: state=56; clock_counter = clock_counter+1;
    case 53:
            if (pixels[261] <= 4):  Label=1; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 56:
            if (pixels[484] <= 6):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 59:
            if (pixels[658] <= 5): clock_counter = clock_counter+1; state=60; 
            else: state=63; clock_counter = clock_counter+1;
    case 60:
            if (pixels[326] <= 1):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 63:
            if (pixels[434] <= 87):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 66:
            if (pixels[211] <= 28): clock_counter = clock_counter+1; state=67; 
            else: state=96; clock_counter = clock_counter+1;
    case 67:
            if (pixels[98] <= 0): clock_counter = clock_counter+1; state=68; 
            else: state=83; clock_counter = clock_counter+1;
    case 68:
            if (pixels[267] <= 128): clock_counter = clock_counter+1; state=69; 
            else: state=76; clock_counter = clock_counter+1;
    case 69:
            if (pixels[95] <= 1): clock_counter = clock_counter+1; state=70; 
            else: state=73; clock_counter = clock_counter+1;
    case 70:
            if (pixels[155] <= 78):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 73:
            if (pixels[575] <= 10):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 76:
            if (pixels[381] <= 2): clock_counter = clock_counter+1; state=77; 
            else: state=80; clock_counter = clock_counter+1;
    case 77:
            if (pixels[412] <= 3):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=7; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 80:
            if (pixels[405] <= 9):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 83:
            if (pixels[242] <= 7): clock_counter = clock_counter+1; state=84; 
            else: state=89; clock_counter = clock_counter+1;
    case 84:
            if (pixels[595] <= 14): clock_counter = clock_counter+1; state=85; 
            else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 85:
            if (pixels[240] <= 1):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 89:
            if (pixels[263] <= 65): clock_counter = clock_counter+1; state=90; 
            else: state=93; clock_counter = clock_counter+1;
    case 90:
            if (pixels[238] <= 124):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 93:
            if (pixels[436] <= 13):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 96:
            if (pixels[156] <= 0): clock_counter = clock_counter+1; state=97; 
            else: state=112; clock_counter = clock_counter+1;
    case 97:
            if (pixels[381] <= 2): clock_counter = clock_counter+1; state=98; 
            else: state=105; clock_counter = clock_counter+1;
    case 98:
            if (pixels[217] <= 3): clock_counter = clock_counter+1; state=99; 
            else: state=102; clock_counter = clock_counter+1;
    case 99:
            if (pixels[542] <= 68):  Label=9; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 102:
             if (pixels[357] <= 6):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 105:
             if (pixels[154] <= 2): clock_counter = clock_counter+1; state=106; 
             else: state=109; clock_counter = clock_counter+1;
    case 106:
             if (pixels[470] <= 0):  Label=9; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 109:
             if (pixels[292] <= 82):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 112:
             if (pixels[101] <= 1): clock_counter = clock_counter+1; state=113; 
             else: state=120; clock_counter = clock_counter+1;
    case 113:
             if (pixels[656] <= 1): clock_counter = clock_counter+1; state=114; 
             else: state=117; clock_counter = clock_counter+1;
    case 114:
             if (pixels[572] <= 1):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 117:
             if (pixels[326] <= 0):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 120:
             if (pixels[271] <= 136): clock_counter = clock_counter+1; state=121; 
             else: state=124; clock_counter = clock_counter+1;
    case 121:
             if (pixels[296] <= 146):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 124:
             if (pixels[408] <= 7):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 127:
             if (pixels[435] <= 0): clock_counter = clock_counter+1; state=128; 
             else: state=189; clock_counter = clock_counter+1;
    case 128:
             if (pixels[489] <= 48): clock_counter = clock_counter+1; state=129; 
             else: state=160; clock_counter = clock_counter+1;
    case 129:
             if (pixels[380] <= 2): clock_counter = clock_counter+1; state=130; 
             else: state=145; clock_counter = clock_counter+1;
    case 130:
             if (pixels[324] <= 177): clock_counter = clock_counter+1; state=131; 
             else: state=138; clock_counter = clock_counter+1;
    case 131:
             if (pixels[214] <= 0): clock_counter = clock_counter+1; state=132; 
             else: state=135; clock_counter = clock_counter+1;
    case 132:
             if (pixels[464] <= 2):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 135:
             if (pixels[717] <= 40):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 138:
             if (pixels[427] <= 74): clock_counter = clock_counter+1; state=139; 
             else: state=142; clock_counter = clock_counter+1;
    case 139:
             if (pixels[241] <= 1):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 142:
             if (pixels[102] <= 3):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 145:
             if (pixels[298] <= 104): clock_counter = clock_counter+1; state=146; 
             else: state=153; clock_counter = clock_counter+1;
    case 146:
             if (pixels[485] <= 93): clock_counter = clock_counter+1; state=147; 
             else: state=150; clock_counter = clock_counter+1;
    case 147:
             if (pixels[376] <= 74):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 150:
             if (pixels[655] <= 89):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 153:
             if (pixels[456] <= 18): clock_counter = clock_counter+1; state=154; 
             else: state=157; clock_counter = clock_counter+1;
    case 154:
             if (pixels[397] <= 16):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 157:
             if (pixels[239] <= 10):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 160:
             if (pixels[320] <= 1): clock_counter = clock_counter+1; state=161; 
             else: state=176; clock_counter = clock_counter+1;
    case 161:
             if (pixels[344] <= 61): clock_counter = clock_counter+1; state=162; 
             else: state=169; clock_counter = clock_counter+1;
    case 162:
             if (pixels[685] <= 20): clock_counter = clock_counter+1; state=163; 
             else: state=166; clock_counter = clock_counter+1;
    case 163:
             if (pixels[343] <= 124):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 166:
             if (pixels[458] <= 170):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 169:
             if (pixels[599] <= 6): clock_counter = clock_counter+1; state=170; 
             else: state=173; clock_counter = clock_counter+1;
    case 170:
             if (pixels[210] <= 10):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 173:
             if (pixels[511] <= 248):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 176:
             if (pixels[358] <= 169): clock_counter = clock_counter+1; state=177; 
             else: state=184; clock_counter = clock_counter+1;
    case 177:
             if (pixels[513] <= 71): clock_counter = clock_counter+1; state=178; 
             else: state=181; clock_counter = clock_counter+1;
    case 178:
             if (pixels[383] <= 20):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 181:
             if (pixels[405] <= 225):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 184:
             if (pixels[400] <= 36): clock_counter = clock_counter+1; state=185; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 185:
             if (pixels[550] <= 126):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 189:
             if (pixels[346] <= 0): clock_counter = clock_counter+1; state=190; 
             else: state=221; clock_counter = clock_counter+1;
    case 190:
             if (pixels[348] <= 98): clock_counter = clock_counter+1; state=191; 
             else: state=206; clock_counter = clock_counter+1;
    case 191:
             if (pixels[371] <= 97): clock_counter = clock_counter+1; state=192; 
             else: state=199; clock_counter = clock_counter+1;
    case 192:
             if (pixels[679] <= 0): clock_counter = clock_counter+1; state=193; 
             else: state=196; clock_counter = clock_counter+1;
    case 193:
             if (pixels[517] <= 8):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 196:
             if (pixels[157] <= 15):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 199:
             if (pixels[213] <= 1): clock_counter = clock_counter+1; state=200; 
             else: state=203; clock_counter = clock_counter+1;
    case 200:
             if (pixels[244] <= 99):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 203:
             if (pixels[487] <= 139):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 206:
             if (pixels[353] <= 1): clock_counter = clock_counter+1; state=207; 
             else: state=214; clock_counter = clock_counter+1;
    case 207:
             if (pixels[513] <= 95): clock_counter = clock_counter+1; state=208; 
             else: state=211; clock_counter = clock_counter+1;
    case 208:
             if (pixels[150] <= 52):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 211:
             if (pixels[130] <= 28):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 214:
             if (pixels[466] <= 30): clock_counter = clock_counter+1; state=215; 
             else: state=218; clock_counter = clock_counter+1;
    case 215:
             if (pixels[405] <= 51):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 218:
             if (pixels[298] <= 8):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 221:
             if (pixels[655] <= 0): clock_counter = clock_counter+1; state=222; 
             else: state=237; clock_counter = clock_counter+1;
    case 222:
             if (pixels[271] <= 1): clock_counter = clock_counter+1; state=223; 
             else: state=230; clock_counter = clock_counter+1;
    case 223:
             if (pixels[484] <= 5): clock_counter = clock_counter+1; state=224; 
             else: state=227; clock_counter = clock_counter+1;
    case 224:
             if (pixels[516] <= 49):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 227:
             if (pixels[218] <= 11):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 230:
             if (pixels[354] <= 10): clock_counter = clock_counter+1; state=231; 
             else: state=234; clock_counter = clock_counter+1;
    case 231:
             if (pixels[357] <= 4):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 234:
             if (pixels[156] <= 6):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 237:
             if (pixels[354] <= 0): clock_counter = clock_counter+1; state=238; 
             else: state=245; clock_counter = clock_counter+1;
    case 238:
             if (pixels[514] <= 76): clock_counter = clock_counter+1; state=239; 
             else: state=242; clock_counter = clock_counter+1;
    case 239:
             if (pixels[357] <= 9):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 242:
             if (pixels[384] <= 162):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 245:
             if (pixels[434] <= 41): clock_counter = clock_counter+1; state=246; 
             else: state=249; clock_counter = clock_counter+1;
    case 246:
             if (pixels[484] <= 6):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 249:
             if (pixels[487] <= 2):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 252:
             if (pixels[489] <= 39): clock_counter = clock_counter+1; state=253; 
             else: state=380; clock_counter = clock_counter+1;
    case 253:
             if (pixels[290] <= 34): clock_counter = clock_counter+1; state=254; 
             else: state=317; clock_counter = clock_counter+1;
    case 254:
             if (pixels[486] <= 58): clock_counter = clock_counter+1; state=255; 
             else: state=286; clock_counter = clock_counter+1;
    case 255:
             if (pixels[490] <= 120): clock_counter = clock_counter+1; state=256; 
             else: state=271; clock_counter = clock_counter+1;
    case 256:
             if (pixels[315] <= 61): clock_counter = clock_counter+1; state=257; 
             else: state=264; clock_counter = clock_counter+1;
    case 257:
             if (pixels[180] <= 0): clock_counter = clock_counter+1; state=258; 
             else: state=261; clock_counter = clock_counter+1;
    case 258:
             if (pixels[125] <= 11):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 261:
             if (pixels[264] <= 149):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 264:
             if (pixels[627] <= 5): clock_counter = clock_counter+1; state=265; 
             else: state=268; clock_counter = clock_counter+1;
    case 265:
             if (pixels[208] <= 86):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 268:
             if (pixels[296] <= 76):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 271:
             if (pixels[297] <= 2): clock_counter = clock_counter+1; state=272; 
             else: state=279; clock_counter = clock_counter+1;
    case 272:
             if (pixels[215] <= 5): clock_counter = clock_counter+1; state=273; 
             else: state=276; clock_counter = clock_counter+1;
    case 273:
             if (pixels[410] <= 47):  Label=1; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 276:
             if (pixels[354] <= 76):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 279:
             if (pixels[155] <= 4): clock_counter = clock_counter+1; state=280; 
             else: state=283; clock_counter = clock_counter+1;
    case 280:
             if (pixels[569] <= 8):  Label=9; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 283:
             if (pixels[487] <= 96):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 286:
             if (pixels[656] <= 0): clock_counter = clock_counter+1; state=287; 
             else: state=302; clock_counter = clock_counter+1;
    case 287:
             if (pixels[152] <= 8): clock_counter = clock_counter+1; state=288; 
             else: state=295; clock_counter = clock_counter+1;
    case 288:
             if (pixels[601] <= 82): clock_counter = clock_counter+1; state=289; 
             else: state=292; clock_counter = clock_counter+1;
    case 289:
             if (pixels[161] <= 9):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 292:
             if (pixels[243] <= 26):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 295:
             if (pixels[383] <= 1): clock_counter = clock_counter+1; state=296; 
             else: state=299; clock_counter = clock_counter+1;
    case 296:
             if (pixels[465] <= 11):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 299:
             if (pixels[487] <= 117):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 302:
             if (pixels[467] <= 65): clock_counter = clock_counter+1; state=303; 
             else: state=310; clock_counter = clock_counter+1;
    case 303:
             if (pixels[463] <= 2): clock_counter = clock_counter+1; state=304; 
             else: state=307; clock_counter = clock_counter+1;
    case 304:
             if (pixels[409] <= 23):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 307:
             if (pixels[459] <= 53):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 310:
             if (pixels[179] <= 5): clock_counter = clock_counter+1; state=311; 
             else: state=314; clock_counter = clock_counter+1;
    case 311:
             if (pixels[329] <= 13):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 314:
             if (pixels[316] <= 21):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 317:
             if (pixels[297] <= 5): clock_counter = clock_counter+1; state=318; 
             else: state=349; clock_counter = clock_counter+1;
    case 318:
             if (pixels[486] <= 58): clock_counter = clock_counter+1; state=319; 
             else: state=334; clock_counter = clock_counter+1;
    case 319:
             if (pixels[186] <= 1): clock_counter = clock_counter+1; state=320; 
             else: state=327; clock_counter = clock_counter+1;
    case 320:
             if (pixels[293] <= 217): clock_counter = clock_counter+1; state=321; 
             else: state=324; clock_counter = clock_counter+1;
    case 321:
             if (pixels[300] <= 76):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 324:
             if (pixels[463] <= 210):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 327:
             if (pixels[301] <= 2): clock_counter = clock_counter+1; state=328; 
             else: state=331; clock_counter = clock_counter+1;
    case 328:
             if (pixels[295] <= 201):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 331:
             if (pixels[381] <= 17):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 334:
             if (pixels[656] <= 12): clock_counter = clock_counter+1; state=335; 
             else: state=342; clock_counter = clock_counter+1;
    case 335:
             if (pixels[430] <= 83): clock_counter = clock_counter+1; state=336; 
             else: state=339; clock_counter = clock_counter+1;
    case 336:
             if (pixels[319] <= 251):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 339:
             if (pixels[601] <= 34):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 342:
             if (pixels[300] <= 5): clock_counter = clock_counter+1; state=343; 
             else: state=346; clock_counter = clock_counter+1;
    case 343:
             if (pixels[571] <= 43):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 346:
             if (pixels[379] <= 247):  Label=0; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 349:
             if (pixels[598] <= 0): clock_counter = clock_counter+1; state=350; 
             else: state=365; clock_counter = clock_counter+1;
    case 350:
             if (pixels[210] <= 4): clock_counter = clock_counter+1; state=351; 
             else: state=358; clock_counter = clock_counter+1;
    case 351:
             if (pixels[404] <= 9): clock_counter = clock_counter+1; state=352; 
             else: state=355; clock_counter = clock_counter+1;
    case 352:
             if (pixels[543] <= 107):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 355:
             if (pixels[266] <= 58):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 358:
             if (pixels[653] <= 69): clock_counter = clock_counter+1; state=359; 
             else: state=362; clock_counter = clock_counter+1;
    case 359:
             if (pixels[154] <= 43):  Label=9; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 362:
             if (pixels[319] <= 62):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 365:
             if (pixels[486] <= 6): clock_counter = clock_counter+1; state=366; 
             else: state=373; clock_counter = clock_counter+1;
    case 366:
             if (pixels[427] <= 168): clock_counter = clock_counter+1; state=367; 
             else: state=370; clock_counter = clock_counter+1;
    case 367:
             if (pixels[318] <= 78):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 370:
             if (pixels[267] <= 10):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 373:
             if (pixels[400] <= 30): clock_counter = clock_counter+1; state=374; 
             else: state=377; clock_counter = clock_counter+1;
    case 374:
             if (pixels[545] <= 128):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 377:
             if (pixels[241] <= 5):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 380:
             if (pixels[234] <= 0): clock_counter = clock_counter+1; state=381; 
             else: state=442; clock_counter = clock_counter+1;
    case 381:
             if (pixels[402] <= 0): clock_counter = clock_counter+1; state=382; 
             else: state=411; clock_counter = clock_counter+1;
    case 382:
             if (pixels[149] <= 2): clock_counter = clock_counter+1; state=383; 
             else: state=398; clock_counter = clock_counter+1;
    case 383:
             if (pixels[300] <= 20): clock_counter = clock_counter+1; state=384; 
             else: state=391; clock_counter = clock_counter+1;
    case 384:
             if (pixels[493] <= 159): clock_counter = clock_counter+1; state=385; 
             else: state=388; clock_counter = clock_counter+1;
    case 385:
             if (pixels[406] <= 150):  Label=1; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 388:
             if (pixels[657] <= 16):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 391:
             if (pixels[265] <= 2): clock_counter = clock_counter+1; state=392; 
             else: state=395; clock_counter = clock_counter+1;
    case 392:
             if (pixels[460] <= 249):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 395:
             if (pixels[514] <= 14):  Label=9; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 398:
             if (pixels[343] <= 2): clock_counter = clock_counter+1; state=399; 
             else: state=406; clock_counter = clock_counter+1;
    case 399:
             if (pixels[543] <= 20): clock_counter = clock_counter+1; state=400; 
             else: state=403; clock_counter = clock_counter+1;
    case 400:
             if (pixels[318] <= 13):  Label=3; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 403:
             if (pixels[290] <= 25):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 406:
             if (pixels[181] <= 100):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else: state=408; clock_counter = clock_counter+1;
    case 408:
             if (pixels[498] <= 75):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 411:
             if (pixels[103] <= 1): clock_counter = clock_counter+1; state=412; 
             else: state=427; clock_counter = clock_counter+1;
    case 412:
             if (pixels[276] <= 4): clock_counter = clock_counter+1; state=413; 
             else: state=420; clock_counter = clock_counter+1;
    case 413:
             if (pixels[522] <= 2): clock_counter = clock_counter+1; state=414; 
             else: state=417; clock_counter = clock_counter+1;
    case 414:
             if (pixels[712] <= 1):  Label=1; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 417:
             if (pixels[573] <= 188):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 420:
             if (pixels[381] <= 116): clock_counter = clock_counter+1; state=421; 
             else: state=424; clock_counter = clock_counter+1;
    case 421:
             if (pixels[187] <= 3):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 424:
             if (pixels[601] <= 97):  Label=4; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 427:
             if (pixels[271] <= 17): clock_counter = clock_counter+1; state=428; 
             else: state=435; clock_counter = clock_counter+1;
    case 428:
             if (pixels[348] <= 4): clock_counter = clock_counter+1; state=429; 
             else: state=432; clock_counter = clock_counter+1;
    case 429:
             if (pixels[317] <= 44):  Label=5; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 432:
             if (pixels[624] <= 252):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 435:
             if (pixels[293] <= 77): clock_counter = clock_counter+1; state=436; 
             else: state=439; clock_counter = clock_counter+1;
    case 436:
             if (pixels[517] <= 254):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 439:
             if (pixels[412] <= 215):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 442:
             if (pixels[658] <= 0): clock_counter = clock_counter+1; state=443; 
             else: state=474; clock_counter = clock_counter+1;
    case 443:
             if (pixels[345] <= 23): clock_counter = clock_counter+1; state=444; 
             else: state=459; clock_counter = clock_counter+1;
    case 444:
             if (pixels[514] <= 24): clock_counter = clock_counter+1; state=445; 
             else: state=452; clock_counter = clock_counter+1;
    case 445:
             if (pixels[556] <= 14): clock_counter = clock_counter+1; state=446; 
             else: state=449; clock_counter = clock_counter+1;
    case 446:
             if (pixels[603] <= 199):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 449:
             if (pixels[397] <= 52):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 452:
             if (pixels[356] <= 10): clock_counter = clock_counter+1; state=453; 
             else: state=456; clock_counter = clock_counter+1;
    case 453:
             if (pixels[683] <= 2):  Label=2; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 456:
             if (pixels[436] <= 6):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 459:
             if (pixels[575] <= 231): clock_counter = clock_counter+1; state=460; 
             else: state=467; clock_counter = clock_counter+1;
    case 460:
             if (pixels[210] <= 66): clock_counter = clock_counter+1; state=461; 
             else: state=464; clock_counter = clock_counter+1;
    case 461:
             if (pixels[406] <= 4):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 464:
             if (pixels[555] <= 9):  Label=9; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 467:
             if (pixels[239] <= 68): clock_counter = clock_counter+1; state=468; 
             else: state=471; clock_counter = clock_counter+1;
    case 468:
             if (pixels[214] <= 101):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 471:
             if (pixels[399] <= 252):  Label=6; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 474:
             if (pixels[515] <= 84): clock_counter = clock_counter+1; state=475; 
             else: state=490; clock_counter = clock_counter+1;
    case 475:
             if (pixels[545] <= 5): clock_counter = clock_counter+1; state=476; 
             else: state=483; clock_counter = clock_counter+1;
    case 476:
             if (pixels[318] <= 93): clock_counter = clock_counter+1; state=477; 
             else: state=480; clock_counter = clock_counter+1;
    case 477:
             if (pixels[210] <= 126):  Label=1; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 480:
             if (pixels[513] <= 42):  Label=9; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 483:
             if (pixels[578] <= 21): clock_counter = clock_counter+1; state=484; 
             else: state=487; clock_counter = clock_counter+1;
    case 484:
             if (pixels[295] <= 226):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 487:
             if (pixels[575] <= 250):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 490:
             if (pixels[319] <= 0): clock_counter = clock_counter+1; state=491; 
             else: state=498; clock_counter = clock_counter+1;
    case 491:
             if (pixels[344] <= 48): clock_counter = clock_counter+1; state=492; 
             else: state=495; clock_counter = clock_counter+1;
    case 492:
             if (pixels[608] <= 5):  Label=7; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 495:
             if (pixels[122] <= 5):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 498:
             if (pixels[294] <= 249): clock_counter = clock_counter+1; state=499; 
             else: state=502; clock_counter = clock_counter+1;
    case 499:
             if (pixels[743] <= 21):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
    case 502:
             if (pixels[470] <= 185):  Label=8; state=0;ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;

 return (Label,clock_counter)
