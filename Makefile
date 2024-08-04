all: run

.PHONY: build/main.rom clean

build/main.rom: main.gbasm 
	mkdir -p build
	gbasm $< $@

run: build/main.rom
	gb $<

clean:
	rm -rf build
