#!/opt/homebrew/bin/python3
import typer
import json

app = typer.Typer()

@app.command("add")
def add(url: str, overridable: bool = False):
    url = url.replace("https://", "").replace("http://", "")
    name = url.replace("www.", "").split('.')[0].capitalize()
    
    add_to_file(name, url, overridable)
    
@app.command("remove")
def remove(keyword: str):
    remove_from_file(keyword)    

@app.command("run")
def run():
    run_block()
    
@app.command("stop")
def stop():
    clean_up()

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

def get_websites():
    websites = []
    with open("websites.json", "r") as file:
        data = json.load(file)
        
        for entry in data:
            url = entry['url']
            websites.append(url)
    
    return websites

def run_block():
    hosts_path = "/etc/hosts"
    input("Running...\nTo stop, use the 'the stop command'")
    print(get_websites())
    
    while True:
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in get_websites():
                if website not in content:
                    file.write("127.0.0.1" + " " + website + "\n")
                    
def clean_up():
    hosts_path = "/etc/hosts"
    with open(hosts_path, 'r+') as file: 
            content = file.readlines() 
            file.seek(0) 
            for line in content: 
                if not any(website in line for website in get_websites()): 
                    file.write(line) 
            file.truncate()

if __name__ == "__main__":
    app()