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
 instrukcje znajdują się [tutaj](https://code.visualstudio.com/docs/setup/linux). W moim przypadku zwykły instalator nie zadziałał - musiałem zainstalować go z repozytorium, wszystkie instrukcje w linku.
3. Zainstaluj rozszerzenie Python - Rozszerzenia pobiera się bezpośrednio w aplikacji VS Code w zakładce `Extensions`
4. Przejdź do zakładki Source Control - jeżeli znajduje się komunikat o braku Git'a pobierz go według instrukcji
5. Kliknij `Clone Repository` i wklej link `https://github.com/M1chol/jetracer-ai-kit-python.git`
6. Wybierz folder do którego ma zostać sklonowane repozytorium
7. Następnym krokiem jest stworzenie środowiska wirtualnego kliknij `Ctrl+Shift+P` i wyszukaj `Environment` wybierz `Python: Create Environment...` a następnie `Venv` i wybierz wersję Pythona. Proponuję wersję > 3.7, ja zainstalowałem python 3.8 za pomocą komendy `sudo apt install python3.8` po restarcie aplikacji powinna pojawić się nowa wersja.
8. Teraz instalujemy odpowiednie biblioteki, otwórz terminal `Ctrl+tilda` lub kliknij wykrzyknik w lewym dolnym i zmień zakładkę
9. wpisz komendę `pip install -r requirements.txt` 
10. ostatnim problemem na jaki napotkamy będzie problem braku uprawnień biblioteki `gpio`, aby rozwiązać ten problem w terminalu systemu wpisz kolejno komendy 
 `sudo usermod -aG gpio $USER`  
 `sudo chown root.gpio /dev/gpiochip0`
 `sudo chmod 660 /dev/gpiochip0`
 więcej informacji i permanentne rozwiązanie [tutaj](https://github.com/NVIDIA/jetson-gpio/issues/20)