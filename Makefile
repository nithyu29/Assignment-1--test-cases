# default: giftcardreader

# giftcardreader: giftcardreader.c giftcard.h
# 	gcc -g -o giftcardreader giftcardreader.c

# asan: giftcardreader.c giftcard.h
# 	gcc -fsanitize=address -g -o giftcardreader giftcardreader.c

# test: giftcardreader
# 	./runtests.sh

# # .PHONY tells make to always assume this target needs
# # to be rebuilt
# .PHONY: clean
# clean:
# 	rm -f *.o giftcardreader

# with coverage
# default: giftcardreader

# giftcardreader: giftcardreader.c giftcard.h
#     gcc -g -o giftcardreader --coverage giftcardreader.c

# asan: giftcardreader.c giftcard.h
#     gcc -fsanitize=address -g -o giftcardreader giftcardreader.c

# test: giftcardreader
#     ./runtests.sh

# # .PHONY tells make to always assume this target needs
# # to be rebuilt
# .PHONY: clean
# clean:
#     rm -f *.o giftcardreader


# with coverage
# default: giftcardreader

giftcardreader: giftcardreader.c giftcard.h
	gcc -g -o giftcardreader --coverage giftcardreader.c

coverage:
	gcc -g -fprofile-arcs -ftest-coverage -o giftcardreader-coverage giftcardreader.c
	/runtests.sh
	lcov -o --capture --directory . --output-file coverage.info
	genhtml coverage.info --output-directory coverage-report


asan: giftcardreader.c giftcard.h
	gcc -fsanitize=address -g -o giftcardreader giftcardreader.c

test: giftcardreader
	./runtests.sh

# .PHONY tells make to always assume this target needs
# to be rebuilt
.PHONY: clean
clean:
	rm -f *.o giftcardreader

