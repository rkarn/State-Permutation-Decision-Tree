def Lockedinference_rate(pixels, encoded_state_label, encoded_transition_label):
 clock_counter=0; state=0; Label=10; ml_inference_completed=0; #assigning dummy default label to 10
 while(clock_counter < 8):
  match state:
    case x if x == encoded_state_label[0]:
           if (pixels[409] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[112]; 
           else: state=encoded_transition_label[109]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[1]:
           if (pixels[434] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[50]; 
           else: state=encoded_transition_label[211]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[2]:
           if (pixels[455] <= 3): clock_counter = clock_counter+1; state=encoded_transition_label[135]; 
           else: state=encoded_transition_label[183]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[3]:
           if (pixels[324] <= 13): clock_counter = clock_counter+1; state=encoded_transition_label[144]; 
           else: state=encoded_transition_label[52]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[4]:
           if (pixels[518] <= 3): clock_counter = clock_counter+1; state=encoded_transition_label[12]; 
           else: state=encoded_transition_label[98]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[5]:
           if (pixels[183] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[101]; 
           else: state=encoded_transition_label[59]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[6]:
           if (pixels[599] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[171]; 
           else: state=encoded_transition_label[137]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[7]:
           if (pixels[467] <= 1):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
           else:  Label=7; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[8]:
            if (pixels[220] <= 3):  Label=0; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[9]:
            if (pixels[271] <= 5): clock_counter = clock_counter+1; state=encoded_transition_label[127]; 
            else: state=encoded_transition_label[110]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[10]:
            if (pixels[245] <= 5):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[11]:
            if (pixels[490] <= 36):  Label=0; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[12]:
            if (pixels[542] <= 8): clock_counter = clock_counter+1; state=encoded_transition_label[246]; 
            else: state=encoded_transition_label[4]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[13]:
            if (pixels[466] <= 54): clock_counter = clock_counter+1; state=encoded_transition_label[121]; 
            else: state=encoded_transition_label[113]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[14]:
            if (pixels[128] <= 7):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[15]:
            if (pixels[487] <= 11):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[16]:
            if (pixels[375] <= 48): clock_counter = clock_counter+1; state=encoded_transition_label[56]; 
            else: state=encoded_transition_label[102]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[17]:
            if (pixels[344] <= 5):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[18]:
            if (pixels[177] <= 5):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[19]:
            if (pixels[284] <= 2): clock_counter = clock_counter+1; state=encoded_transition_label[150]; 
            else: state=encoded_transition_label[44]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[20]:
            if (pixels[269] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[243]; 
            else: state=encoded_transition_label[58]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[21]:
            if (pixels[486] <= 163): clock_counter = clock_counter+1; state=encoded_transition_label[241]; 
            else: state=encoded_transition_label[139]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[22]:
            if (pixels[266] <= 158):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[23]:
            if (pixels[575] <= 132):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[24]:
            if (pixels[353] <= 159): clock_counter = clock_counter+1; state=encoded_transition_label[28]; 
            else: state=encoded_transition_label[153]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[25]:
            if (pixels[513] <= 84):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[26]:
            if (pixels[288] <= 175):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[27]:
            if (pixels[180] <= 36): clock_counter = clock_counter+1; state=encoded_transition_label[43]; 
            else: state=encoded_transition_label[218]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[28]:
            if (pixels[597] <= 21): clock_counter = clock_counter+1; state=encoded_transition_label[11]; 
            else: state=encoded_transition_label[125]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[29]:
            if (pixels[464] <= 205):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[30]:
            if (pixels[292] <= 17):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[31]:
            if (pixels[298] <= 228): clock_counter = clock_counter+1; state=encoded_transition_label[237]; 
            else: state=encoded_transition_label[191]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[32]:
            if (pixels[488] <= 30):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[33]:
            if (pixels[323] <= 98):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[34]:
            if (pixels[627] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[84]; 
            else: state=encoded_transition_label[160]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[35]:
            if (pixels[359] <= 27): clock_counter = clock_counter+1; state=encoded_transition_label[174]; 
            else: state=encoded_transition_label[134]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[36]:
            if (pixels[518] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[185]; 
            else: state=encoded_transition_label[170]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[37]:
            if (pixels[183] <= 3): clock_counter = clock_counter+1; state=encoded_transition_label[2]; 
            else: state=encoded_transition_label[231]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[38]:
            if (pixels[570] <= 11):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[39]:
            if (pixels[351] <= 3):  Label=0; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[40]:
            if (pixels[399] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[114]; 
            else: state=encoded_transition_label[22]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[41]:
            if (pixels[459] <= 50):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[42]:
            if (pixels[240] <= 3):  Label=4; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=9; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[43]:
            if (pixels[239] <= 4): clock_counter = clock_counter+1; state=encoded_transition_label[47]; 
            else: state=encoded_transition_label[217]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[44]:
            if (pixels[485] <= 238): clock_counter = clock_counter+1; state=encoded_transition_label[29]; 
            else: state=encoded_transition_label[35]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[45]:
            if (pixels[539] <= 35):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[46]:
            if (pixels[464] <= 224):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[47]:
            if (pixels[689] <= 200): clock_counter = clock_counter+1; state=encoded_transition_label[229]; 
            else: state=encoded_transition_label[131]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[48]:
            if (pixels[431] <= 164):  Label=0; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[49]:
            if (pixels[576] <= 14):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=9; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[50]:
            if (pixels[353] <= 144): clock_counter = clock_counter+1; state=encoded_transition_label[155]; 
            else: state=encoded_transition_label[202]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[51]:
            if (pixels[489] <= 169): clock_counter = clock_counter+1; state=encoded_transition_label[105]; 
            else: state=encoded_transition_label[206]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[52]:
             if (pixels[324] <= 163): clock_counter = clock_counter+1; state=encoded_transition_label[223]; 
             else: state=encoded_transition_label[207]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[53]:
             if (pixels[436] <= 34):  Label=0; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[54]:
             if (pixels[301] <= 5):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[55]:
             if (pixels[345] <= 27): clock_counter = clock_counter+1; state=encoded_transition_label[70]; 
             else: state=encoded_transition_label[167]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[56]:
             if (pixels[323] <= 143):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[57]:
             if (pixels[386] <= 241):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[58]:
             if (pixels[270] <= 63): clock_counter = clock_counter+1; state=encoded_transition_label[106]; 
             else: state=encoded_transition_label[92]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[59]:
             if (pixels[512] <= 181): clock_counter = clock_counter+1; state=encoded_transition_label[168]; 
             else: state=encoded_transition_label[20]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[60]:
             if (pixels[239] <= 204):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[61]:
             if (pixels[400] <= 129):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[62]:
             if (pixels[238] <= 66): clock_counter = clock_counter+1; state=encoded_transition_label[136]; 
             else: state=encoded_transition_label[41]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[63]:
             if (pixels[294] <= 13):  Label=8; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[64]:
             if (pixels[151] <= 254):  Label=0; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[65]:
             if (pixels[375] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[180]; 
             else: state=encoded_transition_label[192]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[66]:
             if (pixels[550] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[24]; 
             else: state=encoded_transition_label[145]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[67]:
             if (pixels[234] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[220]; 
             else: state=encoded_transition_label[62]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[68]:
             if (pixels[149] <= 7): clock_counter = clock_counter+1; state=encoded_transition_label[128]; 
             else: state=encoded_transition_label[74]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[69]:
             if (pixels[300] <= 15): clock_counter = clock_counter+1; state=encoded_transition_label[224]; 
             else: state=encoded_transition_label[226]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[70]:
             if (pixels[493] <= 2):  Label=1; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[71]:
             if (pixels[183] <= 2):  Label=1; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[72]:
             if (pixels[515] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[16]; 
             else: state=encoded_transition_label[130]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[73]:
             if (pixels[545] <= 210):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[74]:
             if (pixels[681] <= 3):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[75]:
             if (pixels[713] <= 8): clock_counter = clock_counter+1; state=encoded_transition_label[15]; 
             else: state=encoded_transition_label[238]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[76]:
             if (pixels[320] <= 64): clock_counter = clock_counter+1; state=encoded_transition_label[119]; 
             else: state=encoded_transition_label[63]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[77]:
             if (pixels[487] <= 9):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[78]:
             if (pixels[325] <= 4):  Label=1; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[79]:
             if (pixels[601] <= 14): clock_counter = clock_counter+1; state=encoded_transition_label[129]; 
             else: state=encoded_transition_label[6]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[80]:
             if (pixels[210] <= 250):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[81]:
             if (pixels[348] <= 26):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[82]:
             if (pixels[372] <= 3): clock_counter = clock_counter+1; state=encoded_transition_label[81]; 
             else: state=encoded_transition_label[13]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[83]:
             if (pixels[685] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[216]; 
             else: state=encoded_transition_label[210]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[84]:
             if (pixels[460] <= 8): clock_counter = clock_counter+1; state=encoded_transition_label[133]; 
             else: state=encoded_transition_label[33]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[85]:
             if (pixels[490] <= 58):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[86]:
             if (pixels[320] <= 84):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[87]:
             if (pixels[543] <= 106): clock_counter = clock_counter+1; state=encoded_transition_label[69]; 
             else: state=encoded_transition_label[1]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[88]:
             if (pixels[265] <= 78):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[89]:
             if (pixels[349] <= 15):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[90]:
             if (pixels[542] <= 49): clock_counter = clock_counter+1; state=encoded_transition_label[197]; 
             else: state=encoded_transition_label[200]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[91]:
             if (pixels[439] <= 155): clock_counter = clock_counter+1; state=encoded_transition_label[40]; 
             else: state=encoded_transition_label[122]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[92]:
             if (pixels[378] <= 1):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[93]:
             if (pixels[268] <= 24):  Label=4; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[94]:
             if (pixels[213] <= 14): clock_counter = clock_counter+1; state=encoded_transition_label[96]; 
             else: state=encoded_transition_label[201]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[95]:
             if (pixels[294] <= 243):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[96]:
             if (pixels[302] <= 15):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[97]:
             if (pixels[351] <= 21): clock_counter = clock_counter+1; state=encoded_transition_label[166]; 
             else: state=encoded_transition_label[94]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[98]:
             if (pixels[515] <= 48): clock_counter = clock_counter+1; state=encoded_transition_label[179]; 
             else: state=encoded_transition_label[228]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[99]:
             if (pixels[468] <= 7): clock_counter = clock_counter+1; state=encoded_transition_label[49]; 
             else: state=encoded_transition_label[61]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[100]:
             if (pixels[151] <= 32): clock_counter = clock_counter+1; state=encoded_transition_label[148]; 
             else: state=encoded_transition_label[181]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[101]:
             if (pixels[513] <= 245):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[102]:
             if (pixels[235] <= 25):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[103]:
             if (pixels[464] <= 25): clock_counter = clock_counter+1; state=encoded_transition_label[188]; 
             else: state=encoded_transition_label[138]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[104]:
             if (pixels[401] <= 138):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[105]:
             if (pixels[567] <= 84):  Label=4; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[106]:
             if (pixels[273] <= 9): clock_counter = clock_counter+1; state=encoded_transition_label[71]; 
             else: state=encoded_transition_label[190]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[107]:
             if (pixels[661] <= 27): clock_counter = clock_counter+1; state=encoded_transition_label[66]; 
             else: state=encoded_transition_label[111]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[108]:
             if (pixels[176] <= 5):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[109]:
             if (pixels[400] <= 12):  Label=8; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[110]:
             if (pixels[156] <= 109): clock_counter = clock_counter+1; state=encoded_transition_label[219]; 
             else: state=encoded_transition_label[7]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[111]:
             if (pixels[354] <= 58):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[112]:
             if (pixels[495] <= 1):  Label=8; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[113]:
             if (pixels[290] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[184]; 
             else: state=encoded_transition_label[187]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[114]:
             if (pixels[544] <= 5): clock_counter = clock_counter+1; state=encoded_transition_label[164]; 
             else: state=encoded_transition_label[93]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[115]:
             if (pixels[513] <= 12): clock_counter = clock_counter+1; state=encoded_transition_label[176]; 
             else: state=encoded_transition_label[239]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[116]:
             if (pixels[292] <= 114):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[117]:
             if (pixels[657] <= 10):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[118]:
             if (pixels[526] <= 11): clock_counter = clock_counter+1; state=encoded_transition_label[10]; 
             else: state=encoded_transition_label[65]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[119]:
             if (pixels[275] <= 6):  Label=1; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[120]:
             if (pixels[342] <= 24):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[121]:
             if (pixels[384] <= 11): clock_counter = clock_counter+1; state=encoded_transition_label[5]; 
             else: state=encoded_transition_label[240]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[122]:
             if (pixels[487] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[14]; 
             else: state=encoded_transition_label[209]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[123]:
             if (pixels[521] <= 1):  Label=9; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[124]:
             if (pixels[498] <= 28):  Label=8; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[125]:
             if (pixels[655] <= 7): clock_counter = clock_counter+1; state=encoded_transition_label[36]; 
             else: state=encoded_transition_label[25]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[126]:
             if (pixels[572] <= 10):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[127]:
             if (pixels[354] <= 119):  Label=0; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[128]:
             if (pixels[155] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[90]; 
             else: state=encoded_transition_label[76]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[129]:
             if (pixels[239] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[178]; 
             else: state=encoded_transition_label[95]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[130]:
             if (pixels[96] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[232]; 
             else: state=encoded_transition_label[64]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[131]:
             if (pixels[183] <= 82): clock_counter = clock_counter+1; state=encoded_transition_label[143]; 
             else: state=encoded_transition_label[169]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[132]:
             if (pixels[322] <= 12): clock_counter = clock_counter+1; state=encoded_transition_label[230]; 
             else: state=encoded_transition_label[175]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[133]:
             if (pixels[542] <= 139): clock_counter = clock_counter+1; state=encoded_transition_label[55]; 
             else: state=encoded_transition_label[21]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[134]:
             if (pixels[267] <= 120):  Label=4; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[135]:
             if (pixels[243] <= 0):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[136]:
             if (pixels[405] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[67]; 
             else: state=encoded_transition_label[124]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[137]:
             if (pixels[290] <= 27):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[138]:
             if (pixels[402] <= 16):  Label=1; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[139]:
             if (pixels[492] <= 11): clock_counter = clock_counter+1; state=encoded_transition_label[242]; 
             else: state=encoded_transition_label[141]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[140]:
             if (pixels[326] <= 4): clock_counter = clock_counter+1; state=encoded_transition_label[116]; 
             else: state=encoded_transition_label[42]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[141]:
             if (pixels[269] <= 117):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[142]:
             if (pixels[438] <= 16):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[143]:
             if (pixels[203] <= 5): clock_counter = clock_counter+1; state=encoded_transition_label[108]; 
             else: state=encoded_transition_label[45]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[144]:
             if (pixels[184] <= 1):  Label=4; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[145]:
             if (pixels[539] <= 14):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[146]:
             if (pixels[215] <= 2): clock_counter = clock_counter+1; state=encoded_transition_label[30]; 
             else: state=encoded_transition_label[60]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[147]:
             if (pixels[575] <= 13): clock_counter = clock_counter+1; state=encoded_transition_label[156]; 
             else: state=encoded_transition_label[227]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[148]:
             if (pixels[373] <= 203): clock_counter = clock_counter+1; state=encoded_transition_label[203]; 
             else:  Label=4; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[149]:
             if (pixels[491] <= 246):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[150]:
             if (pixels[191] <= 28): clock_counter = clock_counter+1; state=encoded_transition_label[214]; 
             else:  Label=4; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[151]:
             if (pixels[266] <= 191):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[152]:
             if (pixels[544] <= 17): clock_counter = clock_counter+1; state=encoded_transition_label[126]; 
             else: state=encoded_transition_label[245]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[153]:
             if (pixels[599] <= 73):  Label=4; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[154]:
             if (pixels[370] <= 42):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[155]:
             if (pixels[432] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[117]; 
             else: state=encoded_transition_label[115]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[156]:
             if (pixels[377] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[186]; 
             else: state=encoded_transition_label[51]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[157]:
             if (pixels[486] <= 18): clock_counter = clock_counter+1; state=encoded_transition_label[26]; 
             else: state=encoded_transition_label[0]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[158]:
             if (pixels[539] <= 9): clock_counter = clock_counter+1; state=encoded_transition_label[27]; 
             else: state=encoded_transition_label[165]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[159]:
             if (pixels[581] <= 23):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[160]:
             if (pixels[624] <= 111):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[161]:
             if (pixels[428] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[151]; 
             else: state=encoded_transition_label[146]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[162]:
             if (pixels[570] <= 123):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[163]:
             if (pixels[209] <= 11):  Label=4; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[164]:
             if (pixels[218] <= 4): clock_counter = clock_counter+1; state=encoded_transition_label[247]; 
             else: state=encoded_transition_label[225]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[165]:
             if (pixels[491] <= 15): clock_counter = clock_counter+1; state=encoded_transition_label[53]; 
             else: state=encoded_transition_label[163]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[166]:
             if (pixels[176] <= 2):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[167]:
             if (pixels[294] <= 164):  Label=9; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[168]:
             if (pixels[328] <= 6): clock_counter = clock_counter+1; state=encoded_transition_label[104]; 
             else: state=encoded_transition_label[79]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[169]:
             if (pixels[298] <= 217):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[170]:
             if (pixels[456] <= 141):  Label=7; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[171]:
             if (pixels[569] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[123]; 
             else: state=encoded_transition_label[142]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[172]:
             if (pixels[317] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[37]; 
             else: state=encoded_transition_label[32]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[173]:
             if (pixels[178] <= 4): clock_counter = clock_counter+1; state=encoded_transition_label[100]; 
             else: state=encoded_transition_label[3]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[174]:
             if (pixels[319] <= 187):  Label=9; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[175]:
             if (pixels[343] <= 66):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[176]:
             if (pixels[237] <= 18): clock_counter = clock_counter+1; state=encoded_transition_label[34]; 
             else: state=encoded_transition_label[38]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[177]:
             if (pixels[182] <= 76):  Label=4; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[178]:
             if (pixels[191] <= 4):  Label=9; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[179]:
             if (pixels[104] <= 2): clock_counter = clock_counter+1; state=encoded_transition_label[48]; 
             else: state=encoded_transition_label[159]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[180]:
             if (pixels[488] <= 9): clock_counter = clock_counter+1; state=encoded_transition_label[18]; 
             else: state=encoded_transition_label[161]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[181]:
             if (pixels[354] <= 9):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[182]:
             if (pixels[657] <= 2):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[183]:
             if (pixels[271] <= 25): clock_counter = clock_counter+1; state=encoded_transition_label[68]; 
             else: state=encoded_transition_label[244]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[184]:
             if (pixels[235] <= 22):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[185]:
             if (pixels[350] <= 1):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[186]:
             if (pixels[656] <= 2): clock_counter = clock_counter+1; state=encoded_transition_label[103]; 
             else: state=encoded_transition_label[213]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[187]:
             if (pixels[319] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[120]; 
             else: state=encoded_transition_label[194]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[188]:
             if (pixels[344] <= 43): clock_counter = clock_counter+1; state=encoded_transition_label[158]; 
             else: state=encoded_transition_label[189]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[189]:
             if (pixels[321] <= 9): clock_counter = clock_counter+1; state=encoded_transition_label[173]; 
             else: state=encoded_transition_label[88]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[190]:
             if (pixels[489] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[83]; 
             else: state=encoded_transition_label[236]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[191]:
             if (pixels[351] <= 38):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[192]:
             if (pixels[342] <= 54):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[193]:
             if (pixels[487] <= 19): clock_counter = clock_counter+1; state=encoded_transition_label[77]; 
             else: state=encoded_transition_label[147]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[194]:
             if (pixels[265] <= 123):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[195]:
             if (pixels[324] <= 101):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[196]:
             if (pixels[180] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[199]; 
             else: state=encoded_transition_label[107]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[197]:
             if (pixels[296] <= 5): clock_counter = clock_counter+1; state=encoded_transition_label[72]; 
             else: state=encoded_transition_label[205]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[198]:
             if (pixels[243] <= 9):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[199]:
             if (pixels[570] <= 17):  Label=4; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[200]:
             if (pixels[99] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[78]; 
             else: state=encoded_transition_label[89]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[201]:
             if (pixels[601] <= 5):  Label=9; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[202]:
             if (pixels[242] <= 5):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[203]:
             if (pixels[270] <= 3): clock_counter = clock_counter+1; state=encoded_transition_label[172]; 
             else: state=encoded_transition_label[57]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[204]:
             if (pixels[572] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[82]; 
             else: state=encoded_transition_label[97]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[205]:
             if (pixels[520] <= 56): clock_counter = clock_counter+1; state=encoded_transition_label[86]; 
             else: state=encoded_transition_label[8]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[206]:
             if (pixels[101] <= 49):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[207]:
             if (pixels[349] <= 195):  Label=4; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[208]:
             if (pixels[623] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[73]; 
             else: state=encoded_transition_label[182]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[209]:
             if (pixels[430] <= 0):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[210]:
             if (pixels[273] <= 10):  Label=6; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[211]:
             if (pixels[571] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[215]; 
             else: state=encoded_transition_label[149]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[212]:
             if (pixels[293] <= 10): clock_counter = clock_counter+1; state=encoded_transition_label[17]; 
             else: state=encoded_transition_label[91]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[213]:
             if (pixels[182] <= 125):  Label=4; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[214]:
             if (pixels[402] <= 8):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[215]:
             if (pixels[462] <= 98): clock_counter = clock_counter+1; state=encoded_transition_label[152]; 
             else: state=encoded_transition_label[195]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[216]:
             if (pixels[351] <= 88):  Label=0; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[217]:
             if (pixels[374] <= 13):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[218]:
             if (pixels[488] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[118]; 
             else: state=encoded_transition_label[162]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[219]:
             if (pixels[290] <= 23): clock_counter = clock_counter+1; state=encoded_transition_label[248]; 
             else: state=encoded_transition_label[54]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[220]:
             if (pixels[296] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[132]; 
             else: state=encoded_transition_label[80]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[221]:
             if (pixels[299] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[23]; 
             else: state=encoded_transition_label[233]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[222]:
             if (pixels[267] <= 49):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[223]:
             if (pixels[380] <= 129):  Label=0; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[224]:
             if (pixels[485] <= 197): clock_counter = clock_counter+1; state=encoded_transition_label[46]; 
             else: state=encoded_transition_label[140]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[225]:
             if (pixels[378] <= 2):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[226]:
             if (pixels[379] <= 22):  Label=0; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[227]:
             if (pixels[298] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[31]; 
             else: state=encoded_transition_label[99]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[228]:
             if (pixels[267] <= 139): clock_counter = clock_counter+1; state=encoded_transition_label[75]; 
             else: state=encoded_transition_label[204]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[229]:
             if (pixels[328] <= 107):  Label=5; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[230]:
             if (pixels[188] <= 28):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[231]:
             if (pixels[379] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[221]; 
             else: state=encoded_transition_label[154]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[232]:
             if (pixels[457] <= 23):  Label=0; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[233]:
             if (pixels[485] <= 69):  Label=3; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[234]:
             if (pixels[376] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[193]; 
             else: state=encoded_transition_label[222]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[235]:
             if (pixels[321] <= 58): clock_counter = clock_counter+1; state=encoded_transition_label[9]; 
             else: state=encoded_transition_label[208]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[236]:
             if (pixels[373] <= 7): clock_counter = clock_counter+1; state=encoded_transition_label[196]; 
             else: state=encoded_transition_label[19]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[237]:
             if (pixels[569] <= 4):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[238]:
             if (pixels[185] <= 11):  Label=4; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[239]:
             if (pixels[267] <= 244): clock_counter = clock_counter+1; state=encoded_transition_label[198]; 
             else: state=encoded_transition_label[177]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[240]:
             if (pixels[406] <= 1):  Label=2; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[241]:
             if (pixels[486] <= 24):  Label=1; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[242]:
             if (pixels[295] <= 245): clock_counter = clock_counter+1; state=encoded_transition_label[212]; 
             else: state=encoded_transition_label[234]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[243]:
             if (pixels[407] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[157]; 
             else: state=encoded_transition_label[87]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[244]:
             if (pixels[462] <= 103):  Label=0; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[245]:
             if (pixels[515] <= 8):  Label=8; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[246]:
             if (pixels[494] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[39]; 
             else: state=encoded_transition_label[235]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[247]:
             if (pixels[545] <= 224):  Label=8; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[248]:
             if (pixels[383] <= 249):  Label=8; state=encoded_transition_label[85];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[85];ml_inference_completed=1; clock_counter = clock_counter+1;
    case _:
           import random; Label=random.randint(0,9); state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
 return (Label,clock_counter)
