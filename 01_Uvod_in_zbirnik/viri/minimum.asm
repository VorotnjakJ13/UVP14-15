; Najmanši element v zaporedju (tabeli)

	JMP start
stev_el:DB 5 ; Število elementov v tabeli
tabela:	DB 7 ; Tabela
	DB 2
	DB 8
	DB 3
	DB 5
min: 	DB 0 ; Na koncu bo tu min	

start: 	MOV C, tabela	; Naslov začetka tabele 
	ADD C, [stev_el]   ; Naslov zadnjega elementa + 1
	MOV A, tabela	   ; Kazalec na začetek tabele
	MOV B, [tabela]	   ; V B trenutni min
	INC A		   ; Premik kazalca za en element
.zanka: CMP A, C	; Ali je kazalec A presegel tabelo?
	JZ konec	; Če je, končamo zanko
	CMP B, [A]	; Ali smo našli manjši element 
	JBE povec	; Če nismo, ...
	MOV B, [A]	; sicer ga zapišemo v B
povec:	INC A		; Premik kazaleca naprej
	JMP .zanka 	; Ponovimo zanko
	
konec:	MOV [min], B	; Shranimo min
	HLT

