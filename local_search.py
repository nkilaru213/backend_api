import os

SEARCH_DIR = "./dummy_data"

def search_files(query: str):
    results = []
    for root, dirs, files in os.walk(SEARCH_DIR):
        for f in files:
            path = os.path.join(root, f)
            try:
                with open(path, 'r', errors='ignore') as fh:
                    content = fh.read()
                    if query.lower() in content.lower():
                        snippet = content[:200].replace("\n"," ")
                        results.append({"file": path, "snippet": snippet})
            except:
                pass
    return results
