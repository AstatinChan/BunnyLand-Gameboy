all: run

.PHONY: build/main.rom clean

tileset.gbasm: ./scripts/generate-tiledata.py $(wildcard ./sprites/**/* ./sprites/*)
	python ./scripts/generate-tiledata.py > tileset.gbasm

dialogues.gbasm: ./dialogues.gbtxt ./scripts/generate_from_gbtxt.py
	python ./scripts/generate_from_gbtxt.py dialogues.gbtxt > dialogues.gbasm

build/main.rom: main.gbasm tileset.gbasm dialogues.gbasm
	mkdir -p build
	gbasm $< $@

run: build/main.rom
	mkdir -p recordings
	gb $< --record-input "./recordings/$(shell date -Iseconds).record"

sameboy: build/main.rom
	sameboy build/main.rom

gearboy: build/main.rom
	gearboy build/main.rom

clean:
	rm -rf build
