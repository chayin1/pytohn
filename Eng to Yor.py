# Translating English numbers to yoruba counting from 0 to 200 and addition of 400,500,700,800,900,1000
Eng_Yor = {0:"ọdọ",1:"ọ̀kan",2:"méjì",3:"mẹ́ta",4:"mẹ́rin",5:"márùnún",
           6:"mẹ́fà",7:"méje",8:"mẹ́jọ",9:"mẹ́sánán",
           10:"mẹ́wàá",11:"mọ̀kànlá",12:"méjìlá",13:"mẹ́tàlá",14:"mẹ́rìnlá",
           15:"màrúndínlógún",16:"mẹ́rìndínlógún",17:"mẹ́tàdínlógún",18:"méjìdínlógún",
           19:"mọ́kàndínlógún",20:"ogún",
           21:"mọ́kànlélógún",22:"méjìlélógún",23:"mẹ́tàlélógún",24:"mẹ́rìnlélógún",
           25:"márùndínlọ́gbọ̀n",26:"mẹ́rìndínlọ́gbọ̀n",27:"mẹ́tàdínlọ́gbọ̀n",
           28:"méjídínlọ́gbọ̀n",29:"mọ́kàndínlọ́gbọ̀n",30:"ọgbọ̀n",
           31:"mọ́kànlélọ́gbọ̀n",32:"méjílélọ́gbọ̀n",33:"mẹ́tàlélọ́gbọ̀n",34:"mẹ́rìnlélọ́gbọ̀n",35:"márùndínlógójì",
           36:"mẹ́rìndínlógójì",37:"mẹ́tàdínlógójì",38:"méjídi nlógójì",39:"mọ́kàndínlógójì",40:"ogójì",
           41:"mọ́kànlélógójì",42:"méjílélógójì",43:"mẹ́tàlélógójì",44:"mẹ́rìnlélógójì",45:"márùndínláàdọ́ta",
           46:"mẹ́rìndínláàdọ́ta",47:"mẹ́tàdínláàdọ́ta",48:"méjídínláàdọ́ta",49:"mọ́kàndínláàdọ́ta",50:"a`ádo´ta",51:"mó?kànléláa`do´?ta",52:"méjílélógójì",53:"mé?tàlélógójì",54:"mé?rìnlélógójì",55:"márùndi´nlo´?go´?ta",
           56:"mé?rìndi´nllo´?go´?ta",57:"mé?tàdi´nllo´?go´?ta",
           58:"méjídi´nllo´?go´?ta",59:"mó?kàndi´nlo´?go´?ta",60:"?go´?ta",61:"mó?kànlélo´?go´?ta",62:"méjílélo´?go´?ta",
           63:"mé?tàlélo´?go´?ta",64:"mé?rìnlélo´?go´?ta",
           65:"márùndi´nláàdo´?rin",66:"mé?rìndi´nláàdo´?rin",67:"mé?tàdi´nláàdo´?rin",68:"méjídi´nláàdo´?rin",
           69:"mó?kàndi´nláàdo´?rin",70:"àádo´?rin",71:"mó?kànléláàdo´?rin",72:"méjíléláàdo´?rin",73:"mé?tàléláàdo´?rin",
           74:"mé?rìnléláàdo´?rin",75:"márùndi´nlo´?go´?rin",76:"mé?rìndi´nlo´?go´?rin",77:"mé?tàdi´nlo´?go´?rin",78:"méjídi´nlo´?go´?rin",
           79:"mó?kàndi´nlo´?go´?rin",80:"?go´?rin",81:"mó?kànlélo´?go´?rin",
           82:"méjílélo´?go´?rin",83:"mé?tàlélo´?go´?rin",84:"mé?rìnlélo´?go´?rin",85:"márùndi´nláa`do´?ru`nu´n",86:"mé?rìndi´nláa`do´?ru`nu´n",
           87:"mé?tàdi´nláa`do´?ru`nu´n",88:"méjídi´nláa`do´?ru`nu´n",
           89:"mó?kàndi´nláa`do´?ru`nu´n",90:"àádò?rún",91:"mó?kànléláa`do´?ru`nu´n",92:"méji`léláa`do´?ru`nu´n",
           93:"mé?tàléláa`do´?ru`nu´n",94:"mé?rìnléláa`do´?ru`nu´n",
           95:"màrúndínl?´g?´ru`nu´n",96:"m?´rìndínl?´g?´ru`nu´n",97:"mé?tàdínl?´g?´ru`nu´n",98:"méjídínl?´g?´ru`nu´n",
           99:"mó?kàndínl?´g?´ru`nu´n",100:"?g?´ru`nu´n",
           101:"m?´ka`nle´l?´g?´ru`nu´n",102:"méji`lél?´g?´ru`nu´n",103:"mé?tàlél?´g?´ru`nu´n",104:"mé?rìnlél?´g?´ru`nu´n",
           105:"ma´ru`ndínláa`do´?fa",106:"m?´rìndínláa`do´?fa",107:"mé?tàdínláa`do´?fa",108:"méji`dínláa`do´?fa",
           109:"mó?kàndínláa`do´?fa",110:"a`ádo´?fa",
           111:"m?´ka`nle´láa`do´?fa",112:"méji`léláa`do´?fa",113:"mé?tàléláa`do´?fa",114:"mé?rìnléláa`do´?fa",
           115:"ma´ru`ndínlo´?go´?fa",116:"m?´rìndínlo´?go´?fa",117:"mé?tàdínlo´?go´?fa",118:"méjídínlo´?go´?fa",
           119:"mó?kàndínlo´?go´?fa",120:"?go´?fa`",121:"m?´ka`nle´lo´?go´?fa",
           122:"méji`lélo´?go´?fa",123:"mé?tàlélo´?go´?fa",124:"mé?rìnlélo´?go´?fa",125:"ma´ru`ndínláàdóje",
           126:"m?´rìndínláàdóje",127:"mé?tàdínláàdóje",128:"méji`dínláàdóje",
           129:"mó?kàndínláa`do´?fa",130:"a`ádóje",131:"m?´ka`nle´la`ádóje",132:"méji`léla`ádóje",
           133:"mé?tàléla`ádóje",134:"mé?rìnléla`ádóje",135:"ma´ru`ndínlógóje",
           136:"m?´rìndínlógóje",137:"mé?tàdínlógóje",138:"méjídínlógóje",139:"mó?kàndínlógóje",140:"ogóje",
           141:"m?´ka`nle´lógóje",142:"méji`lélógóje",143:"mé?tàlélógóje",144:"mé?rìnlélógóje",145:"ma´ru`ndínláa`do´?j?",
           146:"m?´rìndínláa`do´?j?",147:"mé?tàdínláa`do´?j?",148:"méjídínláa`do´?j?",149:"mó?kàndínláa`do´?j?",150:"a`ádo´?j?",
           151:"m?´ka`nle´láa`do´?j?",152:"méji`léláa`do´?j?",153:"mé?tàléláa`do´?j?",154:"mé?rìnléláa`do´?j?",
           155:"ma´ru`ndínl?go´?j?",156:"m?´rìndínl?go´?j?",157:"mé?tàdínl?go´?j?",158:"méjídínl?go´?j?",159:"mó?kàndínlo´?go´?j?",

           160:"?go´?j?",161:"m?´ka`nle´l?´go´?j?",162:"méji`lél?´go´?j?",163:"mé?tàlél?´go´?j?",164:"mé?rìnlél?´go´?j?",
           165:"ma´ru`ndínláa`do´?sa`nán",166:"m?´rìndínláa`do´?sa`nán",
           167:"mé?tàdínláa`do´?sa`nán",168:"méjídínláa`do´?sa`nán",169:"mó?kàndínláa`do´?sa`nán",170:"a`ádo´?sa`nán",
           171:"m?´ka`nle´láa`do´?sa`nán",172:"méji`léláa`do´?sa`nán",173:"mé?tàléláa`do´?sa`nán",174:"mé?rìnléláa`do´?sa`nán",
           175:"ma´ru`ndínlo´?go´?sa`nán",176:"m?´rìndínlo´?go´?sa`nán",
           177:"mé?tàdínlo´?go´?sa`nán",178:"méjídínlo´?go´?sa`nán",179:"mó?kàndínlo´?go´?sa`nán",180:"?go´?sa`nán",
           181:"m?´ka`nle´lo´?go´?sa`nán",
           182:"méji`lélo´?go´?sa`nán",183:"mé?tàlélo´?go´?sa`nán",184:"mé?rìnlélo´?go´?sa`nán",185 :"ma´ru`ndínláa`do´?wa`á",
           186:"m?´rìndínláa`do´?wa`á",
           187:"mé?tàdínláa`do´?wa`á",188:"méjídínláa`do´?wa`á",
           189:"mó?kàndínláa`do´?wa`á",190:"a`ádo´?wa`á",
           191: "m?´ka`nle´láa`do´?wa`á",192: "méji`léláa`do´?wa`á",
           193: "mé?tàléláa`do´?wa`á",194: "mé?rìnléláa`do´?wa`á",
           195: "ma´ru`ndínnígba",196: "m?´rìndínnígba",
           197: "mé?tàdínnígba", 198: "méjídínnígba",
           199: "mó?kàndínnígba",
           200: "igba",

}
# This is for the user input
name = input("Enter your name >>> ")

print(name,"Welcome to English to Yoruba number dictionary ")
for i in range(200):
    Trans_number = int(input("Enter English number from 1 to 200 to get the yoruba number>>> "))
# This is for the user input
    if Trans_number == 1 in Eng_Yor:
        print(Eng_Yor[1])
    elif Trans_number == 2 in Eng_Yor:
        print(Eng_Yor[2])
    elif Trans_number == 0 in Eng_Yor:
        print(Eng_Yor[0])
    elif Trans_number == 3 in Eng_Yor:
        print(Eng_Yor[3])
    elif Trans_number == 4 in Eng_Yor:
        print(Eng_Yor[4])
    elif Trans_number == 5 in Eng_Yor:
        print(Eng_Yor[5])
    elif Trans_number == 6 in Eng_Yor:
        print(Eng_Yor[6])
    elif Trans_number == 7 in Eng_Yor:
        print(Eng_Yor[7])
    elif Trans_number == 8 in Eng_Yor:
        print(Eng_Yor[8])
    elif Trans_number == 9 in Eng_Yor:
        print(Eng_Yor[9])
    elif Trans_number == 10 in Eng_Yor:
        print(Eng_Yor[10])
    elif Trans_number == 11 in Eng_Yor:
        print(Eng_Yor[11])
    elif Trans_number == 12 in Eng_Yor:
        print(Eng_Yor[12])
    elif Trans_number == 13 in Eng_Yor:
        print(Eng_Yor[13])
    elif Trans_number == 14 in Eng_Yor:
        print(Eng_Yor[14])
    elif Trans_number == 15 in Eng_Yor:
        print(Eng_Yor[15])
    elif Trans_number == 16 in Eng_Yor:
        print(Eng_Yor[16])
    elif Trans_number == 17 in Eng_Yor:
        print(Eng_Yor[17])
    elif Trans_number == 18 in Eng_Yor:
        print(Eng_Yor[18])
    elif Trans_number == 19 in Eng_Yor:
        print(Eng_Yor[19])
    elif Trans_number == 20 in Eng_Yor:
        print(Eng_Yor[20])
    elif Trans_number == 21 in Eng_Yor:
        print(Eng_Yor[21])
    elif Trans_number == 22 in Eng_Yor:
        print(Eng_Yor[22])
    elif Trans_number == 23 in Eng_Yor:
        print(Eng_Yor[23])
    elif Trans_number == 24 in Eng_Yor:
        print(Eng_Yor[24])
    elif Trans_number == 25 in Eng_Yor:
        print(Eng_Yor[25])
    elif Trans_number == 26 in Eng_Yor:
        print(Eng_Yor[26])
    elif Trans_number == 27 in Eng_Yor:
        print(Eng_Yor[27])
    elif Trans_number == 28 in Eng_Yor:
        print(Eng_Yor[28])
    elif Trans_number == 29 in Eng_Yor:
        print(Eng_Yor[29])
    elif Trans_number == 30 in Eng_Yor:
        print(Eng_Yor[30])
    elif Trans_number == 31 in Eng_Yor:
        print(Eng_Yor[31])
    elif Trans_number == 32 in Eng_Yor:
        print(Eng_Yor[32])
    elif Trans_number == 33 in Eng_Yor:
        print(Eng_Yor[33])
    elif Trans_number == 34 in Eng_Yor:
        print(Eng_Yor[34])
    elif Trans_number == 35 in Eng_Yor:
        print(Eng_Yor[35])
    elif Trans_number == 36 in Eng_Yor:
        print(Eng_Yor[36])
    elif Trans_number == 37 in Eng_Yor:
        print(Eng_Yor[37])
    elif Trans_number == 38 in Eng_Yor:
        print(Eng_Yor[38])
    elif Trans_number == 39 in Eng_Yor:
        print(Eng_Yor[39])
    elif Trans_number == 40 in Eng_Yor:
        print(Eng_Yor[40])
    elif Trans_number == 41 in Eng_Yor:
        print(Eng_Yor[41])
    elif Trans_number == 42 in Eng_Yor:
        print(Eng_Yor[42])
    elif Trans_number == 43 in Eng_Yor:
        print(Eng_Yor[43])
    elif Trans_number == 44 in Eng_Yor:
        print(Eng_Yor[44])
    elif Trans_number == 45 in Eng_Yor:
        print(Eng_Yor[45])
    elif Trans_number == 46 in Eng_Yor:
        print(Eng_Yor[46])
    elif Trans_number == 47 in Eng_Yor:
        print(Eng_Yor[47])
    elif Trans_number == 48 in Eng_Yor:
        print(Eng_Yor[48])
    elif Trans_number == 49 in Eng_Yor:
        print(Eng_Yor[49])
    elif Trans_number == 50 in Eng_Yor:
        print(Eng_Yor[50])
    elif Trans_number == 51 in Eng_Yor:
        print(Eng_Yor[51])
    elif Trans_number == 52 in Eng_Yor:
        print(Eng_Yor[52])
    elif Trans_number == 53 in Eng_Yor:
        print(Eng_Yor[53])
    elif Trans_number == 54 in Eng_Yor:
        print(Eng_Yor[54])
    elif Trans_number == 55 in Eng_Yor:
        print(Eng_Yor[55])
    elif Trans_number == 56 in Eng_Yor:
        print(Eng_Yor[56])
    elif Trans_number == 57 in Eng_Yor:
        print(Eng_Yor[57])
    elif Trans_number == 58 in Eng_Yor:
        print(Eng_Yor[58])
    elif Trans_number == 59 in Eng_Yor:
        print(Eng_Yor[59])
    elif Trans_number == 60 in Eng_Yor:
        print(Eng_Yor[60])
    elif Trans_number == 61 in Eng_Yor:
        print(Eng_Yor[61])
    elif Trans_number == 62 in Eng_Yor:
        print(Eng_Yor[62])
    elif Trans_number == 63 in Eng_Yor:
        print(Eng_Yor[63])
    elif Trans_number == 64 in Eng_Yor:
        print(Eng_Yor[64])
    elif Trans_number == 65 in Eng_Yor:
        print(Eng_Yor[65])
    elif Trans_number == 66 in Eng_Yor:
        print(Eng_Yor[66])
    elif Trans_number == 67 in Eng_Yor:
        print(Eng_Yor[67])
    elif Trans_number == 68 in Eng_Yor:
        print(Eng_Yor[68])
    elif Trans_number == 69 in Eng_Yor:
        print(Eng_Yor[69])
    elif Trans_number == 70 in Eng_Yor:
        print(Eng_Yor[70])
    elif Trans_number == 71 in Eng_Yor:
        print(Eng_Yor[71])
    elif Trans_number == 72 in Eng_Yor:
        print(Eng_Yor[72])
    elif Trans_number == 73 in Eng_Yor:
        print(Eng_Yor[73])
    elif Trans_number == 74 in Eng_Yor:
        print(Eng_Yor[74])
    elif Trans_number == 75 in Eng_Yor:
        print(Eng_Yor[75])
    elif Trans_number == 76 in Eng_Yor:
        print(Eng_Yor[76])
    elif Trans_number == 77 in Eng_Yor:
        print(Eng_Yor[77])
    elif Trans_number == 78 in Eng_Yor:
        print(Eng_Yor[78])
    elif Trans_number == 79 in Eng_Yor:
        print(Eng_Yor[79])
    elif Trans_number == 80 in Eng_Yor:
        print(Eng_Yor[80])
    elif Trans_number == 81 in Eng_Yor:
        print(Eng_Yor[81])
    elif Trans_number == 82 in Eng_Yor:
        print(Eng_Yor[82])
    elif Trans_number == 83 in Eng_Yor:
        print(Eng_Yor[83])
    elif Trans_number == 84 in Eng_Yor:
        print(Eng_Yor[84])
    elif Trans_number == 85 in Eng_Yor:
        print(Eng_Yor[85])
    elif Trans_number == 86 in Eng_Yor:
        print(Eng_Yor[86])
    elif Trans_number == 87 in Eng_Yor:
        print(Eng_Yor[87])
    elif Trans_number == 88 in Eng_Yor:
        print(Eng_Yor[88])
    elif Trans_number == 89 in Eng_Yor:
        print(Eng_Yor[89])
    elif Trans_number == 90 in Eng_Yor:
        print(Eng_Yor[90])
    elif Trans_number == 91 in Eng_Yor:
        print(Eng_Yor[91])
    elif Trans_number == 92 in Eng_Yor:
        print(Eng_Yor[92])
    elif Trans_number == 93 in Eng_Yor:
        print(Eng_Yor[93])
    elif Trans_number == 94 in Eng_Yor:
        print(Eng_Yor[94])
    elif Trans_number == 95 in Eng_Yor:
        print(Eng_Yor[95])
    elif Trans_number == 96 in Eng_Yor:
        print(Eng_Yor[96])
    elif Trans_number == 97 in Eng_Yor:
        print(Eng_Yor[97])
    elif Trans_number == 98 in Eng_Yor:
        print(Eng_Yor[98])
    elif Trans_number == 99 in Eng_Yor:
        print(Eng_Yor[99])
    elif Trans_number == 100 in Eng_Yor:
        print(Eng_Yor[100])
    elif Trans_number == 101 in Eng_Yor:
        print(Eng_Yor[101])
    elif Trans_number == 102 in Eng_Yor:
        print(Eng_Yor[102])
    elif Trans_number == 103 in Eng_Yor:
        print(Eng_Yor[103])
    elif Trans_number == 104 in Eng_Yor:
        print(Eng_Yor[104])
    elif Trans_number == 105 in Eng_Yor:
        print(Eng_Yor[105])
    elif Trans_number == 106 in Eng_Yor:
        print(Eng_Yor[106])
    elif Trans_number == 107 in Eng_Yor:
        print(Eng_Yor[107])
    elif Trans_number == 108 in Eng_Yor:
        print(Eng_Yor[108])
    elif Trans_number == 109 in Eng_Yor:
        print(Eng_Yor[109])
    elif Trans_number == 110 in Eng_Yor:
        print(Eng_Yor[110])
    elif Trans_number == 111 in Eng_Yor:
        print(Eng_Yor[111])
    elif Trans_number == 112 in Eng_Yor:
        print(Eng_Yor[112])
    elif Trans_number == 113 in Eng_Yor:
        print(Eng_Yor[113])
    elif Trans_number == 114 in Eng_Yor:
        print(Eng_Yor[114])
    elif Trans_number == 115 in Eng_Yor:
        print(Eng_Yor[115])
    elif Trans_number == 116 in Eng_Yor:
        print(Eng_Yor[116])
    elif Trans_number == 117 in Eng_Yor:
        print(Eng_Yor[117])
    elif Trans_number == 118 in Eng_Yor:
        print(Eng_Yor[118])
    elif Trans_number == 119 in Eng_Yor:
        print(Eng_Yor[119])
    elif Trans_number == 120 in Eng_Yor:
        print(Eng_Yor[120])
    elif Trans_number == 121 in Eng_Yor:
        print(Eng_Yor[121])
    elif Trans_number == 122 in Eng_Yor:
        print(Eng_Yor[122])
    elif Trans_number == 123 in Eng_Yor:
        print(Eng_Yor[123])
    elif Trans_number == 124 in Eng_Yor:
        print(Eng_Yor[124])
    elif Trans_number == 125 in Eng_Yor:
        print(Eng_Yor[125])
    elif Trans_number == 126 in Eng_Yor:
        print(Eng_Yor[126])
    elif Trans_number == 127 in Eng_Yor:
        print(Eng_Yor[127])
    elif Trans_number == 128 in Eng_Yor:
        print(Eng_Yor[128])
    elif Trans_number == 129 in Eng_Yor:
        print(Eng_Yor[129])
    elif Trans_number == 130 in Eng_Yor:
        print(Eng_Yor[130])
    elif Trans_number == 131 in Eng_Yor:
        print(Eng_Yor[131])
    elif Trans_number == 132 in Eng_Yor:
        print(Eng_Yor[132])
    elif Trans_number == 133 in Eng_Yor:
        print(Eng_Yor[133])
    elif Trans_number == 134 in Eng_Yor:
        print(Eng_Yor[134])
    elif Trans_number == 135 in Eng_Yor:
        print(Eng_Yor[135])
    elif Trans_number == 136 in Eng_Yor:
        print(Eng_Yor[136])
    elif Trans_number == 137 in Eng_Yor:
        print(Eng_Yor[137])
    elif Trans_number == 138 in Eng_Yor:
        print(Eng_Yor[138])
    elif Trans_number == 139 in Eng_Yor:
        print(Eng_Yor[139])
    elif Trans_number == 140 in Eng_Yor:
        print(Eng_Yor[140])
    elif Trans_number == 141 in Eng_Yor:
        print(Eng_Yor[141])
    elif Trans_number == 142 in Eng_Yor:
        print(Eng_Yor[142])
    elif Trans_number == 143 in Eng_Yor:
        print(Eng_Yor[143])
    elif Trans_number == 144 in Eng_Yor:
        print(Eng_Yor[144])
    elif Trans_number == 145 in Eng_Yor:
        print(Eng_Yor[145])
    elif Trans_number == 146 in Eng_Yor:
        print(Eng_Yor[146])
    elif Trans_number == 147 in Eng_Yor:
        print(Eng_Yor[147])
    elif Trans_number == 148 in Eng_Yor:
        print(Eng_Yor[148])
    elif Trans_number == 149 in Eng_Yor:
        print(Eng_Yor[149])
    elif Trans_number == 150 in Eng_Yor:
        print(Eng_Yor[150])
    elif Trans_number == 151 in Eng_Yor:
        print(Eng_Yor[151])
    elif Trans_number == 152 in Eng_Yor:
        print(Eng_Yor[152])
    elif Trans_number == 153 in Eng_Yor:
        print(Eng_Yor[153])
    elif Trans_number == 154 in Eng_Yor:
        print(Eng_Yor[154])
    elif Trans_number == 155 in Eng_Yor:
        print(Eng_Yor[155])
    elif Trans_number == 156 in Eng_Yor:
        print(Eng_Yor[156])
    elif Trans_number == 157 in Eng_Yor:
        print(Eng_Yor[157])
    elif Trans_number == 158 in Eng_Yor:
        print(Eng_Yor[158])
    elif Trans_number == 159 in Eng_Yor:
        print(Eng_Yor[159])
    elif Trans_number == 160 in Eng_Yor:
        print(Eng_Yor[160])
    elif Trans_number == 161 in Eng_Yor:
        print(Eng_Yor[161])
    elif Trans_number == 162 in Eng_Yor:
        print(Eng_Yor[162])
    elif Trans_number == 163 in Eng_Yor:
        print(Eng_Yor[163])
    elif Trans_number == 164 in Eng_Yor:
        print(Eng_Yor[164])
    elif Trans_number == 165 in Eng_Yor:
        print(Eng_Yor[165])
    elif Trans_number == 166 in Eng_Yor:
        print(Eng_Yor[166])
    elif Trans_number == 167 in Eng_Yor:
        print(Eng_Yor[167])
    elif Trans_number == 168 in Eng_Yor:
        print(Eng_Yor[168])
    elif Trans_number == 169 in Eng_Yor:
        print(Eng_Yor[169])
    elif Trans_number == 170 in Eng_Yor:
        print(Eng_Yor[170])
    elif Trans_number == 171 in Eng_Yor:
        print(Eng_Yor[171])
    elif Trans_number == 172 in Eng_Yor:
        print(Eng_Yor[172])
    elif Trans_number == 173 in Eng_Yor:
        print(Eng_Yor[173])
    elif Trans_number == 174 in Eng_Yor:
        print(Eng_Yor[174])
    elif Trans_number == 175 in Eng_Yor:
        print(Eng_Yor[175])
    elif Trans_number == 176 in Eng_Yor:
        print(Eng_Yor[176])
    elif Trans_number == 177 in Eng_Yor:
        print(Eng_Yor[177])
    elif Trans_number == 178 in Eng_Yor:
        print(Eng_Yor[178])
    elif Trans_number == 179 in Eng_Yor:
        print(Eng_Yor[179])
    elif Trans_number == 180 in Eng_Yor:
        print(Eng_Yor[180])
    elif Trans_number == 181 in Eng_Yor:
        print(Eng_Yor[181])
    elif Trans_number == 182 in Eng_Yor:
        print(Eng_Yor[182])
    elif Trans_number == 183 in Eng_Yor:
        print(Eng_Yor[183])
    elif Trans_number == 184 in Eng_Yor:
        print(Eng_Yor[184])
    elif Trans_number == 185 in Eng_Yor:
        print(Eng_Yor[185])
    elif Trans_number == 186 in Eng_Yor:
        print(Eng_Yor[186])
    elif Trans_number == 187 in Eng_Yor:
        print(Eng_Yor[187])
    elif Trans_number == 188 in Eng_Yor:
        print(Eng_Yor[188])
    elif Trans_number == 189 in Eng_Yor:
        print(Eng_Yor[189])
    elif Trans_number == 190 in Eng_Yor:
        print(Eng_Yor[190])
    elif Trans_number == 191 in Eng_Yor:
        print(Eng_Yor[191])
    elif Trans_number == 192 in Eng_Yor:
        print(Eng_Yor[192])
    elif Trans_number == 193 in Eng_Yor:
        print(Eng_Yor[193])
    elif Trans_number == 194 in Eng_Yor:
        print(Eng_Yor[194])
    elif Trans_number == 195 in Eng_Yor:
        print(Eng_Yor[195])
    elif Trans_number == 196 in Eng_Yor:
        print(Eng_Yor[196])
    elif Trans_number == 197 in Eng_Yor:
        print(Eng_Yor[197])
    elif Trans_number == 198 in Eng_Yor:
        print(Eng_Yor[198])
    elif Trans_number == 199 in Eng_Yor:
        print(Eng_Yor[199])
    elif Trans_number == 200 in Eng_Yor:
        print(Eng_Yor[200])
    else:
        print("Incorect input")