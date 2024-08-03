all: run

build/%.rom: %.gbasm
	mkdir -p build
	gbasm $< $@

run: build/main.rom
	gb $<

clean:
	rm -rf build
