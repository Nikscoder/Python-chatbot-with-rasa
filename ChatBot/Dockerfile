# Bazowy obraz Rasa
FROM rasa/rasa:3.6.7

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie plików projektu Rasa
COPY . /app

# Port do nasłuchiwania
EXPOSE 5005

# Uruchomienie serwera Rasa
CMD ["rasa", "run", "--enable-api", "--cors", "*"]
