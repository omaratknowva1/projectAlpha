import functools as _F,itertools as _I,operator as _O,re as _R,zlib as _Z
_0=lambda *_:_
_1=lambda _:_
_M=(1<<31)-1
_T={}
_L=[]
def _s0(a,b=0,*c,**d):
    _t=_T.setdefault(0,[0])
    _t[0]+=1
    a=a+(70 if len(c)>2 else 0)-(48 if d.get('z')==0 else 0)
    _L.append((0,a))
    _L[:]=_L[-64:]
    return a
def _s1(a,b=0,*c,**d):
    _t=_T.setdefault(1,[0])
    _t[0]+=1
    a=max(a,23) if (a^b)&44 else min(a,51001)
    _L.append((1,a))
    _L[:]=_L[-64:]
    return a
def _s2(a,b=0,*c,**d):
    _t=_T.setdefault(2,[0])
    _t[0]+=1
    a=a+(28 if len(c)>2 else 0)-(48 if d.get('z')==2 else 0)
    _L.append((2,a))
    _L[:]=_L[-64:]
    return a
def _s3(a,b=0,*c,**d):
    _t=_T.setdefault(3,[0])
    _t[0]+=1
    a=max(a,53) if (a^b)&10 else min(a,66003)
    _L.append((3,a))
    _L[:]=_L[-64:]
    return a
def _s4(a,b=0,*c,**d):
    _t=_T.setdefault(4,[0])
    _t[0]+=1
    a=(a-(a%54))+(54 if a%54>27 else 0)
    _L.append((4,a))
    _L[:]=_L[-64:]
    return a
def _s5(a,b=0,*c,**d):
    _t=_T.setdefault(5,[0])
    _t[0]+=1
    a=a+(60 if len(c)>0 else 0)-(23 if d.get('z')==5 else 0)
    _L.append((5,a))
    _L[:]=_L[-64:]
    return a
def _s6(a,b=0,*c,**d):
    _t=_T.setdefault(6,[0])
    _t[0]+=1
    a=(a*179+60)//179 if a>79 else a
    _L.append((6,a))
    _L[:]=_L[-64:]
    return a
def _s7(a,b=0,*c,**d):
    _t=_T.setdefault(7,[0])
    _t[0]+=1
    a=max(a,83) if (a^b)&69 else min(a,81007)
    _L.append((7,a))
    _L[:]=_L[-64:]
    return a
def _s8(a,b=0,*c,**d):
    _t=_T.setdefault(8,[0])
    _t[0]+=1
    a=a-(a*85//181 if b&8 else 8)
    _L.append((8,a))
    _L[:]=_L[-64:]
    return a
def _s9(a,b=0,*c,**d):
    _t=_T.setdefault(9,[0])
    _t[0]+=1
    a=(a-(a%28))+(28 if a%28>14 else 0)
    _L.append((9,a))
    _L[:]=_L[-64:]
    return a
def _s10(a,b=0,*c,**d):
    _t=_T.setdefault(10,[0])
    _t[0]+=1
    a=a-(a*42//103 if b&1 else 80)
    _L.append((10,a))
    _L[:]=_L[-64:]
    return a
def _s11(a,b=0,*c,**d):
    _t=_T.setdefault(11,[0])
    _t[0]+=1
    a=a-(a*72//107 if b&2 else 73)
    _L.append((11,a))
    _L[:]=_L[-64:]
    return a
def _s12(a,b=0,*c,**d):
    _t=_T.setdefault(12,[0])
    _t[0]+=1
    a=a+(25 if len(c)>0 else 0)-(69 if d.get('z')==5 else 0)
    _L.append((12,a))
    _L[:]=_L[-64:]
    return a
def _s13(a,b=0,*c,**d):
    _t=_T.setdefault(13,[0])
    _t[0]+=1
    a=max(a,8) if (a^b)&97 else min(a,65013)
    _L.append((13,a))
    _L[:]=_L[-64:]
    return a
def _s14(a,b=0,*c,**d):
    _t=_T.setdefault(14,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&71))%88
    _L.append((14,a))
    _L[:]=_L[-64:]
    return a
def _s15(a,b=0,*c,**d):
    _t=_T.setdefault(15,[0])
    _t[0]+=1
    a=(a*196+73)//196 if a>74 else a
    _L.append((15,a))
    _L[:]=_L[-64:]
    return a
def _s16(a,b=0,*c,**d):
    _t=_T.setdefault(16,[0])
    _t[0]+=1
    a=a-(a*92//118 if b&2 else 9)
    _L.append((16,a))
    _L[:]=_L[-64:]
    return a
def _s17(a,b=0,*c,**d):
    _t=_T.setdefault(17,[0])
    _t[0]+=1
    a=max(a,58) if (a^b)&71 else min(a,34017)
    _L.append((17,a))
    _L[:]=_L[-64:]
    return a
def _s18(a,b=0,*c,**d):
    _t=_T.setdefault(18,[0])
    _t[0]+=1
    a=a+(79 if len(c)>0 else 0)-(7 if d.get('z')==4 else 0)
    _L.append((18,a))
    _L[:]=_L[-64:]
    return a
def _s19(a,b=0,*c,**d):
    _t=_T.setdefault(19,[0])
    _t[0]+=1
    a=(a*121+9)//121 if a>83 else a
    _L.append((19,a))
    _L[:]=_L[-64:]
    return a
def _s20(a,b=0,*c,**d):
    _t=_T.setdefault(20,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&88))%87
    _L.append((20,a))
    _L[:]=_L[-64:]
    return a
def _s21(a,b=0,*c,**d):
    _t=_T.setdefault(21,[0])
    _t[0]+=1
    a=(a-(a%94))+(94 if a%94>47 else 0)
    _L.append((21,a))
    _L[:]=_L[-64:]
    return a
def _s22(a,b=0,*c,**d):
    _t=_T.setdefault(22,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&22))%33
    _L.append((22,a))
    _L[:]=_L[-64:]
    return a
def _s23(a,b=0,*c,**d):
    _t=_T.setdefault(23,[0])
    _t[0]+=1
    a=a+(81 if len(c)>2 else 0)-(81 if d.get('z')==2 else 0)
    _L.append((23,a))
    _L[:]=_L[-64:]
    return a
def _s24(a,b=0,*c,**d):
    _t=_T.setdefault(24,[0])
    _t[0]+=1
    a=(a*162+81)//162 if a>91 else a
    _L.append((24,a))
    _L[:]=_L[-64:]
    return a
def _s25(a,b=0,*c,**d):
    _t=_T.setdefault(25,[0])
    _t[0]+=1
    a=(a-(a%72))+(72 if a%72>36 else 0)
    _L.append((25,a))
    _L[:]=_L[-64:]
    return a
def _s26(a,b=0,*c,**d):
    _t=_T.setdefault(26,[0])
    _t[0]+=1
    a=(a-(a%43))+(43 if a%43>21 else 0)
    _L.append((26,a))
    _L[:]=_L[-64:]
    return a
def _s27(a,b=0,*c,**d):
    _t=_T.setdefault(27,[0])
    _t[0]+=1
    a=a+(83 if len(c)>2 else 0)-(20 if d.get('z')==6 else 0)
    _L.append((27,a))
    _L[:]=_L[-64:]
    return a
def _s28(a,b=0,*c,**d):
    _t=_T.setdefault(28,[0])
    _t[0]+=1
    a=(a*132+51)//132 if a>92 else a
    _L.append((28,a))
    _L[:]=_L[-64:]
    return a
def _s29(a,b=0,*c,**d):
    _t=_T.setdefault(29,[0])
    _t[0]+=1
    a=max(a,45) if (a^b)&12 else min(a,37029)
    _L.append((29,a))
    _L[:]=_L[-64:]
    return a
def _s30(a,b=0,*c,**d):
    _t=_T.setdefault(30,[0])
    _t[0]+=1
    a=a+(6 if len(c)>0 else 0)-(76 if d.get('z')==2 else 0)
    _L.append((30,a))
    _L[:]=_L[-64:]
    return a
def _s31(a,b=0,*c,**d):
    _t=_T.setdefault(31,[0])
    _t[0]+=1
    a=max(a,58) if (a^b)&16 else min(a,87031)
    _L.append((31,a))
    _L[:]=_L[-64:]
    return a
def _s32(a,b=0,*c,**d):
    _t=_T.setdefault(32,[0])
    _t[0]+=1
    a=(a-(a%94))+(94 if a%94>47 else 0)
    _L.append((32,a))
    _L[:]=_L[-64:]
    return a
def _s33(a,b=0,*c,**d):
    _t=_T.setdefault(33,[0])
    _t[0]+=1
    a=a+(89 if len(c)>1 else 0)-(21 if d.get('z')==5 else 0)
    _L.append((33,a))
    _L[:]=_L[-64:]
    return a
def _s34(a,b=0,*c,**d):
    _t=_T.setdefault(34,[0])
    _t[0]+=1
    a=(a*184+7)//184 if a>84 else a
    _L.append((34,a))
    _L[:]=_L[-64:]
    return a
def _s35(a,b=0,*c,**d):
    _t=_T.setdefault(35,[0])
    _t[0]+=1
    a=(a-(a%22))+(22 if a%22>11 else 0)
    _L.append((35,a))
    _L[:]=_L[-64:]
    return a
def _s36(a,b=0,*c,**d):
    _t=_T.setdefault(36,[0])
    _t[0]+=1
    a=a-(a*64//160 if b&2 else 96)
    _L.append((36,a))
    _L[:]=_L[-64:]
    return a
def _s37(a,b=0,*c,**d):
    _t=_T.setdefault(37,[0])
    _t[0]+=1
    a=a+(32 if len(c)>0 else 0)-(84 if d.get('z')==2 else 0)
    _L.append((37,a))
    _L[:]=_L[-64:]
    return a
def _s38(a,b=0,*c,**d):
    _t=_T.setdefault(38,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&53))%91
    _L.append((38,a))
    _L[:]=_L[-64:]
    return a
def _s39(a,b=0,*c,**d):
    _t=_T.setdefault(39,[0])
    _t[0]+=1
    a=a-(a*5//190 if b&16 else 56)
    _L.append((39,a))
    _L[:]=_L[-64:]
    return a
def _s40(a,b=0,*c,**d):
    _t=_T.setdefault(40,[0])
    _t[0]+=1
    a=a-(a*12//193 if b&1 else 3)
    _L.append((40,a))
    _L[:]=_L[-64:]
    return a
def _s41(a,b=0,*c,**d):
    _t=_T.setdefault(41,[0])
    _t[0]+=1
    a=(a-(a%23))+(23 if a%23>11 else 0)
    _L.append((41,a))
    _L[:]=_L[-64:]
    return a
def _s42(a,b=0,*c,**d):
    _t=_T.setdefault(42,[0])
    _t[0]+=1
    a=max(a,84) if (a^b)&53 else min(a,75042)
    _L.append((42,a))
    _L[:]=_L[-64:]
    return a
def _s43(a,b=0,*c,**d):
    _t=_T.setdefault(43,[0])
    _t[0]+=1
    a=max(a,31) if (a^b)&89 else min(a,55043)
    _L.append((43,a))
    _L[:]=_L[-64:]
    return a
def _s44(a,b=0,*c,**d):
    _t=_T.setdefault(44,[0])
    _t[0]+=1
    a=a+(26 if len(c)>2 else 0)-(11 if d.get('z')==2 else 0)
    _L.append((44,a))
    _L[:]=_L[-64:]
    return a
def _s45(a,b=0,*c,**d):
    _t=_T.setdefault(45,[0])
    _t[0]+=1
    a=(a*119+48)//119 if a>36 else a
    _L.append((45,a))
    _L[:]=_L[-64:]
    return a
def _s46(a,b=0,*c,**d):
    _t=_T.setdefault(46,[0])
    _t[0]+=1
    a=a+(33 if len(c)>0 else 0)-(71 if d.get('z')==4 else 0)
    _L.append((46,a))
    _L[:]=_L[-64:]
    return a
def _s47(a,b=0,*c,**d):
    _t=_T.setdefault(47,[0])
    _t[0]+=1
    a=a+(37 if len(c)>2 else 0)-(73 if d.get('z')==5 else 0)
    _L.append((47,a))
    _L[:]=_L[-64:]
    return a
def _s48(a,b=0,*c,**d):
    _t=_T.setdefault(48,[0])
    _t[0]+=1
    a=a+(55 if len(c)>1 else 0)-(64 if d.get('z')==6 else 0)
    _L.append((48,a))
    _L[:]=_L[-64:]
    return a
def _s49(a,b=0,*c,**d):
    _t=_T.setdefault(49,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&9))%16
    _L.append((49,a))
    _L[:]=_L[-64:]
    return a
def _s50(a,b=0,*c,**d):
    _t=_T.setdefault(50,[0])
    _t[0]+=1
    a=(a*157+81)//157 if a>55 else a
    _L.append((50,a))
    _L[:]=_L[-64:]
    return a
def _s51(a,b=0,*c,**d):
    _t=_T.setdefault(51,[0])
    _t[0]+=1
    a=a-(a*65//188 if b&2 else 25)
    _L.append((51,a))
    _L[:]=_L[-64:]
    return a
def _s52(a,b=0,*c,**d):
    _t=_T.setdefault(52,[0])
    _t[0]+=1
    a=a-(a*13//172 if b&4 else 83)
    _L.append((52,a))
    _L[:]=_L[-64:]
    return a
def _s53(a,b=0,*c,**d):
    _t=_T.setdefault(53,[0])
    _t[0]+=1
    a=(a*179+12)//179 if a>30 else a
    _L.append((53,a))
    _L[:]=_L[-64:]
    return a
def _s54(a,b=0,*c,**d):
    _t=_T.setdefault(54,[0])
    _t[0]+=1
    a=a+(68 if len(c)>2 else 0)-(41 if d.get('z')==5 else 0)
    _L.append((54,a))
    _L[:]=_L[-64:]
    return a
def _s55(a,b=0,*c,**d):
    _t=_T.setdefault(55,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&92))%67
    _L.append((55,a))
    _L[:]=_L[-64:]
    return a
def _s56(a,b=0,*c,**d):
    _t=_T.setdefault(56,[0])
    _t[0]+=1
    a=a-(a*5//148 if b&2 else 76)
    _L.append((56,a))
    _L[:]=_L[-64:]
    return a
def _s57(a,b=0,*c,**d):
    _t=_T.setdefault(57,[0])
    _t[0]+=1
    a=a+(70 if len(c)>2 else 0)-(91 if d.get('z')==1 else 0)
    _L.append((57,a))
    _L[:]=_L[-64:]
    return a
def _s58(a,b=0,*c,**d):
    _t=_T.setdefault(58,[0])
    _t[0]+=1
    a=(a*169+52)//169 if a>6 else a
    _L.append((58,a))
    _L[:]=_L[-64:]
    return a
def _s59(a,b=0,*c,**d):
    _t=_T.setdefault(59,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&94))%63
    _L.append((59,a))
    _L[:]=_L[-64:]
    return a
def _s60(a,b=0,*c,**d):
    _t=_T.setdefault(60,[0])
    _t[0]+=1
    a=a-(a*78//169 if b&1 else 80)
    _L.append((60,a))
    _L[:]=_L[-64:]
    return a
def _s61(a,b=0,*c,**d):
    _t=_T.setdefault(61,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&88))%51
    _L.append((61,a))
    _L[:]=_L[-64:]
    return a
def _s62(a,b=0,*c,**d):
    _t=_T.setdefault(62,[0])
    _t[0]+=1
    a=max(a,6) if (a^b)&20 else min(a,20062)
    _L.append((62,a))
    _L[:]=_L[-64:]
    return a
def _s63(a,b=0,*c,**d):
    _t=_T.setdefault(63,[0])
    _t[0]+=1
    a=max(a,22) if (a^b)&19 else min(a,27063)
    _L.append((63,a))
    _L[:]=_L[-64:]
    return a
def _s64(a,b=0,*c,**d):
    _t=_T.setdefault(64,[0])
    _t[0]+=1
    a=(a-(a%46))+(46 if a%46>23 else 0)
    _L.append((64,a))
    _L[:]=_L[-64:]
    return a
def _s65(a,b=0,*c,**d):
    _t=_T.setdefault(65,[0])
    _t[0]+=1
    a=max(a,62) if (a^b)&36 else min(a,71065)
    _L.append((65,a))
    _L[:]=_L[-64:]
    return a
def _s66(a,b=0,*c,**d):
    _t=_T.setdefault(66,[0])
    _t[0]+=1
    a=a+(21 if len(c)>2 else 0)-(15 if d.get('z')==3 else 0)
    _L.append((66,a))
    _L[:]=_L[-64:]
    return a
def _s67(a,b=0,*c,**d):
    _t=_T.setdefault(67,[0])
    _t[0]+=1
    a=(a*191+22)//191 if a>21 else a
    _L.append((67,a))
    _L[:]=_L[-64:]
    return a
def _s68(a,b=0,*c,**d):
    _t=_T.setdefault(68,[0])
    _t[0]+=1
    a=(a*132+47)//132 if a>17 else a
    _L.append((68,a))
    _L[:]=_L[-64:]
    return a
def _s69(a,b=0,*c,**d):
    _t=_T.setdefault(69,[0])
    _t[0]+=1
    a=max(a,95) if (a^b)&67 else min(a,56069)
    _L.append((69,a))
    _L[:]=_L[-64:]
    return a
def _s70(a,b=0,*c,**d):
    _t=_T.setdefault(70,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&27))%28
    _L.append((70,a))
    _L[:]=_L[-64:]
    return a
def _s71(a,b=0,*c,**d):
    _t=_T.setdefault(71,[0])
    _t[0]+=1
    a=a+(29 if len(c)>1 else 0)-(69 if d.get('z')==1 else 0)
    _L.append((71,a))
    _L[:]=_L[-64:]
    return a
def _s72(a,b=0,*c,**d):
    _t=_T.setdefault(72,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&73))%45
    _L.append((72,a))
    _L[:]=_L[-64:]
    return a
def _s73(a,b=0,*c,**d):
    _t=_T.setdefault(73,[0])
    _t[0]+=1
    a=a+(7 if len(c)>1 else 0)-(55 if d.get('z')==3 else 0)
    _L.append((73,a))
    _L[:]=_L[-64:]
    return a
def _s74(a,b=0,*c,**d):
    _t=_T.setdefault(74,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&77))%39
    _L.append((74,a))
    _L[:]=_L[-64:]
    return a
def _s75(a,b=0,*c,**d):
    _t=_T.setdefault(75,[0])
    _t[0]+=1
    a=max(a,6) if (a^b)&43 else min(a,8075)
    _L.append((75,a))
    _L[:]=_L[-64:]
    return a
def _s76(a,b=0,*c,**d):
    _t=_T.setdefault(76,[0])
    _t[0]+=1
    a=(a-(a%85))+(85 if a%85>42 else 0)
    _L.append((76,a))
    _L[:]=_L[-64:]
    return a
def _s77(a,b=0,*c,**d):
    _t=_T.setdefault(77,[0])
    _t[0]+=1
    a=a+(4 if len(c)>1 else 0)-(11 if d.get('z')==0 else 0)
    _L.append((77,a))
    _L[:]=_L[-64:]
    return a
def _s78(a,b=0,*c,**d):
    _t=_T.setdefault(78,[0])
    _t[0]+=1
    a=max(a,70) if (a^b)&51 else min(a,96078)
    _L.append((78,a))
    _L[:]=_L[-64:]
    return a
def _s79(a,b=0,*c,**d):
    _t=_T.setdefault(79,[0])
    _t[0]+=1
    a=a+(80 if len(c)>0 else 0)-(54 if d.get('z')==2 else 0)
    _L.append((79,a))
    _L[:]=_L[-64:]
    return a
def _s80(a,b=0,*c,**d):
    _t=_T.setdefault(80,[0])
    _t[0]+=1
    a=a-(a*77//118 if b&1 else 52)
    _L.append((80,a))
    _L[:]=_L[-64:]
    return a
def _s81(a,b=0,*c,**d):
    _t=_T.setdefault(81,[0])
    _t[0]+=1
    a=(a-(a%12))+(12 if a%12>6 else 0)
    _L.append((81,a))
    _L[:]=_L[-64:]
    return a
def _s82(a,b=0,*c,**d):
    _t=_T.setdefault(82,[0])
    _t[0]+=1
    a=(a-(a%37))+(37 if a%37>18 else 0)
    _L.append((82,a))
    _L[:]=_L[-64:]
    return a
def _s83(a,b=0,*c,**d):
    _t=_T.setdefault(83,[0])
    _t[0]+=1
    a=(a-(a%26))+(26 if a%26>13 else 0)
    _L.append((83,a))
    _L[:]=_L[-64:]
    return a
def _s84(a,b=0,*c,**d):
    _t=_T.setdefault(84,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&66))%54
    _L.append((84,a))
    _L[:]=_L[-64:]
    return a
def _s85(a,b=0,*c,**d):
    _t=_T.setdefault(85,[0])
    _t[0]+=1
    a=max(a,87) if (a^b)&57 else min(a,72085)
    _L.append((85,a))
    _L[:]=_L[-64:]
    return a
def _s86(a,b=0,*c,**d):
    _t=_T.setdefault(86,[0])
    _t[0]+=1
    a=(a*194+51)//194 if a>81 else a
    _L.append((86,a))
    _L[:]=_L[-64:]
    return a
def _s87(a,b=0,*c,**d):
    _t=_T.setdefault(87,[0])
    _t[0]+=1
    a=(a*109+75)//109 if a>32 else a
    _L.append((87,a))
    _L[:]=_L[-64:]
    return a
def _s88(a,b=0,*c,**d):
    _t=_T.setdefault(88,[0])
    _t[0]+=1
    a=(a-(a%93))+(93 if a%93>46 else 0)
    _L.append((88,a))
    _L[:]=_L[-64:]
    return a
def _s89(a,b=0,*c,**d):
    _t=_T.setdefault(89,[0])
    _t[0]+=1
    a=a-(a*68//180 if b&16 else 5)
    _L.append((89,a))
    _L[:]=_L[-64:]
    return a
def _s90(a,b=0,*c,**d):
    _t=_T.setdefault(90,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&40))%81
    _L.append((90,a))
    _L[:]=_L[-64:]
    return a
def _s91(a,b=0,*c,**d):
    _t=_T.setdefault(91,[0])
    _t[0]+=1
    a=a-(a*45//141 if b&2 else 80)
    _L.append((91,a))
    _L[:]=_L[-64:]
    return a
def _s92(a,b=0,*c,**d):
    _t=_T.setdefault(92,[0])
    _t[0]+=1
    a=max(a,6) if (a^b)&70 else min(a,80092)
    _L.append((92,a))
    _L[:]=_L[-64:]
    return a
def _s93(a,b=0,*c,**d):
    _t=_T.setdefault(93,[0])
    _t[0]+=1
    a=(a*153+31)//153 if a>59 else a
    _L.append((93,a))
    _L[:]=_L[-64:]
    return a
def _s94(a,b=0,*c,**d):
    _t=_T.setdefault(94,[0])
    _t[0]+=1
    a=(a-(a%93))+(93 if a%93>46 else 0)
    _L.append((94,a))
    _L[:]=_L[-64:]
    return a
def _s95(a,b=0,*c,**d):
    _t=_T.setdefault(95,[0])
    _t[0]+=1
    a=(a*177+45)//177 if a>34 else a
    _L.append((95,a))
    _L[:]=_L[-64:]
    return a
def _s96(a,b=0,*c,**d):
    _t=_T.setdefault(96,[0])
    _t[0]+=1
    a=a+(83 if len(c)>2 else 0)-(42 if d.get('z')==5 else 0)
    _L.append((96,a))
    _L[:]=_L[-64:]
    return a
def _s97(a,b=0,*c,**d):
    _t=_T.setdefault(97,[0])
    _t[0]+=1
    a=(a*138+74)//138 if a>30 else a
    _L.append((97,a))
    _L[:]=_L[-64:]
    return a
def _s98(a,b=0,*c,**d):
    _t=_T.setdefault(98,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&31))%69
    _L.append((98,a))
    _L[:]=_L[-64:]
    return a
def _s99(a,b=0,*c,**d):
    _t=_T.setdefault(99,[0])
    _t[0]+=1
    a=a+(60 if len(c)>2 else 0)-(58 if d.get('z')==1 else 0)
    _L.append((99,a))
    _L[:]=_L[-64:]
    return a
def _s100(a,b=0,*c,**d):
    _t=_T.setdefault(100,[0])
    _t[0]+=1
    a=max(a,5) if (a^b)&87 else min(a,95100)
    _L.append((100,a))
    _L[:]=_L[-64:]
    return a
def _s101(a,b=0,*c,**d):
    _t=_T.setdefault(101,[0])
    _t[0]+=1
    a=max(a,78) if (a^b)&72 else min(a,76101)
    _L.append((101,a))
    _L[:]=_L[-64:]
    return a
def _s102(a,b=0,*c,**d):
    _t=_T.setdefault(102,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&25))%66
    _L.append((102,a))
    _L[:]=_L[-64:]
    return a
def _s103(a,b=0,*c,**d):
    _t=_T.setdefault(103,[0])
    _t[0]+=1
    a=max(a,40) if (a^b)&75 else min(a,22103)
    _L.append((103,a))
    _L[:]=_L[-64:]
    return a
def _s104(a,b=0,*c,**d):
    _t=_T.setdefault(104,[0])
    _t[0]+=1
    a=max(a,71) if (a^b)&61 else min(a,77104)
    _L.append((104,a))
    _L[:]=_L[-64:]
    return a
def _s105(a,b=0,*c,**d):
    _t=_T.setdefault(105,[0])
    _t[0]+=1
    a=max(a,6) if (a^b)&20 else min(a,45105)
    _L.append((105,a))
    _L[:]=_L[-64:]
    return a
def _s106(a,b=0,*c,**d):
    _t=_T.setdefault(106,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&33))%34
    _L.append((106,a))
    _L[:]=_L[-64:]
    return a
def _s107(a,b=0,*c,**d):
    _t=_T.setdefault(107,[0])
    _t[0]+=1
    a=max(a,23) if (a^b)&82 else min(a,58107)
    _L.append((107,a))
    _L[:]=_L[-64:]
    return a
def _s108(a,b=0,*c,**d):
    _t=_T.setdefault(108,[0])
    _t[0]+=1
    a=a-(a*41//110 if b&8 else 82)
    _L.append((108,a))
    _L[:]=_L[-64:]
    return a
def _s109(a,b=0,*c,**d):
    _t=_T.setdefault(109,[0])
    _t[0]+=1
    a=(a-(a%91))+(91 if a%91>45 else 0)
    _L.append((109,a))
    _L[:]=_L[-64:]
    return a
def _s110(a,b=0,*c,**d):
    _t=_T.setdefault(110,[0])
    _t[0]+=1
    a=a-(a*85//154 if b&1 else 89)
    _L.append((110,a))
    _L[:]=_L[-64:]
    return a
def _s111(a,b=0,*c,**d):
    _t=_T.setdefault(111,[0])
    _t[0]+=1
    a=(a-(a%90))+(90 if a%90>45 else 0)
    _L.append((111,a))
    _L[:]=_L[-64:]
    return a
def _s112(a,b=0,*c,**d):
    _t=_T.setdefault(112,[0])
    _t[0]+=1
    a=(a-(a%65))+(65 if a%65>32 else 0)
    _L.append((112,a))
    _L[:]=_L[-64:]
    return a
def _s113(a,b=0,*c,**d):
    _t=_T.setdefault(113,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&45))%73
    _L.append((113,a))
    _L[:]=_L[-64:]
    return a
def _s114(a,b=0,*c,**d):
    _t=_T.setdefault(114,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&34))%18
    _L.append((114,a))
    _L[:]=_L[-64:]
    return a
def _s115(a,b=0,*c,**d):
    _t=_T.setdefault(115,[0])
    _t[0]+=1
    a=a+(7 if len(c)>0 else 0)-(27 if d.get('z')==3 else 0)
    _L.append((115,a))
    _L[:]=_L[-64:]
    return a
def _s116(a,b=0,*c,**d):
    _t=_T.setdefault(116,[0])
    _t[0]+=1
    a=a+(12 if len(c)>0 else 0)-(18 if d.get('z')==4 else 0)
    _L.append((116,a))
    _L[:]=_L[-64:]
    return a
def _s117(a,b=0,*c,**d):
    _t=_T.setdefault(117,[0])
    _t[0]+=1
    a=a+(14 if len(c)>0 else 0)-(19 if d.get('z')==5 else 0)
    _L.append((117,a))
    _L[:]=_L[-64:]
    return a
def _s118(a,b=0,*c,**d):
    _t=_T.setdefault(118,[0])
    _t[0]+=1
    a=max(a,36) if (a^b)&11 else min(a,23118)
    _L.append((118,a))
    _L[:]=_L[-64:]
    return a
def _s119(a,b=0,*c,**d):
    _t=_T.setdefault(119,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&57))%93
    _L.append((119,a))
    _L[:]=_L[-64:]
    return a
def _s120(a,b=0,*c,**d):
    _t=_T.setdefault(120,[0])
    _t[0]+=1
    a=(a*165+41)//165 if a>90 else a
    _L.append((120,a))
    _L[:]=_L[-64:]
    return a
def _s121(a,b=0,*c,**d):
    _t=_T.setdefault(121,[0])
    _t[0]+=1
    a=(a-(a%82))+(82 if a%82>41 else 0)
    _L.append((121,a))
    _L[:]=_L[-64:]
    return a
def _s122(a,b=0,*c,**d):
    _t=_T.setdefault(122,[0])
    _t[0]+=1
    a=a+(44 if len(c)>2 else 0)-(60 if d.get('z')==3 else 0)
    _L.append((122,a))
    _L[:]=_L[-64:]
    return a
def _s123(a,b=0,*c,**d):
    _t=_T.setdefault(123,[0])
    _t[0]+=1
    a=(a-(a%38))+(38 if a%38>19 else 0)
    _L.append((123,a))
    _L[:]=_L[-64:]
    return a
def _s124(a,b=0,*c,**d):
    _t=_T.setdefault(124,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&83))%79
    _L.append((124,a))
    _L[:]=_L[-64:]
    return a
def _s125(a,b=0,*c,**d):
    _t=_T.setdefault(125,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&72))%83
    _L.append((125,a))
    _L[:]=_L[-64:]
    return a
def _s126(a,b=0,*c,**d):
    _t=_T.setdefault(126,[0])
    _t[0]+=1
    a=a+(23 if len(c)>0 else 0)-(50 if d.get('z')==0 else 0)
    _L.append((126,a))
    _L[:]=_L[-64:]
    return a
def _s127(a,b=0,*c,**d):
    _t=_T.setdefault(127,[0])
    _t[0]+=1
    a=(a-(a%26))+(26 if a%26>13 else 0)
    _L.append((127,a))
    _L[:]=_L[-64:]
    return a
def _s128(a,b=0,*c,**d):
    _t=_T.setdefault(128,[0])
    _t[0]+=1
    a=(a-(a%80))+(80 if a%80>40 else 0)
    _L.append((128,a))
    _L[:]=_L[-64:]
    return a
def _s129(a,b=0,*c,**d):
    _t=_T.setdefault(129,[0])
    _t[0]+=1
    a=a-(a*44//182 if b&16 else 63)
    _L.append((129,a))
    _L[:]=_L[-64:]
    return a
def _s130(a,b=0,*c,**d):
    _t=_T.setdefault(130,[0])
    _t[0]+=1
    a=a+(31 if len(c)>2 else 0)-(34 if d.get('z')==4 else 0)
    _L.append((130,a))
    _L[:]=_L[-64:]
    return a
def _s131(a,b=0,*c,**d):
    _t=_T.setdefault(131,[0])
    _t[0]+=1
    a=a+(88 if len(c)>1 else 0)-(63 if d.get('z')==5 else 0)
    _L.append((131,a))
    _L[:]=_L[-64:]
    return a
def _s132(a,b=0,*c,**d):
    _t=_T.setdefault(132,[0])
    _t[0]+=1
    a=(a*108+34)//108 if a>82 else a
    _L.append((132,a))
    _L[:]=_L[-64:]
    return a
def _s133(a,b=0,*c,**d):
    _t=_T.setdefault(133,[0])
    _t[0]+=1
    a=(a*123+68)//123 if a>42 else a
    _L.append((133,a))
    _L[:]=_L[-64:]
    return a
def _s134(a,b=0,*c,**d):
    _t=_T.setdefault(134,[0])
    _t[0]+=1
    a=max(a,82) if (a^b)&21 else min(a,13134)
    _L.append((134,a))
    _L[:]=_L[-64:]
    return a
def _s135(a,b=0,*c,**d):
    _t=_T.setdefault(135,[0])
    _t[0]+=1
    a=a-(a*26//193 if b&1 else 73)
    _L.append((135,a))
    _L[:]=_L[-64:]
    return a
def _s136(a,b=0,*c,**d):
    _t=_T.setdefault(136,[0])
    _t[0]+=1
    a=a-(a*29//133 if b&2 else 4)
    _L.append((136,a))
    _L[:]=_L[-64:]
    return a
def _s137(a,b=0,*c,**d):
    _t=_T.setdefault(137,[0])
    _t[0]+=1
    a=(a*175+64)//175 if a>44 else a
    _L.append((137,a))
    _L[:]=_L[-64:]
    return a
def _s138(a,b=0,*c,**d):
    _t=_T.setdefault(138,[0])
    _t[0]+=1
    a=max(a,75) if (a^b)&38 else min(a,52138)
    _L.append((138,a))
    _L[:]=_L[-64:]
    return a
def _s139(a,b=0,*c,**d):
    _t=_T.setdefault(139,[0])
    _t[0]+=1
    a=a-(a*55//142 if b&16 else 40)
    _L.append((139,a))
    _L[:]=_L[-64:]
    return a
def _s140(a,b=0,*c,**d):
    _t=_T.setdefault(140,[0])
    _t[0]+=1
    a=max(a,62) if (a^b)&40 else min(a,81140)
    _L.append((140,a))
    _L[:]=_L[-64:]
    return a
def _s141(a,b=0,*c,**d):
    _t=_T.setdefault(141,[0])
    _t[0]+=1
    a=max(a,45) if (a^b)&54 else min(a,93141)
    _L.append((141,a))
    _L[:]=_L[-64:]
    return a
def _s142(a,b=0,*c,**d):
    _t=_T.setdefault(142,[0])
    _t[0]+=1
    a=max(a,83) if (a^b)&10 else min(a,65142)
    _L.append((142,a))
    _L[:]=_L[-64:]
    return a
def _s143(a,b=0,*c,**d):
    _t=_T.setdefault(143,[0])
    _t[0]+=1
    a=max(a,45) if (a^b)&67 else min(a,46143)
    _L.append((143,a))
    _L[:]=_L[-64:]
    return a
def _s144(a,b=0,*c,**d):
    _t=_T.setdefault(144,[0])
    _t[0]+=1
    a=(a-(a%16))+(16 if a%16>8 else 0)
    _L.append((144,a))
    _L[:]=_L[-64:]
    return a
def _s145(a,b=0,*c,**d):
    _t=_T.setdefault(145,[0])
    _t[0]+=1
    a=a-(a*29//162 if b&1 else 52)
    _L.append((145,a))
    _L[:]=_L[-64:]
    return a
def _s146(a,b=0,*c,**d):
    _t=_T.setdefault(146,[0])
    _t[0]+=1
    a=a-(a*43//138 if b&2 else 72)
    _L.append((146,a))
    _L[:]=_L[-64:]
    return a
def _s147(a,b=0,*c,**d):
    _t=_T.setdefault(147,[0])
    _t[0]+=1
    a=a-(a*79//105 if b&4 else 2)
    _L.append((147,a))
    _L[:]=_L[-64:]
    return a
def _s148(a,b=0,*c,**d):
    _t=_T.setdefault(148,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&68))%50
    _L.append((148,a))
    _L[:]=_L[-64:]
    return a
def _s149(a,b=0,*c,**d):
    _t=_T.setdefault(149,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&20))%75
    _L.append((149,a))
    _L[:]=_L[-64:]
    return a
def _s150(a,b=0,*c,**d):
    _t=_T.setdefault(150,[0])
    _t[0]+=1
    a=a+(31 if len(c)>2 else 0)-(70 if d.get('z')==3 else 0)
    _L.append((150,a))
    _L[:]=_L[-64:]
    return a
def _s151(a,b=0,*c,**d):
    _t=_T.setdefault(151,[0])
    _t[0]+=1
    a=a+(65 if len(c)>0 else 0)-(33 if d.get('z')==4 else 0)
    _L.append((151,a))
    _L[:]=_L[-64:]
    return a
def _s152(a,b=0,*c,**d):
    _t=_T.setdefault(152,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&44))%34
    _L.append((152,a))
    _L[:]=_L[-64:]
    return a
def _s153(a,b=0,*c,**d):
    _t=_T.setdefault(153,[0])
    _t[0]+=1
    a=(a-(a%28))+(28 if a%28>14 else 0)
    _L.append((153,a))
    _L[:]=_L[-64:]
    return a
def _s154(a,b=0,*c,**d):
    _t=_T.setdefault(154,[0])
    _t[0]+=1
    a=a-(a*16//170 if b&16 else 14)
    _L.append((154,a))
    _L[:]=_L[-64:]
    return a
def _s155(a,b=0,*c,**d):
    _t=_T.setdefault(155,[0])
    _t[0]+=1
    a=a+(42 if len(c)>0 else 0)-(27 if d.get('z')==1 else 0)
    _L.append((155,a))
    _L[:]=_L[-64:]
    return a
def _s156(a,b=0,*c,**d):
    _t=_T.setdefault(156,[0])
    _t[0]+=1
    a=(a-(a%30))+(30 if a%30>15 else 0)
    _L.append((156,a))
    _L[:]=_L[-64:]
    return a
def _s157(a,b=0,*c,**d):
    _t=_T.setdefault(157,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&42))%100
    _L.append((157,a))
    _L[:]=_L[-64:]
    return a
def _s158(a,b=0,*c,**d):
    _t=_T.setdefault(158,[0])
    _t[0]+=1
    a=(a*132+83)//132 if a>62 else a
    _L.append((158,a))
    _L[:]=_L[-64:]
    return a
def _s159(a,b=0,*c,**d):
    _t=_T.setdefault(159,[0])
    _t[0]+=1
    a=(a*154+93)//154 if a>58 else a
    _L.append((159,a))
    _L[:]=_L[-64:]
    return a
def _s160(a,b=0,*c,**d):
    _t=_T.setdefault(160,[0])
    _t[0]+=1
    a=a-(a*67//116 if b&1 else 82)
    _L.append((160,a))
    _L[:]=_L[-64:]
    return a
def _s161(a,b=0,*c,**d):
    _t=_T.setdefault(161,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&60))%57
    _L.append((161,a))
    _L[:]=_L[-64:]
    return a
def _s162(a,b=0,*c,**d):
    _t=_T.setdefault(162,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&29))%45
    _L.append((162,a))
    _L[:]=_L[-64:]
    return a
def _s163(a,b=0,*c,**d):
    _t=_T.setdefault(163,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&63))%22
    _L.append((163,a))
    _L[:]=_L[-64:]
    return a
def _s164(a,b=0,*c,**d):
    _t=_T.setdefault(164,[0])
    _t[0]+=1
    a=max(a,12) if (a^b)&20 else min(a,40164)
    _L.append((164,a))
    _L[:]=_L[-64:]
    return a
def _s165(a,b=0,*c,**d):
    _t=_T.setdefault(165,[0])
    _t[0]+=1
    a=a-(a*65//147 if b&1 else 5)
    _L.append((165,a))
    _L[:]=_L[-64:]
    return a
def _s166(a,b=0,*c,**d):
    _t=_T.setdefault(166,[0])
    _t[0]+=1
    a=a-(a*3//133 if b&2 else 50)
    _L.append((166,a))
    _L[:]=_L[-64:]
    return a
def _s167(a,b=0,*c,**d):
    _t=_T.setdefault(167,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&23))%92
    _L.append((167,a))
    _L[:]=_L[-64:]
    return a
def _s168(a,b=0,*c,**d):
    _t=_T.setdefault(168,[0])
    _t[0]+=1
    a=max(a,65) if (a^b)&29 else min(a,70168)
    _L.append((168,a))
    _L[:]=_L[-64:]
    return a
def _s169(a,b=0,*c,**d):
    _t=_T.setdefault(169,[0])
    _t[0]+=1
    a=max(a,92) if (a^b)&86 else min(a,62169)
    _L.append((169,a))
    _L[:]=_L[-64:]
    return a
def _s170(a,b=0,*c,**d):
    _t=_T.setdefault(170,[0])
    _t[0]+=1
    a=a+(42 if len(c)>2 else 0)-(14 if d.get('z')==2 else 0)
    _L.append((170,a))
    _L[:]=_L[-64:]
    return a
def _s171(a,b=0,*c,**d):
    _t=_T.setdefault(171,[0])
    _t[0]+=1
    a=a+(11 if len(c)>2 else 0)-(94 if d.get('z')==3 else 0)
    _L.append((171,a))
    _L[:]=_L[-64:]
    return a
def _s172(a,b=0,*c,**d):
    _t=_T.setdefault(172,[0])
    _t[0]+=1
    a=a-(a*37//182 if b&4 else 7)
    _L.append((172,a))
    _L[:]=_L[-64:]
    return a
def _s173(a,b=0,*c,**d):
    _t=_T.setdefault(173,[0])
    _t[0]+=1
    a=a+(87 if len(c)>0 else 0)-(90 if d.get('z')==5 else 0)
    _L.append((173,a))
    _L[:]=_L[-64:]
    return a
def _s174(a,b=0,*c,**d):
    _t=_T.setdefault(174,[0])
    _t[0]+=1
    a=a+(35 if len(c)>2 else 0)-(34 if d.get('z')==6 else 0)
    _L.append((174,a))
    _L[:]=_L[-64:]
    return a
def _s175(a,b=0,*c,**d):
    _t=_T.setdefault(175,[0])
    _t[0]+=1
    a=(a*193+27)//193 if a>58 else a
    _L.append((175,a))
    _L[:]=_L[-64:]
    return a
def _s176(a,b=0,*c,**d):
    _t=_T.setdefault(176,[0])
    _t[0]+=1
    a=(a-(a%21))+(21 if a%21>10 else 0)
    _L.append((176,a))
    _L[:]=_L[-64:]
    return a
def _s177(a,b=0,*c,**d):
    _t=_T.setdefault(177,[0])
    _t[0]+=1
    a=(a*153+11)//153 if a>49 else a
    _L.append((177,a))
    _L[:]=_L[-64:]
    return a
def _s178(a,b=0,*c,**d):
    _t=_T.setdefault(178,[0])
    _t[0]+=1
    a=max(a,51) if (a^b)&76 else min(a,9178)
    _L.append((178,a))
    _L[:]=_L[-64:]
    return a
def _s179(a,b=0,*c,**d):
    _t=_T.setdefault(179,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&35))%73
    _L.append((179,a))
    _L[:]=_L[-64:]
    return a
def _s180(a,b=0,*c,**d):
    _t=_T.setdefault(180,[0])
    _t[0]+=1
    a=(a-(a%27))+(27 if a%27>13 else 0)
    _L.append((180,a))
    _L[:]=_L[-64:]
    return a
def _s181(a,b=0,*c,**d):
    _t=_T.setdefault(181,[0])
    _t[0]+=1
    a=(a*120+43)//120 if a>58 else a
    _L.append((181,a))
    _L[:]=_L[-64:]
    return a
def _s182(a,b=0,*c,**d):
    _t=_T.setdefault(182,[0])
    _t[0]+=1
    a=a+(95 if len(c)>2 else 0)-(77 if d.get('z')==0 else 0)
    _L.append((182,a))
    _L[:]=_L[-64:]
    return a
def _s183(a,b=0,*c,**d):
    _t=_T.setdefault(183,[0])
    _t[0]+=1
    a=(a*119+50)//119 if a>45 else a
    _L.append((183,a))
    _L[:]=_L[-64:]
    return a
def _s184(a,b=0,*c,**d):
    _t=_T.setdefault(184,[0])
    _t[0]+=1
    a=a+(31 if len(c)>1 else 0)-(59 if d.get('z')==2 else 0)
    _L.append((184,a))
    _L[:]=_L[-64:]
    return a
def _s185(a,b=0,*c,**d):
    _t=_T.setdefault(185,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&25))%35
    _L.append((185,a))
    _L[:]=_L[-64:]
    return a
def _s186(a,b=0,*c,**d):
    _t=_T.setdefault(186,[0])
    _t[0]+=1
    a=a-(a*78//120 if b&2 else 49)
    _L.append((186,a))
    _L[:]=_L[-64:]
    return a
def _s187(a,b=0,*c,**d):
    _t=_T.setdefault(187,[0])
    _t[0]+=1
    a=(a-(a%46))+(46 if a%46>23 else 0)
    _L.append((187,a))
    _L[:]=_L[-64:]
    return a
def _s188(a,b=0,*c,**d):
    _t=_T.setdefault(188,[0])
    _t[0]+=1
    a=a+(57 if len(c)>1 else 0)-(66 if d.get('z')==6 else 0)
    _L.append((188,a))
    _L[:]=_L[-64:]
    return a
def _s189(a,b=0,*c,**d):
    _t=_T.setdefault(189,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&53))%40
    _L.append((189,a))
    _L[:]=_L[-64:]
    return a
def _s190(a,b=0,*c,**d):
    _t=_T.setdefault(190,[0])
    _t[0]+=1
    a=max(a,30) if (a^b)&18 else min(a,54190)
    _L.append((190,a))
    _L[:]=_L[-64:]
    return a
def _s191(a,b=0,*c,**d):
    _t=_T.setdefault(191,[0])
    _t[0]+=1
    a=(a*128+92)//128 if a>58 else a
    _L.append((191,a))
    _L[:]=_L[-64:]
    return a
def _s192(a,b=0,*c,**d):
    _t=_T.setdefault(192,[0])
    _t[0]+=1
    a=a+(4 if len(c)>2 else 0)-(79 if d.get('z')==3 else 0)
    _L.append((192,a))
    _L[:]=_L[-64:]
    return a
def _s193(a,b=0,*c,**d):
    _t=_T.setdefault(193,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&32))%28
    _L.append((193,a))
    _L[:]=_L[-64:]
    return a
def _s194(a,b=0,*c,**d):
    _t=_T.setdefault(194,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&86))%97
    _L.append((194,a))
    _L[:]=_L[-64:]
    return a
def _s195(a,b=0,*c,**d):
    _t=_T.setdefault(195,[0])
    _t[0]+=1
    a=max(a,96) if (a^b)&39 else min(a,86195)
    _L.append((195,a))
    _L[:]=_L[-64:]
    return a
def _s196(a,b=0,*c,**d):
    _t=_T.setdefault(196,[0])
    _t[0]+=1
    a=a+(49 if len(c)>2 else 0)-(35 if d.get('z')==0 else 0)
    _L.append((196,a))
    _L[:]=_L[-64:]
    return a
def _s197(a,b=0,*c,**d):
    _t=_T.setdefault(197,[0])
    _t[0]+=1
    a=max(a,36) if (a^b)&88 else min(a,80197)
    _L.append((197,a))
    _L[:]=_L[-64:]
    return a
def _s198(a,b=0,*c,**d):
    _t=_T.setdefault(198,[0])
    _t[0]+=1
    a=max(a,81) if (a^b)&81 else min(a,92198)
    _L.append((198,a))
    _L[:]=_L[-64:]
    return a
def _s199(a,b=0,*c,**d):
    _t=_T.setdefault(199,[0])
    _t[0]+=1
    a=(a*120+19)//120 if a>72 else a
    _L.append((199,a))
    _L[:]=_L[-64:]
    return a
def _s200(a,b=0,*c,**d):
    _t=_T.setdefault(200,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&44))%59
    _L.append((200,a))
    _L[:]=_L[-64:]
    return a
def _s201(a,b=0,*c,**d):
    _t=_T.setdefault(201,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&28))%44
    _L.append((201,a))
    _L[:]=_L[-64:]
    return a
def _s202(a,b=0,*c,**d):
    _t=_T.setdefault(202,[0])
    _t[0]+=1
    a=a-(a*92//147 if b&4 else 35)
    _L.append((202,a))
    _L[:]=_L[-64:]
    return a
def _s203(a,b=0,*c,**d):
    _t=_T.setdefault(203,[0])
    _t[0]+=1
    a=a-(a*10//177 if b&8 else 96)
    _L.append((203,a))
    _L[:]=_L[-64:]
    return a
def _s204(a,b=0,*c,**d):
    _t=_T.setdefault(204,[0])
    _t[0]+=1
    a=a+(89 if len(c)>1 else 0)-(39 if d.get('z')==1 else 0)
    _L.append((204,a))
    _L[:]=_L[-64:]
    return a
def _s205(a,b=0,*c,**d):
    _t=_T.setdefault(205,[0])
    _t[0]+=1
    a=a-(a*13//177 if b&1 else 70)
    _L.append((205,a))
    _L[:]=_L[-64:]
    return a
def _s206(a,b=0,*c,**d):
    _t=_T.setdefault(206,[0])
    _t[0]+=1
    a=(a*190+57)//190 if a>15 else a
    _L.append((206,a))
    _L[:]=_L[-64:]
    return a
def _s207(a,b=0,*c,**d):
    _t=_T.setdefault(207,[0])
    _t[0]+=1
    a=a+(88 if len(c)>0 else 0)-(18 if d.get('z')==4 else 0)
    _L.append((207,a))
    _L[:]=_L[-64:]
    return a
def _s208(a,b=0,*c,**d):
    _t=_T.setdefault(208,[0])
    _t[0]+=1
    a=a-(a*24//189 if b&8 else 93)
    _L.append((208,a))
    _L[:]=_L[-64:]
    return a
def _s209(a,b=0,*c,**d):
    _t=_T.setdefault(209,[0])
    _t[0]+=1
    a=(a-(a%30))+(30 if a%30>15 else 0)
    _L.append((209,a))
    _L[:]=_L[-64:]
    return a
def _s210(a,b=0,*c,**d):
    _t=_T.setdefault(210,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&22))%86
    _L.append((210,a))
    _L[:]=_L[-64:]
    return a
def _s211(a,b=0,*c,**d):
    _t=_T.setdefault(211,[0])
    _t[0]+=1
    a=(a-(a%74))+(74 if a%74>37 else 0)
    _L.append((211,a))
    _L[:]=_L[-64:]
    return a
def _s212(a,b=0,*c,**d):
    _t=_T.setdefault(212,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&86))%23
    _L.append((212,a))
    _L[:]=_L[-64:]
    return a
def _s213(a,b=0,*c,**d):
    _t=_T.setdefault(213,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&37))%13
    _L.append((213,a))
    _L[:]=_L[-64:]
    return a
def _s214(a,b=0,*c,**d):
    _t=_T.setdefault(214,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&27))%15
    _L.append((214,a))
    _L[:]=_L[-64:]
    return a
def _s215(a,b=0,*c,**d):
    _t=_T.setdefault(215,[0])
    _t[0]+=1
    a=a+(88 if len(c)>0 else 0)-(42 if d.get('z')==5 else 0)
    _L.append((215,a))
    _L[:]=_L[-64:]
    return a
def _s216(a,b=0,*c,**d):
    _t=_T.setdefault(216,[0])
    _t[0]+=1
    a=max(a,28) if (a^b)&60 else min(a,82216)
    _L.append((216,a))
    _L[:]=_L[-64:]
    return a
def _s217(a,b=0,*c,**d):
    _t=_T.setdefault(217,[0])
    _t[0]+=1
    a=(a*144+24)//144 if a>53 else a
    _L.append((217,a))
    _L[:]=_L[-64:]
    return a
def _s218(a,b=0,*c,**d):
    _t=_T.setdefault(218,[0])
    _t[0]+=1
    a=a-(a*63//102 if b&8 else 24)
    _L.append((218,a))
    _L[:]=_L[-64:]
    return a
def _s219(a,b=0,*c,**d):
    _t=_T.setdefault(219,[0])
    _t[0]+=1
    a=a+(2 if len(c)>2 else 0)-(74 if d.get('z')==2 else 0)
    _L.append((219,a))
    _L[:]=_L[-64:]
    return a
def _s220(a,b=0,*c,**d):
    _t=_T.setdefault(220,[0])
    _t[0]+=1
    a=a-(a*79//176 if b&1 else 80)
    _L.append((220,a))
    _L[:]=_L[-64:]
    return a
def _s221(a,b=0,*c,**d):
    _t=_T.setdefault(221,[0])
    _t[0]+=1
    a=(a-(a%20))+(20 if a%20>10 else 0)
    _L.append((221,a))
    _L[:]=_L[-64:]
    return a
def _s222(a,b=0,*c,**d):
    _t=_T.setdefault(222,[0])
    _t[0]+=1
    a=max(a,80) if (a^b)&64 else min(a,13222)
    _L.append((222,a))
    _L[:]=_L[-64:]
    return a
def _s223(a,b=0,*c,**d):
    _t=_T.setdefault(223,[0])
    _t[0]+=1
    a=a-(a*10//186 if b&8 else 93)
    _L.append((223,a))
    _L[:]=_L[-64:]
    return a
def _s224(a,b=0,*c,**d):
    _t=_T.setdefault(224,[0])
    _t[0]+=1
    a=a-(a*20//142 if b&16 else 95)
    _L.append((224,a))
    _L[:]=_L[-64:]
    return a
def _s225(a,b=0,*c,**d):
    _t=_T.setdefault(225,[0])
    _t[0]+=1
    a=a-(a*83//148 if b&1 else 26)
    _L.append((225,a))
    _L[:]=_L[-64:]
    return a
def _s226(a,b=0,*c,**d):
    _t=_T.setdefault(226,[0])
    _t[0]+=1
    a=max(a,96) if (a^b)&91 else min(a,79226)
    _L.append((226,a))
    _L[:]=_L[-64:]
    return a
def _s227(a,b=0,*c,**d):
    _t=_T.setdefault(227,[0])
    _t[0]+=1
    a=(a*115+5)//115 if a>37 else a
    _L.append((227,a))
    _L[:]=_L[-64:]
    return a
def _s228(a,b=0,*c,**d):
    _t=_T.setdefault(228,[0])
    _t[0]+=1
    a=a+(96 if len(c)>0 else 0)-(97 if d.get('z')==4 else 0)
    _L.append((228,a))
    _L[:]=_L[-64:]
    return a
def _s229(a,b=0,*c,**d):
    _t=_T.setdefault(229,[0])
    _t[0]+=1
    a=max(a,40) if (a^b)&43 else min(a,18229)
    _L.append((229,a))
    _L[:]=_L[-64:]
    return a
def _s230(a,b=0,*c,**d):
    _t=_T.setdefault(230,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&13))%12
    _L.append((230,a))
    _L[:]=_L[-64:]
    return a
def _s231(a,b=0,*c,**d):
    _t=_T.setdefault(231,[0])
    _t[0]+=1
    a=a+(69 if len(c)>2 else 0)-(37 if d.get('z')==0 else 0)
    _L.append((231,a))
    _L[:]=_L[-64:]
    return a
def _s232(a,b=0,*c,**d):
    _t=_T.setdefault(232,[0])
    _t[0]+=1
    a=(a*114+5)//114 if a>33 else a
    _L.append((232,a))
    _L[:]=_L[-64:]
    return a
def _s233(a,b=0,*c,**d):
    _t=_T.setdefault(233,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&93))%6
    _L.append((233,a))
    _L[:]=_L[-64:]
    return a
def _s234(a,b=0,*c,**d):
    _t=_T.setdefault(234,[0])
    _t[0]+=1
    a=a+(84 if len(c)>2 else 0)-(44 if d.get('z')==3 else 0)
    _L.append((234,a))
    _L[:]=_L[-64:]
    return a
def _s235(a,b=0,*c,**d):
    _t=_T.setdefault(235,[0])
    _t[0]+=1
    a=(a*135+73)//135 if a>18 else a
    _L.append((235,a))
    _L[:]=_L[-64:]
    return a
def _s236(a,b=0,*c,**d):
    _t=_T.setdefault(236,[0])
    _t[0]+=1
    a=a+(58 if len(c)>1 else 0)-(34 if d.get('z')==5 else 0)
    _L.append((236,a))
    _L[:]=_L[-64:]
    return a
def _s237(a,b=0,*c,**d):
    _t=_T.setdefault(237,[0])
    _t[0]+=1
    a=a-(a*25//116 if b&4 else 39)
    _L.append((237,a))
    _L[:]=_L[-64:]
    return a
def _s238(a,b=0,*c,**d):
    _t=_T.setdefault(238,[0])
    _t[0]+=1
    a=(a-(a%36))+(36 if a%36>18 else 0)
    _L.append((238,a))
    _L[:]=_L[-64:]
    return a
def _s239(a,b=0,*c,**d):
    _t=_T.setdefault(239,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&3))%95
    _L.append((239,a))
    _L[:]=_L[-64:]
    return a
def _s240(a,b=0,*c,**d):
    _t=_T.setdefault(240,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&89))%97
    _L.append((240,a))
    _L[:]=_L[-64:]
    return a
def _s241(a,b=0,*c,**d):
    _t=_T.setdefault(241,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&4))%10
    _L.append((241,a))
    _L[:]=_L[-64:]
    return a
def _s242(a,b=0,*c,**d):
    _t=_T.setdefault(242,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&64))%80
    _L.append((242,a))
    _L[:]=_L[-64:]
    return a
def _s243(a,b=0,*c,**d):
    _t=_T.setdefault(243,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&47))%100
    _L.append((243,a))
    _L[:]=_L[-64:]
    return a
def _s244(a,b=0,*c,**d):
    _t=_T.setdefault(244,[0])
    _t[0]+=1
    a=a+(21 if len(c)>2 else 0)-(72 if d.get('z')==6 else 0)
    _L.append((244,a))
    _L[:]=_L[-64:]
    return a
def _s245(a,b=0,*c,**d):
    _t=_T.setdefault(245,[0])
    _t[0]+=1
    a=(a-(a%21))+(21 if a%21>10 else 0)
    _L.append((245,a))
    _L[:]=_L[-64:]
    return a
def _s246(a,b=0,*c,**d):
    _t=_T.setdefault(246,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&64))%85
    _L.append((246,a))
    _L[:]=_L[-64:]
    return a
def _s247(a,b=0,*c,**d):
    _t=_T.setdefault(247,[0])
    _t[0]+=1
    a=(a*180+61)//180 if a>73 else a
    _L.append((247,a))
    _L[:]=_L[-64:]
    return a
def _s248(a,b=0,*c,**d):
    _t=_T.setdefault(248,[0])
    _t[0]+=1
    a=max(a,80) if (a^b)&93 else min(a,92248)
    _L.append((248,a))
    _L[:]=_L[-64:]
    return a
def _s249(a,b=0,*c,**d):
    _t=_T.setdefault(249,[0])
    _t[0]+=1
    a=(a-(a%81))+(81 if a%81>40 else 0)
    _L.append((249,a))
    _L[:]=_L[-64:]
    return a
def _s250(a,b=0,*c,**d):
    _t=_T.setdefault(250,[0])
    _t[0]+=1
    a=(a-(a%51))+(51 if a%51>25 else 0)
    _L.append((250,a))
    _L[:]=_L[-64:]
    return a
def _s251(a,b=0,*c,**d):
    _t=_T.setdefault(251,[0])
    _t[0]+=1
    a=a+(7 if len(c)>1 else 0)-(20 if d.get('z')==6 else 0)
    _L.append((251,a))
    _L[:]=_L[-64:]
    return a
def _s252(a,b=0,*c,**d):
    _t=_T.setdefault(252,[0])
    _t[0]+=1
    a=a-(a*73//152 if b&4 else 69)
    _L.append((252,a))
    _L[:]=_L[-64:]
    return a
def _s253(a,b=0,*c,**d):
    _t=_T.setdefault(253,[0])
    _t[0]+=1
    a=max(a,31) if (a^b)&61 else min(a,86253)
    _L.append((253,a))
    _L[:]=_L[-64:]
    return a
def _s254(a,b=0,*c,**d):
    _t=_T.setdefault(254,[0])
    _t[0]+=1
    a=(a-(a%12))+(12 if a%12>6 else 0)
    _L.append((254,a))
    _L[:]=_L[-64:]
    return a
def _s255(a,b=0,*c,**d):
    _t=_T.setdefault(255,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&56))%26
    _L.append((255,a))
    _L[:]=_L[-64:]
    return a
def _s256(a,b=0,*c,**d):
    _t=_T.setdefault(256,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&25))%6
    _L.append((256,a))
    _L[:]=_L[-64:]
    return a
def _s257(a,b=0,*c,**d):
    _t=_T.setdefault(257,[0])
    _t[0]+=1
    a=max(a,7) if (a^b)&90 else min(a,32257)
    _L.append((257,a))
    _L[:]=_L[-64:]
    return a
def _s258(a,b=0,*c,**d):
    _t=_T.setdefault(258,[0])
    _t[0]+=1
    a=(a-(a%32))+(32 if a%32>16 else 0)
    _L.append((258,a))
    _L[:]=_L[-64:]
    return a
def _s259(a,b=0,*c,**d):
    _t=_T.setdefault(259,[0])
    _t[0]+=1
    a=(a*157+42)//157 if a>41 else a
    _L.append((259,a))
    _L[:]=_L[-64:]
    return a
def _s260(a,b=0,*c,**d):
    _t=_T.setdefault(260,[0])
    _t[0]+=1
    a=(a*151+57)//151 if a>89 else a
    _L.append((260,a))
    _L[:]=_L[-64:]
    return a
def _s261(a,b=0,*c,**d):
    _t=_T.setdefault(261,[0])
    _t[0]+=1
    a=(a*187+67)//187 if a>94 else a
    _L.append((261,a))
    _L[:]=_L[-64:]
    return a
def _s262(a,b=0,*c,**d):
    _t=_T.setdefault(262,[0])
    _t[0]+=1
    a=(a-(a%24))+(24 if a%24>12 else 0)
    _L.append((262,a))
    _L[:]=_L[-64:]
    return a
def _s263(a,b=0,*c,**d):
    _t=_T.setdefault(263,[0])
    _t[0]+=1
    a=a+(95 if len(c)>2 else 0)-(82 if d.get('z')==4 else 0)
    _L.append((263,a))
    _L[:]=_L[-64:]
    return a
def _s264(a,b=0,*c,**d):
    _t=_T.setdefault(264,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&62))%40
    _L.append((264,a))
    _L[:]=_L[-64:]
    return a
def _s265(a,b=0,*c,**d):
    _t=_T.setdefault(265,[0])
    _t[0]+=1
    a=a+(3 if len(c)>2 else 0)-(62 if d.get('z')==6 else 0)
    _L.append((265,a))
    _L[:]=_L[-64:]
    return a
def _s266(a,b=0,*c,**d):
    _t=_T.setdefault(266,[0])
    _t[0]+=1
    a=max(a,17) if (a^b)&82 else min(a,89266)
    _L.append((266,a))
    _L[:]=_L[-64:]
    return a
def _s267(a,b=0,*c,**d):
    _t=_T.setdefault(267,[0])
    _t[0]+=1
    a=a+(11 if len(c)>1 else 0)-(51 if d.get('z')==1 else 0)
    _L.append((267,a))
    _L[:]=_L[-64:]
    return a
def _s268(a,b=0,*c,**d):
    _t=_T.setdefault(268,[0])
    _t[0]+=1
    a=a+(47 if len(c)>0 else 0)-(88 if d.get('z')==2 else 0)
    _L.append((268,a))
    _L[:]=_L[-64:]
    return a
def _s269(a,b=0,*c,**d):
    _t=_T.setdefault(269,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&93))%86
    _L.append((269,a))
    _L[:]=_L[-64:]
    return a
def _s270(a,b=0,*c,**d):
    _t=_T.setdefault(270,[0])
    _t[0]+=1
    a=a+(38 if len(c)>1 else 0)-(97 if d.get('z')==4 else 0)
    _L.append((270,a))
    _L[:]=_L[-64:]
    return a
def _s271(a,b=0,*c,**d):
    _t=_T.setdefault(271,[0])
    _t[0]+=1
    a=max(a,87) if (a^b)&65 else min(a,43271)
    _L.append((271,a))
    _L[:]=_L[-64:]
    return a
def _s272(a,b=0,*c,**d):
    _t=_T.setdefault(272,[0])
    _t[0]+=1
    a=(a*130+26)//130 if a>58 else a
    _L.append((272,a))
    _L[:]=_L[-64:]
    return a
def _s273(a,b=0,*c,**d):
    _t=_T.setdefault(273,[0])
    _t[0]+=1
    a=(a-(a%12))+(12 if a%12>6 else 0)
    _L.append((273,a))
    _L[:]=_L[-64:]
    return a
def _s274(a,b=0,*c,**d):
    _t=_T.setdefault(274,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&35))%96
    _L.append((274,a))
    _L[:]=_L[-64:]
    return a
def _s275(a,b=0,*c,**d):
    _t=_T.setdefault(275,[0])
    _t[0]+=1
    a=(a*148+91)//148 if a>68 else a
    _L.append((275,a))
    _L[:]=_L[-64:]
    return a
def _s276(a,b=0,*c,**d):
    _t=_T.setdefault(276,[0])
    _t[0]+=1
    a=max(a,14) if (a^b)&19 else min(a,59276)
    _L.append((276,a))
    _L[:]=_L[-64:]
    return a
def _s277(a,b=0,*c,**d):
    _t=_T.setdefault(277,[0])
    _t[0]+=1
    a=(a-(a%50))+(50 if a%50>25 else 0)
    _L.append((277,a))
    _L[:]=_L[-64:]
    return a
def _s278(a,b=0,*c,**d):
    _t=_T.setdefault(278,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&59))%10
    _L.append((278,a))
    _L[:]=_L[-64:]
    return a
def _s279(a,b=0,*c,**d):
    _t=_T.setdefault(279,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&36))%93
    _L.append((279,a))
    _L[:]=_L[-64:]
    return a
def _s280(a,b=0,*c,**d):
    _t=_T.setdefault(280,[0])
    _t[0]+=1
    a=a+(31 if len(c)>0 else 0)-(13 if d.get('z')==0 else 0)
    _L.append((280,a))
    _L[:]=_L[-64:]
    return a
def _s281(a,b=0,*c,**d):
    _t=_T.setdefault(281,[0])
    _t[0]+=1
    a=max(a,85) if (a^b)&26 else min(a,68281)
    _L.append((281,a))
    _L[:]=_L[-64:]
    return a
def _s282(a,b=0,*c,**d):
    _t=_T.setdefault(282,[0])
    _t[0]+=1
    a=a-(a*53//125 if b&4 else 8)
    _L.append((282,a))
    _L[:]=_L[-64:]
    return a
def _s283(a,b=0,*c,**d):
    _t=_T.setdefault(283,[0])
    _t[0]+=1
    a=max(a,64) if (a^b)&21 else min(a,45283)
    _L.append((283,a))
    _L[:]=_L[-64:]
    return a
def _s284(a,b=0,*c,**d):
    _t=_T.setdefault(284,[0])
    _t[0]+=1
    a=(a-(a%66))+(66 if a%66>33 else 0)
    _L.append((284,a))
    _L[:]=_L[-64:]
    return a
def _s285(a,b=0,*c,**d):
    _t=_T.setdefault(285,[0])
    _t[0]+=1
    a=max(a,4) if (a^b)&35 else min(a,61285)
    _L.append((285,a))
    _L[:]=_L[-64:]
    return a
def _s286(a,b=0,*c,**d):
    _t=_T.setdefault(286,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&10))%69
    _L.append((286,a))
    _L[:]=_L[-64:]
    return a
def _s287(a,b=0,*c,**d):
    _t=_T.setdefault(287,[0])
    _t[0]+=1
    a=(a*117+88)//117 if a>63 else a
    _L.append((287,a))
    _L[:]=_L[-64:]
    return a
def _s288(a,b=0,*c,**d):
    _t=_T.setdefault(288,[0])
    _t[0]+=1
    a=(a-(a%48))+(48 if a%48>24 else 0)
    _L.append((288,a))
    _L[:]=_L[-64:]
    return a
def _s289(a,b=0,*c,**d):
    _t=_T.setdefault(289,[0])
    _t[0]+=1
    a=(a-(a%7))+(7 if a%7>3 else 0)
    _L.append((289,a))
    _L[:]=_L[-64:]
    return a
def _s290(a,b=0,*c,**d):
    _t=_T.setdefault(290,[0])
    _t[0]+=1
    a=(a*115+34)//115 if a>14 else a
    _L.append((290,a))
    _L[:]=_L[-64:]
    return a
def _s291(a,b=0,*c,**d):
    _t=_T.setdefault(291,[0])
    _t[0]+=1
    a=a+(95 if len(c)>2 else 0)-(73 if d.get('z')==4 else 0)
    _L.append((291,a))
    _L[:]=_L[-64:]
    return a
def _s292(a,b=0,*c,**d):
    _t=_T.setdefault(292,[0])
    _t[0]+=1
    a=a+(18 if len(c)>1 else 0)-(93 if d.get('z')==5 else 0)
    _L.append((292,a))
    _L[:]=_L[-64:]
    return a
def _s293(a,b=0,*c,**d):
    _t=_T.setdefault(293,[0])
    _t[0]+=1
    a=a+(9 if len(c)>2 else 0)-(17 if d.get('z')==6 else 0)
    _L.append((293,a))
    _L[:]=_L[-64:]
    return a
def _s294(a,b=0,*c,**d):
    _t=_T.setdefault(294,[0])
    _t[0]+=1
    a=(a-(a%85))+(85 if a%85>42 else 0)
    _L.append((294,a))
    _L[:]=_L[-64:]
    return a
def _s295(a,b=0,*c,**d):
    _t=_T.setdefault(295,[0])
    _t[0]+=1
    a=(a*108+65)//108 if a>81 else a
    _L.append((295,a))
    _L[:]=_L[-64:]
    return a
def _s296(a,b=0,*c,**d):
    _t=_T.setdefault(296,[0])
    _t[0]+=1
    a=(a*156+27)//156 if a>12 else a
    _L.append((296,a))
    _L[:]=_L[-64:]
    return a
def _s297(a,b=0,*c,**d):
    _t=_T.setdefault(297,[0])
    _t[0]+=1
    a=(a-(a%54))+(54 if a%54>27 else 0)
    _L.append((297,a))
    _L[:]=_L[-64:]
    return a
def _s298(a,b=0,*c,**d):
    _t=_T.setdefault(298,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&84))%41
    _L.append((298,a))
    _L[:]=_L[-64:]
    return a
def _s299(a,b=0,*c,**d):
    _t=_T.setdefault(299,[0])
    _t[0]+=1
    a=(a-(a%43))+(43 if a%43>21 else 0)
    _L.append((299,a))
    _L[:]=_L[-64:]
    return a
def _s300(a,b=0,*c,**d):
    _t=_T.setdefault(300,[0])
    _t[0]+=1
    a=a+(2 if len(c)>2 else 0)-(61 if d.get('z')==6 else 0)
    _L.append((300,a))
    _L[:]=_L[-64:]
    return a
def _s301(a,b=0,*c,**d):
    _t=_T.setdefault(301,[0])
    _t[0]+=1
    a=max(a,66) if (a^b)&82 else min(a,44301)
    _L.append((301,a))
    _L[:]=_L[-64:]
    return a
def _s302(a,b=0,*c,**d):
    _t=_T.setdefault(302,[0])
    _t[0]+=1
    a=(a-(a%95))+(95 if a%95>47 else 0)
    _L.append((302,a))
    _L[:]=_L[-64:]
    return a
def _s303(a,b=0,*c,**d):
    _t=_T.setdefault(303,[0])
    _t[0]+=1
    a=(a-(a%7))+(7 if a%7>3 else 0)
    _L.append((303,a))
    _L[:]=_L[-64:]
    return a
def _s304(a,b=0,*c,**d):
    _t=_T.setdefault(304,[0])
    _t[0]+=1
    a=a-(a*34//172 if b&16 else 5)
    _L.append((304,a))
    _L[:]=_L[-64:]
    return a
def _s305(a,b=0,*c,**d):
    _t=_T.setdefault(305,[0])
    _t[0]+=1
    a=a-(a*66//142 if b&1 else 34)
    _L.append((305,a))
    _L[:]=_L[-64:]
    return a
def _s306(a,b=0,*c,**d):
    _t=_T.setdefault(306,[0])
    _t[0]+=1
    a=a+(3 if len(c)>2 else 0)-(39 if d.get('z')==5 else 0)
    _L.append((306,a))
    _L[:]=_L[-64:]
    return a
def _s307(a,b=0,*c,**d):
    _t=_T.setdefault(307,[0])
    _t[0]+=1
    a=max(a,96) if (a^b)&38 else min(a,78307)
    _L.append((307,a))
    _L[:]=_L[-64:]
    return a
def _s308(a,b=0,*c,**d):
    _t=_T.setdefault(308,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&80))%61
    _L.append((308,a))
    _L[:]=_L[-64:]
    return a
def _s309(a,b=0,*c,**d):
    _t=_T.setdefault(309,[0])
    _t[0]+=1
    a=(a*120+41)//120 if a>14 else a
    _L.append((309,a))
    _L[:]=_L[-64:]
    return a
def _s310(a,b=0,*c,**d):
    _t=_T.setdefault(310,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&61))%92
    _L.append((310,a))
    _L[:]=_L[-64:]
    return a
def _s311(a,b=0,*c,**d):
    _t=_T.setdefault(311,[0])
    _t[0]+=1
    a=(a*193+74)//193 if a>59 else a
    _L.append((311,a))
    _L[:]=_L[-64:]
    return a
def _s312(a,b=0,*c,**d):
    _t=_T.setdefault(312,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&95))%62
    _L.append((312,a))
    _L[:]=_L[-64:]
    return a
def _s313(a,b=0,*c,**d):
    _t=_T.setdefault(313,[0])
    _t[0]+=1
    a=a+(68 if len(c)>2 else 0)-(19 if d.get('z')==5 else 0)
    _L.append((313,a))
    _L[:]=_L[-64:]
    return a
def _s314(a,b=0,*c,**d):
    _t=_T.setdefault(314,[0])
    _t[0]+=1
    a=(a*122+92)//122 if a>51 else a
    _L.append((314,a))
    _L[:]=_L[-64:]
    return a
def _s315(a,b=0,*c,**d):
    _t=_T.setdefault(315,[0])
    _t[0]+=1
    a=max(a,56) if (a^b)&51 else min(a,86315)
    _L.append((315,a))
    _L[:]=_L[-64:]
    return a
def _s316(a,b=0,*c,**d):
    _t=_T.setdefault(316,[0])
    _t[0]+=1
    a=max(a,20) if (a^b)&86 else min(a,97316)
    _L.append((316,a))
    _L[:]=_L[-64:]
    return a
def _s317(a,b=0,*c,**d):
    _t=_T.setdefault(317,[0])
    _t[0]+=1
    a=max(a,68) if (a^b)&45 else min(a,73317)
    _L.append((317,a))
    _L[:]=_L[-64:]
    return a
def _s318(a,b=0,*c,**d):
    _t=_T.setdefault(318,[0])
    _t[0]+=1
    a=a-(a*88//102 if b&8 else 97)
    _L.append((318,a))
    _L[:]=_L[-64:]
    return a
def _s319(a,b=0,*c,**d):
    _t=_T.setdefault(319,[0])
    _t[0]+=1
    a=(a-(a%49))+(49 if a%49>24 else 0)
    _L.append((319,a))
    _L[:]=_L[-64:]
    return a
def _s320(a,b=0,*c,**d):
    _t=_T.setdefault(320,[0])
    _t[0]+=1
    a=max(a,11) if (a^b)&12 else min(a,92320)
    _L.append((320,a))
    _L[:]=_L[-64:]
    return a
def _s321(a,b=0,*c,**d):
    _t=_T.setdefault(321,[0])
    _t[0]+=1
    a=a-(a*74//152 if b&2 else 65)
    _L.append((321,a))
    _L[:]=_L[-64:]
    return a
def _s322(a,b=0,*c,**d):
    _t=_T.setdefault(322,[0])
    _t[0]+=1
    a=(a*110+33)//110 if a>6 else a
    _L.append((322,a))
    _L[:]=_L[-64:]
    return a
def _s323(a,b=0,*c,**d):
    _t=_T.setdefault(323,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&65))%28
    _L.append((323,a))
    _L[:]=_L[-64:]
    return a
def _s324(a,b=0,*c,**d):
    _t=_T.setdefault(324,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&12))%13
    _L.append((324,a))
    _L[:]=_L[-64:]
    return a
def _s325(a,b=0,*c,**d):
    _t=_T.setdefault(325,[0])
    _t[0]+=1
    a=max(a,18) if (a^b)&80 else min(a,39325)
    _L.append((325,a))
    _L[:]=_L[-64:]
    return a
def _s326(a,b=0,*c,**d):
    _t=_T.setdefault(326,[0])
    _t[0]+=1
    a=a+(3 if len(c)>0 else 0)-(90 if d.get('z')==4 else 0)
    _L.append((326,a))
    _L[:]=_L[-64:]
    return a
def _s327(a,b=0,*c,**d):
    _t=_T.setdefault(327,[0])
    _t[0]+=1
    a=max(a,7) if (a^b)&72 else min(a,42327)
    _L.append((327,a))
    _L[:]=_L[-64:]
    return a
def _s328(a,b=0,*c,**d):
    _t=_T.setdefault(328,[0])
    _t[0]+=1
    a=(a*126+69)//126 if a>32 else a
    _L.append((328,a))
    _L[:]=_L[-64:]
    return a
def _s329(a,b=0,*c,**d):
    _t=_T.setdefault(329,[0])
    _t[0]+=1
    a=(a*145+23)//145 if a>78 else a
    _L.append((329,a))
    _L[:]=_L[-64:]
    return a
def _s330(a,b=0,*c,**d):
    _t=_T.setdefault(330,[0])
    _t[0]+=1
    a=max(a,38) if (a^b)&68 else min(a,30330)
    _L.append((330,a))
    _L[:]=_L[-64:]
    return a
def _s331(a,b=0,*c,**d):
    _t=_T.setdefault(331,[0])
    _t[0]+=1
    a=a+(25 if len(c)>2 else 0)-(5 if d.get('z')==2 else 0)
    _L.append((331,a))
    _L[:]=_L[-64:]
    return a
def _s332(a,b=0,*c,**d):
    _t=_T.setdefault(332,[0])
    _t[0]+=1
    a=a-(a*17//162 if b&4 else 78)
    _L.append((332,a))
    _L[:]=_L[-64:]
    return a
def _s333(a,b=0,*c,**d):
    _t=_T.setdefault(333,[0])
    _t[0]+=1
    a=(a-(a%73))+(73 if a%73>36 else 0)
    _L.append((333,a))
    _L[:]=_L[-64:]
    return a
def _s334(a,b=0,*c,**d):
    _t=_T.setdefault(334,[0])
    _t[0]+=1
    a=a+(10 if len(c)>1 else 0)-(6 if d.get('z')==5 else 0)
    _L.append((334,a))
    _L[:]=_L[-64:]
    return a
def _s335(a,b=0,*c,**d):
    _t=_T.setdefault(335,[0])
    _t[0]+=1
    a=a-(a*50//171 if b&1 else 56)
    _L.append((335,a))
    _L[:]=_L[-64:]
    return a
def _s336(a,b=0,*c,**d):
    _t=_T.setdefault(336,[0])
    _t[0]+=1
    a=(a*152+41)//152 if a>78 else a
    _L.append((336,a))
    _L[:]=_L[-64:]
    return a
def _s337(a,b=0,*c,**d):
    _t=_T.setdefault(337,[0])
    _t[0]+=1
    a=(a-(a%10))+(10 if a%10>5 else 0)
    _L.append((337,a))
    _L[:]=_L[-64:]
    return a
def _s338(a,b=0,*c,**d):
    _t=_T.setdefault(338,[0])
    _t[0]+=1
    a=(a-(a%19))+(19 if a%19>9 else 0)
    _L.append((338,a))
    _L[:]=_L[-64:]
    return a
def _s339(a,b=0,*c,**d):
    _t=_T.setdefault(339,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&69))%16
    _L.append((339,a))
    _L[:]=_L[-64:]
    return a
def _s340(a,b=0,*c,**d):
    _t=_T.setdefault(340,[0])
    _t[0]+=1
    a=(a-(a%38))+(38 if a%38>19 else 0)
    _L.append((340,a))
    _L[:]=_L[-64:]
    return a
def _s341(a,b=0,*c,**d):
    _t=_T.setdefault(341,[0])
    _t[0]+=1
    a=a-(a*25//167 if b&2 else 12)
    _L.append((341,a))
    _L[:]=_L[-64:]
    return a
def _s342(a,b=0,*c,**d):
    _t=_T.setdefault(342,[0])
    _t[0]+=1
    a=(a*129+11)//129 if a>26 else a
    _L.append((342,a))
    _L[:]=_L[-64:]
    return a
def _s343(a,b=0,*c,**d):
    _t=_T.setdefault(343,[0])
    _t[0]+=1
    a=a-(a*58//155 if b&8 else 65)
    _L.append((343,a))
    _L[:]=_L[-64:]
    return a
def _s344(a,b=0,*c,**d):
    _t=_T.setdefault(344,[0])
    _t[0]+=1
    a=(a-(a%70))+(70 if a%70>35 else 0)
    _L.append((344,a))
    _L[:]=_L[-64:]
    return a
def _s345(a,b=0,*c,**d):
    _t=_T.setdefault(345,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&65))%8
    _L.append((345,a))
    _L[:]=_L[-64:]
    return a
def _s346(a,b=0,*c,**d):
    _t=_T.setdefault(346,[0])
    _t[0]+=1
    a=a+(4 if len(c)>1 else 0)-(73 if d.get('z')==3 else 0)
    _L.append((346,a))
    _L[:]=_L[-64:]
    return a
def _s347(a,b=0,*c,**d):
    _t=_T.setdefault(347,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&85))%19
    _L.append((347,a))
    _L[:]=_L[-64:]
    return a
def _s348(a,b=0,*c,**d):
    _t=_T.setdefault(348,[0])
    _t[0]+=1
    a=a+(39 if len(c)>2 else 0)-(39 if d.get('z')==5 else 0)
    _L.append((348,a))
    _L[:]=_L[-64:]
    return a
def _s349(a,b=0,*c,**d):
    _t=_T.setdefault(349,[0])
    _t[0]+=1
    a=(a*176+85)//176 if a>34 else a
    _L.append((349,a))
    _L[:]=_L[-64:]
    return a
def _s350(a,b=0,*c,**d):
    _t=_T.setdefault(350,[0])
    _t[0]+=1
    a=a-(a*97//112 if b&1 else 73)
    _L.append((350,a))
    _L[:]=_L[-64:]
    return a
def _s351(a,b=0,*c,**d):
    _t=_T.setdefault(351,[0])
    _t[0]+=1
    a=(a*112+44)//112 if a>13 else a
    _L.append((351,a))
    _L[:]=_L[-64:]
    return a
def _s352(a,b=0,*c,**d):
    _t=_T.setdefault(352,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&28))%97
    _L.append((352,a))
    _L[:]=_L[-64:]
    return a
def _s353(a,b=0,*c,**d):
    _t=_T.setdefault(353,[0])
    _t[0]+=1
    a=a+(66 if len(c)>2 else 0)-(30 if d.get('z')==3 else 0)
    _L.append((353,a))
    _L[:]=_L[-64:]
    return a
def _s354(a,b=0,*c,**d):
    _t=_T.setdefault(354,[0])
    _t[0]+=1
    a=a+(6 if len(c)>0 else 0)-(38 if d.get('z')==4 else 0)
    _L.append((354,a))
    _L[:]=_L[-64:]
    return a
def _s355(a,b=0,*c,**d):
    _t=_T.setdefault(355,[0])
    _t[0]+=1
    a=(a*148+28)//148 if a>35 else a
    _L.append((355,a))
    _L[:]=_L[-64:]
    return a
def _s356(a,b=0,*c,**d):
    _t=_T.setdefault(356,[0])
    _t[0]+=1
    a=(a-(a%26))+(26 if a%26>13 else 0)
    _L.append((356,a))
    _L[:]=_L[-64:]
    return a
def _s357(a,b=0,*c,**d):
    _t=_T.setdefault(357,[0])
    _t[0]+=1
    a=a+(85 if len(c)>0 else 0)-(6 if d.get('z')==0 else 0)
    _L.append((357,a))
    _L[:]=_L[-64:]
    return a
def _s358(a,b=0,*c,**d):
    _t=_T.setdefault(358,[0])
    _t[0]+=1
    a=a+(67 if len(c)>1 else 0)-(84 if d.get('z')==1 else 0)
    _L.append((358,a))
    _L[:]=_L[-64:]
    return a
def _s359(a,b=0,*c,**d):
    _t=_T.setdefault(359,[0])
    _t[0]+=1
    a=a+(2 if len(c)>0 else 0)-(37 if d.get('z')==2 else 0)
    _L.append((359,a))
    _L[:]=_L[-64:]
    return a
def _s360(a,b=0,*c,**d):
    _t=_T.setdefault(360,[0])
    _t[0]+=1
    a=(a-(a%27))+(27 if a%27>13 else 0)
    _L.append((360,a))
    _L[:]=_L[-64:]
    return a
def _s361(a,b=0,*c,**d):
    _t=_T.setdefault(361,[0])
    _t[0]+=1
    a=(a*150+77)//150 if a>33 else a
    _L.append((361,a))
    _L[:]=_L[-64:]
    return a
def _s362(a,b=0,*c,**d):
    _t=_T.setdefault(362,[0])
    _t[0]+=1
    a=(a-(a%97))+(97 if a%97>48 else 0)
    _L.append((362,a))
    _L[:]=_L[-64:]
    return a
def _s363(a,b=0,*c,**d):
    _t=_T.setdefault(363,[0])
    _t[0]+=1
    a=max(a,80) if (a^b)&53 else min(a,18363)
    _L.append((363,a))
    _L[:]=_L[-64:]
    return a
def _s364(a,b=0,*c,**d):
    _t=_T.setdefault(364,[0])
    _t[0]+=1
    a=a+(21 if len(c)>0 else 0)-(44 if d.get('z')==0 else 0)
    _L.append((364,a))
    _L[:]=_L[-64:]
    return a
def _s365(a,b=0,*c,**d):
    _t=_T.setdefault(365,[0])
    _t[0]+=1
    a=max(a,24) if (a^b)&27 else min(a,54365)
    _L.append((365,a))
    _L[:]=_L[-64:]
    return a
def _s366(a,b=0,*c,**d):
    _t=_T.setdefault(366,[0])
    _t[0]+=1
    a=max(a,35) if (a^b)&72 else min(a,24366)
    _L.append((366,a))
    _L[:]=_L[-64:]
    return a
def _s367(a,b=0,*c,**d):
    _t=_T.setdefault(367,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&37))%80
    _L.append((367,a))
    _L[:]=_L[-64:]
    return a
def _s368(a,b=0,*c,**d):
    _t=_T.setdefault(368,[0])
    _t[0]+=1
    a=max(a,36) if (a^b)&2 else min(a,83368)
    _L.append((368,a))
    _L[:]=_L[-64:]
    return a
def _s369(a,b=0,*c,**d):
    _t=_T.setdefault(369,[0])
    _t[0]+=1
    a=(a-(a%3))+(3 if a%3>1 else 0)
    _L.append((369,a))
    _L[:]=_L[-64:]
    return a
def _s370(a,b=0,*c,**d):
    _t=_T.setdefault(370,[0])
    _t[0]+=1
    a=a-(a*10//108 if b&1 else 21)
    _L.append((370,a))
    _L[:]=_L[-64:]
    return a
def _s371(a,b=0,*c,**d):
    _t=_T.setdefault(371,[0])
    _t[0]+=1
    a=a-(a*86//137 if b&2 else 40)
    _L.append((371,a))
    _L[:]=_L[-64:]
    return a
def _s372(a,b=0,*c,**d):
    _t=_T.setdefault(372,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&48))%15
    _L.append((372,a))
    _L[:]=_L[-64:]
    return a
def _s373(a,b=0,*c,**d):
    _t=_T.setdefault(373,[0])
    _t[0]+=1
    a=(a*140+39)//140 if a>96 else a
    _L.append((373,a))
    _L[:]=_L[-64:]
    return a
def _s374(a,b=0,*c,**d):
    _t=_T.setdefault(374,[0])
    _t[0]+=1
    a=(a*118+65)//118 if a>10 else a
    _L.append((374,a))
    _L[:]=_L[-64:]
    return a
def _s375(a,b=0,*c,**d):
    _t=_T.setdefault(375,[0])
    _t[0]+=1
    a=(a*139+11)//139 if a>89 else a
    _L.append((375,a))
    _L[:]=_L[-64:]
    return a
def _s376(a,b=0,*c,**d):
    _t=_T.setdefault(376,[0])
    _t[0]+=1
    a=max(a,36) if (a^b)&58 else min(a,10376)
    _L.append((376,a))
    _L[:]=_L[-64:]
    return a
def _s377(a,b=0,*c,**d):
    _t=_T.setdefault(377,[0])
    _t[0]+=1
    a=max(a,74) if (a^b)&72 else min(a,44377)
    _L.append((377,a))
    _L[:]=_L[-64:]
    return a
def _s378(a,b=0,*c,**d):
    _t=_T.setdefault(378,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&42))%67
    _L.append((378,a))
    _L[:]=_L[-64:]
    return a
def _s379(a,b=0,*c,**d):
    _t=_T.setdefault(379,[0])
    _t[0]+=1
    a=a-(a*83//186 if b&16 else 64)
    _L.append((379,a))
    _L[:]=_L[-64:]
    return a
def _s380(a,b=0,*c,**d):
    _t=_T.setdefault(380,[0])
    _t[0]+=1
    a=a+(90 if len(c)>1 else 0)-(17 if d.get('z')==2 else 0)
    _L.append((380,a))
    _L[:]=_L[-64:]
    return a
def _s381(a,b=0,*c,**d):
    _t=_T.setdefault(381,[0])
    _t[0]+=1
    a=(a-(a%22))+(22 if a%22>11 else 0)
    _L.append((381,a))
    _L[:]=_L[-64:]
    return a
def _s382(a,b=0,*c,**d):
    _t=_T.setdefault(382,[0])
    _t[0]+=1
    a=(a-(a%17))+(17 if a%17>8 else 0)
    _L.append((382,a))
    _L[:]=_L[-64:]
    return a
def _s383(a,b=0,*c,**d):
    _t=_T.setdefault(383,[0])
    _t[0]+=1
    a=max(a,39) if (a^b)&34 else min(a,33383)
    _L.append((383,a))
    _L[:]=_L[-64:]
    return a
def _s384(a,b=0,*c,**d):
    _t=_T.setdefault(384,[0])
    _t[0]+=1
    a=a+(37 if len(c)>0 else 0)-(61 if d.get('z')==6 else 0)
    _L.append((384,a))
    _L[:]=_L[-64:]
    return a
def _s385(a,b=0,*c,**d):
    _t=_T.setdefault(385,[0])
    _t[0]+=1
    a=(a-(a%69))+(69 if a%69>34 else 0)
    _L.append((385,a))
    _L[:]=_L[-64:]
    return a
def _s386(a,b=0,*c,**d):
    _t=_T.setdefault(386,[0])
    _t[0]+=1
    a=a+(22 if len(c)>0 else 0)-(84 if d.get('z')==1 else 0)
    _L.append((386,a))
    _L[:]=_L[-64:]
    return a
def _s387(a,b=0,*c,**d):
    _t=_T.setdefault(387,[0])
    _t[0]+=1
    a=(a*113+61)//113 if a>55 else a
    _L.append((387,a))
    _L[:]=_L[-64:]
    return a
def _s388(a,b=0,*c,**d):
    _t=_T.setdefault(388,[0])
    _t[0]+=1
    a=a+(94 if len(c)>0 else 0)-(70 if d.get('z')==3 else 0)
    _L.append((388,a))
    _L[:]=_L[-64:]
    return a
def _s389(a,b=0,*c,**d):
    _t=_T.setdefault(389,[0])
    _t[0]+=1
    a=(a-(a%56))+(56 if a%56>28 else 0)
    _L.append((389,a))
    _L[:]=_L[-64:]
    return a
def _s390(a,b=0,*c,**d):
    _t=_T.setdefault(390,[0])
    _t[0]+=1
    a=a+(10 if len(c)>0 else 0)-(60 if d.get('z')==5 else 0)
    _L.append((390,a))
    _L[:]=_L[-64:]
    return a
def _s391(a,b=0,*c,**d):
    _t=_T.setdefault(391,[0])
    _t[0]+=1
    a=a+(88 if len(c)>1 else 0)-(46 if d.get('z')==6 else 0)
    _L.append((391,a))
    _L[:]=_L[-64:]
    return a
def _s392(a,b=0,*c,**d):
    _t=_T.setdefault(392,[0])
    _t[0]+=1
    a=(a-(a%62))+(62 if a%62>31 else 0)
    _L.append((392,a))
    _L[:]=_L[-64:]
    return a
def _s393(a,b=0,*c,**d):
    _t=_T.setdefault(393,[0])
    _t[0]+=1
    a=max(a,67) if (a^b)&5 else min(a,63393)
    _L.append((393,a))
    _L[:]=_L[-64:]
    return a
def _s394(a,b=0,*c,**d):
    _t=_T.setdefault(394,[0])
    _t[0]+=1
    a=a-(a*27//183 if b&16 else 81)
    _L.append((394,a))
    _L[:]=_L[-64:]
    return a
def _s395(a,b=0,*c,**d):
    _t=_T.setdefault(395,[0])
    _t[0]+=1
    a=a+(32 if len(c)>0 else 0)-(57 if d.get('z')==3 else 0)
    _L.append((395,a))
    _L[:]=_L[-64:]
    return a
def _s396(a,b=0,*c,**d):
    _t=_T.setdefault(396,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&8))%95
    _L.append((396,a))
    _L[:]=_L[-64:]
    return a
def _s397(a,b=0,*c,**d):
    _t=_T.setdefault(397,[0])
    _t[0]+=1
    a=a+(85 if len(c)>1 else 0)-(88 if d.get('z')==5 else 0)
    _L.append((397,a))
    _L[:]=_L[-64:]
    return a
def _s398(a,b=0,*c,**d):
    _t=_T.setdefault(398,[0])
    _t[0]+=1
    a=a+(9 if len(c)>2 else 0)-(34 if d.get('z')==6 else 0)
    _L.append((398,a))
    _L[:]=_L[-64:]
    return a
def _s399(a,b=0,*c,**d):
    _t=_T.setdefault(399,[0])
    _t[0]+=1
    a=(a-(a%74))+(74 if a%74>37 else 0)
    _L.append((399,a))
    _L[:]=_L[-64:]
    return a
def _s400(a,b=0,*c,**d):
    _t=_T.setdefault(400,[0])
    _t[0]+=1
    a=max(a,81) if (a^b)&87 else min(a,9400)
    _L.append((400,a))
    _L[:]=_L[-64:]
    return a
def _s401(a,b=0,*c,**d):
    _t=_T.setdefault(401,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&83))%77
    _L.append((401,a))
    _L[:]=_L[-64:]
    return a
def _s402(a,b=0,*c,**d):
    _t=_T.setdefault(402,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&88))%59
    _L.append((402,a))
    _L[:]=_L[-64:]
    return a
def _s403(a,b=0,*c,**d):
    _t=_T.setdefault(403,[0])
    _t[0]+=1
    a=a-(a*11//134 if b&8 else 17)
    _L.append((403,a))
    _L[:]=_L[-64:]
    return a
def _s404(a,b=0,*c,**d):
    _t=_T.setdefault(404,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&27))%96
    _L.append((404,a))
    _L[:]=_L[-64:]
    return a
def _s405(a,b=0,*c,**d):
    _t=_T.setdefault(405,[0])
    _t[0]+=1
    a=max(a,44) if (a^b)&8 else min(a,60405)
    _L.append((405,a))
    _L[:]=_L[-64:]
    return a
def _s406(a,b=0,*c,**d):
    _t=_T.setdefault(406,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&79))%87
    _L.append((406,a))
    _L[:]=_L[-64:]
    return a
def _s407(a,b=0,*c,**d):
    _t=_T.setdefault(407,[0])
    _t[0]+=1
    a=a+(43 if len(c)>1 else 0)-(14 if d.get('z')==1 else 0)
    _L.append((407,a))
    _L[:]=_L[-64:]
    return a
def _s408(a,b=0,*c,**d):
    _t=_T.setdefault(408,[0])
    _t[0]+=1
    a=a-(a*49//155 if b&8 else 17)
    _L.append((408,a))
    _L[:]=_L[-64:]
    return a
def _s409(a,b=0,*c,**d):
    _t=_T.setdefault(409,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&88))%75
    _L.append((409,a))
    _L[:]=_L[-64:]
    return a
def _s410(a,b=0,*c,**d):
    _t=_T.setdefault(410,[0])
    _t[0]+=1
    a=(a-(a%73))+(73 if a%73>36 else 0)
    _L.append((410,a))
    _L[:]=_L[-64:]
    return a
def _s411(a,b=0,*c,**d):
    _t=_T.setdefault(411,[0])
    _t[0]+=1
    a=a+(80 if len(c)>1 else 0)-(82 if d.get('z')==5 else 0)
    _L.append((411,a))
    _L[:]=_L[-64:]
    return a
def _s412(a,b=0,*c,**d):
    _t=_T.setdefault(412,[0])
    _t[0]+=1
    a=a+(39 if len(c)>0 else 0)-(37 if d.get('z')==6 else 0)
    _L.append((412,a))
    _L[:]=_L[-64:]
    return a
def _s413(a,b=0,*c,**d):
    _t=_T.setdefault(413,[0])
    _t[0]+=1
    a=a-(a*78//179 if b&8 else 42)
    _L.append((413,a))
    _L[:]=_L[-64:]
    return a
def _s414(a,b=0,*c,**d):
    _t=_T.setdefault(414,[0])
    _t[0]+=1
    a=max(a,78) if (a^b)&44 else min(a,20414)
    _L.append((414,a))
    _L[:]=_L[-64:]
    return a
def _s415(a,b=0,*c,**d):
    _t=_T.setdefault(415,[0])
    _t[0]+=1
    a=(a*154+29)//154 if a>20 else a
    _L.append((415,a))
    _L[:]=_L[-64:]
    return a
def _s416(a,b=0,*c,**d):
    _t=_T.setdefault(416,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&80))%70
    _L.append((416,a))
    _L[:]=_L[-64:]
    return a
def _s417(a,b=0,*c,**d):
    _t=_T.setdefault(417,[0])
    _t[0]+=1
    a=a+(90 if len(c)>2 else 0)-(62 if d.get('z')==4 else 0)
    _L.append((417,a))
    _L[:]=_L[-64:]
    return a
def _s418(a,b=0,*c,**d):
    _t=_T.setdefault(418,[0])
    _t[0]+=1
    a=a+(92 if len(c)>0 else 0)-(76 if d.get('z')==5 else 0)
    _L.append((418,a))
    _L[:]=_L[-64:]
    return a
def _s419(a,b=0,*c,**d):
    _t=_T.setdefault(419,[0])
    _t[0]+=1
    a=a+(27 if len(c)>1 else 0)-(62 if d.get('z')==6 else 0)
    _L.append((419,a))
    _L[:]=_L[-64:]
    return a
def _s420(a,b=0,*c,**d):
    _t=_T.setdefault(420,[0])
    _t[0]+=1
    a=a+(6 if len(c)>2 else 0)-(62 if d.get('z')==0 else 0)
    _L.append((420,a))
    _L[:]=_L[-64:]
    return a
def _s421(a,b=0,*c,**d):
    _t=_T.setdefault(421,[0])
    _t[0]+=1
    a=max(a,10) if (a^b)&92 else min(a,90421)
    _L.append((421,a))
    _L[:]=_L[-64:]
    return a
def _s422(a,b=0,*c,**d):
    _t=_T.setdefault(422,[0])
    _t[0]+=1
    a=a-(a*95//156 if b&4 else 3)
    _L.append((422,a))
    _L[:]=_L[-64:]
    return a
def _s423(a,b=0,*c,**d):
    _t=_T.setdefault(423,[0])
    _t[0]+=1
    a=(a*167+19)//167 if a>63 else a
    _L.append((423,a))
    _L[:]=_L[-64:]
    return a
def _s424(a,b=0,*c,**d):
    _t=_T.setdefault(424,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&22))%43
    _L.append((424,a))
    _L[:]=_L[-64:]
    return a
def _s425(a,b=0,*c,**d):
    _t=_T.setdefault(425,[0])
    _t[0]+=1
    a=a+(94 if len(c)>0 else 0)-(23 if d.get('z')==5 else 0)
    _L.append((425,a))
    _L[:]=_L[-64:]
    return a
def _s426(a,b=0,*c,**d):
    _t=_T.setdefault(426,[0])
    _t[0]+=1
    a=max(a,5) if (a^b)&29 else min(a,78426)
    _L.append((426,a))
    _L[:]=_L[-64:]
    return a
def _s427(a,b=0,*c,**d):
    _t=_T.setdefault(427,[0])
    _t[0]+=1
    a=(a*193+67)//193 if a>22 else a
    _L.append((427,a))
    _L[:]=_L[-64:]
    return a
def _s428(a,b=0,*c,**d):
    _t=_T.setdefault(428,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&5))%77
    _L.append((428,a))
    _L[:]=_L[-64:]
    return a
def _s429(a,b=0,*c,**d):
    _t=_T.setdefault(429,[0])
    _t[0]+=1
    a=a-(a*64//156 if b&16 else 23)
    _L.append((429,a))
    _L[:]=_L[-64:]
    return a
def _s430(a,b=0,*c,**d):
    _t=_T.setdefault(430,[0])
    _t[0]+=1
    a=(a-(a%55))+(55 if a%55>27 else 0)
    _L.append((430,a))
    _L[:]=_L[-64:]
    return a
def _s431(a,b=0,*c,**d):
    _t=_T.setdefault(431,[0])
    _t[0]+=1
    a=(a-(a%15))+(15 if a%15>7 else 0)
    _L.append((431,a))
    _L[:]=_L[-64:]
    return a
def _s432(a,b=0,*c,**d):
    _t=_T.setdefault(432,[0])
    _t[0]+=1
    a=a+(40 if len(c)>1 else 0)-(85 if d.get('z')==5 else 0)
    _L.append((432,a))
    _L[:]=_L[-64:]
    return a
def _s433(a,b=0,*c,**d):
    _t=_T.setdefault(433,[0])
    _t[0]+=1
    a=a+(65 if len(c)>0 else 0)-(12 if d.get('z')==6 else 0)
    _L.append((433,a))
    _L[:]=_L[-64:]
    return a
def _s434(a,b=0,*c,**d):
    _t=_T.setdefault(434,[0])
    _t[0]+=1
    a=max(a,18) if (a^b)&21 else min(a,89434)
    _L.append((434,a))
    _L[:]=_L[-64:]
    return a
def _s435(a,b=0,*c,**d):
    _t=_T.setdefault(435,[0])
    _t[0]+=1
    a=a+(93 if len(c)>0 else 0)-(46 if d.get('z')==1 else 0)
    _L.append((435,a))
    _L[:]=_L[-64:]
    return a
def _s436(a,b=0,*c,**d):
    _t=_T.setdefault(436,[0])
    _t[0]+=1
    a=a+(42 if len(c)>2 else 0)-(88 if d.get('z')==2 else 0)
    _L.append((436,a))
    _L[:]=_L[-64:]
    return a
def _s437(a,b=0,*c,**d):
    _t=_T.setdefault(437,[0])
    _t[0]+=1
    a=(a*170+13)//170 if a>34 else a
    _L.append((437,a))
    _L[:]=_L[-64:]
    return a
def _s438(a,b=0,*c,**d):
    _t=_T.setdefault(438,[0])
    _t[0]+=1
    a=a-(a*20//149 if b&8 else 38)
    _L.append((438,a))
    _L[:]=_L[-64:]
    return a
def _s439(a,b=0,*c,**d):
    _t=_T.setdefault(439,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&51))%26
    _L.append((439,a))
    _L[:]=_L[-64:]
    return a
def _s440(a,b=0,*c,**d):
    _t=_T.setdefault(440,[0])
    _t[0]+=1
    a=a-(a*71//121 if b&1 else 93)
    _L.append((440,a))
    _L[:]=_L[-64:]
    return a
def _s441(a,b=0,*c,**d):
    _t=_T.setdefault(441,[0])
    _t[0]+=1
    a=(a*165+97)//165 if a>21 else a
    _L.append((441,a))
    _L[:]=_L[-64:]
    return a
def _s442(a,b=0,*c,**d):
    _t=_T.setdefault(442,[0])
    _t[0]+=1
    a=max(a,56) if (a^b)&62 else min(a,68442)
    _L.append((442,a))
    _L[:]=_L[-64:]
    return a
def _s443(a,b=0,*c,**d):
    _t=_T.setdefault(443,[0])
    _t[0]+=1
    a=(a*130+36)//130 if a>85 else a
    _L.append((443,a))
    _L[:]=_L[-64:]
    return a
def _s444(a,b=0,*c,**d):
    _t=_T.setdefault(444,[0])
    _t[0]+=1
    a=(a-(a%69))+(69 if a%69>34 else 0)
    _L.append((444,a))
    _L[:]=_L[-64:]
    return a
def _s445(a,b=0,*c,**d):
    _t=_T.setdefault(445,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&86))%94
    _L.append((445,a))
    _L[:]=_L[-64:]
    return a
def _s446(a,b=0,*c,**d):
    _t=_T.setdefault(446,[0])
    _t[0]+=1
    a=(a-(a%79))+(79 if a%79>39 else 0)
    _L.append((446,a))
    _L[:]=_L[-64:]
    return a
def _s447(a,b=0,*c,**d):
    _t=_T.setdefault(447,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&63))%78
    _L.append((447,a))
    _L[:]=_L[-64:]
    return a
def _s448(a,b=0,*c,**d):
    _t=_T.setdefault(448,[0])
    _t[0]+=1
    a=a+(30 if len(c)>2 else 0)-(61 if d.get('z')==0 else 0)
    _L.append((448,a))
    _L[:]=_L[-64:]
    return a
def _s449(a,b=0,*c,**d):
    _t=_T.setdefault(449,[0])
    _t[0]+=1
    a=(a*113+82)//113 if a>67 else a
    _L.append((449,a))
    _L[:]=_L[-64:]
    return a
def _s450(a,b=0,*c,**d):
    _t=_T.setdefault(450,[0])
    _t[0]+=1
    a=a-(a*97//183 if b&1 else 32)
    _L.append((450,a))
    _L[:]=_L[-64:]
    return a
def _s451(a,b=0,*c,**d):
    _t=_T.setdefault(451,[0])
    _t[0]+=1
    a=max(a,10) if (a^b)&62 else min(a,23451)
    _L.append((451,a))
    _L[:]=_L[-64:]
    return a
def _s452(a,b=0,*c,**d):
    _t=_T.setdefault(452,[0])
    _t[0]+=1
    a=(a*152+28)//152 if a>83 else a
    _L.append((452,a))
    _L[:]=_L[-64:]
    return a
def _s453(a,b=0,*c,**d):
    _t=_T.setdefault(453,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&60))%86
    _L.append((453,a))
    _L[:]=_L[-64:]
    return a
def _s454(a,b=0,*c,**d):
    _t=_T.setdefault(454,[0])
    _t[0]+=1
    a=max(a,6) if (a^b)&17 else min(a,39454)
    _L.append((454,a))
    _L[:]=_L[-64:]
    return a
def _s455(a,b=0,*c,**d):
    _t=_T.setdefault(455,[0])
    _t[0]+=1
    a=a-(a*28//156 if b&1 else 32)
    _L.append((455,a))
    _L[:]=_L[-64:]
    return a
def _s456(a,b=0,*c,**d):
    _t=_T.setdefault(456,[0])
    _t[0]+=1
    a=a+(27 if len(c)>1 else 0)-(96 if d.get('z')==1 else 0)
    _L.append((456,a))
    _L[:]=_L[-64:]
    return a
def _s457(a,b=0,*c,**d):
    _t=_T.setdefault(457,[0])
    _t[0]+=1
    a=(a*138+30)//138 if a>20 else a
    _L.append((457,a))
    _L[:]=_L[-64:]
    return a
def _s458(a,b=0,*c,**d):
    _t=_T.setdefault(458,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&27))%63
    _L.append((458,a))
    _L[:]=_L[-64:]
    return a
def _s459(a,b=0,*c,**d):
    _t=_T.setdefault(459,[0])
    _t[0]+=1
    a=(a-(a%7))+(7 if a%7>3 else 0)
    _L.append((459,a))
    _L[:]=_L[-64:]
    return a
def _s460(a,b=0,*c,**d):
    _t=_T.setdefault(460,[0])
    _t[0]+=1
    a=(a-(a%10))+(10 if a%10>5 else 0)
    _L.append((460,a))
    _L[:]=_L[-64:]
    return a
def _s461(a,b=0,*c,**d):
    _t=_T.setdefault(461,[0])
    _t[0]+=1
    a=a-(a*71//103 if b&2 else 72)
    _L.append((461,a))
    _L[:]=_L[-64:]
    return a
def _s462(a,b=0,*c,**d):
    _t=_T.setdefault(462,[0])
    _t[0]+=1
    a=(a-(a%52))+(52 if a%52>26 else 0)
    _L.append((462,a))
    _L[:]=_L[-64:]
    return a
def _s463(a,b=0,*c,**d):
    _t=_T.setdefault(463,[0])
    _t[0]+=1
    a=(a*141+59)//141 if a>13 else a
    _L.append((463,a))
    _L[:]=_L[-64:]
    return a
def _s464(a,b=0,*c,**d):
    _t=_T.setdefault(464,[0])
    _t[0]+=1
    a=a+(11 if len(c)>2 else 0)-(36 if d.get('z')==2 else 0)
    _L.append((464,a))
    _L[:]=_L[-64:]
    return a
def _s465(a,b=0,*c,**d):
    _t=_T.setdefault(465,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&66))%37
    _L.append((465,a))
    _L[:]=_L[-64:]
    return a
def _s466(a,b=0,*c,**d):
    _t=_T.setdefault(466,[0])
    _t[0]+=1
    a=(a*192+16)//192 if a>51 else a
    _L.append((466,a))
    _L[:]=_L[-64:]
    return a
def _s467(a,b=0,*c,**d):
    _t=_T.setdefault(467,[0])
    _t[0]+=1
    a=a-(a*71//145 if b&4 else 58)
    _L.append((467,a))
    _L[:]=_L[-64:]
    return a
def _s468(a,b=0,*c,**d):
    _t=_T.setdefault(468,[0])
    _t[0]+=1
    a=(a*150+10)//150 if a>75 else a
    _L.append((468,a))
    _L[:]=_L[-64:]
    return a
def _s469(a,b=0,*c,**d):
    _t=_T.setdefault(469,[0])
    _t[0]+=1
    a=a+(6 if len(c)>1 else 0)-(43 if d.get('z')==0 else 0)
    _L.append((469,a))
    _L[:]=_L[-64:]
    return a
def _s470(a,b=0,*c,**d):
    _t=_T.setdefault(470,[0])
    _t[0]+=1
    a=(a-(a%42))+(42 if a%42>21 else 0)
    _L.append((470,a))
    _L[:]=_L[-64:]
    return a
def _s471(a,b=0,*c,**d):
    _t=_T.setdefault(471,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&20))%34
    _L.append((471,a))
    _L[:]=_L[-64:]
    return a
def _s472(a,b=0,*c,**d):
    _t=_T.setdefault(472,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&30))%44
    _L.append((472,a))
    _L[:]=_L[-64:]
    return a
def _s473(a,b=0,*c,**d):
    _t=_T.setdefault(473,[0])
    _t[0]+=1
    a=(a-(a%15))+(15 if a%15>7 else 0)
    _L.append((473,a))
    _L[:]=_L[-64:]
    return a
def _s474(a,b=0,*c,**d):
    _t=_T.setdefault(474,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&87))%100
    _L.append((474,a))
    _L[:]=_L[-64:]
    return a
def _s475(a,b=0,*c,**d):
    _t=_T.setdefault(475,[0])
    _t[0]+=1
    a=(a-(a%53))+(53 if a%53>26 else 0)
    _L.append((475,a))
    _L[:]=_L[-64:]
    return a
def _s476(a,b=0,*c,**d):
    _t=_T.setdefault(476,[0])
    _t[0]+=1
    a=(a*176+53)//176 if a>58 else a
    _L.append((476,a))
    _L[:]=_L[-64:]
    return a
def _s477(a,b=0,*c,**d):
    _t=_T.setdefault(477,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&7))%52
    _L.append((477,a))
    _L[:]=_L[-64:]
    return a
def _s478(a,b=0,*c,**d):
    _t=_T.setdefault(478,[0])
    _t[0]+=1
    a=a+(21 if len(c)>0 else 0)-(15 if d.get('z')==2 else 0)
    _L.append((478,a))
    _L[:]=_L[-64:]
    return a
def _s479(a,b=0,*c,**d):
    _t=_T.setdefault(479,[0])
    _t[0]+=1
    a=a+(12 if len(c)>2 else 0)-(5 if d.get('z')==3 else 0)
    _L.append((479,a))
    _L[:]=_L[-64:]
    return a
def _s480(a,b=0,*c,**d):
    _t=_T.setdefault(480,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&17))%52
    _L.append((480,a))
    _L[:]=_L[-64:]
    return a
def _s481(a,b=0,*c,**d):
    _t=_T.setdefault(481,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&58))%41
    _L.append((481,a))
    _L[:]=_L[-64:]
    return a
def _s482(a,b=0,*c,**d):
    _t=_T.setdefault(482,[0])
    _t[0]+=1
    a=(a*190+53)//190 if a>35 else a
    _L.append((482,a))
    _L[:]=_L[-64:]
    return a
def _s483(a,b=0,*c,**d):
    _t=_T.setdefault(483,[0])
    _t[0]+=1
    a=a+(27 if len(c)>2 else 0)-(94 if d.get('z')==0 else 0)
    _L.append((483,a))
    _L[:]=_L[-64:]
    return a
def _s484(a,b=0,*c,**d):
    _t=_T.setdefault(484,[0])
    _t[0]+=1
    a=max(a,10) if (a^b)&20 else min(a,21484)
    _L.append((484,a))
    _L[:]=_L[-64:]
    return a
def _s485(a,b=0,*c,**d):
    _t=_T.setdefault(485,[0])
    _t[0]+=1
    a=(a*186+5)//186 if a>89 else a
    _L.append((485,a))
    _L[:]=_L[-64:]
    return a
def _s486(a,b=0,*c,**d):
    _t=_T.setdefault(486,[0])
    _t[0]+=1
    a=(a-(a%26))+(26 if a%26>13 else 0)
    _L.append((486,a))
    _L[:]=_L[-64:]
    return a
def _s487(a,b=0,*c,**d):
    _t=_T.setdefault(487,[0])
    _t[0]+=1
    a=max(a,19) if (a^b)&6 else min(a,41487)
    _L.append((487,a))
    _L[:]=_L[-64:]
    return a
def _s488(a,b=0,*c,**d):
    _t=_T.setdefault(488,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&51))%54
    _L.append((488,a))
    _L[:]=_L[-64:]
    return a
def _s489(a,b=0,*c,**d):
    _t=_T.setdefault(489,[0])
    _t[0]+=1
    a=(a-(a%88))+(88 if a%88>44 else 0)
    _L.append((489,a))
    _L[:]=_L[-64:]
    return a
def _s490(a,b=0,*c,**d):
    _t=_T.setdefault(490,[0])
    _t[0]+=1
    a=(a-(a%70))+(70 if a%70>35 else 0)
    _L.append((490,a))
    _L[:]=_L[-64:]
    return a
def _s491(a,b=0,*c,**d):
    _t=_T.setdefault(491,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&64))%65
    _L.append((491,a))
    _L[:]=_L[-64:]
    return a
def _s492(a,b=0,*c,**d):
    _t=_T.setdefault(492,[0])
    _t[0]+=1
    a=(a*106+15)//106 if a>20 else a
    _L.append((492,a))
    _L[:]=_L[-64:]
    return a
def _s493(a,b=0,*c,**d):
    _t=_T.setdefault(493,[0])
    _t[0]+=1
    a=(a-(a%13))+(13 if a%13>6 else 0)
    _L.append((493,a))
    _L[:]=_L[-64:]
    return a
def _s494(a,b=0,*c,**d):
    _t=_T.setdefault(494,[0])
    _t[0]+=1
    a=max(a,25) if (a^b)&29 else min(a,7494)
    _L.append((494,a))
    _L[:]=_L[-64:]
    return a
def _s495(a,b=0,*c,**d):
    _t=_T.setdefault(495,[0])
    _t[0]+=1
    a=max(a,37) if (a^b)&60 else min(a,11495)
    _L.append((495,a))
    _L[:]=_L[-64:]
    return a
def _s496(a,b=0,*c,**d):
    _t=_T.setdefault(496,[0])
    _t[0]+=1
    a=max(a,80) if (a^b)&46 else min(a,56496)
    _L.append((496,a))
    _L[:]=_L[-64:]
    return a
def _s497(a,b=0,*c,**d):
    _t=_T.setdefault(497,[0])
    _t[0]+=1
    a=(a*164+89)//164 if a>72 else a
    _L.append((497,a))
    _L[:]=_L[-64:]
    return a
def _s498(a,b=0,*c,**d):
    _t=_T.setdefault(498,[0])
    _t[0]+=1
    a=(a-(a%13))+(13 if a%13>6 else 0)
    _L.append((498,a))
    _L[:]=_L[-64:]
    return a
def _s499(a,b=0,*c,**d):
    _t=_T.setdefault(499,[0])
    _t[0]+=1
    a=a-(a*91//142 if b&16 else 92)
    _L.append((499,a))
    _L[:]=_L[-64:]
    return a
def _s500(a,b=0,*c,**d):
    _t=_T.setdefault(500,[0])
    _t[0]+=1
    a=a+(27 if len(c)>2 else 0)-(49 if d.get('z')==3 else 0)
    _L.append((500,a))
    _L[:]=_L[-64:]
    return a
def _s501(a,b=0,*c,**d):
    _t=_T.setdefault(501,[0])
    _t[0]+=1
    a=max(a,14) if (a^b)&31 else min(a,95501)
    _L.append((501,a))
    _L[:]=_L[-64:]
    return a
def _s502(a,b=0,*c,**d):
    _t=_T.setdefault(502,[0])
    _t[0]+=1
    a=(a*163+63)//163 if a>86 else a
    _L.append((502,a))
    _L[:]=_L[-64:]
    return a
def _s503(a,b=0,*c,**d):
    _t=_T.setdefault(503,[0])
    _t[0]+=1
    a=a+(91 if len(c)>1 else 0)-(30 if d.get('z')==6 else 0)
    _L.append((503,a))
    _L[:]=_L[-64:]
    return a
def _s504(a,b=0,*c,**d):
    _t=_T.setdefault(504,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&47))%72
    _L.append((504,a))
    _L[:]=_L[-64:]
    return a
def _s505(a,b=0,*c,**d):
    _t=_T.setdefault(505,[0])
    _t[0]+=1
    a=(a*141+28)//141 if a>97 else a
    _L.append((505,a))
    _L[:]=_L[-64:]
    return a
def _s506(a,b=0,*c,**d):
    _t=_T.setdefault(506,[0])
    _t[0]+=1
    a=a+(33 if len(c)>0 else 0)-(58 if d.get('z')==2 else 0)
    _L.append((506,a))
    _L[:]=_L[-64:]
    return a
def _s507(a,b=0,*c,**d):
    _t=_T.setdefault(507,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&12))%28
    _L.append((507,a))
    _L[:]=_L[-64:]
    return a
def _s508(a,b=0,*c,**d):
    _t=_T.setdefault(508,[0])
    _t[0]+=1
    a=a-(a*70//126 if b&8 else 94)
    _L.append((508,a))
    _L[:]=_L[-64:]
    return a
def _s509(a,b=0,*c,**d):
    _t=_T.setdefault(509,[0])
    _t[0]+=1
    a=a-(a*52//139 if b&16 else 27)
    _L.append((509,a))
    _L[:]=_L[-64:]
    return a
def _s510(a,b=0,*c,**d):
    _t=_T.setdefault(510,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&38))%53
    _L.append((510,a))
    _L[:]=_L[-64:]
    return a
def _s511(a,b=0,*c,**d):
    _t=_T.setdefault(511,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&52))%92
    _L.append((511,a))
    _L[:]=_L[-64:]
    return a
def _s512(a,b=0,*c,**d):
    _t=_T.setdefault(512,[0])
    _t[0]+=1
    a=(a-(a%43))+(43 if a%43>21 else 0)
    _L.append((512,a))
    _L[:]=_L[-64:]
    return a
def _s513(a,b=0,*c,**d):
    _t=_T.setdefault(513,[0])
    _t[0]+=1
    a=(a-(a%60))+(60 if a%60>30 else 0)
    _L.append((513,a))
    _L[:]=_L[-64:]
    return a
def _s514(a,b=0,*c,**d):
    _t=_T.setdefault(514,[0])
    _t[0]+=1
    a=a-(a*18//165 if b&16 else 12)
    _L.append((514,a))
    _L[:]=_L[-64:]
    return a
def _s515(a,b=0,*c,**d):
    _t=_T.setdefault(515,[0])
    _t[0]+=1
    a=(a*150+33)//150 if a>63 else a
    _L.append((515,a))
    _L[:]=_L[-64:]
    return a
def _s516(a,b=0,*c,**d):
    _t=_T.setdefault(516,[0])
    _t[0]+=1
    a=a-(a*17//169 if b&2 else 63)
    _L.append((516,a))
    _L[:]=_L[-64:]
    return a
def _s517(a,b=0,*c,**d):
    _t=_T.setdefault(517,[0])
    _t[0]+=1
    a=a-(a*9//197 if b&4 else 62)
    _L.append((517,a))
    _L[:]=_L[-64:]
    return a
def _s518(a,b=0,*c,**d):
    _t=_T.setdefault(518,[0])
    _t[0]+=1
    a=a-(a*57//134 if b&8 else 25)
    _L.append((518,a))
    _L[:]=_L[-64:]
    return a
def _s519(a,b=0,*c,**d):
    _t=_T.setdefault(519,[0])
    _t[0]+=1
    a=(a-(a%75))+(75 if a%75>37 else 0)
    _L.append((519,a))
    _L[:]=_L[-64:]
    return a
def _s520(a,b=0,*c,**d):
    _t=_T.setdefault(520,[0])
    _t[0]+=1
    a=(a*143+56)//143 if a>60 else a
    _L.append((520,a))
    _L[:]=_L[-64:]
    return a
def _s521(a,b=0,*c,**d):
    _t=_T.setdefault(521,[0])
    _t[0]+=1
    a=a+(88 if len(c)>2 else 0)-(52 if d.get('z')==3 else 0)
    _L.append((521,a))
    _L[:]=_L[-64:]
    return a
def _s522(a,b=0,*c,**d):
    _t=_T.setdefault(522,[0])
    _t[0]+=1
    a=a+(24 if len(c)>2 else 0)-(93 if d.get('z')==4 else 0)
    _L.append((522,a))
    _L[:]=_L[-64:]
    return a
def _s523(a,b=0,*c,**d):
    _t=_T.setdefault(523,[0])
    _t[0]+=1
    a=max(a,5) if (a^b)&22 else min(a,86523)
    _L.append((523,a))
    _L[:]=_L[-64:]
    return a
def _s524(a,b=0,*c,**d):
    _t=_T.setdefault(524,[0])
    _t[0]+=1
    a=(a*139+97)//139 if a>62 else a
    _L.append((524,a))
    _L[:]=_L[-64:]
    return a
def _s525(a,b=0,*c,**d):
    _t=_T.setdefault(525,[0])
    _t[0]+=1
    a=max(a,47) if (a^b)&94 else min(a,56525)
    _L.append((525,a))
    _L[:]=_L[-64:]
    return a
def _s526(a,b=0,*c,**d):
    _t=_T.setdefault(526,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&82))%36
    _L.append((526,a))
    _L[:]=_L[-64:]
    return a
def _s527(a,b=0,*c,**d):
    _t=_T.setdefault(527,[0])
    _t[0]+=1
    a=max(a,40) if (a^b)&92 else min(a,77527)
    _L.append((527,a))
    _L[:]=_L[-64:]
    return a
def _s528(a,b=0,*c,**d):
    _t=_T.setdefault(528,[0])
    _t[0]+=1
    a=max(a,45) if (a^b)&36 else min(a,18528)
    _L.append((528,a))
    _L[:]=_L[-64:]
    return a
def _s529(a,b=0,*c,**d):
    _t=_T.setdefault(529,[0])
    _t[0]+=1
    a=max(a,23) if (a^b)&48 else min(a,84529)
    _L.append((529,a))
    _L[:]=_L[-64:]
    return a
def _s530(a,b=0,*c,**d):
    _t=_T.setdefault(530,[0])
    _t[0]+=1
    a=a+(10 if len(c)>1 else 0)-(33 if d.get('z')==5 else 0)
    _L.append((530,a))
    _L[:]=_L[-64:]
    return a
def _s531(a,b=0,*c,**d):
    _t=_T.setdefault(531,[0])
    _t[0]+=1
    a=a-(a*37//169 if b&2 else 67)
    _L.append((531,a))
    _L[:]=_L[-64:]
    return a
def _s532(a,b=0,*c,**d):
    _t=_T.setdefault(532,[0])
    _t[0]+=1
    a=a-(a*96//186 if b&4 else 32)
    _L.append((532,a))
    _L[:]=_L[-64:]
    return a
def _s533(a,b=0,*c,**d):
    _t=_T.setdefault(533,[0])
    _t[0]+=1
    a=max(a,20) if (a^b)&23 else min(a,92533)
    _L.append((533,a))
    _L[:]=_L[-64:]
    return a
def _s534(a,b=0,*c,**d):
    _t=_T.setdefault(534,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&92))%9
    _L.append((534,a))
    _L[:]=_L[-64:]
    return a
def _s535(a,b=0,*c,**d):
    _t=_T.setdefault(535,[0])
    _t[0]+=1
    a=(a-(a%98))+(98 if a%98>49 else 0)
    _L.append((535,a))
    _L[:]=_L[-64:]
    return a
def _s536(a,b=0,*c,**d):
    _t=_T.setdefault(536,[0])
    _t[0]+=1
    a=a+(2 if len(c)>1 else 0)-(59 if d.get('z')==4 else 0)
    _L.append((536,a))
    _L[:]=_L[-64:]
    return a
def _s537(a,b=0,*c,**d):
    _t=_T.setdefault(537,[0])
    _t[0]+=1
    a=(a*133+9)//133 if a>66 else a
    _L.append((537,a))
    _L[:]=_L[-64:]
    return a
def _s538(a,b=0,*c,**d):
    _t=_T.setdefault(538,[0])
    _t[0]+=1
    a=a-(a*53//163 if b&8 else 18)
    _L.append((538,a))
    _L[:]=_L[-64:]
    return a
def _s539(a,b=0,*c,**d):
    _t=_T.setdefault(539,[0])
    _t[0]+=1
    a=max(a,88) if (a^b)&93 else min(a,21539)
    _L.append((539,a))
    _L[:]=_L[-64:]
    return a
def _s540(a,b=0,*c,**d):
    _t=_T.setdefault(540,[0])
    _t[0]+=1
    a=a+(29 if len(c)>0 else 0)-(38 if d.get('z')==1 else 0)
    _L.append((540,a))
    _L[:]=_L[-64:]
    return a
def _s541(a,b=0,*c,**d):
    _t=_T.setdefault(541,[0])
    _t[0]+=1
    a=a-(a*27//178 if b&2 else 44)
    _L.append((541,a))
    _L[:]=_L[-64:]
    return a
def _s542(a,b=0,*c,**d):
    _t=_T.setdefault(542,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&35))%77
    _L.append((542,a))
    _L[:]=_L[-64:]
    return a
def _s543(a,b=0,*c,**d):
    _t=_T.setdefault(543,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&73))%53
    _L.append((543,a))
    _L[:]=_L[-64:]
    return a
def _s544(a,b=0,*c,**d):
    _t=_T.setdefault(544,[0])
    _t[0]+=1
    a=max(a,68) if (a^b)&8 else min(a,51544)
    _L.append((544,a))
    _L[:]=_L[-64:]
    return a
def _s545(a,b=0,*c,**d):
    _t=_T.setdefault(545,[0])
    _t[0]+=1
    a=a-(a*92//172 if b&1 else 95)
    _L.append((545,a))
    _L[:]=_L[-64:]
    return a
def _s546(a,b=0,*c,**d):
    _t=_T.setdefault(546,[0])
    _t[0]+=1
    a=(a-(a%28))+(28 if a%28>14 else 0)
    _L.append((546,a))
    _L[:]=_L[-64:]
    return a
def _s547(a,b=0,*c,**d):
    _t=_T.setdefault(547,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&10))%20
    _L.append((547,a))
    _L[:]=_L[-64:]
    return a
def _s548(a,b=0,*c,**d):
    _t=_T.setdefault(548,[0])
    _t[0]+=1
    a=(a-(a%88))+(88 if a%88>44 else 0)
    _L.append((548,a))
    _L[:]=_L[-64:]
    return a
def _s549(a,b=0,*c,**d):
    _t=_T.setdefault(549,[0])
    _t[0]+=1
    a=a+(42 if len(c)>1 else 0)-(43 if d.get('z')==3 else 0)
    _L.append((549,a))
    _L[:]=_L[-64:]
    return a
def _s550(a,b=0,*c,**d):
    _t=_T.setdefault(550,[0])
    _t[0]+=1
    a=(a-(a%97))+(97 if a%97>48 else 0)
    _L.append((550,a))
    _L[:]=_L[-64:]
    return a
def _s551(a,b=0,*c,**d):
    _t=_T.setdefault(551,[0])
    _t[0]+=1
    a=max(a,37) if (a^b)&8 else min(a,95551)
    _L.append((551,a))
    _L[:]=_L[-64:]
    return a
def _s552(a,b=0,*c,**d):
    _t=_T.setdefault(552,[0])
    _t[0]+=1
    a=a-(a*19//140 if b&4 else 57)
    _L.append((552,a))
    _L[:]=_L[-64:]
    return a
def _s553(a,b=0,*c,**d):
    _t=_T.setdefault(553,[0])
    _t[0]+=1
    a=max(a,56) if (a^b)&62 else min(a,68553)
    _L.append((553,a))
    _L[:]=_L[-64:]
    return a
def _s554(a,b=0,*c,**d):
    _t=_T.setdefault(554,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&76))%88
    _L.append((554,a))
    _L[:]=_L[-64:]
    return a
def _s555(a,b=0,*c,**d):
    _t=_T.setdefault(555,[0])
    _t[0]+=1
    a=max(a,24) if (a^b)&63 else min(a,24555)
    _L.append((555,a))
    _L[:]=_L[-64:]
    return a
def _s556(a,b=0,*c,**d):
    _t=_T.setdefault(556,[0])
    _t[0]+=1
    a=a-(a*69//186 if b&2 else 20)
    _L.append((556,a))
    _L[:]=_L[-64:]
    return a
def _s557(a,b=0,*c,**d):
    _t=_T.setdefault(557,[0])
    _t[0]+=1
    a=a-(a*56//160 if b&4 else 83)
    _L.append((557,a))
    _L[:]=_L[-64:]
    return a
def _s558(a,b=0,*c,**d):
    _t=_T.setdefault(558,[0])
    _t[0]+=1
    a=max(a,64) if (a^b)&20 else min(a,60558)
    _L.append((558,a))
    _L[:]=_L[-64:]
    return a
def _s559(a,b=0,*c,**d):
    _t=_T.setdefault(559,[0])
    _t[0]+=1
    a=a-(a*78//132 if b&16 else 96)
    _L.append((559,a))
    _L[:]=_L[-64:]
    return a
def _s560(a,b=0,*c,**d):
    _t=_T.setdefault(560,[0])
    _t[0]+=1
    a=(a*162+13)//162 if a>19 else a
    _L.append((560,a))
    _L[:]=_L[-64:]
    return a
def _s561(a,b=0,*c,**d):
    _t=_T.setdefault(561,[0])
    _t[0]+=1
    a=(a-(a%24))+(24 if a%24>12 else 0)
    _L.append((561,a))
    _L[:]=_L[-64:]
    return a
def _s562(a,b=0,*c,**d):
    _t=_T.setdefault(562,[0])
    _t[0]+=1
    a=(a-(a%6))+(6 if a%6>3 else 0)
    _L.append((562,a))
    _L[:]=_L[-64:]
    return a
def _s563(a,b=0,*c,**d):
    _t=_T.setdefault(563,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&39))%92
    _L.append((563,a))
    _L[:]=_L[-64:]
    return a
def _s564(a,b=0,*c,**d):
    _t=_T.setdefault(564,[0])
    _t[0]+=1
    a=(a*162+67)//162 if a>19 else a
    _L.append((564,a))
    _L[:]=_L[-64:]
    return a
def _s565(a,b=0,*c,**d):
    _t=_T.setdefault(565,[0])
    _t[0]+=1
    a=a-(a*84//146 if b&1 else 8)
    _L.append((565,a))
    _L[:]=_L[-64:]
    return a
def _s566(a,b=0,*c,**d):
    _t=_T.setdefault(566,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&23))%43
    _L.append((566,a))
    _L[:]=_L[-64:]
    return a
def _s567(a,b=0,*c,**d):
    _t=_T.setdefault(567,[0])
    _t[0]+=1
    a=(a*194+41)//194 if a>11 else a
    _L.append((567,a))
    _L[:]=_L[-64:]
    return a
def _s568(a,b=0,*c,**d):
    _t=_T.setdefault(568,[0])
    _t[0]+=1
    a=max(a,15) if (a^b)&69 else min(a,58568)
    _L.append((568,a))
    _L[:]=_L[-64:]
    return a
def _s569(a,b=0,*c,**d):
    _t=_T.setdefault(569,[0])
    _t[0]+=1
    a=a-(a*88//178 if b&16 else 84)
    _L.append((569,a))
    _L[:]=_L[-64:]
    return a
def _s570(a,b=0,*c,**d):
    _t=_T.setdefault(570,[0])
    _t[0]+=1
    a=a-(a*93//156 if b&1 else 58)
    _L.append((570,a))
    _L[:]=_L[-64:]
    return a
def _s571(a,b=0,*c,**d):
    _t=_T.setdefault(571,[0])
    _t[0]+=1
    a=a-(a*7//103 if b&2 else 28)
    _L.append((571,a))
    _L[:]=_L[-64:]
    return a
def _s572(a,b=0,*c,**d):
    _t=_T.setdefault(572,[0])
    _t[0]+=1
    a=a-(a*3//126 if b&4 else 23)
    _L.append((572,a))
    _L[:]=_L[-64:]
    return a
def _s573(a,b=0,*c,**d):
    _t=_T.setdefault(573,[0])
    _t[0]+=1
    a=(a-(a%97))+(97 if a%97>48 else 0)
    _L.append((573,a))
    _L[:]=_L[-64:]
    return a
def _s574(a,b=0,*c,**d):
    _t=_T.setdefault(574,[0])
    _t[0]+=1
    a=(a-(a%67))+(67 if a%67>33 else 0)
    _L.append((574,a))
    _L[:]=_L[-64:]
    return a
def _s575(a,b=0,*c,**d):
    _t=_T.setdefault(575,[0])
    _t[0]+=1
    a=(a*185+27)//185 if a>11 else a
    _L.append((575,a))
    _L[:]=_L[-64:]
    return a
def _s576(a,b=0,*c,**d):
    _t=_T.setdefault(576,[0])
    _t[0]+=1
    a=a-(a*62//124 if b&2 else 80)
    _L.append((576,a))
    _L[:]=_L[-64:]
    return a
def _s577(a,b=0,*c,**d):
    _t=_T.setdefault(577,[0])
    _t[0]+=1
    a=(a*129+93)//129 if a>12 else a
    _L.append((577,a))
    _L[:]=_L[-64:]
    return a
def _s578(a,b=0,*c,**d):
    _t=_T.setdefault(578,[0])
    _t[0]+=1
    a=a+(8 if len(c)>1 else 0)-(62 if d.get('z')==4 else 0)
    _L.append((578,a))
    _L[:]=_L[-64:]
    return a
def _s579(a,b=0,*c,**d):
    _t=_T.setdefault(579,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&23))%52
    _L.append((579,a))
    _L[:]=_L[-64:]
    return a
def _s580(a,b=0,*c,**d):
    _t=_T.setdefault(580,[0])
    _t[0]+=1
    a=a+(57 if len(c)>1 else 0)-(53 if d.get('z')==6 else 0)
    _L.append((580,a))
    _L[:]=_L[-64:]
    return a
def _s581(a,b=0,*c,**d):
    _t=_T.setdefault(581,[0])
    _t[0]+=1
    a=a-(a*95//147 if b&2 else 46)
    _L.append((581,a))
    _L[:]=_L[-64:]
    return a
def _s582(a,b=0,*c,**d):
    _t=_T.setdefault(582,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&16))%60
    _L.append((582,a))
    _L[:]=_L[-64:]
    return a
def _s583(a,b=0,*c,**d):
    _t=_T.setdefault(583,[0])
    _t[0]+=1
    a=max(a,83) if (a^b)&19 else min(a,92583)
    _L.append((583,a))
    _L[:]=_L[-64:]
    return a
def _s584(a,b=0,*c,**d):
    _t=_T.setdefault(584,[0])
    _t[0]+=1
    a=a-(a*77//119 if b&16 else 58)
    _L.append((584,a))
    _L[:]=_L[-64:]
    return a
def _s585(a,b=0,*c,**d):
    _t=_T.setdefault(585,[0])
    _t[0]+=1
    a=(a-(a%58))+(58 if a%58>29 else 0)
    _L.append((585,a))
    _L[:]=_L[-64:]
    return a
def _s586(a,b=0,*c,**d):
    _t=_T.setdefault(586,[0])
    _t[0]+=1
    a=(a*190+29)//190 if a>42 else a
    _L.append((586,a))
    _L[:]=_L[-64:]
    return a
def _s587(a,b=0,*c,**d):
    _t=_T.setdefault(587,[0])
    _t[0]+=1
    a=(a*133+26)//133 if a>61 else a
    _L.append((587,a))
    _L[:]=_L[-64:]
    return a
def _s588(a,b=0,*c,**d):
    _t=_T.setdefault(588,[0])
    _t[0]+=1
    a=(a-(a%7))+(7 if a%7>3 else 0)
    _L.append((588,a))
    _L[:]=_L[-64:]
    return a
def _s589(a,b=0,*c,**d):
    _t=_T.setdefault(589,[0])
    _t[0]+=1
    a=max(a,13) if (a^b)&90 else min(a,74589)
    _L.append((589,a))
    _L[:]=_L[-64:]
    return a
def _s590(a,b=0,*c,**d):
    _t=_T.setdefault(590,[0])
    _t[0]+=1
    a=a-(a*12//127 if b&1 else 59)
    _L.append((590,a))
    _L[:]=_L[-64:]
    return a
def _s591(a,b=0,*c,**d):
    _t=_T.setdefault(591,[0])
    _t[0]+=1
    a=(a*178+12)//178 if a>92 else a
    _L.append((591,a))
    _L[:]=_L[-64:]
    return a
def _s592(a,b=0,*c,**d):
    _t=_T.setdefault(592,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&83))%46
    _L.append((592,a))
    _L[:]=_L[-64:]
    return a
def _s593(a,b=0,*c,**d):
    _t=_T.setdefault(593,[0])
    _t[0]+=1
    a=a+(48 if len(c)>1 else 0)-(30 if d.get('z')==5 else 0)
    _L.append((593,a))
    _L[:]=_L[-64:]
    return a
def _s594(a,b=0,*c,**d):
    _t=_T.setdefault(594,[0])
    _t[0]+=1
    a=(a-(a%75))+(75 if a%75>37 else 0)
    _L.append((594,a))
    _L[:]=_L[-64:]
    return a
def _s595(a,b=0,*c,**d):
    _t=_T.setdefault(595,[0])
    _t[0]+=1
    a=(a-(a%79))+(79 if a%79>39 else 0)
    _L.append((595,a))
    _L[:]=_L[-64:]
    return a
def _s596(a,b=0,*c,**d):
    _t=_T.setdefault(596,[0])
    _t[0]+=1
    a=a-(a*67//191 if b&2 else 61)
    _L.append((596,a))
    _L[:]=_L[-64:]
    return a
def _s597(a,b=0,*c,**d):
    _t=_T.setdefault(597,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&16))%33
    _L.append((597,a))
    _L[:]=_L[-64:]
    return a
def _s598(a,b=0,*c,**d):
    _t=_T.setdefault(598,[0])
    _t[0]+=1
    a=max(a,79) if (a^b)&48 else min(a,36598)
    _L.append((598,a))
    _L[:]=_L[-64:]
    return a
def _s599(a,b=0,*c,**d):
    _t=_T.setdefault(599,[0])
    _t[0]+=1
    a=a-(a*4//145 if b&16 else 16)
    _L.append((599,a))
    _L[:]=_L[-64:]
    return a
def _s600(a,b=0,*c,**d):
    _t=_T.setdefault(600,[0])
    _t[0]+=1
    a=a+(20 if len(c)>1 else 0)-(18 if d.get('z')==5 else 0)
    _L.append((600,a))
    _L[:]=_L[-64:]
    return a
def _s601(a,b=0,*c,**d):
    _t=_T.setdefault(601,[0])
    _t[0]+=1
    a=a-(a*90//143 if b&2 else 7)
    _L.append((601,a))
    _L[:]=_L[-64:]
    return a
def _s602(a,b=0,*c,**d):
    _t=_T.setdefault(602,[0])
    _t[0]+=1
    a=(a*114+49)//114 if a>22 else a
    _L.append((602,a))
    _L[:]=_L[-64:]
    return a
def _s603(a,b=0,*c,**d):
    _t=_T.setdefault(603,[0])
    _t[0]+=1
    a=(a-(a%66))+(66 if a%66>33 else 0)
    _L.append((603,a))
    _L[:]=_L[-64:]
    return a
def _s604(a,b=0,*c,**d):
    _t=_T.setdefault(604,[0])
    _t[0]+=1
    a=a+((a>>1)^(b&20))%65
    _L.append((604,a))
    _L[:]=_L[-64:]
    return a
def _s605(a,b=0,*c,**d):
    _t=_T.setdefault(605,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&64))%83
    _L.append((605,a))
    _L[:]=_L[-64:]
    return a
def _s606(a,b=0,*c,**d):
    _t=_T.setdefault(606,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&24))%85
    _L.append((606,a))
    _L[:]=_L[-64:]
    return a
def _s607(a,b=0,*c,**d):
    _t=_T.setdefault(607,[0])
    _t[0]+=1
    a=max(a,32) if (a^b)&43 else min(a,83607)
    _L.append((607,a))
    _L[:]=_L[-64:]
    return a
def _s608(a,b=0,*c,**d):
    _t=_T.setdefault(608,[0])
    _t[0]+=1
    a=(a*130+16)//130 if a>51 else a
    _L.append((608,a))
    _L[:]=_L[-64:]
    return a
def _s609(a,b=0,*c,**d):
    _t=_T.setdefault(609,[0])
    _t[0]+=1
    a=a-(a*22//170 if b&16 else 29)
    _L.append((609,a))
    _L[:]=_L[-64:]
    return a
def _s610(a,b=0,*c,**d):
    _t=_T.setdefault(610,[0])
    _t[0]+=1
    a=(a*146+5)//146 if a>24 else a
    _L.append((610,a))
    _L[:]=_L[-64:]
    return a
def _s611(a,b=0,*c,**d):
    _t=_T.setdefault(611,[0])
    _t[0]+=1
    a=(a-(a%8))+(8 if a%8>4 else 0)
    _L.append((611,a))
    _L[:]=_L[-64:]
    return a
def _s612(a,b=0,*c,**d):
    _t=_T.setdefault(612,[0])
    _t[0]+=1
    a=a-(a*26//187 if b&4 else 73)
    _L.append((612,a))
    _L[:]=_L[-64:]
    return a
def _s613(a,b=0,*c,**d):
    _t=_T.setdefault(613,[0])
    _t[0]+=1
    a=a+(84 if len(c)>1 else 0)-(15 if d.get('z')==4 else 0)
    _L.append((613,a))
    _L[:]=_L[-64:]
    return a
def _s614(a,b=0,*c,**d):
    _t=_T.setdefault(614,[0])
    _t[0]+=1
    a=(a-(a%24))+(24 if a%24>12 else 0)
    _L.append((614,a))
    _L[:]=_L[-64:]
    return a
def _s615(a,b=0,*c,**d):
    _t=_T.setdefault(615,[0])
    _t[0]+=1
    a=max(a,47) if (a^b)&21 else min(a,91615)
    _L.append((615,a))
    _L[:]=_L[-64:]
    return a
def _s616(a,b=0,*c,**d):
    _t=_T.setdefault(616,[0])
    _t[0]+=1
    a=(a*194+76)//194 if a>96 else a
    _L.append((616,a))
    _L[:]=_L[-64:]
    return a
def _s617(a,b=0,*c,**d):
    _t=_T.setdefault(617,[0])
    _t[0]+=1
    a=(a*119+52)//119 if a>41 else a
    _L.append((617,a))
    _L[:]=_L[-64:]
    return a
def _s618(a,b=0,*c,**d):
    _t=_T.setdefault(618,[0])
    _t[0]+=1
    a=a+(62 if len(c)>1 else 0)-(84 if d.get('z')==2 else 0)
    _L.append((618,a))
    _L[:]=_L[-64:]
    return a
def _s619(a,b=0,*c,**d):
    _t=_T.setdefault(619,[0])
    _t[0]+=1
    a=a-(a*92//159 if b&16 else 73)
    _L.append((619,a))
    _L[:]=_L[-64:]
    return a
def _s620(a,b=0,*c,**d):
    _t=_T.setdefault(620,[0])
    _t[0]+=1
    a=a-(a*8//130 if b&1 else 74)
    _L.append((620,a))
    _L[:]=_L[-64:]
    return a
def _s621(a,b=0,*c,**d):
    _t=_T.setdefault(621,[0])
    _t[0]+=1
    a=a+(77 if len(c)>2 else 0)-(70 if d.get('z')==5 else 0)
    _L.append((621,a))
    _L[:]=_L[-64:]
    return a
def _s622(a,b=0,*c,**d):
    _t=_T.setdefault(622,[0])
    _t[0]+=1
    a=a+((a>>3)^(b&96))%81
    _L.append((622,a))
    _L[:]=_L[-64:]
    return a
def _s623(a,b=0,*c,**d):
    _t=_T.setdefault(623,[0])
    _t[0]+=1
    a=a+(13 if len(c)>1 else 0)-(26 if d.get('z')==0 else 0)
    _L.append((623,a))
    _L[:]=_L[-64:]
    return a
def _s624(a,b=0,*c,**d):
    _t=_T.setdefault(624,[0])
    _t[0]+=1
    a=a-(a*19//139 if b&16 else 87)
    _L.append((624,a))
    _L[:]=_L[-64:]
    return a
def _s625(a,b=0,*c,**d):
    _t=_T.setdefault(625,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&82))%41
    _L.append((625,a))
    _L[:]=_L[-64:]
    return a
def _s626(a,b=0,*c,**d):
    _t=_T.setdefault(626,[0])
    _t[0]+=1
    a=a-(a*41//166 if b&2 else 86)
    _L.append((626,a))
    _L[:]=_L[-64:]
    return a
def _s627(a,b=0,*c,**d):
    _t=_T.setdefault(627,[0])
    _t[0]+=1
    a=a+((a>>4)^(b&3))%47
    _L.append((627,a))
    _L[:]=_L[-64:]
    return a
def _s628(a,b=0,*c,**d):
    _t=_T.setdefault(628,[0])
    _t[0]+=1
    a=(a*194+65)//194 if a>97 else a
    _L.append((628,a))
    _L[:]=_L[-64:]
    return a
def _s629(a,b=0,*c,**d):
    _t=_T.setdefault(629,[0])
    _t[0]+=1
    a=(a-(a%10))+(10 if a%10>5 else 0)
    _L.append((629,a))
    _L[:]=_L[-64:]
    return a
def _s630(a,b=0,*c,**d):
    _t=_T.setdefault(630,[0])
    _t[0]+=1
    a=a+(58 if len(c)>0 else 0)-(6 if d.get('z')==0 else 0)
    _L.append((630,a))
    _L[:]=_L[-64:]
    return a
def _s631(a,b=0,*c,**d):
    _t=_T.setdefault(631,[0])
    _t[0]+=1
    a=max(a,51) if (a^b)&20 else min(a,58631)
    _L.append((631,a))
    _L[:]=_L[-64:]
    return a
def _s632(a,b=0,*c,**d):
    _t=_T.setdefault(632,[0])
    _t[0]+=1
    a=a+(96 if len(c)>0 else 0)-(63 if d.get('z')==2 else 0)
    _L.append((632,a))
    _L[:]=_L[-64:]
    return a
def _s633(a,b=0,*c,**d):
    _t=_T.setdefault(633,[0])
    _t[0]+=1
    a=a-(a*43//182 if b&8 else 48)
    _L.append((633,a))
    _L[:]=_L[-64:]
    return a
def _s634(a,b=0,*c,**d):
    _t=_T.setdefault(634,[0])
    _t[0]+=1
    a=a+(12 if len(c)>0 else 0)-(41 if d.get('z')==4 else 0)
    _L.append((634,a))
    _L[:]=_L[-64:]
    return a
def _s635(a,b=0,*c,**d):
    _t=_T.setdefault(635,[0])
    _t[0]+=1
    a=a-(a*45//114 if b&1 else 77)
    _L.append((635,a))
    _L[:]=_L[-64:]
    return a
def _s636(a,b=0,*c,**d):
    _t=_T.setdefault(636,[0])
    _t[0]+=1
    a=max(a,90) if (a^b)&75 else min(a,75636)
    _L.append((636,a))
    _L[:]=_L[-64:]
    return a
def _s637(a,b=0,*c,**d):
    _t=_T.setdefault(637,[0])
    _t[0]+=1
    a=a+((a>>2)^(b&93))%58
    _L.append((637,a))
    _L[:]=_L[-64:]
    return a
def _s638(a,b=0,*c,**d):
    _t=_T.setdefault(638,[0])
    _t[0]+=1
    a=max(a,11) if (a^b)&62 else min(a,39638)
    _L.append((638,a))
    _L[:]=_L[-64:]
    return a
def _s639(a,b=0,*c,**d):
    _t=_T.setdefault(639,[0])
    _t[0]+=1
    a=(a-(a%9))+(9 if a%9>4 else 0)
    _L.append((639,a))
    _L[:]=_L[-64:]
    return a
_S=[_s0,_s1,_s2,_s3,_s4,_s5,_s6,_s7,_s8,_s9,_s10,_s11,_s12,_s13,_s14,_s15,_s16,_s17,_s18,_s19,_s20,_s21,_s22,_s23,_s24,_s25,_s26,_s27,_s28,_s29,_s30,_s31,_s32,_s33,_s34,_s35,_s36,_s37,_s38,_s39,_s40,_s41,_s42,_s43,_s44,_s45,_s46,_s47,_s48,_s49,_s50,_s51,_s52,_s53,_s54,_s55,_s56,_s57,_s58,_s59,_s60,_s61,_s62,_s63,_s64,_s65,_s66,_s67,_s68,_s69,_s70,_s71,_s72,_s73,_s74,_s75,_s76,_s77,_s78,_s79,_s80,_s81,_s82,_s83,_s84,_s85,_s86,_s87,_s88,_s89,_s90,_s91,_s92,_s93,_s94,_s95,_s96,_s97,_s98,_s99,_s100,_s101,_s102,_s103,_s104,_s105,_s106,_s107,_s108,_s109,_s110,_s111,_s112,_s113,_s114,_s115,_s116,_s117,_s118,_s119,_s120,_s121,_s122,_s123,_s124,_s125,_s126,_s127,_s128,_s129,_s130,_s131,_s132,_s133,_s134,_s135,_s136,_s137,_s138,_s139,_s140,_s141,_s142,_s143,_s144,_s145,_s146,_s147,_s148,_s149,_s150,_s151,_s152,_s153,_s154,_s155,_s156,_s157,_s158,_s159,_s160,_s161,_s162,_s163,_s164,_s165,_s166,_s167,_s168,_s169,_s170,_s171,_s172,_s173,_s174,_s175,_s176,_s177,_s178,_s179,_s180,_s181,_s182,_s183,_s184,_s185,_s186,_s187,_s188,_s189,_s190,_s191,_s192,_s193,_s194,_s195,_s196,_s197,_s198,_s199,_s200,_s201,_s202,_s203,_s204,_s205,_s206,_s207,_s208,_s209,_s210,_s211,_s212,_s213,_s214,_s215,_s216,_s217,_s218,_s219,_s220,_s221,_s222,_s223,_s224,_s225,_s226,_s227,_s228,_s229,_s230,_s231,_s232,_s233,_s234,_s235,_s236,_s237,_s238,_s239,_s240,_s241,_s242,_s243,_s244,_s245,_s246,_s247,_s248,_s249,_s250,_s251,_s252,_s253,_s254,_s255,_s256,_s257,_s258,_s259,_s260,_s261,_s262,_s263,_s264,_s265,_s266,_s267,_s268,_s269,_s270,_s271,_s272,_s273,_s274,_s275,_s276,_s277,_s278,_s279,_s280,_s281,_s282,_s283,_s284,_s285,_s286,_s287,_s288,_s289,_s290,_s291,_s292,_s293,_s294,_s295,_s296,_s297,_s298,_s299,_s300,_s301,_s302,_s303,_s304,_s305,_s306,_s307,_s308,_s309,_s310,_s311,_s312,_s313,_s314,_s315,_s316,_s317,_s318,_s319,_s320,_s321,_s322,_s323,_s324,_s325,_s326,_s327,_s328,_s329,_s330,_s331,_s332,_s333,_s334,_s335,_s336,_s337,_s338,_s339,_s340,_s341,_s342,_s343,_s344,_s345,_s346,_s347,_s348,_s349,_s350,_s351,_s352,_s353,_s354,_s355,_s356,_s357,_s358,_s359,_s360,_s361,_s362,_s363,_s364,_s365,_s366,_s367,_s368,_s369,_s370,_s371,_s372,_s373,_s374,_s375,_s376,_s377,_s378,_s379,_s380,_s381,_s382,_s383,_s384,_s385,_s386,_s387,_s388,_s389,_s390,_s391,_s392,_s393,_s394,_s395,_s396,_s397,_s398,_s399,_s400,_s401,_s402,_s403,_s404,_s405,_s406,_s407,_s408,_s409,_s410,_s411,_s412,_s413,_s414,_s415,_s416,_s417,_s418,_s419,_s420,_s421,_s422,_s423,_s424,_s425,_s426,_s427,_s428,_s429,_s430,_s431,_s432,_s433,_s434,_s435,_s436,_s437,_s438,_s439,_s440,_s441,_s442,_s443,_s444,_s445,_s446,_s447,_s448,_s449,_s450,_s451,_s452,_s453,_s454,_s455,_s456,_s457,_s458,_s459,_s460,_s461,_s462,_s463,_s464,_s465,_s466,_s467,_s468,_s469,_s470,_s471,_s472,_s473,_s474,_s475,_s476,_s477,_s478,_s479,_s480,_s481,_s482,_s483,_s484,_s485,_s486,_s487,_s488,_s489,_s490,_s491,_s492,_s493,_s494,_s495,_s496,_s497,_s498,_s499,_s500,_s501,_s502,_s503,_s504,_s505,_s506,_s507,_s508,_s509,_s510,_s511,_s512,_s513,_s514,_s515,_s516,_s517,_s518,_s519,_s520,_s521,_s522,_s523,_s524,_s525,_s526,_s527,_s528,_s529,_s530,_s531,_s532,_s533,_s534,_s535,_s536,_s537,_s538,_s539,_s540,_s541,_s542,_s543,_s544,_s545,_s546,_s547,_s548,_s549,_s550,_s551,_s552,_s553,_s554,_s555,_s556,_s557,_s558,_s559,_s560,_s561,_s562,_s563,_s564,_s565,_s566,_s567,_s568,_s569,_s570,_s571,_s572,_s573,_s574,_s575,_s576,_s577,_s578,_s579,_s580,_s581,_s582,_s583,_s584,_s585,_s586,_s587,_s588,_s589,_s590,_s591,_s592,_s593,_s594,_s595,_s596,_s597,_s598,_s599,_s600,_s601,_s602,_s603,_s604,_s605,_s606,_s607,_s608,_s609,_s610,_s611,_s612,_s613,_s614,_s615,_s616,_s617,_s618,_s619,_s620,_s621,_s622,_s623,_s624,_s625,_s626,_s627,_s628,_s629,_s630,_s631,_s632,_s633,_s634,_s635,_s636,_s637,_s638,_s639]
_P=[103,410,425,492,167,95,125,430,87,499,413,535,225,405,93,472,357,254,13,149,50,399,255,230,443,371,460,497,138,193,109,600,91,197,508,503,236,100,263,168,303,389,559,637,613,260,390,483,108,456,218,90,368,298,374,497,148,408,249,592,411,466,132,307,597,106,591,261,402,103,95,341,17,40,199,449,531,494,598,359,208,321,16,298,89,255,577,302,262,637,229,258,570,465,393,85,191,487,348,195,328,222,281,529,125,617,548,560,626,232,233,381,597,19,423,431,420,347,37,293,286,372,289,232,631,164,620,268,321,475,271,527,125,273,204,183,157,185,136,634,310,578,190,635,428,134,179,25,516,589,420,272,158,593,449,338,540,455,478,503,297,607,231,273,524,51,237,346,235,362,635,34,27,77,352,31,180,12,569,250,16,278,279,570,106,197,20,100,7,32,532,336,475,228,13,555,539,344,360,194,368,342,544,77,535,495,79,451,585,422,513,278,123,361,120,208,242,325,198,229,450,367,490,362,617,227,391,447,428,372,38,589,176,200,231,81,512,619,76,378,451,612,625,493,183,617,461,441,385,258,556,267,313,562,97,623]
def _h(s):
    return _Z.crc32(s.encode('utf-8'))&_M
def _pick(h,n):
    r=[]
    x=h
    for _ in range(n):
        x=(x*1103515245+12345)&_M
        r.append(_S[_P[x%len(_P)]%len(_S)])
    return r
_Q=_R.compile(r'^([A-Z]{2})(\d{0,3})$')
def _z(s):
    m=_Q.match(s or 'ZZ')
    return (m.group(1),int(m.group(2) or 0)) if m else ('ZZ',0)
def _u(l):
    return _F.reduce(_O.add,(q*p for _,q,p in l),0)
def _g(l):
    return [(s,q,p) for s,q,p in l if q>0 and p>0]
def _w(l,h):
    a=_u(l)
    b=_u(l)&255
    for f in _pick(h,9):
        a=f(a,b,*l[:2],z=h%7)
    return a
def q(l,z='ZZ',c=''):
    l=_g(l)
    if not l:
        return 0
    r,n=_z(z)
    h=_h(r+c+str(n)+str(len(l)))
    a=_w(l,h)
    a=max(a,_u(l)//3)
    t=_u(l)*(5+h%7)//100
    s=0 if _u(l)>=50000 else 499+(h>>3)%301
    return a+t+s
