                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ISO C Compiler
                                      3 ; Version 4.6.0 #16555 (Mac OS X ppc)
                                      4 ;--------------------------------------------------------
                                      5 	.module bulkloop
                                      6 	
                                      7 	.optsdcc -mmcs51 --model-small
                                      8 ;--------------------------------------------------------
                                      9 ; Public variables in this module
                                     10 ;--------------------------------------------------------
                                     11 	.globl _handle_set_configuration
                                     12 	.globl _handle_get_configuration
                                     13 	.globl _handle_set_interface
                                     14 	.globl _handle_get_interface
                                     15 	.globl _handle_vendorcommand
                                     16 	.globl _handle_get_descriptor
                                     17 	.globl _main
                                     18 	.globl _handle_hispeed
                                     19 	.globl _handle_setupdata
                                     20 	.globl _ep_addr
                                     21 	.globl _delay
                                     22 	.globl _sio0_init
                                     23 	.globl _printf
                                     24 	.globl _EIPX6
                                     25 	.globl _EIPX5
                                     26 	.globl _EIPX4
                                     27 	.globl _PI2C
                                     28 	.globl _PUSB
                                     29 	.globl _EIEX6
                                     30 	.globl _EIEX5
                                     31 	.globl _EIEX4
                                     32 	.globl _EI2C
                                     33 	.globl _EUSB
                                     34 	.globl _SMOD1
                                     35 	.globl _ERESI
                                     36 	.globl _RESI
                                     37 	.globl _INT6
                                     38 	.globl _CY
                                     39 	.globl _AC
                                     40 	.globl _F0
                                     41 	.globl _RS1
                                     42 	.globl _RS0
                                     43 	.globl _OV
                                     44 	.globl _FL
                                     45 	.globl _P
                                     46 	.globl _TF2
                                     47 	.globl _EXF2
                                     48 	.globl _RCLK
                                     49 	.globl _TCLK
                                     50 	.globl _EXEN2
                                     51 	.globl _TR2
                                     52 	.globl _C_T2
                                     53 	.globl _CP_RL2
                                     54 	.globl _SM01
                                     55 	.globl _SM11
                                     56 	.globl _SM21
                                     57 	.globl _REN1
                                     58 	.globl _TB81
                                     59 	.globl _RB81
                                     60 	.globl _TI1
                                     61 	.globl _RI1
                                     62 	.globl _PS1
                                     63 	.globl _PT2
                                     64 	.globl _PS0
                                     65 	.globl _PT1
                                     66 	.globl _PX1
                                     67 	.globl _PT0
                                     68 	.globl _PX0
                                     69 	.globl _PD7
                                     70 	.globl _PD6
                                     71 	.globl _PD5
                                     72 	.globl _PD4
                                     73 	.globl _PD3
                                     74 	.globl _PD2
                                     75 	.globl _PD1
                                     76 	.globl _PD0
                                     77 	.globl _EA
                                     78 	.globl _ES1
                                     79 	.globl _ET2
                                     80 	.globl _ES0
                                     81 	.globl _ET1
                                     82 	.globl _EX1
                                     83 	.globl _ET0
                                     84 	.globl _EX0
                                     85 	.globl _PC7
                                     86 	.globl _PC6
                                     87 	.globl _PC5
                                     88 	.globl _PC4
                                     89 	.globl _PC3
                                     90 	.globl _PC2
                                     91 	.globl _PC1
                                     92 	.globl _PC0
                                     93 	.globl _SM0
                                     94 	.globl _SM1
                                     95 	.globl _SM2
                                     96 	.globl _REN
                                     97 	.globl _TB8
                                     98 	.globl _RB8
                                     99 	.globl _TI
                                    100 	.globl _RI
                                    101 	.globl _PB7
                                    102 	.globl _PB6
                                    103 	.globl _PB5
                                    104 	.globl _PB4
                                    105 	.globl _PB3
                                    106 	.globl _PB2
                                    107 	.globl _PB1
                                    108 	.globl _PB0
                                    109 	.globl _TF1
                                    110 	.globl _TR1
                                    111 	.globl _TF0
                                    112 	.globl _TR0
                                    113 	.globl _IE1
                                    114 	.globl _IT1
                                    115 	.globl _IE0
                                    116 	.globl _IT0
                                    117 	.globl _PA7
                                    118 	.globl _PA6
                                    119 	.globl _PA5
                                    120 	.globl _PA4
                                    121 	.globl _PA3
                                    122 	.globl _PA2
                                    123 	.globl _PA1
                                    124 	.globl _PA0
                                    125 	.globl _EIP
                                    126 	.globl _B
                                    127 	.globl _EIE
                                    128 	.globl _ACC
                                    129 	.globl _EICON
                                    130 	.globl _PSW
                                    131 	.globl _TH2
                                    132 	.globl _TL2
                                    133 	.globl _RCAP2H
                                    134 	.globl _RCAP2L
                                    135 	.globl _T2CON
                                    136 	.globl _SBUF1
                                    137 	.globl _SCON1
                                    138 	.globl _GPIFSGLDATLNOX
                                    139 	.globl _GPIFSGLDATLX
                                    140 	.globl _GPIFSGLDATH
                                    141 	.globl _GPIFTRIG
                                    142 	.globl _EP01STAT
                                    143 	.globl _IP
                                    144 	.globl _OEE
                                    145 	.globl _OED
                                    146 	.globl _OEC
                                    147 	.globl _OEB
                                    148 	.globl _OEA
                                    149 	.globl _IOE
                                    150 	.globl _IOD
                                    151 	.globl _AUTOPTRSETUP
                                    152 	.globl _EP68FIFOFLGS
                                    153 	.globl _EP24FIFOFLGS
                                    154 	.globl _EP2468STAT
                                    155 	.globl _IE
                                    156 	.globl _INT4CLR
                                    157 	.globl _INT2CLR
                                    158 	.globl _IOC
                                    159 	.globl _AUTOPTRL2
                                    160 	.globl _AUTOPTRH2
                                    161 	.globl _AUTOPTRL1
                                    162 	.globl _AUTOPTRH1
                                    163 	.globl _SBUF0
                                    164 	.globl _SCON0
                                    165 	.globl __XPAGE
                                    166 	.globl _EXIF
                                    167 	.globl _IOB
                                    168 	.globl _CKCON
                                    169 	.globl _TH1
                                    170 	.globl _TH0
                                    171 	.globl _TL1
                                    172 	.globl _TL0
                                    173 	.globl _TMOD
                                    174 	.globl _TCON
                                    175 	.globl _PCON
                                    176 	.globl _DPS
                                    177 	.globl _DPH1
                                    178 	.globl _DPL1
                                    179 	.globl _DPH
                                    180 	.globl _DPL
                                    181 	.globl _SP
                                    182 	.globl _IOA
                                    183 	.globl _sofct
                                    184 	.globl _D5OFF
                                    185 	.globl _D5ON
                                    186 	.globl _D4OFF
                                    187 	.globl _D4ON
                                    188 	.globl _D3OFF
                                    189 	.globl _D3ON
                                    190 	.globl _D2OFF
                                    191 	.globl _D2ON
                                    192 	.globl _GPCR2
                                    193 	.globl _ECC2B2
                                    194 	.globl _ECC2B1
                                    195 	.globl _ECC2B0
                                    196 	.globl _ECC1B2
                                    197 	.globl _ECC1B1
                                    198 	.globl _ECC1B0
                                    199 	.globl _ECCRESET
                                    200 	.globl _ECCCFG
                                    201 	.globl _EP8FIFOBUF
                                    202 	.globl _EP6FIFOBUF
                                    203 	.globl _EP4FIFOBUF
                                    204 	.globl _EP2FIFOBUF
                                    205 	.globl _EP1INBUF
                                    206 	.globl _EP1OUTBUF
                                    207 	.globl _EP0BUF
                                    208 	.globl _UDMACRCQUAL
                                    209 	.globl _UDMACRCL
                                    210 	.globl _UDMACRCH
                                    211 	.globl _GPIFHOLDAMOUNT
                                    212 	.globl _FLOWSTBHPERIOD
                                    213 	.globl _FLOWSTBEDGE
                                    214 	.globl _FLOWSTB
                                    215 	.globl _FLOWHOLDOFF
                                    216 	.globl _FLOWEQ1CTL
                                    217 	.globl _FLOWEQ0CTL
                                    218 	.globl _FLOWLOGIC
                                    219 	.globl _FLOWSTATE
                                    220 	.globl _GPIFABORT
                                    221 	.globl _GPIFREADYSTAT
                                    222 	.globl _GPIFREADYCFG
                                    223 	.globl _XGPIFSGLDATLNOX
                                    224 	.globl _XGPIFSGLDATLX
                                    225 	.globl _XGPIFSGLDATH
                                    226 	.globl _EP8GPIFTRIG
                                    227 	.globl _EP8GPIFPFSTOP
                                    228 	.globl _EP8GPIFFLGSEL
                                    229 	.globl _EP6GPIFTRIG
                                    230 	.globl _EP6GPIFPFSTOP
                                    231 	.globl _EP6GPIFFLGSEL
                                    232 	.globl _EP4GPIFTRIG
                                    233 	.globl _EP4GPIFPFSTOP
                                    234 	.globl _EP4GPIFFLGSEL
                                    235 	.globl _EP2GPIFTRIG
                                    236 	.globl _EP2GPIFPFSTOP
                                    237 	.globl _EP2GPIFFLGSEL
                                    238 	.globl _GPIFTCB0
                                    239 	.globl _GPIFTCB1
                                    240 	.globl _GPIFTCB2
                                    241 	.globl _GPIFTCB3
                                    242 	.globl _GPIFADRL
                                    243 	.globl _GPIFADRH
                                    244 	.globl _GPIFCTLCFG
                                    245 	.globl _GPIFIDLECTL
                                    246 	.globl _GPIFIDLECS
                                    247 	.globl _GPIFWFSELECT
                                    248 	.globl _SETUPDAT
                                    249 	.globl _SUDPTRCTL
                                    250 	.globl _SUDPTRL
                                    251 	.globl _SUDPTRH
                                    252 	.globl _EP8FIFOBCL
                                    253 	.globl _EP8FIFOBCH
                                    254 	.globl _EP6FIFOBCL
                                    255 	.globl _EP6FIFOBCH
                                    256 	.globl _EP4FIFOBCL
                                    257 	.globl _EP4FIFOBCH
                                    258 	.globl _EP2FIFOBCL
                                    259 	.globl _EP2FIFOBCH
                                    260 	.globl _EP8FIFOFLGS
                                    261 	.globl _EP6FIFOFLGS
                                    262 	.globl _EP4FIFOFLGS
                                    263 	.globl _EP2FIFOFLGS
                                    264 	.globl _EP8CS
                                    265 	.globl _EP6CS
                                    266 	.globl _EP4CS
                                    267 	.globl _EP2CS
                                    268 	.globl _EP1INCS
                                    269 	.globl _EP1OUTCS
                                    270 	.globl _EP0CS
                                    271 	.globl _EP8BCL
                                    272 	.globl _EP8BCH
                                    273 	.globl _EP6BCL
                                    274 	.globl _EP6BCH
                                    275 	.globl _EP4BCL
                                    276 	.globl _EP4BCH
                                    277 	.globl _EP2BCL
                                    278 	.globl _EP2BCH
                                    279 	.globl _EP1INBC
                                    280 	.globl _EP1OUTBC
                                    281 	.globl _EP0BCL
                                    282 	.globl _EP0BCH
                                    283 	.globl _FNADDR
                                    284 	.globl _MICROFRAME
                                    285 	.globl _USBFRAMEL
                                    286 	.globl _USBFRAMEH
                                    287 	.globl _TOGCTL
                                    288 	.globl _WAKEUPCS
                                    289 	.globl _SUSPEND
                                    290 	.globl _USBCS
                                    291 	.globl _XAUTODAT2
                                    292 	.globl _XAUTODAT1
                                    293 	.globl _I2CTL
                                    294 	.globl _I2DAT
                                    295 	.globl _I2CS
                                    296 	.globl _PORTECFG
                                    297 	.globl _PORTCCFG
                                    298 	.globl _PORTACFG
                                    299 	.globl _INTSETUP
                                    300 	.globl _INT4IVEC
                                    301 	.globl _INT2IVEC
                                    302 	.globl _CLRERRCNT
                                    303 	.globl _ERRCNTLIM
                                    304 	.globl _USBERRIRQ
                                    305 	.globl _USBERRIE
                                    306 	.globl _GPIFIRQ
                                    307 	.globl _GPIFIE
                                    308 	.globl _EPIRQ
                                    309 	.globl _EPIE
                                    310 	.globl _USBIRQ
                                    311 	.globl _USBIE
                                    312 	.globl _NAKIRQ
                                    313 	.globl _NAKIE
                                    314 	.globl _IBNIRQ
                                    315 	.globl _IBNIE
                                    316 	.globl _EP8FIFOIRQ
                                    317 	.globl _EP8FIFOIE
                                    318 	.globl _EP6FIFOIRQ
                                    319 	.globl _EP6FIFOIE
                                    320 	.globl _EP4FIFOIRQ
                                    321 	.globl _EP4FIFOIE
                                    322 	.globl _EP2FIFOIRQ
                                    323 	.globl _EP2FIFOIE
                                    324 	.globl _OUTPKTEND
                                    325 	.globl _INPKTEND
                                    326 	.globl _EP8ISOINPKTS
                                    327 	.globl _EP6ISOINPKTS
                                    328 	.globl _EP4ISOINPKTS
                                    329 	.globl _EP2ISOINPKTS
                                    330 	.globl _EP8FIFOPFL
                                    331 	.globl _EP8FIFOPFH
                                    332 	.globl _EP6FIFOPFL
                                    333 	.globl _EP6FIFOPFH
                                    334 	.globl _EP4FIFOPFL
                                    335 	.globl _EP4FIFOPFH
                                    336 	.globl _EP2FIFOPFL
                                    337 	.globl _EP2FIFOPFH
                                    338 	.globl _EP8AUTOINLENL
                                    339 	.globl _EP8AUTOINLENH
                                    340 	.globl _EP6AUTOINLENL
                                    341 	.globl _EP6AUTOINLENH
                                    342 	.globl _EP4AUTOINLENL
                                    343 	.globl _EP4AUTOINLENH
                                    344 	.globl _EP2AUTOINLENL
                                    345 	.globl _EP2AUTOINLENH
                                    346 	.globl _EP8FIFOCFG
                                    347 	.globl _EP6FIFOCFG
                                    348 	.globl _EP4FIFOCFG
                                    349 	.globl _EP2FIFOCFG
                                    350 	.globl _EP8CFG
                                    351 	.globl _EP6CFG
                                    352 	.globl _EP4CFG
                                    353 	.globl _EP2CFG
                                    354 	.globl _EP1INCFG
                                    355 	.globl _EP1OUTCFG
                                    356 	.globl _REVCTL
                                    357 	.globl _REVID
                                    358 	.globl _FIFOPINPOLAR
                                    359 	.globl _UART230
                                    360 	.globl _BPADDRL
                                    361 	.globl _BPADDRH
                                    362 	.globl _BREAKPT
                                    363 	.globl _FIFORESET
                                    364 	.globl _PINFLAGSCD
                                    365 	.globl _PINFLAGSAB
                                    366 	.globl _IFCONFIG
                                    367 	.globl _CPUCS
                                    368 	.globl _UNIQID5
                                    369 	.globl _UNIQID4
                                    370 	.globl _UNIQID3
                                    371 	.globl _UNIQID2
                                    372 	.globl _UNIQID1
                                    373 	.globl _UNIQID0
                                    374 	.globl _RES_WAVEDATA_END
                                    375 	.globl _GPIF_WAVE_DATA
                                    376 	.globl _on5
                                    377 	.globl _on
                                    378 	.globl _got_sud
                                    379 	.globl _gotbuf
                                    380 	.globl _handle_set_interface_PARM_2
                                    381 	.globl _handle_get_interface_PARM_2
                                    382 	.globl _lcount
                                    383 	.globl _icount
                                    384 	.globl _bytes
                                    385 	.globl _sudav_isr
                                    386 	.globl _sof_isr
                                    387 	.globl _usbreset_isr
                                    388 	.globl _hispeed_isr
                                    389 ;--------------------------------------------------------
                                    390 ; special function registers
                                    391 ;--------------------------------------------------------
                                    392 	.area RSEG    (ABS,DATA)
      000000                        393 	.org 0x0000
                           000080   394 _IOA	=	0x0080
                           000081   395 _SP	=	0x0081
                           000082   396 _DPL	=	0x0082
                           000083   397 _DPH	=	0x0083
                           000084   398 _DPL1	=	0x0084
                           000085   399 _DPH1	=	0x0085
                           000086   400 _DPS	=	0x0086
                           000087   401 _PCON	=	0x0087
                           000088   402 _TCON	=	0x0088
                           000089   403 _TMOD	=	0x0089
                           00008A   404 _TL0	=	0x008a
                           00008B   405 _TL1	=	0x008b
                           00008C   406 _TH0	=	0x008c
                           00008D   407 _TH1	=	0x008d
                           00008E   408 _CKCON	=	0x008e
                           000090   409 _IOB	=	0x0090
                           000091   410 _EXIF	=	0x0091
                           000092   411 __XPAGE	=	0x0092
                           000098   412 _SCON0	=	0x0098
                           000099   413 _SBUF0	=	0x0099
                           00009A   414 _AUTOPTRH1	=	0x009a
                           00009B   415 _AUTOPTRL1	=	0x009b
                           00009D   416 _AUTOPTRH2	=	0x009d
                           00009E   417 _AUTOPTRL2	=	0x009e
                           0000A0   418 _IOC	=	0x00a0
                           0000A1   419 _INT2CLR	=	0x00a1
                           0000A2   420 _INT4CLR	=	0x00a2
                           0000A8   421 _IE	=	0x00a8
                           0000AA   422 _EP2468STAT	=	0x00aa
                           0000AB   423 _EP24FIFOFLGS	=	0x00ab
                           0000AC   424 _EP68FIFOFLGS	=	0x00ac
                           0000AF   425 _AUTOPTRSETUP	=	0x00af
                           0000B0   426 _IOD	=	0x00b0
                           0000B1   427 _IOE	=	0x00b1
                           0000B2   428 _OEA	=	0x00b2
                           0000B3   429 _OEB	=	0x00b3
                           0000B4   430 _OEC	=	0x00b4
                           0000B5   431 _OED	=	0x00b5
                           0000B6   432 _OEE	=	0x00b6
                           0000B8   433 _IP	=	0x00b8
                           0000BA   434 _EP01STAT	=	0x00ba
                           0000BB   435 _GPIFTRIG	=	0x00bb
                           0000BD   436 _GPIFSGLDATH	=	0x00bd
                           0000BE   437 _GPIFSGLDATLX	=	0x00be
                           0000BF   438 _GPIFSGLDATLNOX	=	0x00bf
                           0000C0   439 _SCON1	=	0x00c0
                           0000C1   440 _SBUF1	=	0x00c1
                           0000C8   441 _T2CON	=	0x00c8
                           0000CA   442 _RCAP2L	=	0x00ca
                           0000CB   443 _RCAP2H	=	0x00cb
                           0000CC   444 _TL2	=	0x00cc
                           0000CD   445 _TH2	=	0x00cd
                           0000D0   446 _PSW	=	0x00d0
                           0000D8   447 _EICON	=	0x00d8
                           0000E0   448 _ACC	=	0x00e0
                           0000E8   449 _EIE	=	0x00e8
                           0000F0   450 _B	=	0x00f0
                           0000F8   451 _EIP	=	0x00f8
                                    452 ;--------------------------------------------------------
                                    453 ; special function bits
                                    454 ;--------------------------------------------------------
                                    455 	.area RSEG    (ABS,DATA)
      000000                        456 	.org 0x0000
                           000080   457 _PA0	=	0x0080
                           000081   458 _PA1	=	0x0081
                           000082   459 _PA2	=	0x0082
                           000083   460 _PA3	=	0x0083
                           000084   461 _PA4	=	0x0084
                           000085   462 _PA5	=	0x0085
                           000086   463 _PA6	=	0x0086
                           000087   464 _PA7	=	0x0087
                           000088   465 _IT0	=	0x0088
                           000089   466 _IE0	=	0x0089
                           00008A   467 _IT1	=	0x008a
                           00008B   468 _IE1	=	0x008b
                           00008C   469 _TR0	=	0x008c
                           00008D   470 _TF0	=	0x008d
                           00008E   471 _TR1	=	0x008e
                           00008F   472 _TF1	=	0x008f
                           000090   473 _PB0	=	0x0090
                           000091   474 _PB1	=	0x0091
                           000092   475 _PB2	=	0x0092
                           000093   476 _PB3	=	0x0093
                           000094   477 _PB4	=	0x0094
                           000095   478 _PB5	=	0x0095
                           000096   479 _PB6	=	0x0096
                           000097   480 _PB7	=	0x0097
                           000098   481 _RI	=	0x0098
                           000099   482 _TI	=	0x0099
                           00009A   483 _RB8	=	0x009a
                           00009B   484 _TB8	=	0x009b
                           00009C   485 _REN	=	0x009c
                           00009D   486 _SM2	=	0x009d
                           00009E   487 _SM1	=	0x009e
                           00009F   488 _SM0	=	0x009f
                           0000A0   489 _PC0	=	0x00a0
                           0000A1   490 _PC1	=	0x00a1
                           0000A2   491 _PC2	=	0x00a2
                           0000A3   492 _PC3	=	0x00a3
                           0000A4   493 _PC4	=	0x00a4
                           0000A5   494 _PC5	=	0x00a5
                           0000A6   495 _PC6	=	0x00a6
                           0000A7   496 _PC7	=	0x00a7
                           0000A8   497 _EX0	=	0x00a8
                           0000A9   498 _ET0	=	0x00a9
                           0000AA   499 _EX1	=	0x00aa
                           0000AB   500 _ET1	=	0x00ab
                           0000AC   501 _ES0	=	0x00ac
                           0000AD   502 _ET2	=	0x00ad
                           0000AE   503 _ES1	=	0x00ae
                           0000AF   504 _EA	=	0x00af
                           0000B0   505 _PD0	=	0x00b0
                           0000B1   506 _PD1	=	0x00b1
                           0000B2   507 _PD2	=	0x00b2
                           0000B3   508 _PD3	=	0x00b3
                           0000B4   509 _PD4	=	0x00b4
                           0000B5   510 _PD5	=	0x00b5
                           0000B6   511 _PD6	=	0x00b6
                           0000B7   512 _PD7	=	0x00b7
                           0000B8   513 _PX0	=	0x00b8
                           0000B9   514 _PT0	=	0x00b9
                           0000BA   515 _PX1	=	0x00ba
                           0000BB   516 _PT1	=	0x00bb
                           0000BC   517 _PS0	=	0x00bc
                           0000BD   518 _PT2	=	0x00bd
                           0000BE   519 _PS1	=	0x00be
                           0000C0   520 _RI1	=	0x00c0
                           0000C1   521 _TI1	=	0x00c1
                           0000C2   522 _RB81	=	0x00c2
                           0000C3   523 _TB81	=	0x00c3
                           0000C4   524 _REN1	=	0x00c4
                           0000C5   525 _SM21	=	0x00c5
                           0000C6   526 _SM11	=	0x00c6
                           0000C7   527 _SM01	=	0x00c7
                           0000C8   528 _CP_RL2	=	0x00c8
                           0000C9   529 _C_T2	=	0x00c9
                           0000CA   530 _TR2	=	0x00ca
                           0000CB   531 _EXEN2	=	0x00cb
                           0000CC   532 _TCLK	=	0x00cc
                           0000CD   533 _RCLK	=	0x00cd
                           0000CE   534 _EXF2	=	0x00ce
                           0000CF   535 _TF2	=	0x00cf
                           0000D0   536 _P	=	0x00d0
                           0000D1   537 _FL	=	0x00d1
                           0000D2   538 _OV	=	0x00d2
                           0000D3   539 _RS0	=	0x00d3
                           0000D4   540 _RS1	=	0x00d4
                           0000D5   541 _F0	=	0x00d5
                           0000D6   542 _AC	=	0x00d6
                           0000D7   543 _CY	=	0x00d7
                           0000DB   544 _INT6	=	0x00db
                           0000DC   545 _RESI	=	0x00dc
                           0000DD   546 _ERESI	=	0x00dd
                           0000DF   547 _SMOD1	=	0x00df
                           0000E8   548 _EUSB	=	0x00e8
                           0000E9   549 _EI2C	=	0x00e9
                           0000EA   550 _EIEX4	=	0x00ea
                           0000EB   551 _EIEX5	=	0x00eb
                           0000EC   552 _EIEX6	=	0x00ec
                           0000F8   553 _PUSB	=	0x00f8
                           0000F9   554 _PI2C	=	0x00f9
                           0000FA   555 _EIPX4	=	0x00fa
                           0000FB   556 _EIPX5	=	0x00fb
                           0000FC   557 _EIPX6	=	0x00fc
                                    558 ;--------------------------------------------------------
                                    559 ; overlayable register banks
                                    560 ;--------------------------------------------------------
                                    561 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                        562 	.ds 8
                                    563 	.area REG_BANK_1	(REL,OVR,DATA)
      000008                        564 	.ds 8
                                    565 ;--------------------------------------------------------
                                    566 ; overlayable bit register bank
                                    567 ;--------------------------------------------------------
                                    568 	.area BIT_BANK	(REL,OVR,DATA)
      000021                        569 bits:
      000021                        570 	.ds 1
                           008000   571 	b0 = bits[0]
                           008100   572 	b1 = bits[1]
                           008200   573 	b2 = bits[2]
                           008300   574 	b3 = bits[3]
                           008400   575 	b4 = bits[4]
                           008500   576 	b5 = bits[5]
                           008600   577 	b6 = bits[6]
                           008700   578 	b7 = bits[7]
                                    579 ;--------------------------------------------------------
                                    580 ; internal ram data
                                    581 ;--------------------------------------------------------
                                    582 	.area DSEG    (DATA)
      000010                        583 _bytes::
      000010                        584 	.ds 2
      000012                        585 _icount::
      000012                        586 	.ds 1
      000013                        587 _lcount::
      000013                        588 	.ds 4
      000017                        589 _handle_get_interface_PARM_2:
      000017                        590 	.ds 3
      00001A                        591 _handle_set_interface_PARM_2:
      00001A                        592 	.ds 1
                                    593 ;--------------------------------------------------------
                                    594 ; overlayable items in internal ram
                                    595 ;--------------------------------------------------------
                                    596 	.area	OSEG    (OVR,DATA)
                                    597 ;--------------------------------------------------------
                                    598 ; Stack segment in internal ram
                                    599 ;--------------------------------------------------------
                                    600 	.area SSEG
      00005F                        601 __start__stack:
      00005F                        602 	.ds	1
                                    603 
                                    604 ;--------------------------------------------------------
                                    605 ; indirectly addressable internal ram data
                                    606 ;--------------------------------------------------------
                                    607 	.area ISEG    (DATA)
                                    608 ;--------------------------------------------------------
                                    609 ; absolute internal ram data
                                    610 ;--------------------------------------------------------
                                    611 	.area IABS    (ABS,DATA)
                                    612 	.area IABS    (ABS,DATA)
                                    613 ;--------------------------------------------------------
                                    614 ; bit data
                                    615 ;--------------------------------------------------------
                                    616 	.area BSEG    (BIT)
      000000                        617 _gotbuf::
      000000                        618 	.ds 1
      000001                        619 _got_sud::
      000001                        620 	.ds 1
      000002                        621 _on::
      000002                        622 	.ds 1
      000003                        623 _on5::
      000003                        624 	.ds 1
                                    625 ;--------------------------------------------------------
                                    626 ; paged external ram data
                                    627 ;--------------------------------------------------------
                                    628 	.area PSEG    (PAG,XDATA)
                                    629 ;--------------------------------------------------------
                                    630 ; uninitialized external ram data
                                    631 ;--------------------------------------------------------
                                    632 	.area XSEG    (XDATA)
                           00E400   633 _GPIF_WAVE_DATA	=	0xe400
                           00E480   634 _RES_WAVEDATA_END	=	0xe480
                           00E507   635 _UNIQID0	=	0xe507
                           00E508   636 _UNIQID1	=	0xe508
                           00E509   637 _UNIQID2	=	0xe509
                           00E50A   638 _UNIQID3	=	0xe50a
                           00E50B   639 _UNIQID4	=	0xe50b
                           00E50C   640 _UNIQID5	=	0xe50c
                           00E600   641 _CPUCS	=	0xe600
                           00E601   642 _IFCONFIG	=	0xe601
                           00E602   643 _PINFLAGSAB	=	0xe602
                           00E603   644 _PINFLAGSCD	=	0xe603
                           00E604   645 _FIFORESET	=	0xe604
                           00E605   646 _BREAKPT	=	0xe605
                           00E606   647 _BPADDRH	=	0xe606
                           00E607   648 _BPADDRL	=	0xe607
                           00E608   649 _UART230	=	0xe608
                           00E609   650 _FIFOPINPOLAR	=	0xe609
                           00E60A   651 _REVID	=	0xe60a
                           00E60B   652 _REVCTL	=	0xe60b
                           00E610   653 _EP1OUTCFG	=	0xe610
                           00E611   654 _EP1INCFG	=	0xe611
                           00E612   655 _EP2CFG	=	0xe612
                           00E613   656 _EP4CFG	=	0xe613
                           00E614   657 _EP6CFG	=	0xe614
                           00E615   658 _EP8CFG	=	0xe615
                           00E618   659 _EP2FIFOCFG	=	0xe618
                           00E619   660 _EP4FIFOCFG	=	0xe619
                           00E61A   661 _EP6FIFOCFG	=	0xe61a
                           00E61B   662 _EP8FIFOCFG	=	0xe61b
                           00E620   663 _EP2AUTOINLENH	=	0xe620
                           00E621   664 _EP2AUTOINLENL	=	0xe621
                           00E622   665 _EP4AUTOINLENH	=	0xe622
                           00E623   666 _EP4AUTOINLENL	=	0xe623
                           00E624   667 _EP6AUTOINLENH	=	0xe624
                           00E625   668 _EP6AUTOINLENL	=	0xe625
                           00E626   669 _EP8AUTOINLENH	=	0xe626
                           00E627   670 _EP8AUTOINLENL	=	0xe627
                           00E630   671 _EP2FIFOPFH	=	0xe630
                           00E631   672 _EP2FIFOPFL	=	0xe631
                           00E632   673 _EP4FIFOPFH	=	0xe632
                           00E633   674 _EP4FIFOPFL	=	0xe633
                           00E634   675 _EP6FIFOPFH	=	0xe634
                           00E635   676 _EP6FIFOPFL	=	0xe635
                           00E636   677 _EP8FIFOPFH	=	0xe636
                           00E637   678 _EP8FIFOPFL	=	0xe637
                           00E640   679 _EP2ISOINPKTS	=	0xe640
                           00E641   680 _EP4ISOINPKTS	=	0xe641
                           00E642   681 _EP6ISOINPKTS	=	0xe642
                           00E643   682 _EP8ISOINPKTS	=	0xe643
                           00E648   683 _INPKTEND	=	0xe648
                           00E649   684 _OUTPKTEND	=	0xe649
                           00E650   685 _EP2FIFOIE	=	0xe650
                           00E651   686 _EP2FIFOIRQ	=	0xe651
                           00E652   687 _EP4FIFOIE	=	0xe652
                           00E653   688 _EP4FIFOIRQ	=	0xe653
                           00E654   689 _EP6FIFOIE	=	0xe654
                           00E655   690 _EP6FIFOIRQ	=	0xe655
                           00E656   691 _EP8FIFOIE	=	0xe656
                           00E657   692 _EP8FIFOIRQ	=	0xe657
                           00E658   693 _IBNIE	=	0xe658
                           00E659   694 _IBNIRQ	=	0xe659
                           00E65A   695 _NAKIE	=	0xe65a
                           00E65B   696 _NAKIRQ	=	0xe65b
                           00E65C   697 _USBIE	=	0xe65c
                           00E65D   698 _USBIRQ	=	0xe65d
                           00E65E   699 _EPIE	=	0xe65e
                           00E65F   700 _EPIRQ	=	0xe65f
                           00E660   701 _GPIFIE	=	0xe660
                           00E661   702 _GPIFIRQ	=	0xe661
                           00E662   703 _USBERRIE	=	0xe662
                           00E663   704 _USBERRIRQ	=	0xe663
                           00E664   705 _ERRCNTLIM	=	0xe664
                           00E665   706 _CLRERRCNT	=	0xe665
                           00E666   707 _INT2IVEC	=	0xe666
                           00E667   708 _INT4IVEC	=	0xe667
                           00E668   709 _INTSETUP	=	0xe668
                           00E670   710 _PORTACFG	=	0xe670
                           00E671   711 _PORTCCFG	=	0xe671
                           00E672   712 _PORTECFG	=	0xe672
                           00E678   713 _I2CS	=	0xe678
                           00E679   714 _I2DAT	=	0xe679
                           00E67A   715 _I2CTL	=	0xe67a
                           00E67B   716 _XAUTODAT1	=	0xe67b
                           00E67C   717 _XAUTODAT2	=	0xe67c
                           00E680   718 _USBCS	=	0xe680
                           00E681   719 _SUSPEND	=	0xe681
                           00E682   720 _WAKEUPCS	=	0xe682
                           00E683   721 _TOGCTL	=	0xe683
                           00E684   722 _USBFRAMEH	=	0xe684
                           00E685   723 _USBFRAMEL	=	0xe685
                           00E686   724 _MICROFRAME	=	0xe686
                           00E687   725 _FNADDR	=	0xe687
                           00E68A   726 _EP0BCH	=	0xe68a
                           00E68B   727 _EP0BCL	=	0xe68b
                           00E68D   728 _EP1OUTBC	=	0xe68d
                           00E68F   729 _EP1INBC	=	0xe68f
                           00E690   730 _EP2BCH	=	0xe690
                           00E691   731 _EP2BCL	=	0xe691
                           00E694   732 _EP4BCH	=	0xe694
                           00E695   733 _EP4BCL	=	0xe695
                           00E698   734 _EP6BCH	=	0xe698
                           00E699   735 _EP6BCL	=	0xe699
                           00E69C   736 _EP8BCH	=	0xe69c
                           00E69D   737 _EP8BCL	=	0xe69d
                           00E6A0   738 _EP0CS	=	0xe6a0
                           00E6A1   739 _EP1OUTCS	=	0xe6a1
                           00E6A2   740 _EP1INCS	=	0xe6a2
                           00E6A3   741 _EP2CS	=	0xe6a3
                           00E6A4   742 _EP4CS	=	0xe6a4
                           00E6A5   743 _EP6CS	=	0xe6a5
                           00E6A6   744 _EP8CS	=	0xe6a6
                           00E6A7   745 _EP2FIFOFLGS	=	0xe6a7
                           00E6A8   746 _EP4FIFOFLGS	=	0xe6a8
                           00E6A9   747 _EP6FIFOFLGS	=	0xe6a9
                           00E6AA   748 _EP8FIFOFLGS	=	0xe6aa
                           00E6AB   749 _EP2FIFOBCH	=	0xe6ab
                           00E6AC   750 _EP2FIFOBCL	=	0xe6ac
                           00E6AD   751 _EP4FIFOBCH	=	0xe6ad
                           00E6AE   752 _EP4FIFOBCL	=	0xe6ae
                           00E6AF   753 _EP6FIFOBCH	=	0xe6af
                           00E6B0   754 _EP6FIFOBCL	=	0xe6b0
                           00E6B1   755 _EP8FIFOBCH	=	0xe6b1
                           00E6B2   756 _EP8FIFOBCL	=	0xe6b2
                           00E6B3   757 _SUDPTRH	=	0xe6b3
                           00E6B4   758 _SUDPTRL	=	0xe6b4
                           00E6B5   759 _SUDPTRCTL	=	0xe6b5
                           00E6B8   760 _SETUPDAT	=	0xe6b8
                           00E6C0   761 _GPIFWFSELECT	=	0xe6c0
                           00E6C1   762 _GPIFIDLECS	=	0xe6c1
                           00E6C2   763 _GPIFIDLECTL	=	0xe6c2
                           00E6C3   764 _GPIFCTLCFG	=	0xe6c3
                           00E6C4   765 _GPIFADRH	=	0xe6c4
                           00E6C5   766 _GPIFADRL	=	0xe6c5
                           00E6CE   767 _GPIFTCB3	=	0xe6ce
                           00E6CF   768 _GPIFTCB2	=	0xe6cf
                           00E6D0   769 _GPIFTCB1	=	0xe6d0
                           00E6D1   770 _GPIFTCB0	=	0xe6d1
                           00E6D2   771 _EP2GPIFFLGSEL	=	0xe6d2
                           00E6D3   772 _EP2GPIFPFSTOP	=	0xe6d3
                           00E6D4   773 _EP2GPIFTRIG	=	0xe6d4
                           00E6DA   774 _EP4GPIFFLGSEL	=	0xe6da
                           00E6DB   775 _EP4GPIFPFSTOP	=	0xe6db
                           00E6DC   776 _EP4GPIFTRIG	=	0xe6dc
                           00E6E2   777 _EP6GPIFFLGSEL	=	0xe6e2
                           00E6E3   778 _EP6GPIFPFSTOP	=	0xe6e3
                           00E6E4   779 _EP6GPIFTRIG	=	0xe6e4
                           00E6EA   780 _EP8GPIFFLGSEL	=	0xe6ea
                           00E6EB   781 _EP8GPIFPFSTOP	=	0xe6eb
                           00E6EC   782 _EP8GPIFTRIG	=	0xe6ec
                           00E6F0   783 _XGPIFSGLDATH	=	0xe6f0
                           00E6F1   784 _XGPIFSGLDATLX	=	0xe6f1
                           00E6F2   785 _XGPIFSGLDATLNOX	=	0xe6f2
                           00E6F3   786 _GPIFREADYCFG	=	0xe6f3
                           00E6F4   787 _GPIFREADYSTAT	=	0xe6f4
                           00E6F5   788 _GPIFABORT	=	0xe6f5
                           00E6C6   789 _FLOWSTATE	=	0xe6c6
                           00E6C7   790 _FLOWLOGIC	=	0xe6c7
                           00E6C8   791 _FLOWEQ0CTL	=	0xe6c8
                           00E6C9   792 _FLOWEQ1CTL	=	0xe6c9
                           00E6CA   793 _FLOWHOLDOFF	=	0xe6ca
                           00E6CB   794 _FLOWSTB	=	0xe6cb
                           00E6CC   795 _FLOWSTBEDGE	=	0xe6cc
                           00E6CD   796 _FLOWSTBHPERIOD	=	0xe6cd
                           00E60C   797 _GPIFHOLDAMOUNT	=	0xe60c
                           00E67D   798 _UDMACRCH	=	0xe67d
                           00E67E   799 _UDMACRCL	=	0xe67e
                           00E67F   800 _UDMACRCQUAL	=	0xe67f
                           00E740   801 _EP0BUF	=	0xe740
                           00E780   802 _EP1OUTBUF	=	0xe780
                           00E7C0   803 _EP1INBUF	=	0xe7c0
                           00F000   804 _EP2FIFOBUF	=	0xf000
                           00F400   805 _EP4FIFOBUF	=	0xf400
                           00F800   806 _EP6FIFOBUF	=	0xf800
                           00FC00   807 _EP8FIFOBUF	=	0xfc00
                           00E628   808 _ECCCFG	=	0xe628
                           00E629   809 _ECCRESET	=	0xe629
                           00E62A   810 _ECC1B0	=	0xe62a
                           00E62B   811 _ECC1B1	=	0xe62b
                           00E62C   812 _ECC1B2	=	0xe62c
                           00E62D   813 _ECC2B0	=	0xe62d
                           00E62E   814 _ECC2B1	=	0xe62e
                           00E62F   815 _ECC2B2	=	0xe62f
                           00E50D   816 _GPCR2	=	0xe50d
                           008800   817 _D2ON	=	0x8800
                           008000   818 _D2OFF	=	0x8000
                           009800   819 _D3ON	=	0x9800
                           009000   820 _D3OFF	=	0x9000
                           00A800   821 _D4ON	=	0xa800
                           00A000   822 _D4OFF	=	0xa000
                           00B800   823 _D5ON	=	0xb800
                           00B000   824 _D5OFF	=	0xb000
                                    825 ;--------------------------------------------------------
                                    826 ; absolute external ram data
                                    827 ;--------------------------------------------------------
                                    828 	.area XABS    (ABS,XDATA)
                                    829 ;--------------------------------------------------------
                                    830 ; initialized external ram data
                                    831 ;--------------------------------------------------------
                                    832 	.area XISEG   (XDATA)
      003C00                        833 _sofct::
      003C00                        834 	.ds 2
                                    835 	.area HOME    (CODE)
                                    836 	.area GSINIT0 (CODE)
                                    837 	.area GSINIT1 (CODE)
                                    838 	.area GSINIT2 (CODE)
                                    839 	.area GSINIT3 (CODE)
                                    840 	.area GSINIT4 (CODE)
                                    841 	.area GSINIT5 (CODE)
                                    842 	.area GSINIT  (CODE)
                                    843 	.area GSFINAL (CODE)
                                    844 	.area CSEG    (CODE)
                                    845 ;--------------------------------------------------------
                                    846 ; interrupt vector
                                    847 ;--------------------------------------------------------
                                    848 	.area HOME    (CODE)
      000000                        849 __interrupt_vect:
      000000 02 00 C8         [24]  850 	ljmp	__sdcc_gsinit_startup
      000003 32               [24]  851 	reti
      000004                        852 	.ds	7
      00000B 32               [24]  853 	reti
      00000C                        854 	.ds	7
      000013 32               [24]  855 	reti
      000014                        856 	.ds	7
      00001B 32               [24]  857 	reti
      00001C                        858 	.ds	7
      000023 32               [24]  859 	reti
      000024                        860 	.ds	7
      00002B 32               [24]  861 	reti
      00002C                        862 	.ds	7
      000033 32               [24]  863 	reti
      000034                        864 	.ds	7
      00003B 32               [24]  865 	reti
      00003C                        866 	.ds	7
      000043 02 3F 00         [24]  867 	ljmp	_usb_isr
      000046                        868 	.ds	5
      00004B 32               [24]  869 	reti
      00004C                        870 	.ds	7
      000053 02 3F 00         [24]  871 	ljmp	_gpif_isr
                                    872 ; restartable atomic support routines
      000056                        873 	.ds	2
      000058                        874 sdcc_atomic_exchange_rollback_start::
      000058 00               [12]  875 	nop
      000059 00               [12]  876 	nop
      00005A                        877 sdcc_atomic_exchange_pdata_impl:
      00005A E2               [24]  878 	movx	a, @r0
      00005B FB               [12]  879 	mov	r3, a
      00005C EA               [12]  880 	mov	a, r2
      00005D F2               [24]  881 	movx	@r0, a
      00005E 80 2C            [24]  882 	sjmp	sdcc_atomic_exchange_exit
      000060 00               [12]  883 	nop
      000061 00               [12]  884 	nop
      000062                        885 sdcc_atomic_exchange_xdata_impl:
      000062 E0               [24]  886 	movx	a, @dptr
      000063 FB               [12]  887 	mov	r3, a
      000064 EA               [12]  888 	mov	a, r2
      000065 F0               [24]  889 	movx	@dptr, a
      000066 80 24            [24]  890 	sjmp	sdcc_atomic_exchange_exit
      000068                        891 sdcc_atomic_compare_exchange_idata_impl:
      000068 E6               [12]  892 	mov	a, @r0
      000069 B5 02 02         [24]  893 	cjne	a, ar2, .+#5
      00006C EB               [12]  894 	mov	a, r3
      00006D F6               [12]  895 	mov	@r0, a
      00006E 22               [24]  896 	ret
      00006F 00               [12]  897 	nop
      000070                        898 sdcc_atomic_compare_exchange_pdata_impl:
      000070 E2               [24]  899 	movx	a, @r0
      000071 B5 02 02         [24]  900 	cjne	a, ar2, .+#5
      000074 EB               [12]  901 	mov	a, r3
      000075 F2               [24]  902 	movx	@r0, a
      000076 22               [24]  903 	ret
      000077 00               [12]  904 	nop
      000078                        905 sdcc_atomic_compare_exchange_xdata_impl:
      000078 E0               [24]  906 	movx	a, @dptr
      000079 B5 02 02         [24]  907 	cjne	a, ar2, .+#5
      00007C EB               [12]  908 	mov	a, r3
      00007D F0               [24]  909 	movx	@dptr, a
      00007E 22               [24]  910 	ret
      00007F                        911 sdcc_atomic_exchange_rollback_end::
                                    912 
      00007F                        913 sdcc_atomic_exchange_gptr_impl::
      00007F 30 F6 E0         [24]  914 	jnb	b.6, sdcc_atomic_exchange_xdata_impl
      000082 A8 82            [24]  915 	mov	r0, dpl
      000084 20 F5 D3         [24]  916 	jb	b.5, sdcc_atomic_exchange_pdata_impl
      000087                        917 sdcc_atomic_exchange_idata_impl:
      000087 EA               [12]  918 	mov	a, r2
      000088 C6               [12]  919 	xch	a, @r0
      000089 F5 82            [12]  920 	mov	dpl, a
      00008B 22               [24]  921 	ret
      00008C                        922 sdcc_atomic_exchange_exit:
      00008C 8B 82            [24]  923 	mov	dpl, r3
      00008E 22               [24]  924 	ret
      00008F                        925 sdcc_atomic_compare_exchange_gptr_impl::
      00008F 30 F6 E6         [24]  926 	jnb	b.6, sdcc_atomic_compare_exchange_xdata_impl
      000092 A8 82            [24]  927 	mov	r0, dpl
      000094 20 F5 D9         [24]  928 	jb	b.5, sdcc_atomic_compare_exchange_pdata_impl
      000097 80 CF            [24]  929 	sjmp	sdcc_atomic_compare_exchange_idata_impl
                                    930 ;--------------------------------------------------------
                                    931 ; global & static initialisations
                                    932 ;--------------------------------------------------------
                                    933 	.area HOME    (CODE)
                                    934 	.area GSINIT  (CODE)
                                    935 	.area GSFINAL (CODE)
                                    936 	.area GSINIT  (CODE)
                                    937 	.globl __sdcc_gsinit_startup
                                    938 	.globl __sdcc_program_startup
                                    939 	.globl __start__stack
                                    940 	.globl __mcs51_genXINIT
                                    941 	.globl __mcs51_genXRAMCLEAR
                                    942 	.globl __mcs51_genRAMCLEAR
                                    943 	.area GSFINAL (CODE)
      000133 02 00 99         [24]  944 	ljmp	__sdcc_program_startup
                                    945 ;--------------------------------------------------------
                                    946 ; Home
                                    947 ;--------------------------------------------------------
                                    948 	.area HOME    (CODE)
                                    949 	.area HOME    (CODE)
      000099                        950 __sdcc_program_startup:
      000099 12 01 36         [24]  951 	lcall	_main
      00009C                        952 __sdcc_program_exit:
      00009C 80 FE            [24]  953 	sjmp	.
                                    954 ;	return from main will return to caller
                                    955 ;--------------------------------------------------------
                                    956 ; code
                                    957 ;--------------------------------------------------------
                                    958 	.area CSEG    (CODE)
                                    959 ;------------------------------------------------------------
                                    960 ;Allocation info for local variables in function 'main'
                                    961 ;------------------------------------------------------------
                                    962 ;i             Allocated to registers r6 r7 
                                    963 ;------------------------------------------------------------
                                    964 ;	build/../bulkloop.c:43: void main(void) {
                                    965 ;	-----------------------------------------
                                    966 ;	 function main
                                    967 ;	-----------------------------------------
      000136                        968 _main:
                           000007   969 	ar7 = 0x07
                           000006   970 	ar6 = 0x06
                           000005   971 	ar5 = 0x05
                           000004   972 	ar4 = 0x04
                           000003   973 	ar3 = 0x03
                           000002   974 	ar2 = 0x02
                           000001   975 	ar1 = 0x01
                           000000   976 	ar0 = 0x00
                                    977 ;	build/../bulkloop.c:45: REVCTL=0; // not using advanced endpoint controls
      000136 90 E6 0B         [24]  978 	mov	dptr,#_REVCTL
      000139 E4               [12]  979 	clr	a
      00013A F0               [24]  980 	movx	@dptr,a
                                    981 ;	build/../bulkloop.c:47: d2off();
      00013B 75 92 80         [24]  982 	mov __XPAGE, #0x80 
      00013E E2               [24]  983 	movx a, @r0 
                                    984 ;	build/../bulkloop.c:48: on=0;
                                    985 ;	assignBit
      00013F C2 02            [12]  986 	clr	_on
                                    987 ;	build/../bulkloop.c:49: lcount=0;
      000141 E4               [12]  988 	clr	a
      000142 F5 13            [12]  989 	mov	_lcount,a
      000144 F5 14            [12]  990 	mov	(_lcount + 1),a
      000146 F5 15            [12]  991 	mov	(_lcount + 2),a
      000148 F5 16            [12]  992 	mov	(_lcount + 3),a
                                    993 ;	build/../bulkloop.c:50: got_sud=FALSE;
                                    994 ;	assignBit
      00014A C2 01            [12]  995 	clr	_got_sud
                                    996 ;	build/../bulkloop.c:51: icount=0;
      00014C 75 12 00         [24]  997 	mov	_icount,#0x00
                                    998 ;	build/../bulkloop.c:52: gotbuf=FALSE;
                                    999 ;	assignBit
      00014F C2 00            [12] 1000 	clr	_gotbuf
                                   1001 ;	build/../bulkloop.c:53: bytes=0;
      000151 E4               [12] 1002 	clr	a
      000152 F5 10            [12] 1003 	mov	_bytes,a
      000154 F5 11            [12] 1004 	mov	(_bytes + 1),a
                                   1005 ;	build/../bulkloop.c:56: RENUMERATE_UNCOND();
      000156 90 E6 80         [24] 1006 	mov	dptr,#_USBCS
      000159 E0               [24] 1007 	movx	a,@dptr
      00015A 43 E0 0A         [24] 1008 	orl	acc,#0x0a
      00015D F0               [24] 1009 	movx	@dptr,a
      00015E 90 05 DC         [24] 1010 	mov	dptr,#0x05dc
      000161 12 0A 2A         [24] 1011 	lcall	_delay
      000164 90 E6 80         [24] 1012 	mov	dptr,#_USBCS
      000167 E0               [24] 1013 	movx	a,@dptr
      000168 53 E0 F7         [24] 1014 	anl	acc,#0xf7
      00016B F0               [24] 1015 	movx	@dptr,a
                                   1016 ;	build/../bulkloop.c:59: SETCPUFREQ(CLK_48M);
      00016C 90 E6 00         [24] 1017 	mov	dptr,#_CPUCS
      00016F E0               [24] 1018 	movx	a,@dptr
      000170 54 E7            [12] 1019 	anl	a,#0xe7
      000172 44 10            [12] 1020 	orl	a,#0x10
      000174 F0               [24] 1021 	movx	@dptr,a
                                   1022 ;	build/../bulkloop.c:60: SETIF48MHZ();
      000175 90 E6 01         [24] 1023 	mov	dptr,#_IFCONFIG
      000178 E0               [24] 1024 	movx	a,@dptr
      000179 43 E0 40         [24] 1025 	orl	acc,#0x40
      00017C F0               [24] 1026 	movx	@dptr,a
                                   1027 ;	build/../bulkloop.c:61: sio0_init(57600);
      00017D 90 E1 00         [24] 1028 	mov	dptr,#0xe100
      000180 E4               [12] 1029 	clr	a
      000181 F5 F0            [12] 1030 	mov	b,a
      000183 12 09 3D         [24] 1031 	lcall	_sio0_init
                                   1032 ;	build/../bulkloop.c:64: USE_USB_INTS();
                                   1033 ;	assignBit
      000186 D2 E8            [12] 1034 	setb	_EUSB
      000188 90 E6 68         [24] 1035 	mov	dptr,#_INTSETUP
      00018B E0               [24] 1036 	movx	a,@dptr
      00018C 43 E0 08         [24] 1037 	orl	acc,#0x08
      00018F F0               [24] 1038 	movx	@dptr,a
                                   1039 ;	build/../bulkloop.c:65: ENABLE_SUDAV();
      000190 90 E6 5C         [24] 1040 	mov	dptr,#_USBIE
      000193 E0               [24] 1041 	movx	a,@dptr
      000194 43 E0 01         [24] 1042 	orl	acc,#0x01
      000197 F0               [24] 1043 	movx	@dptr,a
                                   1044 ;	build/../bulkloop.c:66: ENABLE_SOF();
      000198 90 E6 5C         [24] 1045 	mov	dptr,#_USBIE
      00019B E0               [24] 1046 	movx	a,@dptr
      00019C 43 E0 02         [24] 1047 	orl	acc,#0x02
      00019F F0               [24] 1048 	movx	@dptr,a
                                   1049 ;	build/../bulkloop.c:67: ENABLE_HISPEED();
      0001A0 90 E6 5C         [24] 1050 	mov	dptr,#_USBIE
      0001A3 E0               [24] 1051 	movx	a,@dptr
      0001A4 43 E0 20         [24] 1052 	orl	acc,#0x20
      0001A7 F0               [24] 1053 	movx	@dptr,a
                                   1054 ;	build/../bulkloop.c:68: ENABLE_USBRESET();
      0001A8 90 E6 5C         [24] 1055 	mov	dptr,#_USBIE
      0001AB E0               [24] 1056 	movx	a,@dptr
      0001AC 43 E0 10         [24] 1057 	orl	acc,#0x10
      0001AF F0               [24] 1058 	movx	@dptr,a
                                   1059 ;	build/../bulkloop.c:72: EP2CFG = 0xA2; // 10100010
      0001B0 90 E6 12         [24] 1060 	mov	dptr,#_EP2CFG
      0001B3 74 A2            [12] 1061 	mov	a,#0xa2
      0001B5 F0               [24] 1062 	movx	@dptr,a
                                   1063 ;	build/../bulkloop.c:73: SYNCDELAY;
      0001B6 00               [12] 1064 	nop	
      0001B7 00               [12] 1065 	nop	
      0001B8 00               [12] 1066 	nop	
      0001B9 00               [12] 1067 	nop	
                                   1068 ;	build/../bulkloop.c:74: EP6CFG = 0xE2; // 11100010
      0001BA 90 E6 14         [24] 1069 	mov	dptr,#_EP6CFG
      0001BD 74 E2            [12] 1070 	mov	a,#0xe2
      0001BF F0               [24] 1071 	movx	@dptr,a
                                   1072 ;	build/../bulkloop.c:75: SYNCDELAY;
      0001C0 00               [12] 1073 	nop	
      0001C1 00               [12] 1074 	nop	
      0001C2 00               [12] 1075 	nop	
      0001C3 00               [12] 1076 	nop	
                                   1077 ;	build/../bulkloop.c:76: EP1INCFG &= ~bmVALID;
      0001C4 90 E6 11         [24] 1078 	mov	dptr,#_EP1INCFG
      0001C7 E0               [24] 1079 	movx	a,@dptr
      0001C8 53 E0 7F         [24] 1080 	anl	acc,#0x7f
      0001CB F0               [24] 1081 	movx	@dptr,a
                                   1082 ;	build/../bulkloop.c:77: SYNCDELAY;
      0001CC 00               [12] 1083 	nop	
      0001CD 00               [12] 1084 	nop	
      0001CE 00               [12] 1085 	nop	
      0001CF 00               [12] 1086 	nop	
                                   1087 ;	build/../bulkloop.c:78: EP1OUTCFG &= ~bmVALID;
      0001D0 90 E6 10         [24] 1088 	mov	dptr,#_EP1OUTCFG
      0001D3 E0               [24] 1089 	movx	a,@dptr
      0001D4 53 E0 7F         [24] 1090 	anl	acc,#0x7f
      0001D7 F0               [24] 1091 	movx	@dptr,a
                                   1092 ;	build/../bulkloop.c:79: SYNCDELAY;
      0001D8 00               [12] 1093 	nop	
      0001D9 00               [12] 1094 	nop	
      0001DA 00               [12] 1095 	nop	
      0001DB 00               [12] 1096 	nop	
                                   1097 ;	build/../bulkloop.c:80: EP4CFG &= ~bmVALID;
      0001DC 90 E6 13         [24] 1098 	mov	dptr,#_EP4CFG
      0001DF E0               [24] 1099 	movx	a,@dptr
      0001E0 53 E0 7F         [24] 1100 	anl	acc,#0x7f
      0001E3 F0               [24] 1101 	movx	@dptr,a
                                   1102 ;	build/../bulkloop.c:81: SYNCDELAY;
      0001E4 00               [12] 1103 	nop	
      0001E5 00               [12] 1104 	nop	
      0001E6 00               [12] 1105 	nop	
      0001E7 00               [12] 1106 	nop	
                                   1107 ;	build/../bulkloop.c:82: EP8CFG &= ~bmVALID;
      0001E8 90 E6 15         [24] 1108 	mov	dptr,#_EP8CFG
      0001EB E0               [24] 1109 	movx	a,@dptr
      0001EC 53 E0 7F         [24] 1110 	anl	acc,#0x7f
      0001EF F0               [24] 1111 	movx	@dptr,a
                                   1112 ;	build/../bulkloop.c:83: SYNCDELAY;
      0001F0 00               [12] 1113 	nop	
      0001F1 00               [12] 1114 	nop	
      0001F2 00               [12] 1115 	nop	
      0001F3 00               [12] 1116 	nop	
                                   1117 ;	build/../bulkloop.c:87: EP2BCL = 0x80; // write once
      0001F4 90 E6 91         [24] 1118 	mov	dptr,#_EP2BCL
      0001F7 74 80            [12] 1119 	mov	a,#0x80
      0001F9 F0               [24] 1120 	movx	@dptr,a
                                   1121 ;	build/../bulkloop.c:88: SYNCDELAY;
      0001FA 00               [12] 1122 	nop	
      0001FB 00               [12] 1123 	nop	
      0001FC 00               [12] 1124 	nop	
      0001FD 00               [12] 1125 	nop	
                                   1126 ;	build/../bulkloop.c:89: EP2BCL = 0x80; // do it again
      0001FE 90 E6 91         [24] 1127 	mov	dptr,#_EP2BCL
      000201 74 80            [12] 1128 	mov	a,#0x80
      000203 F0               [24] 1129 	movx	@dptr,a
                                   1130 ;	build/../bulkloop.c:95: EA=1; // global interrupt enable
                                   1131 ;	assignBit
      000204 D2 AF            [12] 1132 	setb	_EA
                                   1133 ;	build/../bulkloop.c:96: printf ( "Done initializing stuff\n" );
      000206 74 10            [12] 1134 	mov	a,#___str_0
      000208 C0 E0            [24] 1135 	push	acc
      00020A 74 13            [12] 1136 	mov	a,#(___str_0 >> 8)
      00020C C0 E0            [24] 1137 	push	acc
      00020E 74 80            [12] 1138 	mov	a,#0x80
      000210 C0 E0            [24] 1139 	push	acc
      000212 12 0A A4         [24] 1140 	lcall	_printf
      000215 15 81            [12] 1141 	dec	sp
      000217 15 81            [12] 1142 	dec	sp
      000219 15 81            [12] 1143 	dec	sp
                                   1144 ;	build/../bulkloop.c:99: d3off();
      00021B 75 92 90         [24] 1145 	mov __XPAGE, #0x90 
      00021E E2               [24] 1146 	movx a, @r0 
                                   1147 ;	build/../bulkloop.c:101: while(TRUE) {
      00021F                       1148 00109$:
                                   1149 ;	build/../bulkloop.c:103: if ( got_sud ) {
      00021F 30 01 1A         [24] 1150 	jnb	_got_sud,00102$
                                   1151 ;	build/../bulkloop.c:104: printf ( "Handle setupdata\n" );
      000222 74 29            [12] 1152 	mov	a,#___str_1
      000224 C0 E0            [24] 1153 	push	acc
      000226 74 13            [12] 1154 	mov	a,#(___str_1 >> 8)
      000228 C0 E0            [24] 1155 	push	acc
      00022A 74 80            [12] 1156 	mov	a,#0x80
      00022C C0 E0            [24] 1157 	push	acc
      00022E 12 0A A4         [24] 1158 	lcall	_printf
      000231 15 81            [12] 1159 	dec	sp
      000233 15 81            [12] 1160 	dec	sp
      000235 15 81            [12] 1161 	dec	sp
                                   1162 ;	build/../bulkloop.c:105: handle_setupdata();
      000237 12 05 1D         [24] 1163 	lcall	_handle_setupdata
                                   1164 ;	build/../bulkloop.c:106: got_sud=FALSE;
                                   1165 ;	assignBit
      00023A C2 01            [12] 1166 	clr	_got_sud
      00023C                       1167 00102$:
                                   1168 ;	build/../bulkloop.c:109: if ( !(EP2468STAT & bmEP2EMPTY) ) {
      00023C E5 AA            [12] 1169 	mov	a,_EP2468STAT
      00023E 20 E0 DE         [24] 1170 	jb	acc.0,00109$
                                   1171 ;	build/../bulkloop.c:110: printf ( "ep2 out received data\n" );
      000241 74 3B            [12] 1172 	mov	a,#___str_2
      000243 C0 E0            [24] 1173 	push	acc
      000245 74 13            [12] 1174 	mov	a,#(___str_2 >> 8)
      000247 C0 E0            [24] 1175 	push	acc
      000249 74 80            [12] 1176 	mov	a,#0x80
      00024B C0 E0            [24] 1177 	push	acc
      00024D 12 0A A4         [24] 1178 	lcall	_printf
      000250 15 81            [12] 1179 	dec	sp
      000252 15 81            [12] 1180 	dec	sp
      000254 15 81            [12] 1181 	dec	sp
                                   1182 ;	build/../bulkloop.c:111: if  ( !(EP2468STAT & bmEP6FULL) ) { // wait for at least one empty in buffer
      000256 E5 AA            [12] 1183 	mov	a,_EP2468STAT
      000258 20 E5 C4         [24] 1184 	jb	acc.5,00109$
                                   1185 ;	build/../bulkloop.c:113: printf ( "Sending data to ep6 in\n");
      00025B 74 52            [12] 1186 	mov	a,#___str_3
      00025D C0 E0            [24] 1187 	push	acc
      00025F 74 13            [12] 1188 	mov	a,#(___str_3 >> 8)
      000261 C0 E0            [24] 1189 	push	acc
      000263 74 80            [12] 1190 	mov	a,#0x80
      000265 C0 E0            [24] 1191 	push	acc
      000267 12 0A A4         [24] 1192 	lcall	_printf
      00026A 15 81            [12] 1193 	dec	sp
      00026C 15 81            [12] 1194 	dec	sp
      00026E 15 81            [12] 1195 	dec	sp
                                   1196 ;	build/../bulkloop.c:115: bytes = MAKEWORD(EP2BCH,EP2BCL);
      000270 90 E6 90         [24] 1197 	mov	dptr,#_EP2BCH
      000273 E0               [24] 1198 	movx	a,@dptr
      000274 FF               [12] 1199 	mov	r7,a
      000275 7E 00            [12] 1200 	mov	r6,#0x00
      000277 90 E6 91         [24] 1201 	mov	dptr,#_EP2BCL
      00027A E0               [24] 1202 	movx	a,@dptr
      00027B FC               [12] 1203 	mov	r4,a
      00027C 7D 00            [12] 1204 	mov	r5,#0x00
      00027E 4E               [12] 1205 	orl	a,r6
      00027F F5 10            [12] 1206 	mov	_bytes,a
      000281 ED               [12] 1207 	mov	a,r5
      000282 4F               [12] 1208 	orl	a,r7
      000283 F5 11            [12] 1209 	mov	(_bytes + 1),a
                                   1210 ;	build/../bulkloop.c:117: for (i=0;i<bytes;++i) EP6FIFOBUF[i] = EP2FIFOBUF[i];
      000285 7F 00            [12] 1211 	mov	r7,#0x00
      000287                       1212 00112$:
      000287 C3               [12] 1213 	clr	c
      000288 EE               [12] 1214 	mov	a,r6
      000289 95 10            [12] 1215 	subb	a,_bytes
      00028B EF               [12] 1216 	mov	a,r7
      00028C 95 11            [12] 1217 	subb	a,(_bytes + 1)
      00028E 50 1B            [24] 1218 	jnc	00103$
      000290 8E 04            [24] 1219 	mov	ar4,r6
      000292 74 F8            [12] 1220 	mov	a,#(_EP6FIFOBUF >> 8)
      000294 2F               [12] 1221 	add	a,r7
      000295 FD               [12] 1222 	mov	r5,a
      000296 8E 82            [24] 1223 	mov	dpl,r6
      000298 74 F0            [12] 1224 	mov	a,#(_EP2FIFOBUF >> 8)
      00029A 2F               [12] 1225 	add	a,r7
      00029B F5 83            [12] 1226 	mov	dph,a
      00029D E0               [24] 1227 	movx	a,@dptr
      00029E FB               [12] 1228 	mov	r3,a
      00029F 8C 82            [24] 1229 	mov	dpl,r4
      0002A1 8D 83            [24] 1230 	mov	dph,r5
      0002A3 F0               [24] 1231 	movx	@dptr,a
      0002A4 0E               [12] 1232 	inc	r6
      0002A5 BE 00 DF         [24] 1233 	cjne	r6,#0x00,00112$
      0002A8 0F               [12] 1234 	inc	r7
      0002A9 80 DC            [24] 1235 	sjmp	00112$
      0002AB                       1236 00103$:
                                   1237 ;	build/../bulkloop.c:123: EP6BCH=MSB(bytes);
      0002AB 90 E6 98         [24] 1238 	mov	dptr,#_EP6BCH
      0002AE E5 11            [12] 1239 	mov	a,(_bytes + 1)
      0002B0 F0               [24] 1240 	movx	@dptr,a
                                   1241 ;	build/../bulkloop.c:124: SYNCDELAY;
      0002B1 00               [12] 1242 	nop	
      0002B2 00               [12] 1243 	nop	
      0002B3 00               [12] 1244 	nop	
      0002B4 00               [12] 1245 	nop	
                                   1246 ;	build/../bulkloop.c:125: EP6BCL=LSB(bytes);
      0002B5 90 E6 99         [24] 1247 	mov	dptr,#_EP6BCL
      0002B8 E5 10            [12] 1248 	mov	a,_bytes
      0002BA F0               [24] 1249 	movx	@dptr,a
                                   1250 ;	build/../bulkloop.c:127: REARM(); // ep2
      0002BB 90 E6 91         [24] 1251 	mov	dptr,#_EP2BCL
      0002BE 74 80            [12] 1252 	mov	a,#0x80
      0002C0 F0               [24] 1253 	movx	@dptr,a
                                   1254 ;	build/../bulkloop.c:134: }
      0002C1 02 02 1F         [24] 1255 	ljmp	00109$
                                   1256 ;------------------------------------------------------------
                                   1257 ;Allocation info for local variables in function 'handle_get_descriptor'
                                   1258 ;------------------------------------------------------------
                                   1259 ;	build/../bulkloop.c:138: BOOL handle_get_descriptor(void) {
                                   1260 ;	-----------------------------------------
                                   1261 ;	 function handle_get_descriptor
                                   1262 ;	-----------------------------------------
      0002C4                       1263 _handle_get_descriptor:
                                   1264 ;	build/../bulkloop.c:139: return FALSE;
      0002C4 75 82 00         [24] 1265 	mov	dpl, #0x00
                                   1266 ;	build/../bulkloop.c:140: }
      0002C7 22               [24] 1267 	ret
                                   1268 ;------------------------------------------------------------
                                   1269 ;Allocation info for local variables in function 'handle_vendorcommand'
                                   1270 ;------------------------------------------------------------
                                   1271 ;cmd           Allocated to registers r7 
                                   1272 ;pep           Allocated to registers r5 r6 
                                   1273 ;------------------------------------------------------------
                                   1274 ;	build/../bulkloop.c:145: BOOL handle_vendorcommand(BYTE cmd) {
                                   1275 ;	-----------------------------------------
                                   1276 ;	 function handle_vendorcommand
                                   1277 ;	-----------------------------------------
      0002C8                       1278 _handle_vendorcommand:
      0002C8 AF 82            [24] 1279 	mov	r7, dpl
                                   1280 ;	build/../bulkloop.c:147: switch ( cmd ) {
      0002CA BF B1 51         [24] 1281 	cjne	r7,#0xb1,00104$
                                   1282 ;	build/../bulkloop.c:151: __xdata BYTE* pep= ep_addr(SETUPDAT[2]);
      0002CD 90 E6 BA         [24] 1283 	mov	dptr,#(_SETUPDAT + 0x0002)
      0002D0 E0               [24] 1284 	movx	a,@dptr
      0002D1 F5 82            [12] 1285 	mov	dpl,a
      0002D3 C0 07            [24] 1286 	push	ar7
      0002D5 12 06 3B         [24] 1287 	lcall	_ep_addr
                                   1288 ;	build/../bulkloop.c:152: printf ( "ep %02x\n" , *pep );
      0002D8 AD 82            [24] 1289 	mov	r5,dpl
      0002DA AE 83            [24] 1290 	mov  r6,dph
      0002DC E0               [24] 1291 	movx	a,@dptr
      0002DD FC               [12] 1292 	mov	r4,a
      0002DE 7B 00            [12] 1293 	mov	r3,#0x00
      0002E0 C0 06            [24] 1294 	push	ar6
      0002E2 C0 05            [24] 1295 	push	ar5
      0002E4 C0 04            [24] 1296 	push	ar4
      0002E6 C0 03            [24] 1297 	push	ar3
      0002E8 74 6A            [12] 1298 	mov	a,#___str_4
      0002EA C0 E0            [24] 1299 	push	acc
      0002EC 74 13            [12] 1300 	mov	a,#(___str_4 >> 8)
      0002EE C0 E0            [24] 1301 	push	acc
      0002F0 74 80            [12] 1302 	mov	a,#0x80
      0002F2 C0 E0            [24] 1303 	push	acc
      0002F4 12 0A A4         [24] 1304 	lcall	_printf
      0002F7 E5 81            [12] 1305 	mov	a,sp
      0002F9 24 FB            [12] 1306 	add	a,#0xfb
      0002FB F5 81            [12] 1307 	mov	sp,a
      0002FD D0 05            [24] 1308 	pop	ar5
      0002FF D0 06            [24] 1309 	pop	ar6
      000301 D0 07            [24] 1310 	pop	ar7
                                   1311 ;	build/../bulkloop.c:153: if (pep) {
      000303 ED               [12] 1312 	mov	a,r5
      000304 4E               [12] 1313 	orl	a,r6
      000305 60 17            [24] 1314 	jz	00104$
                                   1315 ;	build/../bulkloop.c:154: EP0BUF[0] = *pep;
      000307 8D 82            [24] 1316 	mov	dpl,r5
      000309 8E 83            [24] 1317 	mov	dph,r6
      00030B E0               [24] 1318 	movx	a,@dptr
      00030C 90 E7 40         [24] 1319 	mov	dptr,#_EP0BUF
      00030F F0               [24] 1320 	movx	@dptr,a
                                   1321 ;	build/../bulkloop.c:155: EP0BCH=0;
      000310 90 E6 8A         [24] 1322 	mov	dptr,#_EP0BCH
      000313 E4               [12] 1323 	clr	a
      000314 F0               [24] 1324 	movx	@dptr,a
                                   1325 ;	build/../bulkloop.c:156: EP0BCL=1;
      000315 90 E6 8B         [24] 1326 	mov	dptr,#_EP0BCL
      000318 04               [12] 1327 	inc	a
      000319 F0               [24] 1328 	movx	@dptr,a
                                   1329 ;	build/../bulkloop.c:157: return TRUE;
      00031A 75 82 01         [24] 1330 	mov	dpl, #0x01
                                   1331 ;	build/../bulkloop.c:160: default:
      00031D 22               [24] 1332 	ret
      00031E                       1333 00104$:
                                   1334 ;	build/../bulkloop.c:161: printf ( "Need to implement vendor command: %02x\n", cmd );
      00031E 7E 00            [12] 1335 	mov	r6,#0x00
      000320 C0 07            [24] 1336 	push	ar7
      000322 C0 06            [24] 1337 	push	ar6
      000324 74 73            [12] 1338 	mov	a,#___str_5
      000326 C0 E0            [24] 1339 	push	acc
      000328 74 13            [12] 1340 	mov	a,#(___str_5 >> 8)
      00032A C0 E0            [24] 1341 	push	acc
      00032C 74 80            [12] 1342 	mov	a,#0x80
      00032E C0 E0            [24] 1343 	push	acc
      000330 12 0A A4         [24] 1344 	lcall	_printf
      000333 E5 81            [12] 1345 	mov	a,sp
      000335 24 FB            [12] 1346 	add	a,#0xfb
      000337 F5 81            [12] 1347 	mov	sp,a
                                   1348 ;	build/../bulkloop.c:163: return FALSE;
      000339 75 82 00         [24] 1349 	mov	dpl, #0x00
                                   1350 ;	build/../bulkloop.c:164: }
      00033C 22               [24] 1351 	ret
                                   1352 ;------------------------------------------------------------
                                   1353 ;Allocation info for local variables in function 'handle_get_interface'
                                   1354 ;------------------------------------------------------------
                                   1355 ;alt_ifc       Allocated with name '_handle_get_interface_PARM_2'
                                   1356 ;ifc           Allocated to registers r7 
                                   1357 ;------------------------------------------------------------
                                   1358 ;	build/../bulkloop.c:167: BOOL handle_get_interface(BYTE ifc, BYTE* alt_ifc) {
                                   1359 ;	-----------------------------------------
                                   1360 ;	 function handle_get_interface
                                   1361 ;	-----------------------------------------
      00033D                       1362 _handle_get_interface:
      00033D AF 82            [24] 1363 	mov	r7, dpl
                                   1364 ;	build/../bulkloop.c:168: printf ( "Get Interface\n" );
      00033F C0 07            [24] 1365 	push	ar7
      000341 74 9B            [12] 1366 	mov	a,#___str_6
      000343 C0 E0            [24] 1367 	push	acc
      000345 74 13            [12] 1368 	mov	a,#(___str_6 >> 8)
      000347 C0 E0            [24] 1369 	push	acc
      000349 74 80            [12] 1370 	mov	a,#0x80
      00034B C0 E0            [24] 1371 	push	acc
      00034D 12 0A A4         [24] 1372 	lcall	_printf
      000350 15 81            [12] 1373 	dec	sp
      000352 15 81            [12] 1374 	dec	sp
      000354 15 81            [12] 1375 	dec	sp
      000356 D0 07            [24] 1376 	pop	ar7
                                   1377 ;	build/../bulkloop.c:169: if (ifc==0) {*alt_ifc=0; return TRUE;} else { return FALSE;}
      000358 EF               [12] 1378 	mov	a,r7
      000359 70 14            [24] 1379 	jnz	00102$
      00035B AD 17            [24] 1380 	mov	r5,_handle_get_interface_PARM_2
      00035D AE 18            [24] 1381 	mov	r6,(_handle_get_interface_PARM_2 + 1)
      00035F AF 19            [24] 1382 	mov	r7,(_handle_get_interface_PARM_2 + 2)
      000361 8D 82            [24] 1383 	mov	dpl,r5
      000363 8E 83            [24] 1384 	mov	dph,r6
      000365 8F F0            [24] 1385 	mov	b,r7
      000367 E4               [12] 1386 	clr	a
      000368 12 09 0B         [24] 1387 	lcall	__gptrput
      00036B 75 82 01         [24] 1388 	mov	dpl, #0x01
      00036E 22               [24] 1389 	ret
      00036F                       1390 00102$:
      00036F 75 82 00         [24] 1391 	mov	dpl, #0x00
                                   1392 ;	build/../bulkloop.c:170: }
      000372 22               [24] 1393 	ret
                                   1394 ;------------------------------------------------------------
                                   1395 ;Allocation info for local variables in function 'handle_set_interface'
                                   1396 ;------------------------------------------------------------
                                   1397 ;alt_ifc       Allocated with name '_handle_set_interface_PARM_2'
                                   1398 ;ifc           Allocated to registers r7 
                                   1399 ;x             Allocated to registers 
                                   1400 ;x             Allocated to registers 
                                   1401 ;------------------------------------------------------------
                                   1402 ;	build/../bulkloop.c:171: BOOL handle_set_interface(BYTE ifc, BYTE alt_ifc) {
                                   1403 ;	-----------------------------------------
                                   1404 ;	 function handle_set_interface
                                   1405 ;	-----------------------------------------
      000373                       1406 _handle_set_interface:
      000373 AF 82            [24] 1407 	mov	r7, dpl
                                   1408 ;	build/../bulkloop.c:172: printf ( "Set interface %d to alt: %d\n" , ifc, alt_ifc );
      000375 AD 1A            [24] 1409 	mov	r5,_handle_set_interface_PARM_2
      000377 7E 00            [12] 1410 	mov	r6,#0x00
      000379 8F 03            [24] 1411 	mov	ar3,r7
      00037B 7C 00            [12] 1412 	mov	r4,#0x00
      00037D C0 07            [24] 1413 	push	ar7
      00037F C0 05            [24] 1414 	push	ar5
      000381 C0 06            [24] 1415 	push	ar6
      000383 C0 03            [24] 1416 	push	ar3
      000385 C0 04            [24] 1417 	push	ar4
      000387 74 AA            [12] 1418 	mov	a,#___str_7
      000389 C0 E0            [24] 1419 	push	acc
      00038B 74 13            [12] 1420 	mov	a,#(___str_7 >> 8)
      00038D C0 E0            [24] 1421 	push	acc
      00038F 74 80            [12] 1422 	mov	a,#0x80
      000391 C0 E0            [24] 1423 	push	acc
      000393 12 0A A4         [24] 1424 	lcall	_printf
      000396 E5 81            [12] 1425 	mov	a,sp
      000398 24 F9            [12] 1426 	add	a,#0xf9
      00039A F5 81            [12] 1427 	mov	sp,a
      00039C D0 07            [24] 1428 	pop	ar7
                                   1429 ;	build/../bulkloop.c:174: if (ifc==0&&alt_ifc==0) {
      00039E EF               [12] 1430 	mov	a,r7
      00039F 70 65            [24] 1431 	jnz	00112$
      0003A1 E5 1A            [12] 1432 	mov	a,_handle_set_interface_PARM_2
      0003A3 70 61            [24] 1433 	jnz	00112$
                                   1434 ;	build/../bulkloop.c:177: RESETTOGGLE(0x02);
      0003A5 90 E6 83         [24] 1435 	mov	dptr,#_TOGCTL
      0003A8 74 02            [12] 1436 	mov	a,#0x02
      0003AA F0               [24] 1437 	movx	@dptr,a
      0003AB 74 22            [12] 1438 	mov	a,#0x22
      0003AD F0               [24] 1439 	movx	@dptr,a
                                   1440 ;	build/../bulkloop.c:178: RESETTOGGLE(0x86);
      0003AE 74 16            [12] 1441 	mov	a,#0x16
      0003B0 F0               [24] 1442 	movx	@dptr,a
      0003B1 74 36            [12] 1443 	mov	a,#0x36
      0003B3 F0               [24] 1444 	movx	@dptr,a
                                   1445 ;	build/../bulkloop.c:180: RESETFIFO(0x02);
      0003B4 90 E6 04         [24] 1446 	mov	dptr,#_FIFORESET
      0003B7 74 80            [12] 1447 	mov	a,#0x80
      0003B9 F0               [24] 1448 	movx	@dptr,a
      0003BA 00               [12] 1449 	nop	
      0003BB 00               [12] 1450 	nop	
      0003BC 00               [12] 1451 	nop	
      0003BD 00               [12] 1452 	nop	
      0003BE 90 E6 04         [24] 1453 	mov	dptr,#_FIFORESET
      0003C1 74 82            [12] 1454 	mov	a,#0x82
      0003C3 F0               [24] 1455 	movx	@dptr,a
      0003C4 00               [12] 1456 	nop	
      0003C5 00               [12] 1457 	nop	
      0003C6 00               [12] 1458 	nop	
      0003C7 00               [12] 1459 	nop	
      0003C8 90 E6 04         [24] 1460 	mov	dptr,#_FIFORESET
      0003CB E4               [12] 1461 	clr	a
      0003CC F0               [24] 1462 	movx	@dptr,a
      0003CD 00               [12] 1463 	nop	
      0003CE 00               [12] 1464 	nop	
      0003CF 00               [12] 1465 	nop	
      0003D0 00               [12] 1466 	nop	
                                   1467 ;	build/../bulkloop.c:181: EP2BCL=0x80;
      0003D1 90 E6 91         [24] 1468 	mov	dptr,#_EP2BCL
      0003D4 74 80            [12] 1469 	mov	a,#0x80
      0003D6 F0               [24] 1470 	movx	@dptr,a
                                   1471 ;	build/../bulkloop.c:182: SYNCDELAY;
      0003D7 00               [12] 1472 	nop	
      0003D8 00               [12] 1473 	nop	
      0003D9 00               [12] 1474 	nop	
      0003DA 00               [12] 1475 	nop	
                                   1476 ;	build/../bulkloop.c:183: EP2BCL=0X80;
      0003DB 90 E6 91         [24] 1477 	mov	dptr,#_EP2BCL
      0003DE 74 80            [12] 1478 	mov	a,#0x80
      0003E0 F0               [24] 1479 	movx	@dptr,a
                                   1480 ;	build/../bulkloop.c:184: SYNCDELAY;
      0003E1 00               [12] 1481 	nop	
      0003E2 00               [12] 1482 	nop	
      0003E3 00               [12] 1483 	nop	
      0003E4 00               [12] 1484 	nop	
                                   1485 ;	build/../bulkloop.c:185: RESETFIFO(0x86);
      0003E5 90 E6 04         [24] 1486 	mov	dptr,#_FIFORESET
      0003E8 74 80            [12] 1487 	mov	a,#0x80
      0003EA F0               [24] 1488 	movx	@dptr,a
      0003EB 00               [12] 1489 	nop	
      0003EC 00               [12] 1490 	nop	
      0003ED 00               [12] 1491 	nop	
      0003EE 00               [12] 1492 	nop	
      0003EF 90 E6 04         [24] 1493 	mov	dptr,#_FIFORESET
      0003F2 74 86            [12] 1494 	mov	a,#0x86
      0003F4 F0               [24] 1495 	movx	@dptr,a
      0003F5 00               [12] 1496 	nop	
      0003F6 00               [12] 1497 	nop	
      0003F7 00               [12] 1498 	nop	
      0003F8 00               [12] 1499 	nop	
      0003F9 90 E6 04         [24] 1500 	mov	dptr,#_FIFORESET
      0003FC E4               [12] 1501 	clr	a
      0003FD F0               [24] 1502 	movx	@dptr,a
      0003FE 00               [12] 1503 	nop	
      0003FF 00               [12] 1504 	nop	
      000400 00               [12] 1505 	nop	
      000401 00               [12] 1506 	nop	
                                   1507 ;	build/../bulkloop.c:186: return TRUE;
      000402 75 82 01         [24] 1508 	mov	dpl, #0x01
      000405 22               [24] 1509 	ret
      000406                       1510 00112$:
                                   1511 ;	build/../bulkloop.c:188: return FALSE;
      000406 75 82 00         [24] 1512 	mov	dpl, #0x00
                                   1513 ;	build/../bulkloop.c:189: }
      000409 22               [24] 1514 	ret
                                   1515 ;------------------------------------------------------------
                                   1516 ;Allocation info for local variables in function 'handle_get_configuration'
                                   1517 ;------------------------------------------------------------
                                   1518 ;	build/../bulkloop.c:192: BYTE handle_get_configuration(void) {
                                   1519 ;	-----------------------------------------
                                   1520 ;	 function handle_get_configuration
                                   1521 ;	-----------------------------------------
      00040A                       1522 _handle_get_configuration:
                                   1523 ;	build/../bulkloop.c:193: return 1;
      00040A 75 82 01         [24] 1524 	mov	dpl, #0x01
                                   1525 ;	build/../bulkloop.c:194: }
      00040D 22               [24] 1526 	ret
                                   1527 ;------------------------------------------------------------
                                   1528 ;Allocation info for local variables in function 'handle_set_configuration'
                                   1529 ;------------------------------------------------------------
                                   1530 ;cfg           Allocated to registers r7 
                                   1531 ;------------------------------------------------------------
                                   1532 ;	build/../bulkloop.c:195: BOOL handle_set_configuration(BYTE cfg) {
                                   1533 ;	-----------------------------------------
                                   1534 ;	 function handle_set_configuration
                                   1535 ;	-----------------------------------------
      00040E                       1536 _handle_set_configuration:
      00040E AF 82            [24] 1537 	mov	r7, dpl
                                   1538 ;	build/../bulkloop.c:196: return cfg==1 ? TRUE : FALSE; // we only handle cfg 1
      000410 BF 01 04         [24] 1539 	cjne	r7,#0x01,00103$
      000413 7F 01            [12] 1540 	mov	r7,#0x01
      000415 80 02            [24] 1541 	sjmp	00104$
      000417                       1542 00103$:
      000417 7F 00            [12] 1543 	mov	r7,#0x00
      000419                       1544 00104$:
      000419 8F 82            [24] 1545 	mov	dpl,r7
                                   1546 ;	build/../bulkloop.c:197: }
      00041B 22               [24] 1547 	ret
                                   1548 ;------------------------------------------------------------
                                   1549 ;Allocation info for local variables in function 'sudav_isr'
                                   1550 ;------------------------------------------------------------
                                   1551 ;	build/../bulkloop.c:201: void sudav_isr(void) __interrupt (SUDAV_ISR) {
                                   1552 ;	-----------------------------------------
                                   1553 ;	 function sudav_isr
                                   1554 ;	-----------------------------------------
      00041C                       1555 _sudav_isr:
      00041C C0 E0            [24] 1556 	push	acc
      00041E C0 82            [24] 1557 	push	dpl
      000420 C0 83            [24] 1558 	push	dph
                                   1559 ;	build/../bulkloop.c:203: got_sud=TRUE;
                                   1560 ;	assignBit
      000422 D2 01            [12] 1561 	setb	_got_sud
                                   1562 ;	build/../bulkloop.c:204: CLEAR_SUDAV();
      000424 53 91 EF         [24] 1563 	anl	_EXIF,#0xef
      000427 90 E6 5D         [24] 1564 	mov	dptr,#_USBIRQ
      00042A 74 01            [12] 1565 	mov	a,#0x01
      00042C F0               [24] 1566 	movx	@dptr,a
                                   1567 ;	build/../bulkloop.c:205: }
      00042D D0 83            [24] 1568 	pop	dph
      00042F D0 82            [24] 1569 	pop	dpl
      000431 D0 E0            [24] 1570 	pop	acc
      000433 32               [24] 1571 	reti
                                   1572 ;	eliminated unneeded mov psw,# (no regs used in bank)
                                   1573 ;	eliminated unneeded push/pop not_psw
                                   1574 ;	eliminated unneeded push/pop b
                                   1575 ;------------------------------------------------------------
                                   1576 ;Allocation info for local variables in function 'sof_isr'
                                   1577 ;------------------------------------------------------------
                                   1578 ;	build/../bulkloop.c:209: void sof_isr (void) __interrupt (SOF_ISR) __using (1) {
                                   1579 ;	-----------------------------------------
                                   1580 ;	 function sof_isr
                                   1581 ;	-----------------------------------------
      000434                       1582 _sof_isr:
                           00000F  1583 	ar7 = 0x0f
                           00000E  1584 	ar6 = 0x0e
                           00000D  1585 	ar5 = 0x0d
                           00000C  1586 	ar4 = 0x0c
                           00000B  1587 	ar3 = 0x0b
                           00000A  1588 	ar2 = 0x0a
                           000009  1589 	ar1 = 0x09
                           000008  1590 	ar0 = 0x08
      000434 C0 E0            [24] 1591 	push	acc
      000436 C0 82            [24] 1592 	push	dpl
      000438 C0 83            [24] 1593 	push	dph
      00043A C0 D0            [24] 1594 	push	psw
      00043C 75 D0 08         [24] 1595 	mov	psw,#0x08
                                   1596 ;	build/../bulkloop.c:210: ++sofct;
      00043F 90 3C 00         [24] 1597 	mov	dptr,#_sofct
      000442 E0               [24] 1598 	movx	a,@dptr
      000443 24 01            [12] 1599 	add	a, #0x01
      000445 F0               [24] 1600 	movx	@dptr,a
      000446 A3               [24] 1601 	inc	dptr
      000447 E0               [24] 1602 	movx	a,@dptr
      000448 34 00            [12] 1603 	addc	a, #0x00
      00044A F0               [24] 1604 	movx	@dptr,a
                                   1605 ;	build/../bulkloop.c:211: if(sofct==8000) { // about 8000 sof interrupts per second at high speed
      00044B 90 3C 00         [24] 1606 	mov	dptr,#_sofct
      00044E E0               [24] 1607 	movx	a,@dptr
      00044F FE               [12] 1608 	mov	r6,a
      000450 A3               [24] 1609 	inc	dptr
      000451 E0               [24] 1610 	movx	a,@dptr
      000452 FF               [12] 1611 	mov	r7,a
      000453 BE 40 19         [24] 1612 	cjne	r6,#0x40,00105$
      000456 BF 1F 16         [24] 1613 	cjne	r7,#0x1f,00105$
                                   1614 ;	build/../bulkloop.c:212: on5=!on5;
      000459 B2 03            [12] 1615 	cpl	_on5
                                   1616 ;	build/../bulkloop.c:213: if (on5) {d5on();} else {d5off();}
      00045B 30 03 06         [24] 1617 	jnb	_on5,00102$
      00045E 75 92 B8         [24] 1618 	mov __XPAGE, #0xB8 
      000461 E2               [24] 1619 	movx a, @r0 
      000462 80 04            [24] 1620 	sjmp	00103$
      000464                       1621 00102$:
      000464 75 92 B0         [24] 1622 	mov __XPAGE, #0xB0 
      000467 E2               [24] 1623 	movx a, @r0 
      000468                       1624 00103$:
                                   1625 ;	build/../bulkloop.c:214: sofct=0;
      000468 90 3C 00         [24] 1626 	mov	dptr,#_sofct
      00046B E4               [12] 1627 	clr	a
      00046C F0               [24] 1628 	movx	@dptr,a
      00046D A3               [24] 1629 	inc	dptr
      00046E F0               [24] 1630 	movx	@dptr,a
      00046F                       1631 00105$:
                                   1632 ;	build/../bulkloop.c:216: CLEAR_SOF();
      00046F 53 91 EF         [24] 1633 	anl	_EXIF,#0xef
      000472 90 E6 5D         [24] 1634 	mov	dptr,#_USBIRQ
      000475 74 02            [12] 1635 	mov	a,#0x02
      000477 F0               [24] 1636 	movx	@dptr,a
                                   1637 ;	build/../bulkloop.c:217: }
      000478 D0 D0            [24] 1638 	pop	psw
      00047A D0 83            [24] 1639 	pop	dph
      00047C D0 82            [24] 1640 	pop	dpl
      00047E D0 E0            [24] 1641 	pop	acc
      000480 02 00 9E         [24] 1642 	ljmp	sdcc_atomic_maybe_rollback
                                   1643 ;	eliminated unneeded push/pop b
                                   1644 ;------------------------------------------------------------
                                   1645 ;Allocation info for local variables in function 'usbreset_isr'
                                   1646 ;------------------------------------------------------------
                                   1647 ;	build/../bulkloop.c:219: void usbreset_isr(void) __interrupt (USBRESET_ISR) {
                                   1648 ;	-----------------------------------------
                                   1649 ;	 function usbreset_isr
                                   1650 ;	-----------------------------------------
      000483                       1651 _usbreset_isr:
                           000007  1652 	ar7 = 0x07
                           000006  1653 	ar6 = 0x06
                           000005  1654 	ar5 = 0x05
                           000004  1655 	ar4 = 0x04
                           000003  1656 	ar3 = 0x03
                           000002  1657 	ar2 = 0x02
                           000001  1658 	ar1 = 0x01
                           000000  1659 	ar0 = 0x00
      000483 C0 21            [24] 1660 	push	bits
      000485 C0 E0            [24] 1661 	push	acc
      000487 C0 F0            [24] 1662 	push	b
      000489 C0 82            [24] 1663 	push	dpl
      00048B C0 83            [24] 1664 	push	dph
      00048D C0 07            [24] 1665 	push	(0+7)
      00048F C0 06            [24] 1666 	push	(0+6)
      000491 C0 05            [24] 1667 	push	(0+5)
      000493 C0 04            [24] 1668 	push	(0+4)
      000495 C0 03            [24] 1669 	push	(0+3)
      000497 C0 02            [24] 1670 	push	(0+2)
      000499 C0 01            [24] 1671 	push	(0+1)
      00049B C0 00            [24] 1672 	push	(0+0)
      00049D C0 D0            [24] 1673 	push	psw
      00049F 75 D0 00         [24] 1674 	mov	psw,#0x00
                                   1675 ;	build/../bulkloop.c:220: handle_hispeed(FALSE);
      0004A2 75 82 00         [24] 1676 	mov	dpl, #0x00
      0004A5 12 08 0F         [24] 1677 	lcall	_handle_hispeed
                                   1678 ;	build/../bulkloop.c:221: CLEAR_USBRESET();
      0004A8 53 91 EF         [24] 1679 	anl	_EXIF,#0xef
      0004AB 90 E6 5D         [24] 1680 	mov	dptr,#_USBIRQ
      0004AE 74 10            [12] 1681 	mov	a,#0x10
      0004B0 F0               [24] 1682 	movx	@dptr,a
                                   1683 ;	build/../bulkloop.c:222: }
      0004B1 D0 D0            [24] 1684 	pop	psw
      0004B3 D0 00            [24] 1685 	pop	(0+0)
      0004B5 D0 01            [24] 1686 	pop	(0+1)
      0004B7 D0 02            [24] 1687 	pop	(0+2)
      0004B9 D0 03            [24] 1688 	pop	(0+3)
      0004BB D0 04            [24] 1689 	pop	(0+4)
      0004BD D0 05            [24] 1690 	pop	(0+5)
      0004BF D0 06            [24] 1691 	pop	(0+6)
      0004C1 D0 07            [24] 1692 	pop	(0+7)
      0004C3 D0 83            [24] 1693 	pop	dph
      0004C5 D0 82            [24] 1694 	pop	dpl
      0004C7 D0 F0            [24] 1695 	pop	b
      0004C9 D0 E0            [24] 1696 	pop	acc
      0004CB D0 21            [24] 1697 	pop	bits
      0004CD 02 00 9E         [24] 1698 	ljmp	sdcc_atomic_maybe_rollback
                                   1699 ;------------------------------------------------------------
                                   1700 ;Allocation info for local variables in function 'hispeed_isr'
                                   1701 ;------------------------------------------------------------
                                   1702 ;	build/../bulkloop.c:223: void hispeed_isr(void) __interrupt (HISPEED_ISR) {
                                   1703 ;	-----------------------------------------
                                   1704 ;	 function hispeed_isr
                                   1705 ;	-----------------------------------------
      0004D0                       1706 _hispeed_isr:
      0004D0 C0 21            [24] 1707 	push	bits
      0004D2 C0 E0            [24] 1708 	push	acc
      0004D4 C0 F0            [24] 1709 	push	b
      0004D6 C0 82            [24] 1710 	push	dpl
      0004D8 C0 83            [24] 1711 	push	dph
      0004DA C0 07            [24] 1712 	push	(0+7)
      0004DC C0 06            [24] 1713 	push	(0+6)
      0004DE C0 05            [24] 1714 	push	(0+5)
      0004E0 C0 04            [24] 1715 	push	(0+4)
      0004E2 C0 03            [24] 1716 	push	(0+3)
      0004E4 C0 02            [24] 1717 	push	(0+2)
      0004E6 C0 01            [24] 1718 	push	(0+1)
      0004E8 C0 00            [24] 1719 	push	(0+0)
      0004EA C0 D0            [24] 1720 	push	psw
      0004EC 75 D0 00         [24] 1721 	mov	psw,#0x00
                                   1722 ;	build/../bulkloop.c:224: handle_hispeed(TRUE);
      0004EF 75 82 01         [24] 1723 	mov	dpl, #0x01
      0004F2 12 08 0F         [24] 1724 	lcall	_handle_hispeed
                                   1725 ;	build/../bulkloop.c:225: CLEAR_HISPEED();
      0004F5 53 91 EF         [24] 1726 	anl	_EXIF,#0xef
      0004F8 90 E6 5D         [24] 1727 	mov	dptr,#_USBIRQ
      0004FB 74 20            [12] 1728 	mov	a,#0x20
      0004FD F0               [24] 1729 	movx	@dptr,a
                                   1730 ;	build/../bulkloop.c:226: }
      0004FE D0 D0            [24] 1731 	pop	psw
      000500 D0 00            [24] 1732 	pop	(0+0)
      000502 D0 01            [24] 1733 	pop	(0+1)
      000504 D0 02            [24] 1734 	pop	(0+2)
      000506 D0 03            [24] 1735 	pop	(0+3)
      000508 D0 04            [24] 1736 	pop	(0+4)
      00050A D0 05            [24] 1737 	pop	(0+5)
      00050C D0 06            [24] 1738 	pop	(0+6)
      00050E D0 07            [24] 1739 	pop	(0+7)
      000510 D0 83            [24] 1740 	pop	dph
      000512 D0 82            [24] 1741 	pop	dpl
      000514 D0 F0            [24] 1742 	pop	b
      000516 D0 E0            [24] 1743 	pop	acc
      000518 D0 21            [24] 1744 	pop	bits
      00051A 02 00 9E         [24] 1745 	ljmp	sdcc_atomic_maybe_rollback
                                   1746 	.area CSEG    (CODE)
                                   1747 	.area CONST   (CODE)
                                   1748 	.area CONST   (CODE)
      001310                       1749 ___str_0:
      001310 44 6F 6E 65 20 69 6E  1750 	.ascii "Done initializing stuff"
             69 74 69 61 6C 69 7A
             69 6E 67 20 73 74 75
             66 66
      001327 0A                    1751 	.db 0x0a
      001328 00                    1752 	.db 0x00
                                   1753 	.area CSEG    (CODE)
                                   1754 	.area CONST   (CODE)
      001329                       1755 ___str_1:
      001329 48 61 6E 64 6C 65 20  1756 	.ascii "Handle setupdata"
             73 65 74 75 70 64 61
             74 61
      001339 0A                    1757 	.db 0x0a
      00133A 00                    1758 	.db 0x00
                                   1759 	.area CSEG    (CODE)
                                   1760 	.area CONST   (CODE)
      00133B                       1761 ___str_2:
      00133B 65 70 32 20 6F 75 74  1762 	.ascii "ep2 out received data"
             20 72 65 63 65 69 76
             65 64 20 64 61 74 61
      001350 0A                    1763 	.db 0x0a
      001351 00                    1764 	.db 0x00
                                   1765 	.area CSEG    (CODE)
                                   1766 	.area CONST   (CODE)
      001352                       1767 ___str_3:
      001352 53 65 6E 64 69 6E 67  1768 	.ascii "Sending data to ep6 in"
             20 64 61 74 61 20 74
             6F 20 65 70 36 20 69
             6E
      001368 0A                    1769 	.db 0x0a
      001369 00                    1770 	.db 0x00
                                   1771 	.area CSEG    (CODE)
                                   1772 	.area CONST   (CODE)
      00136A                       1773 ___str_4:
      00136A 65 70 20 25 30 32 78  1774 	.ascii "ep %02x"
      001371 0A                    1775 	.db 0x0a
      001372 00                    1776 	.db 0x00
                                   1777 	.area CSEG    (CODE)
                                   1778 	.area CONST   (CODE)
      001373                       1779 ___str_5:
      001373 4E 65 65 64 20 74 6F  1780 	.ascii "Need to implement vendor command: %02x"
             20 69 6D 70 6C 65 6D
             65 6E 74 20 76 65 6E
             64 6F 72 20 63 6F 6D
             6D 61 6E 64 3A 20 25
             30 32 78
      001399 0A                    1781 	.db 0x0a
      00139A 00                    1782 	.db 0x00
                                   1783 	.area CSEG    (CODE)
                                   1784 	.area CONST   (CODE)
      00139B                       1785 ___str_6:
      00139B 47 65 74 20 49 6E 74  1786 	.ascii "Get Interface"
             65 72 66 61 63 65
      0013A8 0A                    1787 	.db 0x0a
      0013A9 00                    1788 	.db 0x00
                                   1789 	.area CSEG    (CODE)
                                   1790 	.area CONST   (CODE)
      0013AA                       1791 ___str_7:
      0013AA 53 65 74 20 69 6E 74  1792 	.ascii "Set interface %d to alt: %d"
             65 72 66 61 63 65 20
             25 64 20 74 6F 20 61
             6C 74 3A 20 25 64
      0013C5 0A                    1793 	.db 0x0a
      0013C6 00                    1794 	.db 0x00
                                   1795 	.area CSEG    (CODE)
                                   1796 	.area XINIT   (CODE)
      0013D2                       1797 __xinit__sofct:
      0013D2 00 00                 1798 	.byte #0x00, #0x00	; 0
                                   1799 	.area CABS    (ABS,CODE)
