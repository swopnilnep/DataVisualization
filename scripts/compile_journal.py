from os import listdir
import datetime

journals_dir = "../journals/"
journals_doc = "../docs/journals.md"

# Open the document
doc = open(journals_doc, 'w')

# Markdown of what comes before the directory listing

pre_markdown = """# Journals

Over the month, Giang and I have documented our process of decision making, analysis and insights into quick thoughts as journals. Theses ideas also outline the process of how we undertook the project over time and how we planned everything step by step. Feel free to take a look below.

"""

table_header = """

| Date | Title | Author | Link |
|---|---|---|---|

"""


# Write to the document
doc.write(pre_markdown.strip()+"\n" * 2)
doc.write(table_header.strip())

link_num = 0
for file_name in sorted(listdir(journals_dir)):
    if file_name[0] != ".":
        
        ''' File Input''' 
        # Take in the first line for a title
        with open(journals_dir+file_name) as f:
            first_line = f.readline().strip()
            # Strip '#' sign out for markdown files
            if first_line[0] == "#": first_line = first_line[1:].strip()
                
        title = first_line 
                
        # Take filename 
        base = file_name.split(".")[0]
        
        ''' Author and Date'''
        author = base.split("_")[1].capitalize()
        
        date = base.split("_")[0]
        date = datetime.datetime.strptime(date,"%Y%m%d").strftime("%d, %b %Y")
                
        '''' HTML Link Constructor '''
        pre = '../journals/'
        post = '.html'
        link = pre+base+post
        
        ''' Markdown Output Link Constructor '''
        
        link_img = "![img_{}](../images/link.png)".format(link_num)
        link_num += 1
        
        md_link = "[{}]({})".format(link_img,link)
        
        ''' Markdown Line '''
 
        # Date | Title | Author | Link
        md_line = "| {} | {} | {} | {} |".format(date, title, author, md_link)
        
        # Write to Markdown document
        doc.write("\n"+md_line)
        

doc.close()