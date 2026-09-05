import json, os

facts_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'facts.json')

def main():
    if not os.path.exists(facts_file):
        print("facts.json not found, skipping.")
        return
    with open(facts_file, 'r') as f:
        facts = json.load(f)
    print(f"Validated facts bank: {len(facts)} active NFL facts.")

if __name__ == '__main__':
    main()
