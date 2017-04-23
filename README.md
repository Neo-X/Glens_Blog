

# Dependancies

sudo pip install pelican  

# To Publish

make publish

# Settings

WHere to find more themes  
https://github.com/getpelican/pelican-themes

Current theme  
https://github.com/nairobilug/pelican-alchemy/tree/f235c81bf323e6134b01915fc9a46b5e89ac238b


# Extras

ruby -rubygems -e 'require "jekyll-import";
    JekyllImport::Importers::Blogger.run({
      "source"                => "blog-04-22-2017.xml",
      "no-blogger-info"       => false, # not to leave blogger-URL info (id and old URL) in the front matter
      "replace-internal-link" => false, # replace internal links using the post_url liquid tag.
    })'
