import sys
from pylint import lint
THRESHOLD = 10
run = lint.Run(["helloworld.py"], exit=False)

score = run.linter.stats.global_note

print(f"{score} pontot ért el a kódunk")

if (score < THRESHOLD):
	sys.exit(1)
else:
	sys.exit(0)