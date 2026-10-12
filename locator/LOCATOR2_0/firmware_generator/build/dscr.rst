ASxxxx Assembler V05.50.4+NoICE+SDCCmods-WIP-R14  (Intel 8051)          Page 1
Hexadecimal [24-Bits]



                                      1 ; Copyright (C) 2009 Ubixum, Inc. 
                                      2 ;
                                      3 ; This library is free software; you can redistribute it and/or
                                      4 ; modify it under the terms of the GNU Lesser General Public
                                      5 ; License as published by the Free Software Foundation; either
                                      6 ; version 2.1 of the License, or (at your option) any later version.
                                      7 ; 
                                      8 ; This library is distributed in the hope that it will be useful,
                                      9 ; but WITHOUT ANY WARRANTY; without even the implied warranty of
                                     10 ; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
                                     11 ; Lesser General Public License for more details.
                                     12 ; 
                                     13 ; You should have received a copy of the GNU Lesser General Public
                                     14 ; License along with this library; if not, write to the Free Software
                                     15 ; Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
                                     16 
                                     17 ; this is a the default 
                                     18 ; full speed and high speed 
                                     19 ; descriptors found in the TRM
                                     20 ; change however you want but leave 
                                     21 ; the descriptor pointers so the setupdat.c file works right
                                     22  
                                     23 
                                     24 .module DEV_DSCR 
                                     25 
                                     26 ; descriptor types
                                     27 ; same as setupdat.h
                           000001    28 DSCR_DEVICE_TYPE=1
                           000002    29 DSCR_CONFIG_TYPE=2
                           000003    30 DSCR_STRING_TYPE=3
                           000004    31 DSCR_INTERFACE_TYPE=4
                           000005    32 DSCR_ENDPOINT_TYPE=5
                           000006    33 DSCR_DEVQUAL_TYPE=6
                                     34 
                                     35 ; for the repeating interfaces
                           000009    36 DSCR_INTERFACE_LEN=9
                           000007    37 DSCR_ENDPOINT_LEN=7
                                     38 
                                     39 ; endpoint types
                           000000    40 ENDPOINT_TYPE_CONTROL=0
                           000001    41 ENDPOINT_TYPE_ISO=1
                           000002    42 ENDPOINT_TYPE_BULK=2
                           000003    43 ENDPOINT_TYPE_INT=3
                                     44 
                                     45     .globl	_dev_dscr, _dev_qual_dscr, _highspd_dscr, _fullspd_dscr, _dev_strings, _dev_strings_end
                                     46 ; These need to be in code memory.  If
                                     47 ; they aren't you'll have to manully copy them somewhere
                                     48 ; in code memory otherwise SUDPTRH:L don't work right
                                     49     .area	DSCR_AREA	(CODE)
                                     50 
      003E00                         51 _dev_dscr:
      003E00 12                      52 	.db	dev_dscr_end-_dev_dscr    ; len
      003E01 01                      53 	.db	DSCR_DEVICE_TYPE		  ; type
      003E02 00 02                   54 	.dw	0x0002					  ; usb 2.0
      003E04 FF                      55 	.db	0xff  					  ; class (vendor specific)
ASxxxx Assembler V05.50.4+NoICE+SDCCmods-WIP-R14  (Intel 8051)          Page 2
Hexadecimal [24-Bits]



      003E05 FF                      56 	.db	0xff					  ; subclass (vendor specific)
      003E06 FF                      57 	.db	0xff					  ; protocol (vendor specific)
      003E07 40                      58 	.db	64						  ; packet size (ep0)
      003E08 B4 04                   59 	.dw	0xB404					  ; vendor id 
      003E0A 04 10                   60 	.dw	0x0410					  ; product id
      003E0C 01 00                   61 	.dw	0x0100					  ; version id
      003E0E 01                      62 	.db	1		                  ; manufacturure str idx
      003E0F 02                      63 	.db	2				          ; product str idx	
      003E10 00                      64 	.db	0				          ; serial str idx 
      003E11 01                      65 	.db	1			              ; n configurations
      003E12                         66 dev_dscr_end:
                                     67 
      003E12                         68 _dev_qual_dscr:
      003E12 0A                      69 	.db	dev_qualdscr_end-_dev_qual_dscr
      003E13 06                      70 	.db	DSCR_DEVQUAL_TYPE
      003E14 00 02                   71 	.dw	0x0002                              ; usb 2.0
      003E16 FF                      72 	.db	0xff
      003E17 FF                      73 	.db	0xff
      003E18 FF                      74 	.db	0xff
      003E19 40                      75 	.db	64                                  ; max packet
      003E1A 01                      76 	.db	1									; n configs
      003E1B 00                      77 	.db	0									; extra reserved byte
      003E1C                         78 dev_qualdscr_end:
                                     79 
      003E1C                         80 _highspd_dscr:
      003E1C 09                      81 	.db	highspd_dscr_end-_highspd_dscr      ; dscr len											;; Descriptor length
      003E1D 02                      82 	.db	DSCR_CONFIG_TYPE
                                     83     ; can't use .dw because byte order is different
      003E1E 20                      84 	.db	(highspd_dscr_realend-_highspd_dscr) % 256 ; total length of config lsb
      003E1F 00                      85 	.db	(highspd_dscr_realend-_highspd_dscr) / 256 ; total length of config msb
      003E20 01                      86 	.db	1								 ; n interfaces
      003E21 01                      87 	.db	1								 ; config number
      003E22 00                      88 	.db	0								 ; config string
      003E23 80                      89 	.db	0x80                             ; attrs = bus powered, no wakeup
      003E24 32                      90 	.db	0x32                             ; max power = 100ma
      003E25                         91 highspd_dscr_end:
                                     92 
                                     93 ; all the interfaces next 
                                     94 ; NOTE the default TRM actually has more alt interfaces
                                     95 ; but you can add them back in if you need them.
                                     96 ; here, we just use the default alt setting 1 from the trm
      003E25 09                      97 	.db	DSCR_INTERFACE_LEN
      003E26 04                      98 	.db	DSCR_INTERFACE_TYPE
      003E27 00                      99 	.db	0				 ; index
      003E28 00                     100 	.db	0				 ; alt setting idx
      003E29 02                     101 	.db	2				 ; n endpoints	
      003E2A FF                     102 	.db	0xff			 ; class
      003E2B FF                     103 	.db	0xff
      003E2C FF                     104 	.db	0xff
      003E2D 03                     105 	.db	3	             ; string index	
                                    106 
                                    107 ; endpoint 2 out
      003E2E 07                     108 	.db	DSCR_ENDPOINT_LEN
      003E2F 05                     109 	.db	DSCR_ENDPOINT_TYPE
      003E30 02                     110 	.db	0x02				;  ep2 dir=OUT and address
ASxxxx Assembler V05.50.4+NoICE+SDCCmods-WIP-R14  (Intel 8051)          Page 3
Hexadecimal [24-Bits]



      003E31 02                     111 	.db	ENDPOINT_TYPE_BULK	; type
      003E32 00                     112 	.db	0x00				; max packet LSB
      003E33 02                     113 	.db	0x02				; max packet size=512 bytes
      003E34 00                     114 	.db	0x00				; polling interval
                                    115 
                                    116 ; endpoint 6 in
      003E35 07                     117 	.db	DSCR_ENDPOINT_LEN
      003E36 05                     118 	.db	DSCR_ENDPOINT_TYPE
      003E37 86                     119 	.db	0x86				;  ep6 dir=in and address
      003E38 02                     120 	.db	ENDPOINT_TYPE_BULK	; type
      003E39 00                     121 	.db	0x00				; max packet LSB
      003E3A 02                     122 	.db	0x02				; max packet size=512 bytes
      003E3B 00                     123 	.db	0x00				; polling interval
                                    124 
      003E3C                        125 highspd_dscr_realend:
                                    126 
      003E3C                        127     .even
      003E3C                        128 _fullspd_dscr:
      003E3C 09                     129 	.db	fullspd_dscr_end-_fullspd_dscr      ; dscr len
      003E3D 02                     130 	.db	DSCR_CONFIG_TYPE
                                    131     ; can't use .dw because byte order is different
      003E3E 20                     132 	.db	(fullspd_dscr_realend-_fullspd_dscr) % 256 ; total length of config lsb
      003E3F 00                     133 	.db	(fullspd_dscr_realend-_fullspd_dscr) / 256 ; total length of config msb
      003E40 01                     134 	.db	1								 ; n interfaces
      003E41 01                     135 	.db	1								 ; config number
      003E42 00                     136 	.db	0								 ; config string
      003E43 80                     137 	.db	0x80                             ; attrs = bus powered, no wakeup
      003E44 32                     138 	.db	0x32                             ; max power = 100ma
      003E45                        139 fullspd_dscr_end:
                                    140 
                                    141 ; all the interfaces next 
                                    142 ; NOTE the default TRM actually has more alt interfaces
                                    143 ; but you can add them back in if you need them.
                                    144 ; here, we just use the default alt setting 1 from the trm
      003E45 09                     145 	.db	DSCR_INTERFACE_LEN
      003E46 04                     146 	.db	DSCR_INTERFACE_TYPE
      003E47 00                     147 	.db	0				 ; index
      003E48 00                     148 	.db	0				 ; alt setting idx
      003E49 02                     149 	.db	2				 ; n endpoints	
      003E4A FF                     150 	.db	0xff			 ; class
      003E4B FF                     151 	.db	0xff
      003E4C FF                     152 	.db	0xff
      003E4D 03                     153 	.db	3	             ; string index	
                                    154 
                                    155 ; endpoint 2 out
      003E4E 07                     156 	.db	DSCR_ENDPOINT_LEN
      003E4F 05                     157 	.db	DSCR_ENDPOINT_TYPE
      003E50 02                     158 	.db	0x02				;  ep2 dir=OUT and address
      003E51 02                     159 	.db	ENDPOINT_TYPE_BULK	; type
      003E52 40                     160 	.db	0x40				; max packet LSB
      003E53 00                     161 	.db	0x00				; max packet size=64 bytes
      003E54 00                     162 	.db	0x00				; polling interval
                                    163 
                                    164 ; endpoint 6 in
      003E55 07                     165 	.db	DSCR_ENDPOINT_LEN
ASxxxx Assembler V05.50.4+NoICE+SDCCmods-WIP-R14  (Intel 8051)          Page 4
Hexadecimal [24-Bits]



      003E56 05                     166 	.db	DSCR_ENDPOINT_TYPE
      003E57 86                     167 	.db	0x86				;  ep6 dir=in and address
      003E58 02                     168 	.db	ENDPOINT_TYPE_BULK	; type
      003E59 40                     169 	.db	0x40				; max packet LSB
      003E5A 00                     170 	.db	0x00				; max packet size=64 bytes
      003E5B 00                     171 	.db	0x00				; polling interval
                                    172 
      003E5C                        173 fullspd_dscr_realend:
                                    174 
      003E5C                        175 .even
      003E5C                        176 _dev_strings:
                                    177 ; sample string
      003E5C                        178 _string0:
      003E5C 04                     179 	.db	string0end-_string0 ; len
      003E5D 03                     180 	.db	DSCR_STRING_TYPE
      003E5E 09 04                  181     .db 0x09, 0x04     ; who knows
      003E60                        182 string0end:
                                    183 ; add more strings here
                                    184 
      003E60                        185 _string1:
      003E60 06                     186     .db string1end-_string1
      003E61 03                     187     .db DSCR_STRING_TYPE
      003E62 48                     188     .ascii 'H'
      003E63 00                     189     .db 0
      003E64 69                     190     .ascii 'i'
      003E65 00                     191     .db 0
      003E66                        192 string1end:
                                    193 
      003E66                        194 _string2:
      003E66 0C                     195     .db string2end-_string2
      003E67 03                     196     .db DSCR_STRING_TYPE
      003E68 54                     197     .ascii 'T'
      003E69 00                     198     .db 0
      003E6A 68                     199     .ascii 'h'
      003E6B 00                     200     .db 0
      003E6C 65                     201     .ascii 'e'
      003E6D 00                     202     .db 0
      003E6E 72                     203     .ascii 'r'
      003E6F 00                     204     .db 0
      003E70 65                     205     .ascii 'e'
      003E71 00                     206     .db 0
      003E72                        207 string2end:
                                    208 
      003E72                        209 _string3:
      003E72 0C                     210     .db string3end-_string3
      003E73 03                     211     .db DSCR_STRING_TYPE
      003E74 69                     212     .ascii 'i'
      003E75 00                     213     .db 0
      003E76 46                     214     .ascii 'F'
      003E77 00                     215     .db 0
      003E78 61                     216     .ascii 'a'
      003E79 00                     217     .db 0
      003E7A 63                     218     .ascii 'c'
      003E7B 00                     219     .db 0
      003E7C 65                     220     .ascii 'e'
ASxxxx Assembler V05.50.4+NoICE+SDCCmods-WIP-R14  (Intel 8051)          Page 5
Hexadecimal [24-Bits]



      003E7D 00                     221     .db 0
      003E7E                        222 string3end:
                                    223     
      003E7E                        224 _dev_strings_end:
      003E7E 00 00                  225     .dw 0x0000   ; just in case someone passes an index higher than the end to the firmware
