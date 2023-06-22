#   Jak adaptovat svou minihru pro úspěšnou implementaci do main programu?

* Návod předpokládá že máte minihru udělanou jako samostatnou pygame hru
* Celé to spočívá v předělání vaše kódu do jedné funkce
* Vaší funkci může main program poslat jakýkoliv parametr, ke kterému má přístup, a od vás naopak očekává počet získaných/stracených followerů 

    * Vemte si příklad z branche Sys, komitu "fungující spouštění minihry" ve složce ./minihry/found_the_items/main.py . Z úplně dedikovaného kódu je za pomocí asi 3 řádků navíc(a pár smazaných)funkce
## Jak na to
* V rychlosti sepíšu jak na to
    * Ujistěte se že jste udělali komit, aby jste se v případě neúspěchu mohli vrátit na původní verzi!!

1. Vyztvořte prázdnou funkci se jménem game a dvěma parametry, clock a screen. tyto parametry nazvěte tak jak je nezýváte a používáte v programu už teď, tvz. "def game(okno, hodiny)"
2. Všechen váš kód, bez import řádků vložte do funkce
3. Smažte řádky kde jste použili pygame.display.set_mode(rozliseni) a pygame.time.Clock() a uložili je do proměných(tyto proměné totiž převezmete z mainu)
4. smažte veškeré pygame.quit() a nahraďte ho "return" keywordem následovaným počtem získaných/stracených followerů, tvz: "return 5" nebo "return x" {x je proměná s počtem hráčů}


* Všechny vaše soubory, potřebné pro spuštění, uložte do složky minigame/"nazev_vasi_hry"/

* Po tomto je vaše minihra alespoň minimálně připravena pro implementaci, díky!