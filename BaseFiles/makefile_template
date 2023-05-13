
EXECUTABLE=main
CC=gcc
SOURCES=main.c test.c


all: $(EXECUTABLE)
	./$(EXECUTABLE)

clean:
	rm -rf *.o ./$(EXECUTABLE)

$(EXECUTABLE): $(SOURCES)
	$(CC) -o $(EXECUTABLE) $(SOURCES) && ./$(EXECUTABLE)
