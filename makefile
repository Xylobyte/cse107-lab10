COURSE = cse107
GROUP_NAME = donovan_griego
ASSIGNMENT = lab10
TARGETS = readscores.py README.md word_count.py simplediff.py design
zip: $(TARGETS)
	zip $(COURSE)_$(GROUP_NAME)_$(ASSIGNMENT).zip $(TARGETS)
	@echo "\n--- zip archive created ---\n"
	zipinfo $(COURSE)_$(GROUP_NAME)_$(ASSIGNMENT).zip