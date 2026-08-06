import json
import argparse

parser = argparse.ArgumentParser(
    description="Check which translation keys are missing from a Minecraft language file."
)

parser.add_argument(
    "language_file",
    help="The language file to check (for example de_de.json)"
)

args = parser.parse_args()

canonical = "en_us.json"

english_file = open(canonical, encoding="utf-8")
english_parsed = json.load(english_file)

language_file = open(args.language_file, encoding="utf_8")
language_parsed = json.load(language_file)

print(f"Following are the keys that are in the {canonical} file but not in the {args.language_file} file")
print(f"They should be in the correct format so you can just copy paste them in, and only change the actual translation\n")
for key in english_parsed:
    if key not in language_parsed:
        print(f'"{key}": "{english_parsed[key]}",')
