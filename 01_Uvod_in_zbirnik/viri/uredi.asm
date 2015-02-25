; Urejanje z izbiranjem


	JMP start
stev_el:DB 5 ; Število elementov v tabeli
tabela:	DB 7 ; Tabela
	DB 2
	DB 8
	DB 3
	DB 5

; rabimo C za konec, A za start, B za min

start: 	MOV A, tabela	; Začetek tabele
	MOV C, tabela
	ADD C, [stev_el] ; Konec tabele + 1
	CALL uredi	 ; Klic funkcije
	HLT
 
; najdi: A - začetek, C - konec + 1, B - pozicija najmanjšega elementa
najdi: 	PUSH A		; Shranimo morebitne stare vrednosti
	PUSH D
	MOV B, A	   
	INC A		   ; Premaknema A na 2. element
.zanka: CMP A, C	; Ali je kazalec v A že presegel tabelo
	JZ konec1	; Če je, končamo zanko
	MOV D, [B]
	CMP D, [A]	
	JBE povec	; Če ne (B <= [A]) si ga ne zapomnimo
	MOV B, A	; Sicer pa ga zapišemo v B
povec:	INC A		; Premaknemo kazalec za eno mesto naprej
	JMP .zanka 	; Ponovimo zanko
konec1:	POP D		; Obnovimo stare vrednosti 
	POP A
	RET

; Urejanje: A - začetek tabele, C - konec + 1, 	
; A bo trenutna pozicija v tabeli
uredi: 	PUSH A		; shranjevanje registrov
	PUSH B
	PUSH D
.zanka2: CMP A, C 	; je A dosegel C?
	JZ konec2
	CALL najdi	; najdi minimum
	MOV D, [A]	; zamenjava minimuma z [B]
	PUSH C
	MOV C, [B]
	MOV [A], C
	MOV [B], D
	POP C
	INC A		; pomik po tabeli naprej
	JMP .zanka2
konec2: POP D		; obnova registrov
	POP B
	POP A
	RET
