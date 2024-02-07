def Lockedinference_rate(pixels, encoded_state_label, encoded_transition_label):
 clock_counter=0; state=0; Label=10; ml_inference_completed=0; #assigning dummy default label to 10
 while(Label == 10):
  match state:
    case x if x == encoded_state_label[0]:
           if (pixels[350] <= 121): clock_counter = clock_counter+1; state=encoded_transition_label[29]; 
           else: state=encoded_transition_label[22]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[1]:
           if (pixels[435] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[141]; 
           else: state=encoded_transition_label[39]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[2]:
           if (pixels[597] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[21]; 
           else: state=encoded_transition_label[185]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[3]:
           if (pixels[458] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[187]; 
           else: state=encoded_transition_label[204]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[4]:
           if (pixels[184] <= 2): clock_counter = clock_counter+1; state=encoded_transition_label[253]; 
           else: state=encoded_transition_label[155]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[5]:
           if (pixels[404] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[20]; 
           else: state=encoded_transition_label[131]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[6]:
           if (pixels[542] <= 13): clock_counter = clock_counter+1; state=encoded_transition_label[231]; 
           else: state=encoded_transition_label[27]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[7]:
           if (pixels[153] <= 29):  Label=7; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
           else:  Label=3; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[8]:
            if (pixels[387] <= 62):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[9]:
            if (pixels[354] <= 26): clock_counter = clock_counter+1; state=encoded_transition_label[163]; 
            else: state=encoded_transition_label[72]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[10]:
            if (pixels[271] <= 38):  Label=1; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[11]:
            if (pixels[238] <= 11):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[12]:
            if (pixels[538] <= 60): clock_counter = clock_counter+1; state=encoded_transition_label[172]; 
            else: state=encoded_transition_label[111]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[13]:
            if (pixels[493] <= 63): clock_counter = clock_counter+1; state=encoded_transition_label[209]; 
            else: state=encoded_transition_label[146]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[14]:
            if (pixels[484] <= 44):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[15]:
            if (pixels[629] <= 0):  Label=9; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=7; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[16]:
            if (pixels[399] <= 9): clock_counter = clock_counter+1; state=encoded_transition_label[139]; 
            else: state=encoded_transition_label[205]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[17]:
            if (pixels[517] <= 15):  Label=0; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[18]:
            if (pixels[487] <= 151):  Label=0; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=4; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[19]:
            if (pixels[571] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[97]; 
            else: state=encoded_transition_label[96]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[20]:
            if (pixels[465] <= 56): clock_counter = clock_counter+1; state=encoded_transition_label[75]; 
            else: state=encoded_transition_label[95]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[21]:
            if (pixels[495] <= 3): clock_counter = clock_counter+1; state=encoded_transition_label[230]; 
            else: state=encoded_transition_label[86]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[22]:
            if (pixels[352] <= 154):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=3; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[23]:
            if (pixels[567] <= 20):  Label=7; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[24]:
            if (pixels[239] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[199]; 
            else: state=encoded_transition_label[252]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[25]:
            if (pixels[183] <= 152):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[26]:
            if (pixels[374] <= 165):  Label=9; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=7; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[27]:
            if (pixels[270] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[114]; 
            else: state=encoded_transition_label[220]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[28]:
            if (pixels[272] <= 23): clock_counter = clock_counter+1; state=encoded_transition_label[176]; 
            else: state=encoded_transition_label[12]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[29]:
            if (pixels[296] <= 10):  Label=6; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[30]:
            if (pixels[517] <= 4):  Label=0; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=4; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[31]:
            if (pixels[490] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[25]; 
            else: state=encoded_transition_label[104]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[32]:
            if (pixels[247] <= 5):  Label=0; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[33]:
            if (pixels[442] <= 105):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[34]:
            if (pixels[489] <= 16): clock_counter = clock_counter+1; state=encoded_transition_label[53]; 
            else: state=encoded_transition_label[180]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[35]:
            if (pixels[380] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[174]; 
            else: state=encoded_transition_label[228]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[36]:
            if (pixels[324] <= 194): clock_counter = clock_counter+1; state=encoded_transition_label[213]; 
            else: state=encoded_transition_label[44]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[37]:
            if (pixels[707] <= 2): clock_counter = clock_counter+1; state=encoded_transition_label[203]; 
            else:  Label=7; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[38]:
            if (pixels[73] <= 14):  Label=0; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=6; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[39]:
            if (pixels[271] <= 4): clock_counter = clock_counter+1; state=encoded_transition_label[200]; 
            else: state=encoded_transition_label[153]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[40]:
            if (pixels[267] <= 163):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=3; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[41]:
            if (pixels[237] <= 1):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[42]:
            if (pixels[298] <= 100): clock_counter = clock_counter+1; state=encoded_transition_label[115]; 
            else: state=encoded_transition_label[46]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[43]:
            if (pixels[485] <= 116): clock_counter = clock_counter+1; state=encoded_transition_label[212]; 
            else: state=encoded_transition_label[89]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[44]:
            if (pixels[376] <= 129):  Label=3; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[45]:
            if (pixels[296] <= 118):  Label=6; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[46]:
            if (pixels[319] <= 6): clock_counter = clock_counter+1; state=encoded_transition_label[132]; 
            else: state=encoded_transition_label[125]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[47]:
            if (pixels[316] <= 204):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[48]:
            if (pixels[406] <= 87):  Label=0; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=5; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[49]:
            if (pixels[347] <= 2): clock_counter = clock_counter+1; state=encoded_transition_label[78]; 
            else: state=encoded_transition_label[188]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[50]:
            if (pixels[344] <= 108): clock_counter = clock_counter+1; state=encoded_transition_label[56]; 
            else: state=encoded_transition_label[52]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[51]:
            if (pixels[351] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[229]; 
            else: state=encoded_transition_label[245]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[52]:
            if (pixels[708] <= 16):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
            else:  Label=7; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[53]:
             if (pixels[152] <= 37):  Label=1; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[54]:
             if (pixels[442] <= 24): clock_counter = clock_counter+1; state=encoded_transition_label[226]; 
             else: state=encoded_transition_label[211]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[55]:
             if (pixels[438] <= 24):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[56]:
             if (pixels[100] <= 13):  Label=0; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[57]:
             if (pixels[385] <= 17): clock_counter = clock_counter+1; state=encoded_transition_label[99]; 
             else: state=encoded_transition_label[0]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[58]:
             if (pixels[513] <= 42): clock_counter = clock_counter+1; state=encoded_transition_label[116]; 
             else: state=encoded_transition_label[84]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[59]:
             if (pixels[514] <= 83):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[60]:
             if (pixels[406] <= 102):  Label=6; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[61]:
             if (pixels[427] <= 44): clock_counter = clock_counter+1; state=encoded_transition_label[4]; 
             else: state=encoded_transition_label[217]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[62]:
             if (pixels[273] <= 8):  Label=6; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[63]:
             if (pixels[319] <= 19):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[64]:
             if (pixels[542] <= 2): clock_counter = clock_counter+1; state=encoded_transition_label[121]; 
             else: state=encoded_transition_label[223]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[65]:
             if (pixels[432] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[33]; 
             else: state=encoded_transition_label[81]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[66]:
             if (pixels[487] <= 55): clock_counter = clock_counter+1; state=encoded_transition_label[216]; 
             else: state=encoded_transition_label[91]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[67]:
             if (pixels[405] <= 13): clock_counter = clock_counter+1; state=encoded_transition_label[158]; 
             else: state=encoded_transition_label[112]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[68]:
             if (pixels[156] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[54]; 
             else: state=encoded_transition_label[206]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[69]:
             if (pixels[153] <= 5):  Label=7; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[70]:
             if (pixels[540] <= 10):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[71]:
             if (pixels[352] <= 7): clock_counter = clock_counter+1; state=encoded_transition_label[119]; 
             else: state=encoded_transition_label[26]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[72]:
             if (pixels[322] <= 29):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[73]:
             if (pixels[376] <= 14):  Label=1; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[74]:
             if (pixels[211] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[24]; 
             else: state=encoded_transition_label[128]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[75]:
             if (pixels[96] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[48]; 
             else: state=encoded_transition_label[222]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[76]:
             if (pixels[267] <= 124):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[77]:
             if (pixels[627] <= 7):  Label=6; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[78]:
             if (pixels[428] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[201]; 
             else: state=encoded_transition_label[160]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[79]:
             if (pixels[402] <= 52):  Label=7; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[80]:
             if (pixels[209] <= 10):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[81]:
             if (pixels[211] <= 28): clock_counter = clock_counter+1; state=encoded_transition_label[191]; 
             else: state=encoded_transition_label[7]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[82]:
             if (pixels[596] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[156]; 
             else: state=encoded_transition_label[239]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[83]:
             if (pixels[267] <= 131): clock_counter = clock_counter+1; state=encoded_transition_label[173]; 
             else: state=encoded_transition_label[251]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[84]:
             if (pixels[98] <= 0):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[85]:
             if (pixels[372] <= 3):  Label=7; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[86]:
             if (pixels[319] <= 2): clock_counter = clock_counter+1; state=encoded_transition_label[197]; 
             else: state=encoded_transition_label[248]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[87]:
             if (pixels[484] <= 2):  Label=3; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[88]:
             if (pixels[512] <= 183):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[89]:
             if (pixels[353] <= 2): clock_counter = clock_counter+1; state=encoded_transition_label[10]; 
             else: state=encoded_transition_label[235]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[90]:
             if (pixels[355] <= 5): clock_counter = clock_counter+1; state=encoded_transition_label[177]; 
             else: state=encoded_transition_label[31]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[91]:
             if (pixels[215] <= 1):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[92]:
             if (pixels[538] <= 5):  Label=9; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[93]:
             if (pixels[155] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[249]; 
             else: state=encoded_transition_label[194]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[94]:
             if (pixels[345] <= 0):  Label=9; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[95]:
             if (pixels[181] <= 1):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[96]:
             if (pixels[270] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[123]; 
             else: state=encoded_transition_label[149]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[97]:
             if (pixels[245] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[88]; 
             else: state=encoded_transition_label[244]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[98]:
             if (pixels[296] <= 110): clock_counter = clock_counter+1; state=encoded_transition_label[215]; 
             else: state=encoded_transition_label[152]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[99]:
             if (pixels[656] <= 14): clock_counter = clock_counter+1; state=encoded_transition_label[175]; 
             else: state=encoded_transition_label[179]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[100]:
             if (pixels[215] <= 171):  Label=6; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[101]:
             if (pixels[328] <= 1):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[102]:
             if (pixels[319] <= 2): clock_counter = clock_counter+1; state=encoded_transition_label[157]; 
             else: state=encoded_transition_label[186]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[103]:
             if (pixels[344] <= 9):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[104]:
             if (pixels[574] <= 236):  Label=8; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[105]:
             if (pixels[655] <= 16): clock_counter = clock_counter+1; state=encoded_transition_label[85]; 
             else: state=encoded_transition_label[63]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[106]:
             if (pixels[566] <= 15): clock_counter = clock_counter+1; state=encoded_transition_label[165]; 
             else: state=encoded_transition_label[59]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[107]:
             if (pixels[214] <= 2):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[108]:
             if (pixels[320] <= 140):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[109]:
             if (pixels[428] <= 140): clock_counter = clock_counter+1; state=encoded_transition_label[247]; 
             else: state=encoded_transition_label[98]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[110]:
             if (pixels[404] <= 1):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[111]:
             if (pixels[187] <= 8):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[112]:
             if (pixels[347] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[60]; 
             else: state=encoded_transition_label[161]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[113]:
             if (pixels[155] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[118]; 
             else: state=encoded_transition_label[143]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[114]:
             if (pixels[238] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[167]; 
             else: state=encoded_transition_label[65]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[115]:
             if (pixels[456] <= 2):  Label=1; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[116]:
             if (pixels[708] <= 0):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[117]:
             if (pixels[372] <= 100): clock_counter = clock_counter+1; state=encoded_transition_label[61]; 
             else: state=encoded_transition_label[225]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[118]:
             if (pixels[349] <= 108):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[119]:
             if (pixels[657] <= 56):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[120]:
             if (pixels[657] <= 15): clock_counter = clock_counter+1; state=encoded_transition_label[9]; 
             else: state=encoded_transition_label[100]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[121]:
             if (pixels[354] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[162]; 
             else: state=encoded_transition_label[154]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[122]:
             if (pixels[488] <= 14):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[123]:
             if (pixels[212] <= 2):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[124]:
             if (pixels[428] <= 17): clock_counter = clock_counter+1; state=encoded_transition_label[224]; 
             else: state=encoded_transition_label[41]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[125]:
             if (pixels[488] <= 14):  Label=8; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[126]:
             if (pixels[598] <= 38):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[127]:
             if (pixels[489] <= 25): clock_counter = clock_counter+1; state=encoded_transition_label[107]; 
             else: state=encoded_transition_label[87]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[128]:
             if (pixels[290] <= 34): clock_counter = clock_counter+1; state=encoded_transition_label[57]; 
             else: state=encoded_transition_label[76]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[129]:
             if (pixels[486] <= 44): clock_counter = clock_counter+1; state=encoded_transition_label[145]; 
             else: state=encoded_transition_label[234]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[130]:
             if (pixels[296] <= 2): clock_counter = clock_counter+1; state=encoded_transition_label[106]; 
             else: state=encoded_transition_label[14]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[131]:
             if (pixels[490] <= 56): clock_counter = clock_counter+1; state=encoded_transition_label[242]; 
             else: state=encoded_transition_label[11]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[132]:
             if (pixels[315] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[233]; 
             else: state=encoded_transition_label[68]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[133]:
             if (pixels[177] <= 1):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[134]:
             if (pixels[328] <= 34):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[135]:
             if (pixels[600] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[93]; 
             else: state=encoded_transition_label[190]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[136]:
             if (pixels[204] <= 6):  Label=1; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[137]:
             if (pixels[355] <= 6):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[138]:
             if (pixels[153] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[124]; 
             else: state=encoded_transition_label[51]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[139]:
             if (pixels[208] <= 51): clock_counter = clock_counter+1; state=encoded_transition_label[164]; 
             else: state=encoded_transition_label[23]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[140]:
             if (pixels[539] <= 2):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[141]:
             if (pixels[316] <= 54):  Label=3; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[142]:
             if (pixels[316] <= 163): clock_counter = clock_counter+1; state=encoded_transition_label[49]; 
             else: state=encoded_transition_label[74]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[143]:
             if (pixels[490] <= 157):  Label=3; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[144]:
             if (pixels[321] <= 248):  Label=8; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[145]:
             if (pixels[657] <= 4): clock_counter = clock_counter+1; state=encoded_transition_label[159]; 
             else: state=encoded_transition_label[208]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[146]:
             if (pixels[152] <= 16): clock_counter = clock_counter+1; state=encoded_transition_label[40]; 
             else: state=encoded_transition_label[16]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[147]:
             if (pixels[270] <= 26): clock_counter = clock_counter+1; state=encoded_transition_label[169]; 
             else: state=encoded_transition_label[55]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[148]:
             if (pixels[601] <= 65):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[149]:
             if (pixels[348] <= 86):  Label=1; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[150]:
             if (pixels[439] <= 54): clock_counter = clock_counter+1; state=encoded_transition_label[43]; 
             else: state=encoded_transition_label[62]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[151]:
             if (pixels[343] <= 5):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[152]:
             if (pixels[324] <= 250):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[153]:
             if (pixels[467] <= 65): clock_counter = clock_counter+1; state=encoded_transition_label[108]; 
             else: state=encoded_transition_label[113]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[154]:
             if (pixels[436] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[193]; 
             else: state=encoded_transition_label[138]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[155]:
             if (pixels[125] <= 13):  Label=8; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[156]:
             if (pixels[432] <= 1):  Label=3; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[157]:
             if (pixels[179] <= 11): clock_counter = clock_counter+1; state=encoded_transition_label[250]; 
             else: state=encoded_transition_label[70]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[158]:
             if (pixels[329] <= 17):  Label=6; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[159]:
             if (pixels[344] <= 88):  Label=3; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[160]:
             if (pixels[297] <= 7): clock_counter = clock_counter+1; state=encoded_transition_label[227]; 
             else: state=encoded_transition_label[236]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[161]:
             if (pixels[486] <= 58): clock_counter = clock_counter+1; state=encoded_transition_label[102]; 
             else: state=encoded_transition_label[240]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[162]:
             if (pixels[186] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[232]; 
             else: state=encoded_transition_label[42]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[163]:
             if (pixels[293] <= 211): clock_counter = clock_counter+1; state=encoded_transition_label[133]; 
             else: state=encoded_transition_label[79]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[164]:
             if (pixels[328] <= 6):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=4; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[165]:
             if (pixels[463] <= 179):  Label=3; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[166]:
             if (pixels[301] <= 78): clock_counter = clock_counter+1; state=encoded_transition_label[170]; 
             else: state=encoded_transition_label[82]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[167]:
             if (pixels[294] <= 251):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[168]:
             if (pixels[381] <= 13):  Label=0; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[169]:
             if (pixels[656] <= 7): clock_counter = clock_counter+1; state=encoded_transition_label[195]; 
             else: state=encoded_transition_label[45]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[170]:
             if (pixels[429] <= 123): clock_counter = clock_counter+1; state=encoded_transition_label[37]; 
             else: state=encoded_transition_label[83]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[171]:
             if (pixels[487] <= 226):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[172]:
             if (pixels[514] <= 33):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[173]:
             if (pixels[300] <= 5): clock_counter = clock_counter+1; state=encoded_transition_label[28]; 
             else: state=encoded_transition_label[126]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[174]:
             if (pixels[515] <= 104):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[175]:
             if (pixels[294] <= 138):  Label=8; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[176]:
             if (pixels[598] <= 3): clock_counter = clock_counter+1; state=encoded_transition_label[3]; 
             else: state=encoded_transition_label[189]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[177]:
             if (pixels[210] <= 3): clock_counter = clock_counter+1; state=encoded_transition_label[196]; 
             else: state=encoded_transition_label[135]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[178]:
             if (pixels[404] <= 7): clock_counter = clock_counter+1; state=encoded_transition_label[120]; 
             else: state=encoded_transition_label[219]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[179]:
             if (pixels[322] <= 117):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[180]:
             if (pixels[265] <= 150):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[181]:
             if (pixels[653] <= 12): clock_counter = clock_counter+1; state=encoded_transition_label[184]; 
             else: state=encoded_transition_label[117]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[182]:
             if (pixels[377] <= 19):  Label=7; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[183]:
             if (pixels[319] <= 92):  Label=3; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[184]:
             if (pixels[486] <= 9): clock_counter = clock_counter+1; state=encoded_transition_label[94]; 
             else: state=encoded_transition_label[202]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[185]:
             if (pixels[427] <= 170): clock_counter = clock_counter+1; state=encoded_transition_label[6]; 
             else: state=encoded_transition_label[246]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[186]:
             if (pixels[269] <= 1):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[187]:
             if (pixels[240] <= 56):  Label=8; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[188]:
             if (pixels[400] <= 16): clock_counter = clock_counter+1; state=encoded_transition_label[32]; 
             else: state=encoded_transition_label[151]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[189]:
             if (pixels[431] <= 2):  Label=3; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[190]:
             if (pixels[241] <= 5):  Label=6; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[191]:
             if (pixels[235] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[136]; 
             else: state=encoded_transition_label[122]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[192]:
             if (pixels[522] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[2]; 
             else: state=encoded_transition_label[241]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[193]:
             if (pixels[300] <= 5): clock_counter = clock_counter+1; state=encoded_transition_label[221]; 
             else: state=encoded_transition_label[183]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[194]:
             if (pixels[150] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[137]; 
             else: state=encoded_transition_label[67]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[195]:
             if (pixels[374] <= 47): clock_counter = clock_counter+1; state=encoded_transition_label[210]; 
             else: state=encoded_transition_label[13]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[196]:
             if (pixels[410] <= 17):  Label=1; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[197]:
             if (pixels[220] <= 21):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[198]:
             if (pixels[543] <= 52): clock_counter = clock_counter+1; state=encoded_transition_label[69]; 
             else: state=encoded_transition_label[19]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[199]:
             if (pixels[293] <= 133):  Label=3; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[200]:
             if (pixels[496] <= 104):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[201]:
             if (pixels[210] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[127]; 
             else: state=encoded_transition_label[64]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[202]:
             if (pixels[188] <= 180): clock_counter = clock_counter+1; state=encoded_transition_label[47]; 
             else: state=encoded_transition_label[58]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[203]:
             if (pixels[354] <= 106):  Label=5; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[204]:
             if (pixels[297] <= 217):  Label=8; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[205]:
             if (pixels[486] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[15]; 
             else: state=encoded_transition_label[142]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[206]:
             if (pixels[213] <= 106):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[207]:
             if (pixels[293] <= 4):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[208]:
             if (pixels[153] <= 75): clock_counter = clock_counter+1; state=encoded_transition_label[17]; 
             else: state=encoded_transition_label[243]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[209]:
             if (pixels[571] <= 20): clock_counter = clock_counter+1; state=encoded_transition_label[92]; 
             else: state=encoded_transition_label[150]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[210]:
             if (pixels[429] <= 245): clock_counter = clock_counter+1; state=encoded_transition_label[5]; 
             else: state=encoded_transition_label[238]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[211]:
             if (pixels[526] <= 51):  Label=7; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[212]:
             if (pixels[154] <= 174):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[213]:
             if (pixels[244] <= 170): clock_counter = clock_counter+1; state=encoded_transition_label[103]; 
             else: state=encoded_transition_label[182]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[214]:
             if (pixels[548] <= 23):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[215]:
             if (pixels[412] <= 192):  Label=6; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[216]:
             if (pixels[660] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[35]; 
             else: state=encoded_transition_label[168]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[217]:
             if (pixels[320] <= 9): clock_counter = clock_counter+1; state=encoded_transition_label[101]; 
             else: state=encoded_transition_label[66]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[218]:
             if (pixels[516] <= 43):  Label=3; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[219]:
             if (pixels[555] <= 2):  Label=3; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[220]:
             if (pixels[260] <= 4): clock_counter = clock_counter+1; state=encoded_transition_label[237]; 
             else: state=encoded_transition_label[192]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[221]:
             if (pixels[183] <= 101):  Label=8; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[222]:
             if (pixels[126] <= 235):  Label=8; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[223]:
             if (pixels[656] <= 3): clock_counter = clock_counter+1; state=encoded_transition_label[178]; 
             else: state=encoded_transition_label[8]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[224]:
             if (pixels[515] <= 12): clock_counter = clock_counter+1; state=encoded_transition_label[18]; 
             else: state=encoded_transition_label[129]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[225]:
             if (pixels[289] <= 1): clock_counter = clock_counter+1; state=encoded_transition_label[181]; 
             else: state=encoded_transition_label[218]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[226]:
             if (pixels[269] <= 4): clock_counter = clock_counter+1; state=encoded_transition_label[90]; 
             else: state=encoded_transition_label[144]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[227]:
             if (pixels[603] <= 1):  Label=8; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=1; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[228]:
             if (pixels[205] <= 35):  Label=4; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=3; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[229]:
             if (pixels[573] <= 179): clock_counter = clock_counter+1; state=encoded_transition_label[30]; 
             else: state=encoded_transition_label[80]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[230]:
             if (pixels[490] <= 43):  Label=9; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[231]:
             if (pixels[661] <= 62):  Label=6; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[232]:
             if (pixels[345] <= 17): clock_counter = clock_counter+1; state=encoded_transition_label[130]; 
             else: state=encoded_transition_label[110]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[233]:
             if (pixels[319] <= 121): clock_counter = clock_counter+1; state=encoded_transition_label[71]; 
             else: state=encoded_transition_label[50]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[234]:
             if (pixels[687] <= 8):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[235]:
             if (pixels[526] <= 78):  Label=6; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=2; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[236]:
             if (pixels[240] <= 3): clock_counter = clock_counter+1; state=encoded_transition_label[109]; 
             else: state=encoded_transition_label[34]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[237]:
             if (pixels[574] <= 18):  Label=9; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=6; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[238]:
             if (pixels[573] <= 127):  Label=9; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[239]:
             if (pixels[515] <= 2): clock_counter = clock_counter+1; state=encoded_transition_label[214]; 
             else: state=encoded_transition_label[105]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[240]:
             if (pixels[545] <= 103): clock_counter = clock_counter+1; state=encoded_transition_label[207]; 
             else: state=encoded_transition_label[166]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[241]:
             if (pixels[512] <= 41): clock_counter = clock_counter+1; state=encoded_transition_label[148]; 
             else: state=encoded_transition_label[73]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[242]:
             if (pixels[318] <= 159):  Label=3; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=5; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[243]:
             if (pixels[495] <= 27):  Label=8; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=0; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[244]:
             if (pixels[154] <= 26): clock_counter = clock_counter+1; state=encoded_transition_label[140]; 
             else: state=encoded_transition_label[147]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[245]:
             if (pixels[375] <= 10):  Label=7; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[246]:
             if (pixels[213] <= 64):  Label=1; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[247]:
             if (pixels[319] <= 0): clock_counter = clock_counter+1; state=encoded_transition_label[36]; 
             else: state=encoded_transition_label[134]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[248]:
             if (pixels[608] <= 5): clock_counter = clock_counter+1; state=encoded_transition_label[1]; 
             else: state=encoded_transition_label[77]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[249]:
             if (pixels[545] <= 143):  Label=8; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=7; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[250]:
             if (pixels[402] <= 173):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[251]:
             if (pixels[545] <= 241): clock_counter = clock_counter+1; state=encoded_transition_label[198]; 
             else: state=encoded_transition_label[38]; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[252]:
             if (pixels[406] <= 34):  Label=2; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=8; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case x if x == encoded_state_label[253]:
             if (pixels[709] <= 158):  Label=8; state=encoded_transition_label[171];ml_inference_completed<=1; clock_counter = clock_counter+1; 
             else:  Label=9; state=encoded_transition_label[171];ml_inference_completed=1; clock_counter = clock_counter+1;
    case _:
           Label=10; state=0;ml_inference_completed=1; clock_counter = clock_counter+1;
 return (Label,clock_counter)
