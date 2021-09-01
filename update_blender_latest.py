import os

url = "https://builder.blender.org/download/daily/"

keyword = "alpha"

symbolic_folder = "blender-latest"

# Download experimental builds html page:
build_page = "build_page.html"
os.system("wget -O " + build_page + " " + url)

# Turn html into array then delete file
with open(build_page, "r") as index :
    page_content = index.readlines()
os.system("rm " + build_page)

# Find links ending in .tar.xz 
links = []
for line in page_content:
    if ".tar.xz" in line:
        stub = line.split("<a href=\"")
        for i in stub:
            if "tar.xz\"" in i:
                link = i.split("\"", 1)
                links.append(link[0])
                
# Remove duplicates
links = list( dict.fromkeys(links) )

# Look for keyword to choose build link
for i in links:
    if keyword in i:
        latest_build_url = i

latest_build_package = latest_build_url.split("/")[-1]
latest_build_name = latest_build_package.rstrip('.tar.xz')

# Check for local latest build folder
if os.path.isdir(os.getcwd() + "/" + latest_build_name):
    print "Already latest build: " + latest_build_name
    exit()
# If not present, download archive
else:
    os.system("wget " + latest_build_url)

# Extract archive then delete file
print "Extracting " + latest_build_package
os.system("tar -xf " + latest_build_package)
os.system("rm " + latest_build_package)

# Create/overwrite a symbolic folder 
# that points to the new build 
link_cmd = ''.join([
    "ln -sfn ",
    os.getcwd(),
    "/",
    latest_build_name,
    " ",
    symbolic_folder
])
print "Making symbolic link to " + symbolic_folder
os.system(link_cmd)

