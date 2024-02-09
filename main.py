import typer
import json

app = typer.Typer()

@app.command("add")
def add(url: str, overridable: bool = False):
    url = url.replace("https://", "").replace("http://", "").replace("www.", "")
    name = url.split('.')[0].capitalize()
    
    add_to_file(name, url, overridable)
    
@app.command("remove")
def remove(keyword: str):
    remove_from_file(keyword)    
    
def add_to_file(name, url, overridable):
    new_entry = {'name': name, 'url': url, 'overridable': overridable}
    
    with open('websites.json', 'r') as file:
        data = json.load(file)
    
    data.append(new_entry)
    
    update_file(data)
    
    typer.echo(f"Added {name} to restricted websites.")
        
def remove_from_file(keyword):
    with open('websites.json', 'r') as file:
        data = json.load(file)
        
        for entry in data:
            name, url = entry['name'], entry['url']
            if keyword.lower() in name.lower() or keyword.lower() in url.lower():
                data.remove(entry)
                update_file(data)
                typer.echo(f"Removed {name} from restricted websites.")
                return
            
        typer.echo(f"Could not find webiste in restricted websites.")

def update_file(data):
    with open('websites.json', 'w') as file:
        json.dump(data, file, indent = 4)    

if __name__ == "__main__":
    app()