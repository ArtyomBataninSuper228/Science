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
      000161 12 0A 30         [24] 1011 	lcall	_delay
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
      000183 12 09 43         [24] 1031 	lcall	_sio0_init
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
                                   1059 ;	build/../bulkloop.c:72: IFCONFIG = 0xEB;
      0001B0 90 E6 01         [24] 1060 	mov	dptr,#_IFCONFIG
      0001B3 74 EB            [12] 1061 	mov	a,#0xeb
      0001B5 F0               [24] 1062 	movx	@dptr,a
                                   1063 ;	build/../bulkloop.c:73: EP2CFG = 0xA2; // 10100010
      0001B6 90 E6 12         [24] 1064 	mov	dptr,#_EP2CFG
      0001B9 74 A2            [12] 1065 	mov	a,#0xa2
      0001BB F0               [24] 1066 	movx	@dptr,a
                                   1067 ;	build/../bulkloop.c:74: SYNCDELAY;
      0001BC 00               [12] 1068 	nop	
      0001BD 00               [12] 1069 	nop	
      0001BE 00               [12] 1070 	nop	
      0001BF 00               [12] 1071 	nop	
                                   1072 ;	build/../bulkloop.c:75: EP6CFG = 0xE2; // 11100010
      0001C0 90 E6 14         [24] 1073 	mov	dptr,#_EP6CFG
      0001C3 74 E2            [12] 1074 	mov	a,#0xe2
      0001C5 F0               [24] 1075 	movx	@dptr,a
                                   1076 ;	build/../bulkloop.c:76: SYNCDELAY;
      0001C6 00               [12] 1077 	nop	
      0001C7 00               [12] 1078 	nop	
      0001C8 00               [12] 1079 	nop	
      0001C9 00               [12] 1080 	nop	
                                   1081 ;	build/../bulkloop.c:77: EP1INCFG &= ~bmVALID;
      0001CA 90 E6 11         [24] 1082 	mov	dptr,#_EP1INCFG
      0001CD E0               [24] 1083 	movx	a,@dptr
      0001CE 53 E0 7F         [24] 1084 	anl	acc,#0x7f
      0001D1 F0               [24] 1085 	movx	@dptr,a
                                   1086 ;	build/../bulkloop.c:78: SYNCDELAY;
      0001D2 00               [12] 1087 	nop	
      0001D3 00               [12] 1088 	nop	
      0001D4 00               [12] 1089 	nop	
      0001D5 00               [12] 1090 	nop	
                                   1091 ;	build/../bulkloop.c:79: EP1OUTCFG &= ~bmVALID;
      0001D6 90 E6 10         [24] 1092 	mov	dptr,#_EP1OUTCFG
      0001D9 E0               [24] 1093 	movx	a,@dptr
      0001DA 53 E0 7F         [24] 1094 	anl	acc,#0x7f
      0001DD F0               [24] 1095 	movx	@dptr,a
                                   1096 ;	build/../bulkloop.c:80: SYNCDELAY;
      0001DE 00               [12] 1097 	nop	
      0001DF 00               [12] 1098 	nop	
      0001E0 00               [12] 1099 	nop	
      0001E1 00               [12] 1100 	nop	
                                   1101 ;	build/../bulkloop.c:81: EP4CFG &= ~bmVALID;
      0001E2 90 E6 13         [24] 1102 	mov	dptr,#_EP4CFG
      0001E5 E0               [24] 1103 	movx	a,@dptr
      0001E6 53 E0 7F         [24] 1104 	anl	acc,#0x7f
      0001E9 F0               [24] 1105 	movx	@dptr,a
                                   1106 ;	build/../bulkloop.c:82: SYNCDELAY;
      0001EA 00               [12] 1107 	nop	
      0001EB 00               [12] 1108 	nop	
      0001EC 00               [12] 1109 	nop	
      0001ED 00               [12] 1110 	nop	
                                   1111 ;	build/../bulkloop.c:83: EP8CFG &= ~bmVALID;
      0001EE 90 E6 15         [24] 1112 	mov	dptr,#_EP8CFG
      0001F1 E0               [24] 1113 	movx	a,@dptr
      0001F2 53 E0 7F         [24] 1114 	anl	acc,#0x7f
      0001F5 F0               [24] 1115 	movx	@dptr,a
                                   1116 ;	build/../bulkloop.c:84: SYNCDELAY;
      0001F6 00               [12] 1117 	nop	
      0001F7 00               [12] 1118 	nop	
      0001F8 00               [12] 1119 	nop	
      0001F9 00               [12] 1120 	nop	
                                   1121 ;	build/../bulkloop.c:88: EP2BCL = 0x80; // write once
      0001FA 90 E6 91         [24] 1122 	mov	dptr,#_EP2BCL
      0001FD 74 80            [12] 1123 	mov	a,#0x80
      0001FF F0               [24] 1124 	movx	@dptr,a
                                   1125 ;	build/../bulkloop.c:89: SYNCDELAY;
      000200 00               [12] 1126 	nop	
      000201 00               [12] 1127 	nop	
      000202 00               [12] 1128 	nop	
      000203 00               [12] 1129 	nop	
                                   1130 ;	build/../bulkloop.c:90: EP2BCL = 0x80; // do it again
      000204 90 E6 91         [24] 1131 	mov	dptr,#_EP2BCL
      000207 74 80            [12] 1132 	mov	a,#0x80
      000209 F0               [24] 1133 	movx	@dptr,a
                                   1134 ;	build/../bulkloop.c:96: EA=1; // global interrupt enable
                                   1135 ;	assignBit
      00020A D2 AF            [12] 1136 	setb	_EA
                                   1137 ;	build/../bulkloop.c:97: printf ( "Done initializing stuff\n" );
      00020C 74 16            [12] 1138 	mov	a,#___str_0
      00020E C0 E0            [24] 1139 	push	acc
      000210 74 13            [12] 1140 	mov	a,#(___str_0 >> 8)
      000212 C0 E0            [24] 1141 	push	acc
      000214 74 80            [12] 1142 	mov	a,#0x80
      000216 C0 E0            [24] 1143 	push	acc
      000218 12 0A AA         [24] 1144 	lcall	_printf
      00021B 15 81            [12] 1145 	dec	sp
      00021D 15 81            [12] 1146 	dec	sp
      00021F 15 81            [12] 1147 	dec	sp
                                   1148 ;	build/../bulkloop.c:100: d3off();
      000221 75 92 90         [24] 1149 	mov __XPAGE, #0x90 
      000224 E2               [24] 1150 	movx a, @r0 
                                   1151 ;	build/../bulkloop.c:102: while(TRUE) {
      000225                       1152 00109$:
                                   1153 ;	build/../bulkloop.c:104: if ( got_sud ) {
      000225 30 01 1A         [24] 1154 	jnb	_got_sud,00102$
                                   1155 ;	build/../bulkloop.c:105: printf ( "Handle setupdata\n" );
      000228 74 2F            [12] 1156 	mov	a,#___str_1
      00022A C0 E0            [24] 1157 	push	acc
      00022C 74 13            [12] 1158 	mov	a,#(___str_1 >> 8)
      00022E C0 E0            [24] 1159 	push	acc
      000230 74 80            [12] 1160 	mov	a,#0x80
      000232 C0 E0            [24] 1161 	push	acc
      000234 12 0A AA         [24] 1162 	lcall	_printf
      000237 15 81            [12] 1163 	dec	sp
      000239 15 81            [12] 1164 	dec	sp
      00023B 15 81            [12] 1165 	dec	sp
                                   1166 ;	build/../bulkloop.c:106: handle_setupdata();
      00023D 12 05 23         [24] 1167 	lcall	_handle_setupdata
                                   1168 ;	build/../bulkloop.c:107: got_sud=FALSE;
                                   1169 ;	assignBit
      000240 C2 01            [12] 1170 	clr	_got_sud
      000242                       1171 00102$:
                                   1172 ;	build/../bulkloop.c:110: if ( !(EP2468STAT & bmEP2EMPTY) ) {
      000242 E5 AA            [12] 1173 	mov	a,_EP2468STAT
      000244 20 E0 DE         [24] 1174 	jb	acc.0,00109$
                                   1175 ;	build/../bulkloop.c:111: printf ( "ep2 out received data\n" );
      000247 74 41            [12] 1176 	mov	a,#___str_2
      000249 C0 E0            [24] 1177 	push	acc
      00024B 74 13            [12] 1178 	mov	a,#(___str_2 >> 8)
      00024D C0 E0            [24] 1179 	push	acc
      00024F 74 80            [12] 1180 	mov	a,#0x80
      000251 C0 E0            [24] 1181 	push	acc
      000253 12 0A AA         [24] 1182 	lcall	_printf
      000256 15 81            [12] 1183 	dec	sp
      000258 15 81            [12] 1184 	dec	sp
      00025A 15 81            [12] 1185 	dec	sp
                                   1186 ;	build/../bulkloop.c:112: if  ( !(EP2468STAT & bmEP6FULL) ) { // wait for at least one empty in buffer
      00025C E5 AA            [12] 1187 	mov	a,_EP2468STAT
      00025E 20 E5 C4         [24] 1188 	jb	acc.5,00109$
                                   1189 ;	build/../bulkloop.c:114: printf ( "Sending data to ep6 in\n");
      000261 74 58            [12] 1190 	mov	a,#___str_3
      000263 C0 E0            [24] 1191 	push	acc
      000265 74 13            [12] 1192 	mov	a,#(___str_3 >> 8)
      000267 C0 E0            [24] 1193 	push	acc
      000269 74 80            [12] 1194 	mov	a,#0x80
      00026B C0 E0            [24] 1195 	push	acc
      00026D 12 0A AA         [24] 1196 	lcall	_printf
      000270 15 81            [12] 1197 	dec	sp
      000272 15 81            [12] 1198 	dec	sp
      000274 15 81            [12] 1199 	dec	sp
                                   1200 ;	build/../bulkloop.c:116: bytes = MAKEWORD(EP2BCH,EP2BCL);
      000276 90 E6 90         [24] 1201 	mov	dptr,#_EP2BCH
      000279 E0               [24] 1202 	movx	a,@dptr
      00027A FF               [12] 1203 	mov	r7,a
      00027B 7E 00            [12] 1204 	mov	r6,#0x00
      00027D 90 E6 91         [24] 1205 	mov	dptr,#_EP2BCL
      000280 E0               [24] 1206 	movx	a,@dptr
      000281 FC               [12] 1207 	mov	r4,a
      000282 7D 00            [12] 1208 	mov	r5,#0x00
      000284 4E               [12] 1209 	orl	a,r6
      000285 F5 10            [12] 1210 	mov	_bytes,a
      000287 ED               [12] 1211 	mov	a,r5
      000288 4F               [12] 1212 	orl	a,r7
      000289 F5 11            [12] 1213 	mov	(_bytes + 1),a
                                   1214 ;	build/../bulkloop.c:118: for (i=0;i<bytes;++i) EP6FIFOBUF[i] = EP2FIFOBUF[i];
      00028B 7F 00            [12] 1215 	mov	r7,#0x00
      00028D                       1216 00112$:
      00028D C3               [12] 1217 	clr	c
      00028E EE               [12] 1218 	mov	a,r6
      00028F 95 10            [12] 1219 	subb	a,_bytes
      000291 EF               [12] 1220 	mov	a,r7
      000292 95 11            [12] 1221 	subb	a,(_bytes + 1)
      000294 50 1B            [24] 1222 	jnc	00103$
      000296 8E 04            [24] 1223 	mov	ar4,r6
      000298 74 F8            [12] 1224 	mov	a,#(_EP6FIFOBUF >> 8)
      00029A 2F               [12] 1225 	add	a,r7
      00029B FD               [12] 1226 	mov	r5,a
      00029C 8E 82            [24] 1227 	mov	dpl,r6
      00029E 74 F0            [12] 1228 	mov	a,#(_EP2FIFOBUF >> 8)
      0002A0 2F               [12] 1229 	add	a,r7
      0002A1 F5 83            [12] 1230 	mov	dph,a
      0002A3 E0               [24] 1231 	movx	a,@dptr
      0002A4 FB               [12] 1232 	mov	r3,a
      0002A5 8C 82            [24] 1233 	mov	dpl,r4
      0002A7 8D 83            [24] 1234 	mov	dph,r5
      0002A9 F0               [24] 1235 	movx	@dptr,a
      0002AA 0E               [12] 1236 	inc	r6
      0002AB BE 00 DF         [24] 1237 	cjne	r6,#0x00,00112$
      0002AE 0F               [12] 1238 	inc	r7
      0002AF 80 DC            [24] 1239 	sjmp	00112$
      0002B1                       1240 00103$:
                                   1241 ;	build/../bulkloop.c:124: EP6BCH=MSB(bytes);
      0002B1 90 E6 98         [24] 1242 	mov	dptr,#_EP6BCH
      0002B4 E5 11            [12] 1243 	mov	a,(_bytes + 1)
      0002B6 F0               [24] 1244 	movx	@dptr,a
                                   1245 ;	build/../bulkloop.c:125: SYNCDELAY;
      0002B7 00               [12] 1246 	nop	
      0002B8 00               [12] 1247 	nop	
      0002B9 00               [12] 1248 	nop	
      0002BA 00               [12] 1249 	nop	
                                   1250 ;	build/../bulkloop.c:126: EP6BCL=LSB(bytes);
      0002BB 90 E6 99         [24] 1251 	mov	dptr,#_EP6BCL
      0002BE E5 10            [12] 1252 	mov	a,_bytes
      0002C0 F0               [24] 1253 	movx	@dptr,a
                                   1254 ;	build/../bulkloop.c:128: REARM(); // ep2
      0002C1 90 E6 91         [24] 1255 	mov	dptr,#_EP2BCL
      0002C4 74 80            [12] 1256 	mov	a,#0x80
      0002C6 F0               [24] 1257 	movx	@dptr,a
                                   1258 ;	build/../bulkloop.c:135: }
      0002C7 02 02 25         [24] 1259 	ljmp	00109$
                                   1260 ;------------------------------------------------------------
                                   1261 ;Allocation info for local variables in function 'handle_get_descriptor'
                                   1262 ;------------------------------------------------------------
                                   1263 ;	build/../bulkloop.c:139: BOOL handle_get_descriptor(void) {
                                   1264 ;	-----------------------------------------
                                   1265 ;	 function handle_get_descriptor
                                   1266 ;	-----------------------------------------
      0002CA                       1267 _handle_get_descriptor:
                                   1268 ;	build/../bulkloop.c:140: return FALSE;
      0002CA 75 82 00         [24] 1269 	mov	dpl, #0x00
                                   1270 ;	build/../bulkloop.c:141: }
      0002CD 22               [24] 1271 	ret
                                   1272 ;------------------------------------------------------------
                                   1273 ;Allocation info for local variables in function 'handle_vendorcommand'
                                   1274 ;------------------------------------------------------------
                                   1275 ;cmd           Allocated to registers r7 
                                   1276 ;pep           Allocated to registers r5 r6 
                                   1277 ;------------------------------------------------------------
                                   1278 ;	build/../bulkloop.c:146: BOOL handle_vendorcommand(BYTE cmd) {
                                   1279 ;	-----------------------------------------
                                   1280 ;	 function handle_vendorcommand
                                   1281 ;	-----------------------------------------
      0002CE                       1282 _handle_vendorcommand:
      0002CE AF 82            [24] 1283 	mov	r7, dpl
                                   1284 ;	build/../bulkloop.c:148: switch ( cmd ) {
      0002D0 BF B1 51         [24] 1285 	cjne	r7,#0xb1,00104$
                                   1286 ;	build/../bulkloop.c:152: __xdata BYTE* pep= ep_addr(SETUPDAT[2]);
      0002D3 90 E6 BA         [24] 1287 	mov	dptr,#(_SETUPDAT + 0x0002)
      0002D6 E0               [24] 1288 	movx	a,@dptr
      0002D7 F5 82            [12] 1289 	mov	dpl,a
      0002D9 C0 07            [24] 1290 	push	ar7
      0002DB 12 06 41         [24] 1291 	lcall	_ep_addr
                                   1292 ;	build/../bulkloop.c:153: printf ( "ep %02x\n" , *pep );
      0002DE AD 82            [24] 1293 	mov	r5,dpl
      0002E0 AE 83            [24] 1294 	mov  r6,dph
      0002E2 E0               [24] 1295 	movx	a,@dptr
      0002E3 FC               [12] 1296 	mov	r4,a
      0002E4 7B 00            [12] 1297 	mov	r3,#0x00
      0002E6 C0 06            [24] 1298 	push	ar6
      0002E8 C0 05            [24] 1299 	push	ar5
      0002EA C0 04            [24] 1300 	push	ar4
      0002EC C0 03            [24] 1301 	push	ar3
      0002EE 74 70            [12] 1302 	mov	a,#___str_4
      0002F0 C0 E0            [24] 1303 	push	acc
      0002F2 74 13            [12] 1304 	mov	a,#(___str_4 >> 8)
      0002F4 C0 E0            [24] 1305 	push	acc
      0002F6 74 80            [12] 1306 	mov	a,#0x80
      0002F8 C0 E0            [24] 1307 	push	acc
      0002FA 12 0A AA         [24] 1308 	lcall	_printf
      0002FD E5 81            [12] 1309 	mov	a,sp
      0002FF 24 FB            [12] 1310 	add	a,#0xfb
      000301 F5 81            [12] 1311 	mov	sp,a
      000303 D0 05            [24] 1312 	pop	ar5
      000305 D0 06            [24] 1313 	pop	ar6
      000307 D0 07            [24] 1314 	pop	ar7
                                   1315 ;	build/../bulkloop.c:154: if (pep) {
      000309 ED               [12] 1316 	mov	a,r5
      00030A 4E               [12] 1317 	orl	a,r6
      00030B 60 17            [24] 1318 	jz	00104$
                                   1319 ;	build/../bulkloop.c:155: EP0BUF[0] = *pep;
      00030D 8D 82            [24] 1320 	mov	dpl,r5
      00030F 8E 83            [24] 1321 	mov	dph,r6
      000311 E0               [24] 1322 	movx	a,@dptr
      000312 90 E7 40         [24] 1323 	mov	dptr,#_EP0BUF
      000315 F0               [24] 1324 	movx	@dptr,a
                                   1325 ;	build/../bulkloop.c:156: EP0BCH=0;
      000316 90 E6 8A         [24] 1326 	mov	dptr,#_EP0BCH
      000319 E4               [12] 1327 	clr	a
      00031A F0               [24] 1328 	movx	@dptr,a
                                   1329 ;	build/../bulkloop.c:157: EP0BCL=1;
      00031B 90 E6 8B         [24] 1330 	mov	dptr,#_EP0BCL
      00031E 04               [12] 1331 	inc	a
      00031F F0               [24] 1332 	movx	@dptr,a
                                   1333 ;	build/../bulkloop.c:158: return TRUE;
      000320 75 82 01         [24] 1334 	mov	dpl, #0x01
                                   1335 ;	build/../bulkloop.c:161: default:
      000323 22               [24] 1336 	ret
      000324                       1337 00104$:
                                   1338 ;	build/../bulkloop.c:162: printf ( "Need to implement vendor command: %02x\n", cmd );
      000324 7E 00            [12] 1339 	mov	r6,#0x00
      000326 C0 07            [24] 1340 	push	ar7
      000328 C0 06            [24] 1341 	push	ar6
      00032A 74 79            [12] 1342 	mov	a,#___str_5
      00032C C0 E0            [24] 1343 	push	acc
      00032E 74 13            [12] 1344 	mov	a,#(___str_5 >> 8)
      000330 C0 E0            [24] 1345 	push	acc
      000332 74 80            [12] 1346 	mov	a,#0x80
      000334 C0 E0            [24] 1347 	push	acc
      000336 12 0A AA         [24] 1348 	lcall	_printf
      000339 E5 81            [12] 1349 	mov	a,sp
      00033B 24 FB            [12] 1350 	add	a,#0xfb
      00033D F5 81            [12] 1351 	mov	sp,a
                                   1352 ;	build/../bulkloop.c:164: return FALSE;
      00033F 75 82 00         [24] 1353 	mov	dpl, #0x00
                                   1354 ;	build/../bulkloop.c:165: }
      000342 22               [24] 1355 	ret
                                   1356 ;------------------------------------------------------------
                                   1357 ;Allocation info for local variables in function 'handle_get_interface'
                                   1358 ;------------------------------------------------------------
                                   1359 ;alt_ifc       Allocated with name '_handle_get_interface_PARM_2'
                                   1360 ;ifc           Allocated to registers r7 
                                   1361 ;------------------------------------------------------------
                                   1362 ;	build/../bulkloop.c:168: BOOL handle_get_interface(BYTE ifc, BYTE* alt_ifc) {
                                   1363 ;	-----------------------------------------
                                   1364 ;	 function handle_get_interface
                                   1365 ;	-----------------------------------------
      000343                       1366 _handle_get_interface:
      000343 AF 82            [24] 1367 	mov	r7, dpl
                                   1368 ;	build/../bulkloop.c:169: printf ( "Get Interface\n" );
      000345 C0 07            [24] 1369 	push	ar7
      000347 74 A1            [12] 1370 	mov	a,#___str_6
      000349 C0 E0            [24] 1371 	push	acc
      00034B 74 13            [12] 1372 	mov	a,#(___str_6 >> 8)
      00034D C0 E0            [24] 1373 	push	acc
      00034F 74 80            [12] 1374 	mov	a,#0x80
      000351 C0 E0            [24] 1375 	push	acc
      000353 12 0A AA         [24] 1376 	lcall	_printf
      000356 15 81            [12] 1377 	dec	sp
      000358 15 81            [12] 1378 	dec	sp
      00035A 15 81            [12] 1379 	dec	sp
      00035C D0 07            [24] 1380 	pop	ar7
                                   1381 ;	build/../bulkloop.c:170: if (ifc==0) {*alt_ifc=0; return TRUE;} else { return FALSE;}
      00035E EF               [12] 1382 	mov	a,r7
      00035F 70 14            [24] 1383 	jnz	00102$
      000361 AD 17            [24] 1384 	mov	r5,_handle_get_interface_PARM_2
      000363 AE 18            [24] 1385 	mov	r6,(_handle_get_interface_PARM_2 + 1)
      000365 AF 19            [24] 1386 	mov	r7,(_handle_get_interface_PARM_2 + 2)
      000367 8D 82            [24] 1387 	mov	dpl,r5
      000369 8E 83            [24] 1388 	mov	dph,r6
      00036B 8F F0            [24] 1389 	mov	b,r7
      00036D E4               [12] 1390 	clr	a
      00036E 12 09 11         [24] 1391 	lcall	__gptrput
      000371 75 82 01         [24] 1392 	mov	dpl, #0x01
      000374 22               [24] 1393 	ret
      000375                       1394 00102$:
      000375 75 82 00         [24] 1395 	mov	dpl, #0x00
                                   1396 ;	build/../bulkloop.c:171: }
      000378 22               [24] 1397 	ret
                                   1398 ;------------------------------------------------------------
                                   1399 ;Allocation info for local variables in function 'handle_set_interface'
                                   1400 ;------------------------------------------------------------
                                   1401 ;alt_ifc       Allocated with name '_handle_set_interface_PARM_2'
                                   1402 ;ifc           Allocated to registers r7 
                                   1403 ;x             Allocated to registers 
                                   1404 ;x             Allocated to registers 
                                   1405 ;------------------------------------------------------------
                                   1406 ;	build/../bulkloop.c:172: BOOL handle_set_interface(BYTE ifc, BYTE alt_ifc) {
                                   1407 ;	-----------------------------------------
                                   1408 ;	 function handle_set_interface
                                   1409 ;	-----------------------------------------
      000379                       1410 _handle_set_interface:
      000379 AF 82            [24] 1411 	mov	r7, dpl
                                   1412 ;	build/../bulkloop.c:173: printf ( "Set interface %d to alt: %d\n" , ifc, alt_ifc );
      00037B AD 1A            [24] 1413 	mov	r5,_handle_set_interface_PARM_2
      00037D 7E 00            [12] 1414 	mov	r6,#0x00
      00037F 8F 03            [24] 1415 	mov	ar3,r7
      000381 7C 00            [12] 1416 	mov	r4,#0x00
      000383 C0 07            [24] 1417 	push	ar7
      000385 C0 05            [24] 1418 	push	ar5
      000387 C0 06            [24] 1419 	push	ar6
      000389 C0 03            [24] 1420 	push	ar3
      00038B C0 04            [24] 1421 	push	ar4
      00038D 74 B0            [12] 1422 	mov	a,#___str_7
      00038F C0 E0            [24] 1423 	push	acc
      000391 74 13            [12] 1424 	mov	a,#(___str_7 >> 8)
      000393 C0 E0            [24] 1425 	push	acc
      000395 74 80            [12] 1426 	mov	a,#0x80
      000397 C0 E0            [24] 1427 	push	acc
      000399 12 0A AA         [24] 1428 	lcall	_printf
      00039C E5 81            [12] 1429 	mov	a,sp
      00039E 24 F9            [12] 1430 	add	a,#0xf9
      0003A0 F5 81            [12] 1431 	mov	sp,a
      0003A2 D0 07            [24] 1432 	pop	ar7
                                   1433 ;	build/../bulkloop.c:175: if (ifc==0&&alt_ifc==0) {
      0003A4 EF               [12] 1434 	mov	a,r7
      0003A5 70 65            [24] 1435 	jnz	00112$
      0003A7 E5 1A            [12] 1436 	mov	a,_handle_set_interface_PARM_2
      0003A9 70 61            [24] 1437 	jnz	00112$
                                   1438 ;	build/../bulkloop.c:178: RESETTOGGLE(0x02);
      0003AB 90 E6 83         [24] 1439 	mov	dptr,#_TOGCTL
      0003AE 74 02            [12] 1440 	mov	a,#0x02
      0003B0 F0               [24] 1441 	movx	@dptr,a
      0003B1 74 22            [12] 1442 	mov	a,#0x22
      0003B3 F0               [24] 1443 	movx	@dptr,a
                                   1444 ;	build/../bulkloop.c:179: RESETTOGGLE(0x86);
      0003B4 74 16            [12] 1445 	mov	a,#0x16
      0003B6 F0               [24] 1446 	movx	@dptr,a
      0003B7 74 36            [12] 1447 	mov	a,#0x36
      0003B9 F0               [24] 1448 	movx	@dptr,a
                                   1449 ;	build/../bulkloop.c:181: RESETFIFO(0x02);
      0003BA 90 E6 04         [24] 1450 	mov	dptr,#_FIFORESET
      0003BD 74 80            [12] 1451 	mov	a,#0x80
      0003BF F0               [24] 1452 	movx	@dptr,a
      0003C0 00               [12] 1453 	nop	
      0003C1 00               [12] 1454 	nop	
      0003C2 00               [12] 1455 	nop	
      0003C3 00               [12] 1456 	nop	
      0003C4 90 E6 04         [24] 1457 	mov	dptr,#_FIFORESET
      0003C7 74 82            [12] 1458 	mov	a,#0x82
      0003C9 F0               [24] 1459 	movx	@dptr,a
      0003CA 00               [12] 1460 	nop	
      0003CB 00               [12] 1461 	nop	
      0003CC 00               [12] 1462 	nop	
      0003CD 00               [12] 1463 	nop	
      0003CE 90 E6 04         [24] 1464 	mov	dptr,#_FIFORESET
      0003D1 E4               [12] 1465 	clr	a
      0003D2 F0               [24] 1466 	movx	@dptr,a
      0003D3 00               [12] 1467 	nop	
      0003D4 00               [12] 1468 	nop	
      0003D5 00               [12] 1469 	nop	
      0003D6 00               [12] 1470 	nop	
                                   1471 ;	build/../bulkloop.c:182: EP2BCL=0x80;
      0003D7 90 E6 91         [24] 1472 	mov	dptr,#_EP2BCL
      0003DA 74 80            [12] 1473 	mov	a,#0x80
      0003DC F0               [24] 1474 	movx	@dptr,a
                                   1475 ;	build/../bulkloop.c:183: SYNCDELAY;
      0003DD 00               [12] 1476 	nop	
      0003DE 00               [12] 1477 	nop	
      0003DF 00               [12] 1478 	nop	
      0003E0 00               [12] 1479 	nop	
                                   1480 ;	build/../bulkloop.c:184: EP2BCL=0X80;
      0003E1 90 E6 91         [24] 1481 	mov	dptr,#_EP2BCL
      0003E4 74 80            [12] 1482 	mov	a,#0x80
      0003E6 F0               [24] 1483 	movx	@dptr,a
                                   1484 ;	build/../bulkloop.c:185: SYNCDELAY;
      0003E7 00               [12] 1485 	nop	
      0003E8 00               [12] 1486 	nop	
      0003E9 00               [12] 1487 	nop	
      0003EA 00               [12] 1488 	nop	
                                   1489 ;	build/../bulkloop.c:186: RESETFIFO(0x86);
      0003EB 90 E6 04         [24] 1490 	mov	dptr,#_FIFORESET
      0003EE 74 80            [12] 1491 	mov	a,#0x80
      0003F0 F0               [24] 1492 	movx	@dptr,a
      0003F1 00               [12] 1493 	nop	
      0003F2 00               [12] 1494 	nop	
      0003F3 00               [12] 1495 	nop	
      0003F4 00               [12] 1496 	nop	
      0003F5 90 E6 04         [24] 1497 	mov	dptr,#_FIFORESET
      0003F8 74 86            [12] 1498 	mov	a,#0x86
      0003FA F0               [24] 1499 	movx	@dptr,a
      0003FB 00               [12] 1500 	nop	
      0003FC 00               [12] 1501 	nop	
      0003FD 00               [12] 1502 	nop	
      0003FE 00               [12] 1503 	nop	
      0003FF 90 E6 04         [24] 1504 	mov	dptr,#_FIFORESET
      000402 E4               [12] 1505 	clr	a
      000403 F0               [24] 1506 	movx	@dptr,a
      000404 00               [12] 1507 	nop	
      000405 00               [12] 1508 	nop	
      000406 00               [12] 1509 	nop	
      000407 00               [12] 1510 	nop	
                                   1511 ;	build/../bulkloop.c:188: return TRUE;
      000408 75 82 01         [24] 1512 	mov	dpl, #0x01
      00040B 22               [24] 1513 	ret
      00040C                       1514 00112$:
                                   1515 ;	build/../bulkloop.c:190: return FALSE;
      00040C 75 82 00         [24] 1516 	mov	dpl, #0x00
                                   1517 ;	build/../bulkloop.c:191: }
      00040F 22               [24] 1518 	ret
                                   1519 ;------------------------------------------------------------
                                   1520 ;Allocation info for local variables in function 'handle_get_configuration'
                                   1521 ;------------------------------------------------------------
                                   1522 ;	build/../bulkloop.c:194: BYTE handle_get_configuration(void) {
                                   1523 ;	-----------------------------------------
                                   1524 ;	 function handle_get_configuration
                                   1525 ;	-----------------------------------------
      000410                       1526 _handle_get_configuration:
                                   1527 ;	build/../bulkloop.c:195: return 1;
      000410 75 82 01         [24] 1528 	mov	dpl, #0x01
                                   1529 ;	build/../bulkloop.c:196: }
      000413 22               [24] 1530 	ret
                                   1531 ;------------------------------------------------------------
                                   1532 ;Allocation info for local variables in function 'handle_set_configuration'
                                   1533 ;------------------------------------------------------------
                                   1534 ;cfg           Allocated to registers r7 
                                   1535 ;------------------------------------------------------------
                                   1536 ;	build/../bulkloop.c:197: BOOL handle_set_configuration(BYTE cfg) {
                                   1537 ;	-----------------------------------------
                                   1538 ;	 function handle_set_configuration
                                   1539 ;	-----------------------------------------
      000414                       1540 _handle_set_configuration:
      000414 AF 82            [24] 1541 	mov	r7, dpl
                                   1542 ;	build/../bulkloop.c:198: return cfg==1 ? TRUE : FALSE; // we only handle cfg 1
      000416 BF 01 04         [24] 1543 	cjne	r7,#0x01,00103$
      000419 7F 01            [12] 1544 	mov	r7,#0x01
      00041B 80 02            [24] 1545 	sjmp	00104$
      00041D                       1546 00103$:
      00041D 7F 00            [12] 1547 	mov	r7,#0x00
      00041F                       1548 00104$:
      00041F 8F 82            [24] 1549 	mov	dpl,r7
                                   1550 ;	build/../bulkloop.c:199: }
      000421 22               [24] 1551 	ret
                                   1552 ;------------------------------------------------------------
                                   1553 ;Allocation info for local variables in function 'sudav_isr'
                                   1554 ;------------------------------------------------------------
                                   1555 ;	build/../bulkloop.c:203: void sudav_isr(void) __interrupt (SUDAV_ISR) {
                                   1556 ;	-----------------------------------------
                                   1557 ;	 function sudav_isr
                                   1558 ;	-----------------------------------------
      000422                       1559 _sudav_isr:
      000422 C0 E0            [24] 1560 	push	acc
      000424 C0 82            [24] 1561 	push	dpl
      000426 C0 83            [24] 1562 	push	dph
                                   1563 ;	build/../bulkloop.c:205: got_sud=TRUE;
                                   1564 ;	assignBit
      000428 D2 01            [12] 1565 	setb	_got_sud
                                   1566 ;	build/../bulkloop.c:206: CLEAR_SUDAV();
      00042A 53 91 EF         [24] 1567 	anl	_EXIF,#0xef
      00042D 90 E6 5D         [24] 1568 	mov	dptr,#_USBIRQ
      000430 74 01            [12] 1569 	mov	a,#0x01
      000432 F0               [24] 1570 	movx	@dptr,a
                                   1571 ;	build/../bulkloop.c:207: }
      000433 D0 83            [24] 1572 	pop	dph
      000435 D0 82            [24] 1573 	pop	dpl
      000437 D0 E0            [24] 1574 	pop	acc
      000439 32               [24] 1575 	reti
                                   1576 ;	eliminated unneeded mov psw,# (no regs used in bank)
                                   1577 ;	eliminated unneeded push/pop not_psw
                                   1578 ;	eliminated unneeded push/pop b
                                   1579 ;------------------------------------------------------------
                                   1580 ;Allocation info for local variables in function 'sof_isr'
                                   1581 ;------------------------------------------------------------
                                   1582 ;	build/../bulkloop.c:211: void sof_isr (void) __interrupt (SOF_ISR) __using (1) {
                                   1583 ;	-----------------------------------------
                                   1584 ;	 function sof_isr
                                   1585 ;	-----------------------------------------
      00043A                       1586 _sof_isr:
                           00000F  1587 	ar7 = 0x0f
                           00000E  1588 	ar6 = 0x0e
                           00000D  1589 	ar5 = 0x0d
                           00000C  1590 	ar4 = 0x0c
                           00000B  1591 	ar3 = 0x0b
                           00000A  1592 	ar2 = 0x0a
                           000009  1593 	ar1 = 0x09
                           000008  1594 	ar0 = 0x08
      00043A C0 E0            [24] 1595 	push	acc
      00043C C0 82            [24] 1596 	push	dpl
      00043E C0 83            [24] 1597 	push	dph
      000440 C0 D0            [24] 1598 	push	psw
      000442 75 D0 08         [24] 1599 	mov	psw,#0x08
                                   1600 ;	build/../bulkloop.c:212: ++sofct;
      000445 90 3C 00         [24] 1601 	mov	dptr,#_sofct
      000448 E0               [24] 1602 	movx	a,@dptr
      000449 24 01            [12] 1603 	add	a, #0x01
      00044B F0               [24] 1604 	movx	@dptr,a
      00044C A3               [24] 1605 	inc	dptr
      00044D E0               [24] 1606 	movx	a,@dptr
      00044E 34 00            [12] 1607 	addc	a, #0x00
      000450 F0               [24] 1608 	movx	@dptr,a
                                   1609 ;	build/../bulkloop.c:213: if(sofct==8000) { // about 8000 sof interrupts per second at high speed
      000451 90 3C 00         [24] 1610 	mov	dptr,#_sofct
      000454 E0               [24] 1611 	movx	a,@dptr
      000455 FE               [12] 1612 	mov	r6,a
      000456 A3               [24] 1613 	inc	dptr
      000457 E0               [24] 1614 	movx	a,@dptr
      000458 FF               [12] 1615 	mov	r7,a
      000459 BE 40 19         [24] 1616 	cjne	r6,#0x40,00105$
      00045C BF 1F 16         [24] 1617 	cjne	r7,#0x1f,00105$
                                   1618 ;	build/../bulkloop.c:214: on5=!on5;
      00045F B2 03            [12] 1619 	cpl	_on5
                                   1620 ;	build/../bulkloop.c:215: if (on5) {d5on();} else {d5off();}
      000461 30 03 06         [24] 1621 	jnb	_on5,00102$
      000464 75 92 B8         [24] 1622 	mov __XPAGE, #0xB8 
      000467 E2               [24] 1623 	movx a, @r0 
      000468 80 04            [24] 1624 	sjmp	00103$
      00046A                       1625 00102$:
      00046A 75 92 B0         [24] 1626 	mov __XPAGE, #0xB0 
      00046D E2               [24] 1627 	movx a, @r0 
      00046E                       1628 00103$:
                                   1629 ;	build/../bulkloop.c:216: sofct=0;
      00046E 90 3C 00         [24] 1630 	mov	dptr,#_sofct
      000471 E4               [12] 1631 	clr	a
      000472 F0               [24] 1632 	movx	@dptr,a
      000473 A3               [24] 1633 	inc	dptr
      000474 F0               [24] 1634 	movx	@dptr,a
      000475                       1635 00105$:
                                   1636 ;	build/../bulkloop.c:218: CLEAR_SOF();
      000475 53 91 EF         [24] 1637 	anl	_EXIF,#0xef
      000478 90 E6 5D         [24] 1638 	mov	dptr,#_USBIRQ
      00047B 74 02            [12] 1639 	mov	a,#0x02
      00047D F0               [24] 1640 	movx	@dptr,a
                                   1641 ;	build/../bulkloop.c:219: }
      00047E D0 D0            [24] 1642 	pop	psw
      000480 D0 83            [24] 1643 	pop	dph
      000482 D0 82            [24] 1644 	pop	dpl
      000484 D0 E0            [24] 1645 	pop	acc
      000486 02 00 9E         [24] 1646 	ljmp	sdcc_atomic_maybe_rollback
                                   1647 ;	eliminated unneeded push/pop b
                                   1648 ;------------------------------------------------------------
                                   1649 ;Allocation info for local variables in function 'usbreset_isr'
                                   1650 ;------------------------------------------------------------
                                   1651 ;	build/../bulkloop.c:221: void usbreset_isr(void) __interrupt (USBRESET_ISR) {
                                   1652 ;	-----------------------------------------
                                   1653 ;	 function usbreset_isr
                                   1654 ;	-----------------------------------------
      000489                       1655 _usbreset_isr:
                           000007  1656 	ar7 = 0x07
                           000006  1657 	ar6 = 0x06
                           000005  1658 	ar5 = 0x05
                           000004  1659 	ar4 = 0x04
                           000003  1660 	ar3 = 0x03
                           000002  1661 	ar2 = 0x02
                           000001  1662 	ar1 = 0x01
                           000000  1663 	ar0 = 0x00
      000489 C0 21            [24] 1664 	push	bits
      00048B C0 E0            [24] 1665 	push	acc
      00048D C0 F0            [24] 1666 	push	b
      00048F C0 82            [24] 1667 	push	dpl
      000491 C0 83            [24] 1668 	push	dph
      000493 C0 07            [24] 1669 	push	(0+7)
      000495 C0 06            [24] 1670 	push	(0+6)
      000497 C0 05            [24] 1671 	push	(0+5)
      000499 C0 04            [24] 1672 	push	(0+4)
      00049B C0 03            [24] 1673 	push	(0+3)
      00049D C0 02            [24] 1674 	push	(0+2)
      00049F C0 01            [24] 1675 	push	(0+1)
      0004A1 C0 00            [24] 1676 	push	(0+0)
      0004A3 C0 D0            [24] 1677 	push	psw
      0004A5 75 D0 00         [24] 1678 	mov	psw,#0x00
                                   1679 ;	build/../bulkloop.c:222: handle_hispeed(FALSE);
      0004A8 75 82 00         [24] 1680 	mov	dpl, #0x00
      0004AB 12 08 15         [24] 1681 	lcall	_handle_hispeed
                                   1682 ;	build/../bulkloop.c:223: CLEAR_USBRESET();
      0004AE 53 91 EF         [24] 1683 	anl	_EXIF,#0xef
      0004B1 90 E6 5D         [24] 1684 	mov	dptr,#_USBIRQ
      0004B4 74 10            [12] 1685 	mov	a,#0x10
      0004B6 F0               [24] 1686 	movx	@dptr,a
                                   1687 ;	build/../bulkloop.c:224: }
      0004B7 D0 D0            [24] 1688 	pop	psw
      0004B9 D0 00            [24] 1689 	pop	(0+0)
      0004BB D0 01            [24] 1690 	pop	(0+1)
      0004BD D0 02            [24] 1691 	pop	(0+2)
      0004BF D0 03            [24] 1692 	pop	(0+3)
      0004C1 D0 04            [24] 1693 	pop	(0+4)
      0004C3 D0 05            [24] 1694 	pop	(0+5)
      0004C5 D0 06            [24] 1695 	pop	(0+6)
      0004C7 D0 07            [24] 1696 	pop	(0+7)
      0004C9 D0 83            [24] 1697 	pop	dph
      0004CB D0 82            [24] 1698 	pop	dpl
      0004CD D0 F0            [24] 1699 	pop	b
      0004CF D0 E0            [24] 1700 	pop	acc
      0004D1 D0 21            [24] 1701 	pop	bits
      0004D3 02 00 9E         [24] 1702 	ljmp	sdcc_atomic_maybe_rollback
                                   1703 ;------------------------------------------------------------
                                   1704 ;Allocation info for local variables in function 'hispeed_isr'
                                   1705 ;------------------------------------------------------------
                                   1706 ;	build/../bulkloop.c:225: void hispeed_isr(void) __interrupt (HISPEED_ISR) {
                                   1707 ;	-----------------------------------------
                                   1708 ;	 function hispeed_isr
                                   1709 ;	-----------------------------------------
      0004D6                       1710 _hispeed_isr:
      0004D6 C0 21            [24] 1711 	push	bits
      0004D8 C0 E0            [24] 1712 	push	acc
      0004DA C0 F0            [24] 1713 	push	b
      0004DC C0 82            [24] 1714 	push	dpl
      0004DE C0 83            [24] 1715 	push	dph
      0004E0 C0 07            [24] 1716 	push	(0+7)
      0004E2 C0 06            [24] 1717 	push	(0+6)
      0004E4 C0 05            [24] 1718 	push	(0+5)
      0004E6 C0 04            [24] 1719 	push	(0+4)
      0004E8 C0 03            [24] 1720 	push	(0+3)
      0004EA C0 02            [24] 1721 	push	(0+2)
      0004EC C0 01            [24] 1722 	push	(0+1)
      0004EE C0 00            [24] 1723 	push	(0+0)
      0004F0 C0 D0            [24] 1724 	push	psw
      0004F2 75 D0 00         [24] 1725 	mov	psw,#0x00
                                   1726 ;	build/../bulkloop.c:226: handle_hispeed(TRUE);
      0004F5 75 82 01         [24] 1727 	mov	dpl, #0x01
      0004F8 12 08 15         [24] 1728 	lcall	_handle_hispeed
                                   1729 ;	build/../bulkloop.c:227: CLEAR_HISPEED();
      0004FB 53 91 EF         [24] 1730 	anl	_EXIF,#0xef
      0004FE 90 E6 5D         [24] 1731 	mov	dptr,#_USBIRQ
      000501 74 20            [12] 1732 	mov	a,#0x20
      000503 F0               [24] 1733 	movx	@dptr,a
                                   1734 ;	build/../bulkloop.c:228: }
      000504 D0 D0            [24] 1735 	pop	psw
      000506 D0 00            [24] 1736 	pop	(0+0)
      000508 D0 01            [24] 1737 	pop	(0+1)
      00050A D0 02            [24] 1738 	pop	(0+2)
      00050C D0 03            [24] 1739 	pop	(0+3)
      00050E D0 04            [24] 1740 	pop	(0+4)
      000510 D0 05            [24] 1741 	pop	(0+5)
      000512 D0 06            [24] 1742 	pop	(0+6)
      000514 D0 07            [24] 1743 	pop	(0+7)
      000516 D0 83            [24] 1744 	pop	dph
      000518 D0 82            [24] 1745 	pop	dpl
      00051A D0 F0            [24] 1746 	pop	b
      00051C D0 E0            [24] 1747 	pop	acc
      00051E D0 21            [24] 1748 	pop	bits
      000520 02 00 9E         [24] 1749 	ljmp	sdcc_atomic_maybe_rollback
                                   1750 	.area CSEG    (CODE)
                                   1751 	.area CONST   (CODE)
                                   1752 	.area CONST   (CODE)
      001316                       1753 ___str_0:
      001316 44 6F 6E 65 20 69 6E  1754 	.ascii "Done initializing stuff"
             69 74 69 61 6C 69 7A
             69 6E 67 20 73 74 75
             66 66
      00132D 0A                    1755 	.db 0x0a
      00132E 00                    1756 	.db 0x00
                                   1757 	.area CSEG    (CODE)
                                   1758 	.area CONST   (CODE)
      00132F                       1759 ___str_1:
      00132F 48 61 6E 64 6C 65 20  1760 	.ascii "Handle setupdata"
             73 65 74 75 70 64 61
             74 61
      00133F 0A                    1761 	.db 0x0a
      001340 00                    1762 	.db 0x00
                                   1763 	.area CSEG    (CODE)
                                   1764 	.area CONST   (CODE)
      001341                       1765 ___str_2:
      001341 65 70 32 20 6F 75 74  1766 	.ascii "ep2 out received data"
             20 72 65 63 65 69 76
             65 64 20 64 61 74 61
      001356 0A                    1767 	.db 0x0a
      001357 00                    1768 	.db 0x00
                                   1769 	.area CSEG    (CODE)
                                   1770 	.area CONST   (CODE)
      001358                       1771 ___str_3:
      001358 53 65 6E 64 69 6E 67  1772 	.ascii "Sending data to ep6 in"
             20 64 61 74 61 20 74
             6F 20 65 70 36 20 69
             6E
      00136E 0A                    1773 	.db 0x0a
      00136F 00                    1774 	.db 0x00
                                   1775 	.area CSEG    (CODE)
                                   1776 	.area CONST   (CODE)
      001370                       1777 ___str_4:
      001370 65 70 20 25 30 32 78  1778 	.ascii "ep %02x"
      001377 0A                    1779 	.db 0x0a
      001378 00                    1780 	.db 0x00
                                   1781 	.area CSEG    (CODE)
                                   1782 	.area CONST   (CODE)
      001379                       1783 ___str_5:
      001379 4E 65 65 64 20 74 6F  1784 	.ascii "Need to implement vendor command: %02x"
             20 69 6D 70 6C 65 6D
             65 6E 74 20 76 65 6E
             64 6F 72 20 63 6F 6D
             6D 61 6E 64 3A 20 25
             30 32 78
      00139F 0A                    1785 	.db 0x0a
      0013A0 00                    1786 	.db 0x00
                                   1787 	.area CSEG    (CODE)
                                   1788 	.area CONST   (CODE)
      0013A1                       1789 ___str_6:
      0013A1 47 65 74 20 49 6E 74  1790 	.ascii "Get Interface"
             65 72 66 61 63 65
      0013AE 0A                    1791 	.db 0x0a
      0013AF 00                    1792 	.db 0x00
                                   1793 	.area CSEG    (CODE)
                                   1794 	.area CONST   (CODE)
      0013B0                       1795 ___str_7:
      0013B0 53 65 74 20 69 6E 74  1796 	.ascii "Set interface %d to alt: %d"
             65 72 66 61 63 65 20
             25 64 20 74 6F 20 61
             6C 74 3A 20 25 64
      0013CB 0A                    1797 	.db 0x0a
      0013CC 00                    1798 	.db 0x00
                                   1799 	.area CSEG    (CODE)
                                   1800 	.area XINIT   (CODE)
      0013D8                       1801 __xinit__sofct:
      0013D8 00 00                 1802 	.byte #0x00, #0x00	; 0
                                   1803 	.area CABS    (ABS,CODE)
