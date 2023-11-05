W tym pliku szczegółowo opisane zostaną informacje dotyczące uruchomienia sterowania robota oraz lidara przy pomocy pythona.

## Uruchamianie w środowisku Jupyter Notebook
zaletą tego sposobu jest szybkość w przygotowaniu robota.

1. Włącz robota  
   Not. Jeżeli chcesz pracować z innego komputera niż robot niezbędne będzie podłączenie robota do sieci.
2. Zaloguj się do Jupyter Notebook  
   Jeżeli pracujesz na robocie uruchom przeglądarkę i połącz się z adresem `localhost:8888` lub `127.0.0.1:8888`.
   Jeżeli pracujesz z innego komputera który jest w tej samej sieci połącz się z adresem ip robota (jest wyświetlony na ekraniku) na adresie `8888` 
3. Zaloguj się do Notebooka przy pomocy hasła `jetson`
4. Pobierz pliki Notebook z repozytorium https://github.com/M1chol/jetracer-ai-kit-python
5. Dodaj pliki do `/Jetracer/notebooks` w zakładce pliki
6. Uruchom pliki


## Uruchamianie robota systemowo
Zaletą tego sposobu jest pominięcie wizualnego środowiska Jupyter. Daje to możliwość obsługiwania pełnych bibliotek np. matplotlib.

1. Włącz robota
2. Zainstaluj środowisko programistyczne VS Code,  
 instrukcje znajdują się [tutaj](https://code.visualstudio.com/docs/setup/linux).  
3. Zainstaluj rozszerzenie Python - Rozszerzenia pobiera się bezpośrednio w aplikacji VS Code w zakładce `Extensions`
4. Przejdź do zakładki Source Control   
5. Kliknij `Clone Repository` i wklej link `https://github.com/M1chol/jetracer-ai-kit-python.git`
6. Wybierz folder do którego ma zostać sklonowane repozytorium   
7. Jako środowisko wybierz python 3 - w prawym dolnym rogu
8. Uruchom pliki
